
# Editing ASCII files 

````{panels}
:column: col-lg-12 p-2

**Goals:** 
- To provide a list of some potentially useful plain text editing software.
- To provide some details for using `vi`. 
- You should choose and install one/some of these or comparable

**Keywords:** ASCII, plain text, vi, Emacs, Atom, Brackets, Visual Studio code

**Associated material:** 


- [The `vi` editor](./vi-editor)
- Additional material: Helpful software. Notes on how to install the very Word-compatible WPS Office and some other software.
- [Random computer stuff](https://github.com/mejk/computer-stuff). Lists of software, installation instructions for some random things and solutions to some problems.
- [A brief list of cross-platform software](https://github.com/mejk/computer-stuff/blob/master/cross-platform-software.md). This is a list of software that can be be installed on Windows, Mac and Linux (and in some cases on mobile platforms as well. Some of the stuff below was extracted from this link. In particular, if you want to have more than listed below & to install `flatpack` that provides convenient access to install software such as Spotify etc. on Linux, then take a look.


````


When programming, editing system files, using LaTeX, and so on, one needs an ASCII editor. MS Word and such cannot be used as they use their own formats. Below are a few notes regarding such editors. There are many options some of which are listed. Some basic details for `vi` are provided since it comes with all Linux/Unix systems including the Mac OSX terminal. Ones should know the basics of `vi` even if some other editors are used for programming and other tasks.


## The `vi` editor

For anyone coming directly from GUI-based systems, the `vi` editor typically appears very cumbersome. It is, however, very lightweight and it is automatically installed with more or less all Linux/Unix based systems including Mac's terminal application. On the more grave side, if things go badly wrong and some files need to be fixed, vi is usually the choice. Even the live distributions include it. On the light side, despite its simplicity it is very powerful and can be used to edit programs, LaTeX documents etc. and for many it is the editor of choice. 

The usual obstacle for the first time users is to understand that `vi` has two different operating modes: 1) *insert mode* and 2) *command mode*. To edit any document, one has to be in the *insert mode*. When one opens `vi`, it always starts in the *command mode*. 


**In command mode:** You cannot insert text, only commands. This includes deleting characters (see below), saving the document, quitting the editor and so on. You can also use the arrow keys to move to a different location the file. The arrow keys cannot be used for this purpose in the *insert mode*.

**In insert mode:** You can type in any text. But you cannot delete characters. For that, you must switch back to the *command mode*. This tends to be the most difficult concept at the beginning.


## Text editors other than `vi`

Note that independent of your operating system, programs (independent of the programming language), system files (independent of the operating system), LaTeX files and some other must be edited with text editors that don't impose any formatting or hidden characters. Below is a list of some possibilities. The ubiquitous and important `vi` editor is discussed after this. Download are available from the web sites.


### [Atom](https://atom.io/)


[Atom](https://atom.io/) is a very powerful editor with lots of plugins for many tasks. It is available for Windows, Linux and Mac. It also has Git control which may be important depending on your preferences.

### [Visual Studio Code](https://code.visualstudio.com/)

Visual Studio Code is from Microsoft but t is free. It is available for Mac, Windows and Linux. 

### [Brackets](http://brackets.io/)

Another beautiful editor that is available for Mac, Windows and Linux. 

### pico and nano

One (or both) of them come installed with Linux and Mac terminal. They are run from the terminal and are very easy to use.

### [Emacs](https://www.gnu.org/software/emacs/)

Is a very powerful editor that is available for Linux, Mac and Windows. It has a bit of a learning curve, but it depending n your longer terms needs it may be worth it. It has excellent support for various programming languages and LaTeX.

### In Linux there are also others

Such as gedit, kate and so forth. The typically even have GUIs.



