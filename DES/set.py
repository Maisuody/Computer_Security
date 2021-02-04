from cx_Freeze import setup, Executable

base = None    

executables = [Executable("DES.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<Security>",
    options = options,
    version = "1.5",
    description = '',
    executables = executables
)
