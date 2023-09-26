#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division, print_function

import glob
import warnings
import numpy as np
import tables
import pandas as pd
from tqdm import tqdm

def split_obs_str(obs):
    if not isinstance(obs, list):
        obs = [obs]
    obs_dict = {}
    for o in obs:
        splitted = o.split('.')
        key = splitted[0]
        current_content = obs_dict.get(key, [])
        current_content.append(splitted[1])
        obs_dict[key] = current_content
    return obs_dict

def get_values_from_table(table, cols, dtype=float):
    values = np.empty((table.nrows, len(cols)), dtype=float)
    for i, row in enumerate(table.iterrows()):
        values[i, :] = [row[col] for col in cols]
    return values

class HDFcontainer:
    def __init__(self,
                 file_list=None,
                 directory=None,
                 id_cols=['Run',
                          'Event',
                          'SubEvent'],
                 exists_col=None):
        assert (directory is not None) or (file_list is not None), \
            'If component is not from aggregation directory or file_list'\
            'is needed!'
        if file_list is None:
            if '*' not in directory:
                directory += '*'
            file_list = glob.glob(directory)
        self.file_list = file_list
        self.id_cols = id_cols
        self.exists_col = exists_col

    def get_observables(self,
                        blacklist_tabs=[],
                        blacklist_cols=[],
                        blacklist_obs=[],
                        check_all=False):
        component_set = set()
        if check_all:
            files = self.file_list
        else:
            files = self.file_list[:1]
        for i, file_name in enumerate(files):
            file_set = set()
            f = tables.open_file(file_name)
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                for table in f.iter_nodes('/', classname='Table'):
                    table_name = table.name
                    if table_name not in blacklist_tabs:
                        col_names = [c for c in table.colnames
                                     if c not in blacklist_cols]
                        for c in col_names:
                            obs = '%s.%s' % (table_name, c)
                            if obs not in blacklist_obs:
                                file_set.add(obs)
                f.close()
                if i == 0:
                    component_set = file_set
                else:
                    component_set = component_set.intersection(file_set)
        return sorted(component_set)

    def get_values(self, table_key, cols):
        if isinstance(cols, str):
            cols = [cols]
        for i, file_name in enumerate(self.file_list):
            f = pd.HDFStore(file_name, 'r')
            table = f[table_key]
            drops = [c for c in table.columns
                     if c not in cols and c not in self.id_cols and
                     c != self.exists_col]
            table.drop(drops, axis=1, inplace=True)
            table.set_index(self.id_cols, inplace=True)
            f.close()
            if i == 0:
                values = table
            else:
                values = values.append(table)
        if self.exists_col is not None:
            mask = values.get(self.exists_col) == 0
            values[mask] = np.NaN
            values.drop(self.exists_col, axis=1, inplace=True)
        rename_dict = {col: '%s.%s' % (table_key, col)
                       for col in values.columns}
        values.rename(columns=rename_dict, inplace=True)
        return values

    def get_df(self, observables):
        n_obs = len(observables)
        obs = split_obs_str(observables)
        finished_cols = 0
        with tqdm(total=n_obs, unit='Observables') as pbar:
            for i, [table_key, cols] in enumerate(obs.iteritems()):
                tab_values = self.get_values(table_key, cols)
                if i == 0:
                    df = tab_values
                else:
                    df = df.join(tab_values, how='outer')
                pbar.update(len(cols))
        return df
