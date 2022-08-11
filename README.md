# pyuic6-Tool
Python script to automate call of pyuic6

## Usage

### Setting up

* Put your project .ui files in a /ui folder at the root of your project
* Create a /ui/converted folder at the root of your project
* Add an empty __init__.py file inside /ui/converted
* Put the two files in /src of this repository in the /ui/tool folder of you project

### Using the ui elements

You can then import the ui elements needed with
```
from ui.converted.[ui_filename] import Ui_[ui_element_name in Qt Designer]
```
and add
```
self._ui = Ui_[ui_element_name in Qt Designer]()
self._ui.setupUi(self)
```
to ``def __init__``

The ui elements will then be accessible from ``self._ui``.

## Benefits
* All .ui files will be automatically converted only if they have been modified.
* Using pyuic6 instead of uic.loadUi:
* * makes code completion available for interface elements
* * ensures a faster interface

## Known issues
Your project has to be run twice for the .ui files changes to be taken into account.

## Attribution
Original code by Abdelrahman Ahmed at https://github.com/Abdelatief/Pyuic5-Tool
