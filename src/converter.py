import os
from os import listdir, getcwd, system
from os.path import isfile, isdir
from sys import stderr


def convert_ui(*args):
    """
    Helper function for PyQt6 package to convert ._ui files to .py files.
    :param args: names of the ._ui files to convert to .py files in the current working directory only.
     if no arguments are passed, all ._ui files in the current working directory get converted.
    :return: None
    """
    directory_files = [file for file in listdir(getcwd()) if isfile(file)]
    uifiles = [file for file in directory_files if file[-3:] == '._ui']
    if len(args) == 0:
        for file in uifiles:
            system(f'pyuic6.py {file} -o {file[:-3] +  ".py"}')
    else:
        for file in args:
            if file in uifiles:
                system(f'pyuic6.py {file} -o {file[:-3] + ".py"}')
            else:
                print(f"Can't find {file} in the current working directory.", file=stderr)


class Converter:
    """
    A helper class to make the conversion of ._ui PyQt6 Designer's files to .py files easier. just by making an instance
    of the class and calling the convert._ui method at the entry point of your code will convert the files without
    having to deal with the cmd or terminal (dev tool to automate the conversion command). Also it helps to separate the
    ._ui files from the .py files in separate folders.
    """
    def __init__(self, ui_directory, py_directory=None):
        """
        if you didn't pass py_directory argument, it will be the same as the ui_directory
        :param ui_directory: Absolute path to the file that contains the _ui files
        :param py_directory: Absolute path to the file where the output .py files will be created
        """
        self.ui_directory = ui_directory if isdir(ui_directory) else None
        if py_directory is None:
            self.py_directory = ui_directory
        else:
            self.py_directory = py_directory if isdir(py_directory) else None

    def convert_ui(self, *args):
        """
        Convert the passed ._ui files if they are found in the ui_directory path to .py files created in the py_directory.
        if no arguments are passed, all the _ui files in the ui_directory will be converted
        :param args: Names of the _ui files to be converted
        :return: None
        """
        if self.ui_directory is None or self.py_directory is None:
            print("Error in _ui path or py path", file=stderr)
            return
        # print("rfid_stock_qt_main_ui.ui " + str(isfile(self.ui_directory + "\\" + "rfid_stock_qt_main_ui.ui")))
        # print("rfid_stock_qt_main_ui.ui"[-3:] == '.ui')
        uifiles = [file for file in listdir(self.ui_directory) if isfile(self.ui_directory + "\\" + file) and file[-3:] == '.ui']
        if len(uifiles) == 0:
            print(f"No current _ui files in {self.ui_directory}.", file=stderr)
        else:
            if len(args) == 0:
                for file in uifiles:
                    self.convert_file(file)
            else:
                for file in args:
                    if file in uifiles:
                        self.convert_file(file)
                    else:
                        print(f"Can't find {file} in the current working directory.", file=stderr)

    def convert_file(self, file):
        """
        :param file: name of a _ui file format to be converted
        :return: None
        """
        try:
            if os.path.getmtime(self.ui_directory + "\\" + file) > os.path.getmtime(self.py_directory + "\\" + file[:-3] + ".py"):
                absolute_uifile_path = f'"{self.ui_directory}\\{file}"'
                absolute_pyfile_path = f'"{self.py_directory}\\{file[:-3] + ".py"}"'
                print(f'pyuic6 {absolute_uifile_path} -o {absolute_pyfile_path}')
                system(f'pyuic6 {absolute_uifile_path} -o {absolute_pyfile_path}')
        except Exception as error:
            print(error, file=stderr)


Converter = Converter("ui", "ui\\converted")
Converter.convert_ui()
