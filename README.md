## Preface
In this documentation I collect everything related to my work. The Repo language is english e.g. to keep it accessible for other people.

### Building the documentation
You need to install ```pandoc```,  ```pip install sphinx```, ```pip install sphinx_rtd_theme``` and ```pip install nbsphinx``` and then you can simply execute ```make html``` in the main repo directory.
The source files are in the ```source``` folder, the build files are in ```build/html```. To view the documentation open the ```index.html``` inside this folder.

### Sphinx structure
Every script or script collection should have its own doc page describing what it does and how it works. Doc pages are written in ReStructured Text markup language and can contain python code. You can even create plots directly in the rst structure. More information on how to use rst and python inside sphinx is available in the [matplotlib primer](http://matplotlib.org/sampledoc) or in the [sphinx sampledoc](https://pythonhosted.org/an_example_pypi_project/sphinx.html). Also it can be a good idea to just look at existing files in this repo if something doesn't work at first try.

In general the documentation is logically grouped in folders in the ```source/doc``` folder. Scripts are in the same structure in the ```source/_pyplots``` folder and can be called from the documentation. The same goes for static content like images which are inside ```source/_static```. The ```source/_pymodules``` folder contains extension modules that are already added in the ```source/config.py``` file.

Instead of using rst files you can directly use iPython notebooks. Currently you can't mix rst and ipynb files in one subdirectory because it messes up the navigation Just look in the existing notebooks for further infos. So you need to convert your ipynb to rst or make all rst files to notebooks. In doubt just rewrite your notebook cells (by copy & paste) to rst which only takes a few minutes.
