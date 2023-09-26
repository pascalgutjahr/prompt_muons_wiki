############################################################
## This is a mashup between virtualenvs activate script and icetrays env-shell.
##
## It prevents all settings and only changes the path so that icetray can
## be found. After calling 'deactivate' all paths are reset.
##
## To use in a project, copy it to the project build folder next to the
## original env-shell.sh and use 'source ./activate.sh' to load the environment.
## For each project change the path of I3_SHELL in line 74.
############################################################

# This file must be used with "source ./activate.sh" *from bash*
# You cannot run it directly

deactivate () {
    # Reset old environment variables if new ones were set
    if [ -n "$_OLD_VIRTUAL_PATH" ] ; then
        PATH="$_OLD_VIRTUAL_PATH"
        export PATH
        unset _OLD_VIRTUAL_PATH
    fi
    if [ -n "$_OLD_VIRTUAL_LD_LIBRARY_PATH" ] ; then
        LD_LIBRARY_PATH="$_OLD_VIRTUAL_LD_LIBRARY_PATH"
        export LD_LIBRARY_PATH
        unset _OLD_VIRTUAL_LD_LIBRARY_PATH
    fi
    if [ -n "$_OLD_VIRTUAL_DYLD_LIBRARY_PATH" ] ; then
        DYLD_LIBRARY_PATH="$_OLD_VIRTUAL_DYLD_LIBRARY_PATH"
        export DYLD_LIBRARY_PATH
        unset _OLD_VIRTUAL_DYLD_LIBRARY_PATH
    fi
    if [ -n "$_OLD_VIRTUAL_PYTHONPATH" ] ; then
        PYTHONPATH="$_OLD_VIRTUAL_PYTHONPATH"
        export PYTHONPATH
        unset _OLD_VIRTUAL_PYTHONPATH
    fi

    # This should detect bash and zsh, which have a hash command that must
    # be called to get it to forget past commands.  Without forgetting
    # past commands the $PATH changes we made may not be respected
    if [ -n "$BASH" -o -n "$ZSH_VERSION" ] ; then
        hash -r 2>/dev/null
    fi

    # Reset old PS1 if a new one was set
    if [ -n "$_OLD_VIRTUAL_PS1" ] ; then
        PS1="$_OLD_VIRTUAL_PS1"
        export PS1
        unset _OLD_VIRTUAL_PS1
    fi

    # Unset all new variables
    unset I3_SHELL
    unset I3_SRC
    unset I3_BUILD
    unset I3_TESTDATA
    if [ ! "$1" = "nondestructive" ] ; then
    # Self destruct!
        unset -f deactivate
    fi
}

# unset irrelavent variables
deactivate nondestructive


###################################################
### activate like virtualenv with env-shell paths
###################################################
# First test if we are in a activated shell
# -> Should always be the case, as we call deactivate first
if [ -z "$I3_SHELL" ]  ; then
    # Indicate the new environments base path. This is the only absolute path
    export I3_SHELL="/Users/tmenne/icecube/software/icerec/parasitic"

    # Set project paths
    _I3_SRC=${I3_SHELL}/src
    _I3_BUILD=${I3_SHELL}/build

    # Check if I3_TESTDATA is given externally and valid
    _I3_TESTDATA=
    if [ -d "$I3_TESTDATA" ] ; then
        if [ $(readlink "$_I3_TESTDATA") != $(readlink "$I3_TESTDATA") ]
        then
            _I3_TESTDATA=$I3_TESTDATA
        fi
    fi

    # Get python version
    _PYVER=`python -V 2>&1`

    # Check for ROOT and set paths accordingly if it exists. If not, leave empty
    if [ -d "$ROOTSYS" ] ; then
    _ROOTSYS=$ROOTSYS
    _PATH=${I3_SHELL}/build/bin:${_ROOTSYS}/bin:$_I3_PORTS/bin:$PATH
    _LD_LIBRARY_PATH=${I3_SHELL}/build/lib:${I3_SHELL}/build/lib/tools:${_ROOTSYS}/lib:$LD_LIBRARY_PATH
    _DYLD_LIBRARY_PATH=${I3_SHELL}/build/lib:${I3_SHELL}/build/lib/tools:${_ROOTSYS}/lib:$_I3_PORTS/lib:$DYLD_LIBRARY_PATH
    _PYTHONPATH=${I3_SHELL}/build/lib:${_ROOTSYS}/lib:$PYTHONPATH
    else
    _ROOTSYS=
    _PATH=${I3_SHELL}/build/bin:$_I3_PORTS/bin:$PATH
    _LD_LIBRARY_PATH=${I3_SHELL}/build/lib:${I3_SHELL}/build/lib/tools::$LD_LIBRARY_PATH
    _DYLD_LIBRARY_PATH=${I3_SHELL}/build/lib:${I3_SHELL}/build/lib/tools:$_I3_PORTS/lib:$DYLD_LIBRARY_PATH
    _PYTHONPATH=${I3_SHELL}/build/lib:$PYTHONPATH
    fi

    # Save the old state before assigning new variables
    _OLD_VIRTUAL_PATH="$PATH"
    _OLD_VIRTUAL_LD_LIBRARY_PATH="$LD_LIBRARY_PATH"
    _OLD_VIRTUAL_DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH"
    _OLD_VIRTUAL_PYTHONPATH="$PYTHONPATH"
    # Set all updated enviroment variables to activate the environment
    export PATH=$_PATH
    export LD_LIBRARY_PATH=$_LD_LIBRARY_PATH
    export DYLD_LIBRARY_PATH=$_DYLD_LIBRARY_PATH
    export PYTHONPATH=$_PYTHONPATH
    # And set all new variables. Those are unset on deactivate
    export I3_SRC=$_I3_SRC
    export I3_BUILD=$_I3_BUILD
    export I3_TESTDATA=$_I3_TESTDATA

    # Set new PS1 to indicate we are in a env-shell
    if [ -z "$I3_SHELL_DISABLE_PROMPT" ] ; then
        _OLD_VIRTUAL_PS1="$PS1"
        if [ "x" != x ] ; then
            PS1="$PS1"
        else
        if [ "`basename \"$I3_SHELL\"`" = "__" ] ; then
            # special case for Aspen magic directories
            # see http://www.zetadev.com/software/aspen/
            PS1="[`basename \`dirname \"$I3_SHELL\"\``] $PS1"
        else
            PS1="(`basename \"$I3_SHELL\"`)$PS1"
        fi
        fi
        export PS1
    fi

    # This should detect bash and zsh, which have a hash command that must
    # be called to get it to forget past commands.  Without forgetting
    # past commands the $PATH changes we made may not be respected
    if [ -n "$BASH" -o -n "$ZSH_VERSION" ] ; then
        hash -r 2>/dev/null
    fi

    # Print activation message
    TOPBAR="************************************************************************"
    WIDTH=`echo "$TOPBAR" | wc -c`
    WIDTH=$(( $WIDTH-2 ))
    printctr()
    {
        LEN=`echo "$*" | wc -c`
        LOFFSET=$(( ($WIDTH-$LEN)/2 ))
        ROFFSET=$(( $WIDTH-$LOFFSET-$LEN ))
        FORMAT="*%${LOFFSET}s%s%${ROFFSET}s*\n"
        printf $FORMAT " " "$*" " "
    }
    if [ -z "$ARGV" ] ; then
        printf "$TOPBAR\n"
        printctr ""
        printctr "W E L C O M E  to  I C E T R A Y"
        printctr ""
        printctr "Version icerec.trunk     r145061"
        printctr ""
        printf "$TOPBAR\n"
        printf "\n"
        printf "Icetray environment has:\n"
        printf "   I3_SRC       = %s\n" $_I3_SRC
        printf "   I3_BUILD     = %s\n" $_I3_BUILD
        [ -z "$_I3_PORTS" ] || printf "   I3_PORTS     = %s\n" $_I3_PORTS
        [ -d "$_I3_TESTDATA" ] && printf "   I3_TESTDATA  = %s\n" $_I3_TESTDATA \
                               || printf "   I3_TESTDATA should be set to an existing directory path\n" \
                                         "   (and 'make rsync' may need to be run) if you wish to run tests."
        echo   "   Python       =" $_PYVER
        [ -n "_ROOTSYS=" ] && printf "   ROOT         = %s\n" $_ROOTSYS
    fi

# If shell is already active, do nothing
else
    echo "We already are in a env-shell: $I3_SHELL"
    echo "Nothing was changed."
fi

