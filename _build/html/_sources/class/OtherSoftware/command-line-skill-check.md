# Test your skills: Command line


````{panels}
:column: col-lg-12 p-2

**Learning goals:** 
- Check your command line skills.

**Keywords:** Linux CLI commands, finding help on commands, wildcards

<!--
**Associated material:** Cheat sheet of the most common Linux commands.
-->
**More information:**

- [The Linux command line for beginners](https://ubuntu.com/tutorials/command-line-for-beginners)
- [The Linux Command Line by William Shotts](https://linuxcommand.org/)

````

<p></p>


## Test your skills

The following expects that you have read and worked through the material in this module.

* Allowing only for a single press of the `Return` key (=the command/string of commands has to be given on one line only and not as a series of commands), find out all the information regarding your CPU and its properties.

` `

* What is the command that can list all files starting with `n` *and* the third letter being also `n` in the directory `/bin`? 

` `

* Allowing only for a single press of the `Return` key (=the command/string of commands has to be given on one line only and not as a series of commands), give the command that lists all the files and directories under the directory `/usr` such that the full path is visible (=information where they are located in the directory structure shows up).

` `

* Allowing only for a single press of the `Return` key (=the command/string of commands has to be given on one line only and not as a series of commands), give the command that lists all the files that start with either the letter `z` or the letter `y` under the directory `/bin` in such a way that listing ordered from the smallest to the largest file and the file sizes are listed in K, M, G etc.

` `

* Important: Document each step and have screen shots when editing the files and printing the outputs of commands. First ensure that you are in your home directory. If you created the course directory as discussed in the Linux module move there or, alternatively, create a new directory for this exercise (it is a good idea since files and directories will be created).  Check both your username and path, and create a new directory called `TESTING` inside the course directory (or the directory that you created). Move inside that directory and create two new empty files without opening the files with an editor. Call the files `mytext_1.txt` and `mytext_2.txt`. Using the `vi` editor (instructions for `vi` are provided at the course web site if you have no previous experience),  edit the files such that the first one has the text:
    ```
    This is my first file.
    ```
    And the second file should have the text:
    ```
    This is my second file.
    ```
    Make sure that you have saved the files. Using a single command and without opening the files, compare the differences between the two files.

` `

* Using a single command, append the following text in `mytext_1.txt`:
    ```
    This text goes in mytext_1.
    ```
    Repeat the comparison between `mytext_1.txt` and `mytext_2.txt` from the previous problem.

` `

* Link a new file `mytext_temp.txt` to `mytext_1.txt`. Show also that the linking worked and show the contents of the new file. Note: This is not the same as copying using `cp`. Use `vi` to edit `mytext_1.txt` and add the following text in it:
    ```
    Written after linking.
	```
    Show the contents of `mytext_tmp.txt` on screen without opening `vi`.

` `

* Delete the files that have names starting `mytex` such a way that you have to confirm each deletion. Then move to the main course directory and delete the directory `TESTING`.

` `

* Open the `vi` editor. Then, open a new terminal window and keep `vi` running in the other. Next, in the new window, list all the processes that `vi` has. Finally, using command line in the second terminal (=not using `vi`), terminate `vi` and show that it has been terminated. 

` `

* Using a single command, find the information about your current display *and* system language.

