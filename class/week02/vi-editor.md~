# The `vi` editor

````{panels}
:column: col-lg-12 p-2

**This file:** 
- Provides the basic instructions for using the `vi` editor.

**Keywords:** ASCII, `vi`, *command mode*, *insert mode*, `vim`



**Associated material:** 

- [Editing ASCII files](./editing-ascii)


````

The `vi` editor is the basic [ASCII](https://en.wikipedia.org/wiki/ASCII) text editor that comes with essentially all Linux/Unix systems. It works on the command line without GUI. It is very lightweight. 

`vi` differs from most editors (with or without GUI) in that it has two modes: 1) *command mode* and 2) *editing or insert mode*. As the names suggest, these modes serve for different purposes. In the *command mode*, one can enter commands such as `copy`, `paste`, `save`, `quit` and so on. Editing text is not possible in the command mode. For editing text, one has to enter the *editing or insert mode*. That mode is exclusively for editing text and for saving the file, one has to switch to *command mode*. Understanding the two modes is the key to using the `vi` editor.

## Why `vi`

First, since it ships with all Linux/Unix systems, it is always there without any additional installations. Second, is also extremely lightweight. Those two factors are very important if something goes wrong with the systems and some of the system files need to be edited; in such case no GUI based editors (even if they are ASCII editors) may be impossible to use.  Although switching between the modes may sound cumbersome, it is very easy to get used to that and `vi` is a favorite of many.

## Switching between the modes

- When `vi` is started, it is always in the command mode.
- Commands are *case sensitive*
- Switch from the *command mode* to the *insert mode*: press the key `i`.
- Switch from the *insert mode* to the *command mode*: press the `esc` key.

## Starting `vi`

To open a file or to create a new file, simply type

```
vi filename.txt
```

If `filename.txt` exists it will be simply opened. If it doesn't exist, it will be created.


````{tabbed} Starting vi

```{figure} ../images/vi-insert-mode.png
:alt: vi
:width: 650px
:align: center
```

````

````{tabbed} Searching in vi

```{figure} ../images/vi-insert-search.png
:alt: vi search
:width: 600px
:align: center
```

````

````{tabbed} Saving in vi

```{figure} ../images/vi-save.png
:alt: vi save
:width: 600px
:align: center
```

````

## `vi` command summary

Below is a summary of some of the most common commands. Open a test file and try them.


| COMMAND  (the commands must be given in the *command mode*) | FUNCTION | NOTES  |
|------------------|------------|---|
| `vi filename.txt` | edit/create a file called `filename.txt` | On the command line terminal. Starts `vi` in *command mode* | 
| `i`           | Switch to *insert mode* | Shows the text `-- INSERT --` at the bottom of the screen |
| `esc`    | Switch to *command mode* | |
|     `x`     |     delete character to the right of the cursor | |
|     `4x`    |    delete 4 characters (to the right of the cursor) | |
|     `X`     |    delete character to the left of the cursor | |
|     `dw`    |    delete word to the right of the cursor | |
|     `2dw`   |    delete 2  words to the right of the cursor ||
|     `dd`    |    delete the current line | |
|     `2dd`   |    delete 2 (current and the next) lines | |
|     `D`     |    delete all characters from the cursor to end of the line |  |
|     `o`     |    insert an empty line below the cursor |  Switches to *insert mode* |
|     `O`     |    insert an empty line above the cursor |  Switches to *insert mode* |
|     `r`     |    replace the character under the cursor|  Switches to *insert mode* |
|     `a`     |     append text to the right of the cursor | Switches to *insert mode* |
|     `cw`    |    replace  the word |    Switches to *insert mode* |
|     `3cw`   |    replace 3 words (to the right; leaves the rest the line after the two words intact) | Switches to *insert mode* |
|     `C`     |    delete the text from cursor to end of line | Switches to *insert mode* |
|     `J`     |    join the line below to the current  line | Switches to *insert mode*. The cursor can be anywhere on the line |
|     `3J`    |    join the 3 following lines below to the current line | Switches to *insert mode*. The cursor can be anywhere on the line |
|     `u`     |    undo  |   Switches to *insert mode* |
|     `ZZ`    |   save the file and quit |  Switches to *insert mode* |
|     `:w`    |   save the file | Switches to *insert mode* |
|     `:w newname.txt` |  save the file with name `newname.txt` | Switches to *insert mode* |
|     `:r name.txt` |  read text into the current file from  file  named `name.txt` | Switches to *insert mode* |
|     `:wq`   |   save the file and quit |  Switches to *insert mode* |
|     `:q!`   |   discard all changes since last save  and quit  | Switches to *insert mode* |
|  `w`   |  move forward word-by-word | |
|  `b`   | move backward word-by-word | |
|  `$ `  | move to the end of the current line | |
|  `0`   | move to the beginning of the current line | |
|  `H`   | go  to the top line of the current screen | |
|  `M`      |go to the middle line of the current screen | |
|  `L`      | go to last line of the current screen | |
|  `G`      | go to the last line of the file | |
|  `1G`     | go  to first line of the file | |
|  `Ctrl-f` | scroll forward one screen | |
|  `Ctrl-b` | scroll backward one screen | |
|  `Ctrl-d` | scroll down one-half screen | |
|  `Ctrl-u` | scroll up one-half screen | |
| `:/` *keyword* + `return` | search for *keyword* in the current text |  To repeat the search forward press `n`, backward: `N` |
| `:s/` *keyword* + `return` | search for *keyword* in the current line |  To repeat the search forward press `n`, backward: `N` |
| `:s/word1/word2` + `return` | search for `word1` on the current line AND replace it by `word2` |  in *command mode*.  |
| `:%s/word1/word2` + `return` | search for all occurrences of `word1` AND replace them by `word2` |  in *command mode*.  |



## `vi` cursor movements:

Instead of using the arrows, the cursors (in *command mode*) can be moved using the following keys:

| COMMAND | FUNCTION | 
|------|------------------|
| `h`  |   move left one space |
| `j`  |   move down one line |
| `k`  |   move up one line |
| `l`  |   move right one space |


## `vi` in readonly-mode

`vi` can also be used in readonly-mode. The search and movement functions work as listed above, but editing and saving is not possible in the readonly mode. Here's how:

```
vi -R filename.txt
```

## `vim` the basic `vi` improved

`vim` is an improved `vi` and a very popular ASCII text editor - `vi` and `vim` are arguably the most popular text editor in Linux/Unix. `vim` adds several features to the basic `vim` and all of the above commands work also in `vim`. It comes (just like the basic `vi`) with most (if not all) current Linux/Unix systems as well as Mac. 

`vim` stands for *Vi IMproved*. It adds features to the basic `vi` and is highly customizable. It also has many plugins including `git` integration and a scripting language. `vim` is available for essentially all operating systems including iOS and Android.









