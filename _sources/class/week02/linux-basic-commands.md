# Basic Linux commands

````{panels}
:column: col-lg-12 p-2

**Learning goals:** 
- To get an overview of the most common Linux commands
- How to find help on your computer
- How to copy, move and remove data and directories
- How to find information about the computer
- How to use wildcards

**Keywords:** Linux CLI commands, finding help on commands, wildcards

**Associated material:** Cheat sheet of the most common Linux commands.

**More information:**

- [The Linux command line for beginners](https://ubuntu.com/tutorials/command-line-for-beginners)
- [The Linux Command Line by William Shotts](https://linuxcommand.org/)

````

This section lists some of the most important and useful commands with examples. More commands will be introduced later with the introduction of other tools.

<p></p>

Additionally, some notes regarding the difference between Linux (bash shell) and OSX (zsh) are provided.
<p></p>

```{warning}
**Important:** When there is a warning sign, take it *very* seriously as there are a few commands that are dangerous!  
```
If there are commands or concepts you don't understand, please ask during the next class or/and used commenting tool given at the top right hand corner of the page.



## How to get help
<hr>

As the very first thing, let's list a couple of methods how to get help using the command line

<ins><code>man</code>: <b style="color:#1371a9;">Get help on any command.</b></ins>
<div class="int">
To get help on help, try <code>man man</code>.

<p></p>
It is instructive to check each of the commands below using man. If for some reason there is no man-page (that's how the manual pages are often called) for a command, that probably means that full documentation was not installed.  
</div>

```
man man    
```

<ins><code>apropos</code>:
<b style="color:#1371a9;">You know what you want to do but cannot remember the command.</b></ins> 

<div class="int">
This can return a long list of commands, but it provides a lot of information. For example, to get to know what kind of copying commands are available, try 
    <p></p>
    <code>apropos copy</code>
</div>
<p></p>
As you can see, the list is very comprehensive.

## Who am I and who is in the system?
<hr>

<ins><code>whoami</code>:
<b style="color:#1371a9;">Who am I. Show my username</b></ins> 

<div class="int">
    As simple as that. This command doesn't have many options as can be checked using <code>man whoami</code>
    <p></p>
</div>

<div class="int">
    
**Example:** 
<p></p>
<div class="clblue">
<pre>
 sam@linux:~$ whoami 
 sam
</pre>
</div>

</div>

<ins><code>who</code>:
<b style="color:#1371a9;">Who is logged in the system and the sessions they have</b></ins> 

<div class="int">
This shows also the users logged in the system, since when and some other information. The command <code>who</code> has lots of options (check using <code>who</code>) including
<p></p>
<ul>    
<li> <code>who -a</code>: Shows all the users logged in, the last time the system was booted and some other information.
<li> <code>who -b </code>: Shows when the systems was booted the last time. being removed.
</ul>
    
<p></p>  
</div>

<div class="int">

**Example 1:**
<p></p>
<div class="clblue">
<pre>
 sam@linux:~$ who 
 sam  tty1         Nov 12 15:21 (:0)
 sam  pts/1        Nov 12 15:21 (:0)
 sam  pts/2        Nov 12 15:21 (:0)
</pre>
</div>
</div>

<div class="int">

**Example 2:** 
<p></p>
<div class="clblue">
<pre>
 sam@linux:~$ who -a
         system boot  Nov 12 14:54
</pre>
</div>

</div>


```python

```

<div class="int">

**Example 3:** 
<p></p>
<div class="clblue">
<pre>
 sam@linux:~$ who 
         system boot  Nov 12 14:54
         run-level 5  Nov 12 14:54
 sam  tty1         Nov 12 15:21 (:0)
 sam  pts/1        Nov 12 15:21 (:0)
 sam  pts/2        Nov 12 15:21 (:0)
</pre>
</div>
</div>

## What is the name of my system and related
<hr>

Below are some of the useful system information commands. There are several more for various purposes, but here only some the more common ones are listed.

<ins><code>hostname</code>:
<b style="color:#1371a9;">Show (can also used to change) hostname (=the name of your computer).</b></ins> 

<div class="int">
The command <code>hostname</code> has several options (check using <code>man hostname</code>) including
<p></p>
<ul>    
<li> <code>hostname -I -a</code>: Shows your IP addresses.
</ul>
    
**OSX note:** This command also exists on Mac, but the options are different, check using <code>man hostname</code>     
<p></p>  
</div>

<div class="int">
    
**Example:** 
<p></p>
<div class="clblue">
<pre>
 sam@linux:~$ hostname
 linux
</pre>
</div>

</div>

<ins><code>uname</code>:
<b style="color:#1371a9;">Shows system information. </b></ins> 

<div class="int">
This is a very useful command and it has several options (check using <code>man uname</code>) including
<p></p>
<ul>    
<li> <code>uname -a</code>: Shows all information.
<li> <code>uname -r</code>: Shows the kernel release.
<li> <code>uname -o</code>: Shows the operating system.
<p></p> 
</ul>
    
**OSX note:** This command also exists on Mac, but some of the options are different, check using <code>man hostname</code>     

 
</div>

<div class="int">
    
**Example 1:** 
<p></p>
<div class="clblue">
<pre>
 sam@linux:~$ uname 
 Linux
</pre>
</div>
</div>

<div class="int">
    
**Example 2:** 
<p></p>
<div class="clblue">
<pre>
 sam@linux:~$ uname -a
 Linux linux 5.4.0-53-generic #59-Ubuntu SMP Wed Oct 21 09:38:44 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
</pre>
</div>
</div>

<ins><code>lscpu</code>:
<b style="color:#1371a9;">Shows information about your CPUs (list CPU). </b></ins> 

<div class="int">
Has several options (check using <code>man lscpu</code>).
<p></p>

    
**OSX note 1:** This command doesn't exist on Mac by default. Instead, you can use the command<br>
 <code>system_profiler SPHardwareDataType</code>     
<p></p>
    
**OSX note 2:** It is possible to get the Linux command + some others by installing the package <code>util-linux</code> using Homebrew:
    
 <code>brew install util-linux</code>
 
</div>

<div class="int">
    
**Example** (the output is truncated to fit in a smaller space): 
<p></p>
<div class="clblue">
<pre>
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
</pre>
</div>
</div>

<ins><code>lsb_release</code>:
<b style="color:#1371a9;">Shows distribution specific information. LSB = Linux Standard Base </b></ins> 

<div class="int">
Has options (check using <code>man lsb_release</code>).
<p></p>
<p></p>
<ul>    
<li> <code>lsb_release -v</code>: Shows the version.
<li> <code>lsb_release -a</code>: Shows all information.
<p></p> 
</ul>    

    
**OSX note:** This command doesn't exist on Mac<br>
<p></p>
    </div>

<div class="int">
    
**Example** (the output is truncated to fit in a smaller space): 
<p></p>
<div class="clblue">
<pre>
sam@linux:~$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.1 LTS
Release:        20.04
Codename:       focal     
</pre>
    </div>    

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

<ins><code>pwd</code>: <b style="color:#1371a9;">Show where am I.</b> 
<div class="int">
The command <code>pwd</code> prints the current directory on screen (also called *work directory* - pwd = print work directory). There are not man options for <code>pwd</code> (check using <code>man pwd</code>). The <code>pwd</code> command shows the full path.
</div>
<p></p>


<div class="int">

**Example:<p></p>**
<div class="clblue">
<pre>
 sam@linux:~$ pwd   
 /home/sam
</pre>
</div>
<p></p>
This means that the user sam is currently in his/her home directory.
</div>

### Show the files and directories 
<hr>

<ins><code>ls</code>: <b style="color:#1371a9;">Show the files and directories, that is, the contents of current directory</b> </ins>

<div class="int"> 
The command <code>ls</code> has a lot of useful options as one can see by using <code>man ls</code>. Here are some (the option <code>-l</code> is used in connection with most of them since it is very useful to see the file/directory details):
<p></p>
<ul>    
<li> <code>ls -l</code>: Long listing, shows the file/directory properties including size, time of last modification, owner and access rights.
<li> <code>ls -lt</code>: The option <code>-t</code> lists the files ordered such that the most recently modified is listed first. This is very useful with the option <code>-l</code> 
<li> <code>ls -ltr</code>: Using the previous with the option <code>-r</code> lists the files in reverse order: such that the most recently modified is listed last.
<li> <code>ls -la</code>: The option <code>-t</code> lists all the files including the hidden files that start with a dot.
<li> <code>ls -lS</code>: The option <code>-S</code> lists the files with the largest one first.  
<li> <code>ls -lh</code>: The option <code>-h</code> lists the files such that size is in a human readable format. This means sizes are given in the form 1k, 1M, 1G. This is very useful.  
</ul>
    
**Note: The dot directories.**  When using <code>ls -la</code>, there are two directories that have the names dot (.) and (..) listed. As described above, dot refers to the current directory and double dot to the  directory above. These can be used when moving around directories as will be done below.  
        
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
        Figure: When getting the long listing with the file and other details, this is how it could look like. The dot directories are also shown. The access rights come in three groups, those of the user's, group's and other's. <code>r</code>=right to read,<code>x</code>=right to execute, <code>w</code>=right to write, <code>-</code>=no right's given. Dash in the first column means file while <code>d</code> stands for directory.  
        </td>
    </tr>
</table>    

-->

```{figure} img/dot-directories.svg
:width: 750px
:name: heart
When getting the long listing with the file and other details, this is how it could look like. The dot directories are also shown. The access rights come in three groups, those of the user's, group's and other's. <code>r</code>=right to read,<code>x</code>=right to execute, <code>w</code>=right to write, <code>-</code>=no right's given. Dash in the first column means file while <code>d</code> stands for directory. 
```    
    
</div>



<ins><code>tree</code>: <b style="color:#1371a9;">Show the directory structure.</b> </ins>

<div class="int"> 
This is a neat tool that can be used to view the directory structure.
The command <code>tree</code> may already be in your system. To check if that is the case, open a terminal window and type
<p></p>
   <code>which tree</code>
<p></p>

If you see something like 
```
/usr/bin/tree
```
<p></p>
    
Then the command is already installed. If that is not the case, you can do it as follows:

- In Ubuntu/Debian-based systems:<br>
   <code>sudo apt install tree</code>

   
Let's check how it works. The command gives the directory tree (as in the Figure) with respect to the argument. If the argument is the root directory <code class="wlblue">/</code>, the command

   <code>tree /</code>

prints the directory tree starting from the root level on the screen. You can stop it by pressing

<kbd>ctrl-C</kbd>

**Note:** The keystroke <kbd>ctrl-C</kbd> can always be used to stop a process than runs on your screen. It is *very* useful. There are other ones as well but they will be introduced later.

If the above would be all there is to <code>tree</code>, then it wouldn't be super useful. But fortunately it takes different optional arguments. One particularly useful one is the option <code>-L number</code> that defines the level. For example, 

  <code>tree -L 1 /</code>
  
shows only one level below the root directory and 

  <code>tree -L 1 -t /</code>

provides listing that is ordered from the ones that was modified the the longest time ago to the latest one.

To get more information about <code>tree</code>, simply type

<code>man tree</code>

on the terminal screen.
    
**OSX note:** If this command is not on your Mac, you can install it using homebrew

<p></p>    
    <code>brew install tree</code>
<p></p>
    
</div>    

### Wildcards 
<hr>

Below is a list of common wildcards. They are very useful when searching, listing copying and so on. These should not be mixed up with the conventions listed above. There is a distinction between wildcards and regular expressions, but we are not going to discuss the latter here.

- <code>*</code>: match any number (zero or more) of characters. Example: <code>ls a*</code> lists all the files and directories starting with the letter a (small a only, capitalization matters).
- <code>?</code>: Match a single character.  Example: <code>ls a?v*</code> lists files that start with the letter a, the second character can be any character, the third character is small v followed by any number of arbitrary characters. 
- <code>[ ]</code>: range of characters. For example A\[abc\]D, matches strings that start with the letter A, end to the letter D and have any combination of the characters abc between them. Example: <code>ls a[dvc]*</code> lists files that start with an a, then have any combination of dvc followed by any number of any characters. 
- <code>[! ]</code>: The exclamation mark is logical not. When used in example A\[!abc\]D, matches strings that start with the letter A, end to the letter D but doesn't have any of abc between them. Example: <code>ls a[!dvc]*</code> lists files that start with an a, then have no  combination of dvc followed by any number of any characters. 

### Moving between directories
<hr>
Now that we know how to see where we are, and list the files and directories, let's look at how to move between directories.

<ins><code>cd</code>: <b style="color:#1371a9;">Change directory.</b></ins>

<div class="int">
<code>cd</code> means change directory. If you want to move, for example, into your downloads directory (it is assumed that you are in your home directory), type<p></p>
    <code>cd Downloads</code> 
    <p></p>    
    
  **Capitalization.** Capitalization matters, usually the downloads directory is spelled with a capital but you can of course check that by using the <code>ls </code> command.   
    <p></p>
    
**Using tilde (~) to get your home directory.** Tilde is refers to your home directory and it is really handy. For example, to move your home directory from wherever you are, typing
    
<p></p>
    <code>cd ~</code> 
    <p></p>      
will take you home. Or, if you want to move from some remote directory to the downloads directory, simply type
<p></p>
    <code>cd ~/Downloads</code> 
    <p></p>
The slash character is needed since it refers to a directory.     
   <p></p>
    
**Using plain <code>cd</code>to get your home directory.** Simply using
    
<p></p>
    <code>cd</code> 
    <p></p> 
    
moves you back to your home directory.    
    <p></p> 
    
**Using double dots  <code>cd ..</code>to move up one level.** Simply using
    
<p></p>
    <code>cd ..</code> 
    <p></p>     
    
moves you up one level. For example, if you are in the downloads directory, <code>cd ..</code> moves back to your home directory since it is one level above, that is, it is the *parent directory*.   
    <p></p>     
    
<p></p>    
</div>

<ins><code>pushd</code>: <b style="color:#1371a9;">Switch easily between two (or more) directories.</b></ins>

<div class="int">
The command <code>pushd</code> adds a directory (or directories) in the directory stack and allows you to move easily between them. In the simplest case, if you are currently located in your home directory, just  type<p></p>
    <code>pushd ~Downloads</code> 
    <p></p>  

This adds the directory <code>Downloads</code> to the stack and moves you there. Typing 
<p></p>
    <code>pushd </code> 
    <p></p>

takes you back home or whatever is the other directory in the stack (there can be more than one). Executing <code>pushd</code> once more takes you to <code>Downloads</code>. This is very handy when moving between directories that have long paths.   
    
**How to see which directories are included in the stack?**    
    <p></p>
    <code>dirs -v</code> 
    <p></p>  

### Creating and deleting files and directories
<hr>
Now that we know how to see where we are and list the files and directories, let's look at how to create and delete files and directories.

<ins><code>touch</code>: <b style="color:#1371a9;">Create an empty file.</b></ins>

<div class="int">
Doesn't sound like much of a command but in practise this it is  very useful. In addition to generating new empty files, <code>touch</code> can also be used to change the time when a file has been modified. This can be very helpful if the system (like some HPC systems) automatically deletes files older than some specified time if they are in some particular directories (such as temporary work directories).
    <p></p>
To create a file called my_text_file.txt, try:
    <p></p>    
<code>touch my_test_file.txt</code>
    
<div class="int">    

<ins><code>mkdir</code>: <b style="color:#1371a9;">Create a new directory.</b></ins>
<div class="int">
To create a new empty directory, called my_test_directory, try:
    <p></p>    
<code>mkdir my_test_directory</code> 
    </div>
<p></p>
<ins><code>rmdir</code>: <b style="color:#1371a9;">Delete a directory.</b></ins>
<div class="int">
To delete a directory, it must be empty (this is a good safeguard). If the directory is not empty, <code>rmdir</code> won't do anything. Since the newly created directory is empty, let's delete it:
    <p></p>    
<code>rmdir my_test_directory</code> 
    </div>

<ins><code>rm</code>: <b style="color:#1371a9;">Delete files.</b></ins>

<div class="int">The command <code>rm</code> is (obviously) very useful but also potentially *very* dangerous especially some of the options. The dangerous options are listed separately with a warning. 
    <p></p>
The command <code>rm</code> does not remove directories, empty or not, unless the corresponding option is given, see below. Here are some useful options <code>rm</code> takes:
<p></p>
<ul>    
<li> <code>rm -v</code> : Verbose. Does not prompt but tells what was done.
<li> <code>rm -i </code> : Interactive remove, prompt for every file being removed.
<li> <code>rm -d</code> : Removes empty directories.
 
</ul>
    
<p></p>    

<!--    
<div class="red"> 
    
 **Important: Be *very* careful with the following options and DO NOT EXECUTE THEM NOW** 

- <code>rm *</code>: Deletes *absolutely everything* in the current directory. There is no way to recover any of the files unless there is a separate backup.
- <code>rm -r *</code>: Deletes *absolutely everything recursively*. That is, everything including subdirectories are deleted. As the most drastic example, the superuser can delete the whole system if this is accidentally executed at the root directory. 
```
    </div>
</div>    
-->


```{warning}
**Important: Be *very* careful with the following options and DO NOT EXECUTE THEM NOW** 

- ``rm * ``  : Deletes *absolutely everything* in the current directory. There is no way to recover any of the files unless there is a separate backup.
- ``rm -r * ``  : Deletes *absolutely everything recursively*. That is, everything including subdirectories are deleted. As the most drastic example, the superuser can delete the whole system if this is accidentally executed at the root directory. 
```

### Copying, renaming and moving files and directories
<hr>
Now that we know how to see where we are and list the files and directories, let's look at how to create and delete files and directories.

<ins><code>cp</code>: <b style="color:#1371a9;">Copy files or/and directories.</b></ins>

<div class="int">
The command <code>cp</code> has lots of useful options, check using <code>man ls</code>. The wildcards listed above are also very useful with this command. Here are some useful options:
<p></p>
<ul>    
<li> <code>cp -r</code>: Copies recursively, that is, copies also subdirectories.
<li> <code>cp -p </code>: This option preserves the date last modified (timestamps), ownership and mode. A very useful option. 
<li> <code>cp -i </code>: Interactive copying. Asks if an existing files should be overwritten or kept.
<li> <code>cp -n</code>: Doesn't allow overwriting existing files.
<li> <code>cp -u</code>: If a file with the same name exists, it is overwritten only of the source file is newer than the existing file at the destination.
 
</ul>
    
</div>
    


<ins><code>mv</code>: <b style="color:#1371a9;">Move or rename files and directories.</b></ins>

<div class="int">
The command <code>mv</code> can be used with both files and directories. Below are some useful options (very similar to <code>cp</code>):
<p></p>
<ul>    
<li> <code>mv -i </code>: Interactive mode. Very useful to avoid overwriting files or/and directories.
<li> <code>mv -n</code>: Prevents overwriting existing files/directories.
<li> <code>mv -u</code>: If a file/directory with the same name exists, it is overwritten only of the source is newer than the destination.
 
</ul>    
</div>    

<div class="int">
<p></p>
    
**Example:** Let's 1) create an empty file, but first check that it is not there, 2) copy it, 3) rename the original, 4) list the files using a wildcard, 4) remove the original, 5) remove the copy as well, and finally 6) check that both of the files have been deleted.  <p></p>
<div class="clblue">
<pre>
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
</pre>
</div>
</div>

## What is in your files - seeing file contents
<hr>

At this time we don't have files with content but since we will needs these commands shortly, let's list them briefly and elaborate when we have files with content.

<ins><code>cat</code>: <b style="color:#1371a9;">Concatenate files and print on screen (or standard output to be more precise).</b></ins>

<div class="int">
<p></p>
<ul>    
</ul>    
</div>    

<ins><code>head</code>: <b style="color:#1371a9;">Show the first 10 lines of a file.</b></ins>

<div class="int">
<p></p>
<ul>    
</ul>    
</div>    

<ins><code>head</code>: <b style="color:#1371a9;">Show the first 10 lines of a file.</b></ins>

<div class="int">
<p></p>
<ul>    
</ul>    
</div>    

<ins><code>tail</code>: <b style="color:#1371a9;">Show the last 10 lines of a file.</b></ins>

<div class="int">
<p></p>
<ul>    
</ul>    
</div>    

<ins><code>more</code>: <b style="color:#1371a9;">Show the file contents screenful-by-screenful.</b></ins>

<div class="int">
<p></p>
<ul>    
</ul>    
</div>    

<ins><code>less</code>: <b style="color:#1371a9;">Opposite of more.</b></ins>

<div class="int">
<p></p>
<ul>    
</ul>    
</div>    

## Find files and directories
<hr>


<ins><code>find</code>: <b style="color:#1371a9;">Find files and directories.</b></ins>
<p></p>
<div class="int">
    The <code>find</code> command is <em>very</em> powerful and it has lots of options and different ways to use them. It also finds files and directories very fast. Here, the basic usage with some options are provided. This is how the command works:
<p></p>

<code>find [where to search] [criterion for searching (name, type, date of modification...)] [-options] [what to find]</code>    
<p></p>

    
The command <code>find</code> is somewhat more complex than the ones above. It's usage is illustrated with examples:
<p></p>
<ul>    
<li> <code>find . -name myfile.txt</code>: Searches the current directory and any directory below it for a file or directory with the precise name myfile.txt.
<li> <code>find . -name "myfile*"</code>: Searches the current directory and any directory below it for a file or directory that start(s) with myfile.
<li><code>find . -type d -name MYDIR</code>: Searches the current directory and any directory below it for a directory (-type d) with the precise name MYDIR.    
 
 
</ul>    
</div>       

<div class="int">
<p></p>
    
**Example 1:** Since at this time we don't have (assuming you have a new installation) much on your computer, let's search for something we know have:<p></p>
<div class="clblue">
<pre>
sam@linux:~$ find . -type d -name Downloads  
./Downloads
</pre>
</div>
</div>

<div class="int">
<p></p>
    
**Example 2:** Let's us a wildcard:<p></p>
<div class="clblue">
<pre>
sam@linux:~$ find . -type d -name "Down"  
./Downloads
</pre>
</div>
</div>

## Beyond the terminal: Shell scripting
<hr>




# Basic Linux commands, part 2
<hr>
Additionally, some notes regarding difference to OSX are provided.



### Compare files

<ins><code>diff</code></ins>

### Linking files

<ins><code>ln</code></ins>

## Processes: View, stop, modify

<ins><code>ps</code></ins>

<ins><code>top</code></ins>

<ins><code>kill</code></ins>

<ins><code>nice</code></ins>

### File permissions and ownership
<hr>

<ins><code>chmod</code>: <b style="color:#1371a9;">Move or rename files and directories.</b></ins>



<ins><code>chown</code>: <b style="color:#1371a9;">Move or rename files and directories.</b></ins>




<ins><code>grep</code>: <b style="color:#1371a9;">Move </b></ins>




<ins><code>sort</code>: <b style="color:#1371a9;">Move.</b></ins>




<ins><code>printenv</code>: <b style="color:#1371a9;">Move.</b></ins>




<ins><code>env</code>: <b style="color:#1371a9;">Move.</b></ins>




<ins><code>export</code>: <b style="color:#1371a9;">Move.</b></ins>



