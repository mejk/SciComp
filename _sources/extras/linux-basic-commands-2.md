# Linux: Some basic & useful commands


````{panels}
:column: col-lg-12 p-2

**Learning goals:** 
- To get an overview of the most common Linux commands
- How to find help on your computer
- How to copy, move and remove data and directories
- How to find information about the computer
- How to use wildcards

**Keywords:** Linux CLI commands, finding help on commands, wildcards

<!--
**Associated material:** Cheat sheet of the most common Linux commands.
-->
**More information:**

- [The Linux command line for beginners](https://ubuntu.com/tutorials/command-line-for-beginners)
- [The Linux Command Line by William Shotts](https://linuxcommand.org/)

````

This section lists some of the most important and useful commands with examples. More commands will be introduced later with the introduction of other tools.

<p></p>

Additionally, some notes regarding the difference between Linux (bash shell) and OSX (zsh) are provided.
<p></p>


## How to get help
<hr>

As the very first thing, let's list a couple of methods how to get help using the command line

`man`: <b style="color:#1371a9;">Get help on any command.</b>

To get help on help, try 
```
man man
````

It is instructive to check each of the commands below using man. If for some reason there is no man-page (that's how the manual pages are often called) for a command, that probably means that full documentation was not installed.  


`apropos`:
<b style="color:#1371a9;">
You know what you want to do but cannot remember the command.
</b>

This can return a long list of commands, but it provides a lot of information. For example, to get to know what kind of copying commands are available, try 

```
apropos copy
```
As you can see, the list is very comprehensive.

## Who am I and who is in the system?

<hr>

`whoami`:
<b style="color:#1371a9;">
Who am I. Show my username
</b>

As simple as that. This command doesn't have many options as can be checked using 
```
man whoami
```

    
**Example:** 
```
 sam@linux:~$ whoami 
 sam
```

`who`:
<b style="color:#1371a9;">
Who is logged in the system and the sessions they have
</b>

This shows also the users logged in the system, since when and some other information. The command `who` has lots of options (check using `who`) including
   
- `who -a`: Shows all the users logged in, the last time the system was booted and some other information.
- `who -b`: Shows when the systems was booted the last time. 


**Example 1:**
```
 sam@linux:~$ who 
 sam  tty1         Nov 12 15:21 (:0)
 sam  pts/1        Nov 12 15:21 (:0)
 sam  pts/2        Nov 12 15:21 (:0)
```

**Example 2:** 
```
 sam@linux:~$ who -b
         system boot  Nov 12 14:54
```

**Example 3:** 
```
 sam@linux:~$ who -a
         system boot  Nov 12 14:54
         run-level 5  Nov 12 14:54
 sam  tty1         Nov 12 15:21 (:0)
 sam  pts/1        Nov 12 15:21 (:0)
 sam  pts/2        Nov 12 15:21 (:0)
```

## What is the name of my system and related
<hr>

Below are some of the useful system information commands. There are several more for various purposes, but here only some the more common ones are listed.

`hostname`:
<b style="color:#1371a9;">
Show (can also used to change) hostname (=the name of your computer).
</b> 


The command `hostname` has several options (check using `man hostname`) including


- `hostname -I -a`: Shows your IP addresses.

    
**OSX note:** This command also exists on Mac, but the options are different, check using `man hostname`     


**Example:** 
```
 sam@linux:~$ hostname
 linux
``` 

`uname`:
<b style="color:#1371a9;">
Shows system information. 
</b>

This is a very useful command and it has several options (check using `man uname`) including
- `uname -a`: Shows all information.
- `uname -r`: Shows the kernel release.
- `uname -o`: Shows the operating system.
    
**OSX note:** This command also exists on Mac, but some of the options are different, check using `man hostname`     

    
**Example 1:** 
```
sam@linux:~$ uname 
 Linux
```

    
**Example 2:** 
```
 sam@linux:~$ uname -a
 Linux linux 5.4.0-53-generic #59-Ubuntu SMP Wed Oct 21 09:38:44 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```

`lscpu`:
<b style="color:#1371a9;">
Shows information about your CPUs (list CPU). 
</b>

Has several options (check using `man lscpu`).

    
**OSX note 1:** This command doesn't exist on Mac by default. Instead, you can use the command
```
system_profiler SPHardwareDataType
```
    
**OSX note 2:** It is possible to get the Linux command + some others by installing the package `util-linux` using Homebrew:
```    
brew install util-linux
```

    
**Example** (the output is truncated to fit in a smaller space): 
```
sam@linux:~$ lscpu 
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
Address sizes:                   39 bits physical, 48 bits virtual
CPU(s):                          12
On-line CPU(s) list:             0-11
Thread(s) per core:              2
Core(s) per socket:              6
Socket(s):                       1
NUMA node(s):                    1
Vendor ID:                       GenuineIntel
CPU family:                      6
Model:                           158
Model name:                      Intel(R) Core(TM) i7-9750H CPU @ 2.60GHz
Stepping:                        10
CPU MHz:                         4266.032
CPU max MHz:                     4500.0000
CPU min MHz:                     800.0000
BogoMIPS:                        5199.98
Virtualization:                  VT-x
L1d cache:                       192 KiB
L1i cache:                       192 KiB
L2 cache:                        1.5 MiB
L3 cache:                        12 MiB
NUMA node0 CPU(s):               0-11
Vulnerability Itlb multihit:     KVM: Mitigation: Split huge pages
```

`lsb_release`:
<b style="color:#1371a9;">
Shows distribution specific information. LSB = Linux Standard Base 
</b>

Has options (check using `man lsb_release`).

- `lsb_release -v`: Shows the version.
- `lsb_release -a`: Shows all information.

    
**OSX note:** This command doesn't exist on Mac<br>
    
**Example** (the output is truncated to fit in a smaller space): 
```
sam@linux:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.1 LTS
Release:        20.04
Codename:       focal     
```

## File / directory operations
<hr>

This section focuses on various file operations, such as how to how to see the current work directory, how to list, create, copy and delete files and directories and how to move between directories. The concepts of file permissions and ownership are also discussed. 

### Some special conventions related to files and directories
<hr>

- Single dot (.) refers to the current directory
- Double dots (..) refers to the directory at the next higher level.
- Tilde (~) refers to home directory
- Hidden files start with a dot (.)
- Hyphen (-) refers to the previous directory where you were

### Home directory and work directory / current directory
<hr>

`pwd`: <b style="color:#1371a9;">Show where I am.</b> 

The command `pwd` prints the current directory on screen (also called *work directory* - pwd = print work directory). There are not man options for `pwd` (check using `man pwd`). The `pwd` command shows the full path.

**Example:<p></p>**
```
 sam@linux:~$ pwd   
 /home/sam
```
This means that the user `sam` is currently in his/her home directory.


### Show the files and directories 
<hr>

`ls`: <b style="color:#1371a9;">Show the files and directories, that is, the contents of current directory</b> 

The command `ls` has a lot of useful options as one can see by using `man ls`. Here are some (the option `-l` is used in connection with most of them since it is very useful to see the file/directory details):

- `ls -l`: Long listing, shows the file/directory properties including size, time of last modification, owner and access rights.
- `ls -lt`: The option `-t` lists the files ordered such that the most recently modified is listed first. This is very useful with the option `-l` 
- `ls -ltr`: Using the previous with the option `-r` lists the files in reverse order: such that the most recently modified is listed last.
- `ls -la`: The option `-t` lists all the files including the hidden files that start with a dot.
- `ls -lS`: The option `-S` lists the files with the largest one first.  
- `ls -lh`: The option `-h` lists the files such that size is in a human readable format. This means sizes are given in the form 1k, 1M, 1G. This is very useful.  

    
**Note: The dot directories.**  When using `ls -la`, there are two directories that have the names dot (.) and (..) listed. As described above, dot refers to the current directory and double dot to the one directly above. These can be used when moving around directories as will be done below.  
        
**Note: File details when using the long listing.**      

<!--    
<table class="lblue">
    <tr>
        <td>
            <img src="./img/dot-directories.svg" width="100%"/>
        </td>
    </tr>    
    <tr>
        <td colspan="1">
        Figure: When getting the long listing with the file and other details, this is how it could look like. The dot directories are also shown. The access rights come in three groups, those of the user's, group's and other's. `r`=right to read,`x`=right to execute, `w`=right to write, `-`=no right's given. Dash in the first column means file while `d` stands for directory.  
        </td>
    </tr>
</table>    

-->

```{figure} img/dot-directories.svg
:width: 750px
:name: heart
When getting the long listing with the file and other details, this is how it could look like. The dot directories are also shown. The access rights come in three groups, those of the user's, group's and other's. `r`=right to read,`x`=right to execute, `w`=right to write, `-`=no right's given. Dash in the first column means file while `d` stands for directory. 
```    
    

`tree`: <b style="color:#1371a9;">Show the directory structure.</b> 

<div class="int"> 
This is a neat tool that can be used to view the directory structure.
The command `tree` may already be in your system. To check if that is the case, open a terminal window and type

```
which tree
```

If you see something like 
```
/usr/bin/tree
```
    
Then the command is already installed. If that is not the case, you can do it as follows:

- In Ubuntu/Debian-based systems:
   ```
   sudo apt install tree
   ```

   
Let's check how it works. The command gives the directory tree (as in the Figure) with respect to the argument. If the argument is the root directory `/`, the command

```
tree /
```

prints the directory tree starting from the root level on the screen. You can stop it by pressing

<kbd>ctrl-C</kbd>

**Note:** The keystroke <kbd>ctrl-C</kbd> can always be used to stop a process than runs on your screen. It is *very* useful. There are other ones as well but they will be introduced later.

If the above would be all there is to `tree`, then it wouldn't be super useful. But fortunately it takes different optional arguments. One particularly useful one is the option `-L number` that defines the level. For example, 

```
tree -L 1 /
```
  
shows only one level below the root directory and 

```
tree -L 1 -t /
```

provides listing that is ordered from the ones that was modified the the longest time ago to the latest one.

To get more information about `tree`, simply type

```
man tree
```

on the terminal screen.
    
**OSX note:** If this command is not on your Mac, you can install it using Homebrew

```
brew install tree
```


## Wildcards 
<hr>

Below is a list of common wildcards. They are very useful when searching, listing copying and so on. These should not be mixed up with the conventions listed above. There is a distinction between wildcards and regular expressions, but we are not going to discuss the latter here.

- `*`: match any number (zero or more) of characters. Example: `ls a*` lists all the files and directories starting with the letter a (small a only, capitalization matters).
- `?`: Match a single character.  Example: `ls a?v*` lists files that start with the letter a, the second character can be any character, the third character is small v followed by any number of arbitrary characters. 
- `[ ]`: range of characters. For example `A\[abc\]D`, matches strings that start with the letter A, end to the letter D and have any combination of the characters abc between them. Example: `ls a[dvc]*` lists files that start with an a, then have any combination of dvc followed by any number of any characters. 
- `[! ]`: The exclamation mark is logical not. When used in example `A\[!abc\]D`, matches strings that start with the letter A, end to the letter D but doesn't have any of abc between them. Example: `ls a[!dvc]*` lists files that start with an a, then have no  combination of dvc followed by any number of any characters. 

## Moving between directories
<hr>
Now that we know how to see where we are, and list the files and directories, let's look at how to move between directories.

`cd`: <b style="color:#1371a9;">Change directory.</b>

`cd` means change directory. If you want to move, for example, into your downloads directory (it is assumed that you are in your home directory), type

```
cd Downloads
``` 
    
**Capitalization.** 
 Capitalization matters, usually the downloads directory is spelled with a capital but you can of course check that by using the `ls ` command.   
    
**Using tilde (~) to get your home directory.** 
Tilde is refers to your home directory and it is really handy. For example, to move your home directory from wherever you are, typing
    

```
cd ~
``` 

will take you home. Or, if you want to move from some remote directory to the downloads directory, simply type

```
cd ~/Downloads
``` 
The slash character is needed since it refers to a directory.     

    
**Using plain `cd` to get your home directory.** 
Simply using
    
```
cd
``` 
    
moves you back to your home directory.    

    
**Using double dots  `cd ..` to move up one level.** Simply using

    
```
cd ..
``` 
    
moves you up one level. For example, if you are in the downloads directory, `cd ..` moves back to your home directory since it is one level above, that is, it is the *parent directory*.   


`pushd`: <b style="color:#1371a9;">Switch easily between two (or more) directories.</b>

The command `pushd` adds a directory (or directories) in the directory stack and allows you to move easily between them. In the simplest case, if you are currently located in your home directory, just  type
    
```
pushd ~Downloads
``` 

This adds the directory `Downloads` to the stack and moves you there. Typing 

```
pushd
``` 

takes you back home or whatever is the other directory in the stack (there can be more than one). Executing `pushd` once more takes you to `Downloads`. This is very handy when moving between directories that have long paths.   
    
**How to see which directories are included in the stack?**    

```
dirs -v
```


## Creating and deleting files and directories

<hr>

Now that we know how to see where we are and list the files and directories, let's look at how to create and delete files and directories.

`touch`: <b style="color:#1371a9;">Create an empty file.</b>


Doesn't sound like much of a command but in practise this it is  very useful. In addition to generating new empty files, `touch` can also be used to change the time when a file has been modified. This can be very helpful if the system (like some HPC systems) automatically deletes files older than some specified time if they are in some particular directories (such as temporary work directories).

To create a file called my_text_file.txt, try:

```
touch my_test_file.txt
```
    
`mkdir`: <b style="color:#1371a9;">Create a new directory.</b>
To create a new empty directory, called my_test_directory, try:

```
mkdir my_test_directory
``` 

`rmdir`: <b style="color:#1371a9;">Delete a directory.</b>

To delete a directory, it must be empty (this is a good safeguard). If the directory is not empty, `rmdir` won't do anything. Since the newly created directory is empty, let's delete it:

```
rmdir my_test_directory
``` 

`rm`: <b style="color:#1371a9;">Delete files.</b>

The command `rm` is (obviously) very useful but also potentially *very* dangerous especially some of the options. The dangerous options are listed separately with a warning. 

The command `rm` does not remove directories, empty or not, unless the corresponding option is given, see below. Here are some useful options `rm` takes:

- `rm -v` : Verbose. Does not prompt but tells what was done.
- `rm -i ` : Interactive remove, prompt for every file being removed.
- `rm -d` : Removes empty directories.
 


<!--    
<div class="red"> 
    
 **Important: Be *very* careful with the following options and DO NOT EXECUTE THEM NOW** 

- `rm *`: Deletes *absolutely everything* in the current directory. There is no way to recover any of the files unless there is a separate backup.
- `rm -r *`: Deletes *absolutely everything recursively*. That is, everything including subdirectories are deleted. As the most drastic example, the superuser can delete the whole system if this is accidentally executed at the root directory. 
```
    </div>
</div>    
-->


```{warning}
**Important: Be *very* careful with the following options and DO NOT EXECUTE THEM NOW** 

- ``rm * ``  : Deletes *absolutely everything* in the current directory. There is no way to recover any of the files unless there is a separate backup.
- ``rm -r * ``  : Deletes *absolutely everything recursively*. That is, everything including subdirectories are deleted. As the most drastic example, the superuser can delete the whole system if this is accidentally executed at the root directory. 
```

## Copying, renaming and moving files and directories

<hr>
Now that we know how to see where we are and list the files and directories, let's look at how to create and delete files and directories.


`cp`: <b style="color:#1371a9;">Copy files or/and directories.</b>


The command `cp` has lots of useful options, check using `man ls`. The wildcards listed above are also very useful with this command. Here are some useful options:

- `cp -r`: Copies recursively, that is, copies also subdirectories.
- `cp -p `: This option preserves the date last modified (timestamps), ownership and mode. A very useful option. 
- `cp -i `: Interactive copying. Asks if an existing file should be overwritten or kept.
- `cp -n`: Doesn't allow overwriting existing files.
- `cp -u`: If a file with the same name exists, it is overwritten only of the source file is newer than the existing file at the destination.



`mv`: <b style="color:#1371a9;">Move or rename files and directories.</b>

The command `mv` can be used with both files and directories. Below are some useful options (very similar to `cp`):

- `mv -i `: Interactive mode. Very useful to avoid overwriting files or/and directories.
- `mv -n`: Prevents overwriting existing files/directories.
- `mv -u`: If a file/directory with the same name exists, it is overwritten only of the source is newer than the destination.
 
**Example:** Let's 1) create an empty file, but first check that it is not there, 2) copy it, 3) rename the original, 4) list the files using a wildcard, 4) remove the original, 5) remove the copy as well, and finally 6) check that both of the files have been deleted.  

```
 sam@linux:~$ ls test.txt   
 ls: cannot access 'test.txt': No such file or directory
 sam@linux:~$ touch test.txt  
 sam@linux:~$ ls test.txt   
 test.txt
 sam@linux:~$ cp test.txt test-copy.txt  
 sam@linux:~$ ls test*  
 test.txt test-copy.txt 
 sam@linux:~$ mv test.txt test-original.txt  
 sam@linux:~$ ls test*  
 test-original.txt test-copy.txt  
 sam@linux:~$ rm test-original.txt   
 sam@linux:~$ rm test-copy.txt   
 sam@linux:~$ ls test*
 ls: cannot access 'test*': No such file or directory
```

## What is in your files - seeing file contents

<hr>

At this time we don't have files with content but since we will needs these commands shortly, let's list them briefly and elaborate when we have files with content.

`cat`: <b style="color:#1371a9;">Concatenate files and print on screen (or standard output to be more precise).</b>

`head`: <b style="color:#1371a9;">Show the first 10 lines of a file.</b>

`tail`: <b style="color:#1371a9;">Show the last 10 lines of a file.</b>

`more`: <b style="color:#1371a9;">Show the file contents screenful-by-screenful.</b>

`less`: <b style="color:#1371a9;">Opposite of more.</b>


## Find files and directories
<hr>


`find`: <b style="color:#1371a9;">Find files and directories.</b>

The `find` command is *very* powerful and it has lots of options and different ways to use them. It also finds files and directories very fast. Here, the basic usage with some options are provided. This is how the command works:


```
find [where to search] [criterion for searching (name, type, date of modification...)] [-options] [what to find]
```

    
The command `find` is somewhat more complex than the ones above. It's usage is illustrated with examples:

- `find . -name myfile.txt`: Searches the current directory and any directory below it for a file or directory with the precise name `myfile.txt`.
- `find . -name "myfile*"`: Searches the current directory and any directory below it for a file or directory that start(s) with `myfile`.
- `find . -type d -name MYDIR`: Searches the current directory and any directory below it for a directory (`-type d`) with the precise name `MYDIR`.    
 
    
**Example 1:** Since at this time you don't have (assuming you have a new installation) much on your computer, let's search for something we know have:

```
sam@linux:~$ find . -type d -name Downloads  
./Downloads
```

**Example 2:** Let's us a wildcard:

```
sam@linux:~$ find . -type d -name "Down"  
./Downloads
```

<!--
# More  Linux commands
<hr>

-->

## Compare files, extract information

`diff`:
<b style="color:#1371a9;">
Compare the contents of files
</b>
Usage:

```
diff file1 file2
```
**Example:** Assume that you have two files, one of the is an older version of some text and the other newer. To see the difference (=changes), use

```
diff old.txt new.txt
```


`grep`: 
<b style="color:#1371a9;">
Extract lines with a given pattern from output 
</b>

**Example:** List all the files with details and in chronological order, but print on screen only the ones that have the pattern `txt` in them:

```
ls -lt | grep txt
```

## Linking files

`ln`: <b style="color:#1371a9;">Link two files.</b>

The most common option is `-s` that makes  a symbolic or soft link. 

**Example:** Link the file new.txt to the file target.txt. This means, for example, that if you delete `link.txt` the file that has the actual content (`target.txt`) remains intact or if you edit `link.txt`, the changes will be put in `target.txt` (similarly, if you directly edit `target.txt`, the changes appear immediately in `link.txt`). This is a very handy command.

```
ln -s target.txt link.txt
```

## Processes: View, stop, modify

`ps`: <b style="color:#1371a9;">Change the execution priority.</b>

This is a very useful command. Here are some examples

Show *all* processes:

```
ps -e
```

Show your active processes:

```
ps -a
```

Show *all* of your processes:

```
ps -fe | grep ${USER}
```


`top`: <b style="color:#1371a9;">Show the processes in the system.</b>

Opens a screen (on your terminal) that shows the processes on your computer and, for example, how much memory and CPU they take, and what is their priority. This is a very handy command. You can quit the screen by typing `q`.

`kill`: <b style="color:#1371a9;">Kill/end processes.</b>

Example 1: The following kills the process number 11220
```
kill -9 11220
```

Example 2: The following kills all of your process and logs you out

```
kill -9 -1
```

`nice`: <b style="color:#1371a9;">Change the execution/scheduling priority.</b>

Priority `-20` is the highest and `+19` the lowest priority. This is important since, when you run your simulations, you should set the priority of the simulation as `+19`. When you do that, the simulation has the lowest priority meaning that you can also use the computer do something else when needed but when you are not using it for other tasks, your simulation will take full resources.


## File permissions and ownership
<hr>

`chmod`: <b style="color:#1371a9;">Change the access rights.</b>

This is a very useful command. 

````{dropdown} Click for a figure showing file details, access rights & ownership
```{figure} img/dot-directories.svg
:width: 750px
:name: directories
When getting the long listing with the file and other details, this is how it could look like. The dot directories are also shown. The access rights come in three groups, those of the user's, group's and other's. `r`=right to read,`x`=right to execute, `w`=right to write, `-`=no right's given. Dash in the first column means file while `d` stands for directory. 
```    
````

`chown`: <b style="color:#1371a9;">Change ownership.</b>

**Example:** Assume that you edited a file `text.txt` as the superuser and now you want to Change the ownership the the user `sam` who belongs to the group `users` (you can see the user and the group by using the option `-l` with `ls`):

```
sudo chown sam:users text.txt
```



## Environment

`printenv`: <b style="color:#1371a9;">Show the environment variables</b>

**Example:** See all the environment variables that have the text `PATH` in them (capitalization matters):

```
printenv |  grep PATH
```

<!--
`sort`: <b style="color:#1371a9;">As the name says, sorts.</b>

`env`: <b style="color:#1371a9;">Move.</b>


`export`: <b style="color:#1371a9;">Move.</b>
-->



<!--
## Beyond the terminal: Shell scripting
<hr>

-->
