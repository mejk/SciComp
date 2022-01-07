# Gromacs installation


````{panels}
:column: col-lg-12 p-2


```{image} ../../images/logos/gromacs-logo.png
:alt: Gromacs
:class: bg-light
:width: 250px
:align: right
```

**Learning goals:** 
- To learn the idea how to build and compile software, and troubleshoot should problems arise
- To understand the idea of software dependencies
- To understand how to use shell/environment variables.
- To install Gromacs

**Keywords:** Gromacs, gcc, g++, Makefile, cmake, building software, environment variable, dot files

**Important:** The compilation and testing processes are CPU intensive. It is *very* important to ensure that you have not blocked the ventilation. Blocking them may cause overheating and, in the worst case, damage. 

**Notes:** The procedure below has been tested on 
- Three different Linux installations using Ubuntu 20.04 LTS with gcc9
- In WSL/WSL2 (Ubuntu 20.04 LTS with gcc9) under Windows 10
- iMac (Catalina, 10.15.7), 3.6 GHz i7 with `gcc` and `g++` version 8 compilers. The Mac default `clang` 11 compiler produced errors.
- Using NVIDIA GPU (CUDA 11.2)
- Instructions for Linux & WSL/WSL2 and Mac are given in separate tabs when there are differences. Also steps for NVIDIA GPUs are indicated when different from the standard Linux installation.


<!--
**Associated material:** Cheat sheet of the most common Linux commands.
-->

````
The instructions below provide a step-by-step guide. The procedure has been tested on several computers using WSL in Windows 10 as well various flavors of Linux. It is also very easy to adjust the installation process to any version of Gromacs or to have multiple versions present if needed.

We install [Gromacs 2020.4](https://manual.gromacs.org/documentation/2020.4/download.html). 

## Official Gromacs documentation
<hr>

- [Gromacs Home Page](http://www.gromacs.org/)
- Gromacs [downloads](https://manual.gromacs.org/documentation/)
- [Manual for Gromacs 2020.4](https://doi.org/10.5281/zenodo.4054996)


## The process

The different steps of the process are summarized in the figure


```{figure} ../../images/gromacs-installation-process.svg
:alt: Gromacs
:class: bg-light
:width: 750px
:align: left
*Summary of the Gromacs installation process. The steps where most errors tend to occur and indicated in red color.*
```

## Preparations
<hr>

Gromacs doesn't require much disk space and it runs with very modest memory requirements. That is, for the purposes of this course, any reasonably modern PC/Mac is going to work. 

Before we start, we need to answer the following questions:

1. Where to download Gromacs
1. Where to install Gromacs
1. Does the system have an NVIDIA GPU
   * Modern Macs use AMD GPUs so the answer is no
   * WSL/WSL2: GPUs are not accessible. This is going to change in WSL2, 
     but it is not currently part of WSL2 (it is available in the WSL2 insider edition). 
   * Linux computers with NVIDIA GPUs perform very well
     * To use an NVIDIA GPU for computing, CUDA drivers need to be installed. The command to
	 check if that has already been done is `nvidia-smi`. If the command is not present,
	 then CUDA drivers have not been installed.

We will create a directory for the course where we will both download and install Gromacs. Below, we will go through the process step-by-step. 


## Check that your system is up-to-date
<hr>

Before we start the installation procedure: Let's check that the system is up-to-date.

````{tabbed} Linux & WSL/WSL2:

Open a  terminal in Linux and execute

```
sudo apt update
sudo apt upgrade
```
````

````{tabbed} Mac:

Open a terminal and update using your package manager. For example

```
brew update
brew upgrade
```

in the case of Homebrew.
````


## Install C/C++ compilers and `cmake`
<hr>

It is highly recommended to read the Gromacs installation guide. That will give you a better idea of the procedure we follow below. 

As the first requirement, we need C/C++ compilers and `cmake`. The C and C__ compilers `gcc` and `g++` are the canonical compilers and they are automatically installed in standard Linux systems (but need to be separately installed in the case of WSL). The tool `cmake` doesn't come as a part of any standard installation so it needs to installed separately.  Let’s check if they are already installed. This can be done with the following commands:

```
gcc --version
g++ --version
cmake --version
```

If you are using `clang` or the Intel C/C++-compiler,
replace `gcc` by `clang` or `icc`. However, `gcc` is strongly recommended and we will not cover issues related to `icc` and `clang`.


If no compilers were found, then let's install the default versions

````{tabbed} Linux & WSL/WSL2:

```
sudo apt install gcc g++ cmake
```
````

````{tabbed} Mac:

The compilers `gcc` and `g++` come with Xcode so you should have them; if for some reason you don't have Xcode installed, do it now. It is a required component. Note that the default C/C++-compilers on Mac are, however, `clang` and `clang++`. The `cmake` tool needs to be separately installed:

```
brew install cmake
```
````

Now that the compilers are installed, check the versions you have using the above commands. Check also where they were installed by using the `which` command

```
which gcc
which g++
which cmake
```

Now that we have `cmake` and a compilers, we can add some tools.

## Install dependencies and tools for Gromacs
<hr>

The modern versions of Gromacs come with most of the dependencies already built in (distributed with the package). If you install older versions (pre-20XX series), there are more dependencies that need to be installed separately, see the documentation for the corresponding version of Gromacs. 

Let’s install the dependencies. These are not absolutely necessary but they are very helpful. Let's start with `zlib` and `grace`. The program `grace` is for plotting; Gromacs' analysis routines provide ready-to-plot files in the `.xvg` format which is the native format for `grace`. Installation:

````{tabbed} Linux & WSL/WSL2:

```
sudo apt install zlib1g grace 
```
````


````{tabbed} Mac:
```
brew install grace zlib
```


If the rare problem *"Could Not Resolve HEAD to a Revision"*, the following seems to help:

```
git -C $(brew --repository homebrew/core) checkout master
```


````

Next, let's install ImageMagick, doxygen and TexLive (provides (pdflatex)). These are not required by Gromacs but in case you wish to install Gromacs documentation (you should), they are needed. This can take some time since the LaTeX packages are quite large:

````{tabbed} Linux & WSL/WSL2:
```
sudo apt install imagemagick doxygen texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra
```
````


````{tabbed} Mac:
```
brew install imagemagick doxygen
```

If you want any of the extra packages check the from Homebrew. You may already have them if you have LaTeX installed.  
````



## Create the necessary directories
<hr>


Now it is time to create the directories. To do that, open a terminal window. In the following, we will create separate locations for downloading the Gromacs source file and for the final installation. While this organization is not absolutely necessary, it is helpful since if we have to reinstall for any reason, it will then be very easy use the downloaded source file(s) again. The actual installation will be done in a local directory and we will create a separate directory for that. That directory is where the executables and other Gromacs files  will be put.

Let's ensure that we are in the home directory. We then either
- move inside the main directory for the course called `CHEM3300G` that we created in Lab1, but if you don't have it, just
- create the main directory for the course called `CHEM3300G` and under that directories `gromacs` where we will download the files and a second directory called `gmx` where will install the software. Execute the following commands:

```
cd
```
If you didn't follow the instructions in Lab1 or skipped directly here, then create the new directory by

```
mkdir CHEM3300G
```

Now, move into the new directory and create a couple of more directories in there:

```
cd CHEM3300G
mkdir gromacs
mkdir gmx
```

## Download Gromacs
<hr>

We install the version 2020.4 version.


If you followed the instructions above, you should now be in the directory `CHEM3300G` (check with `pwd`; if you are not in `CHEM3300G` then you have to move there). Move to the download directory (the directory called `gromacs` that we just created) and download Gromacs and the Regression tests (these are needed for checking that the installation works properly).

````{tabbed} Linux & WSL/WSL2:
Move on to retrieve the files, you have all the tools. Mac users, check the other tab.
````

````{tabbed} Mac:
The tool `wget` is not readily available but has  to be installed separately if it isn't already installed:

```
brew install wget
```
````

```
cd gromacs
wget http://ftp.gromacs.org/pub/gromacs/gromacs-2020.4.tar.gz
wget http://gerrit.gromacs.org/download/regressiontests-2020.4.tar.gz
```




### Check the authenticity of the files

One should check the authenticity (= the digital fingerprint) of the downloaded files.

````{tabbed} Linux & WSL/WSL2:

The digital fingerprint is checked using the command `md5sum`:

```
md5sum gromacs-2020.4.tar.gz
md5sum regressiontests-2020.4.tar.gz
```
````

````{tabbed} Mac:
One must install the package `md5sha1sum`. That gives the command `md5` for checking the digital fingerprint.

```
brew install md5sha1sum
md5 gromacs-2020.4.tar.gz
md5 regressiontests-2020.4.tar.gz
```
````

The checksum values should match the following:

- Gromacs 2020.4 md5sum: aead694ec7d1222cbc40011c88047c3d
- Regression tests' md5sum: 5965bd26a96f1b5916af0484aa1594e2

If not, you need to re-download.


## Unpack, uncompress and create a build directory
<hr>

The next step is to uncompress and unpack the files and to create a *build directory*. The *build directory* is where the software is built: It is a temporary directory for setting up various things for the actual installation. 

Let's ensure that we are still in the correct location. Use

```
pwd
```
to check the location. Should be `CHEM3300G/gromacs`. If not, then move there. 

In the next step we unpack the Gromacs package that contains the source code. Note that you can omit the letter `v` in the `tar` command below: The option `v` produces verbose output and shows what is being produced (use it if you want to see what is going on). 

After unpacking, check that a new directory called `gromacs-2020.4` has been created. 
We then move in the new directory, and create a build directory in there and move into the build directory:


```
tar xzfv gromacs-2020.4.tar.gz
tar xzf regressiontests-2020.4.tar.gz
cd gromacs-2020.4
mkdir build
cd build
```	

## Building Gromacs
<hr>

It is very important that you are located inside the build directory. We just moved there in the previous step so you should be in the right place. 

The steps for building gromacs have two parts: 

1. Building the software with `cmake` and 
1. compilation with `make`. 

`cmake` is a general tool for *building software*. When software is being built, the process checks, among other things, that all the dependencies (=software, libraries etc. that the new software to be installed depends on) are present and sets the paths (=directories) for the actual installation. We can pass arguments such as the installation directory to `cmake` and that is what we will do below; the default installation directory defined in the software's source files is in the system, but we want to have a local installation instead. We can define that in when we run `cmake`. 


We are now ready to execute the `cmake` command. But let's make the process easier by using the *environment variable* that tells our home directory. You can see all of your *environment variables* by giving the command `printenv`. The *environment variable* contains the home directory is called `$HOME`; shell variables start with the dollar sign. 

Execute the command
```
echo $HOME
```
to list your home directory.


We are now ready to build:

````{tabbed} Linux & WSL/WSL2
```
cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=OFF -DCMAKE_INSTALL_PREFIX=${HOME}/CHEM3300G/gmx -DREGRESSIONTEST_PATH=${HOME}/CHEM3300G/gromacs/regressiontests-2020.4
```

**Important:** The above should be copied as is on a single line.

````
````{tabbed} Mac:

Let's install `fftw` separately (+ at the same time a couple of other extras):
```
brew install fftw sphinx pygments 
```

Then, let's turn FFTW building off (we have it now from the previous line) and force the `gcc`/`g++` compilers. Temporary variables are used for `gcc` and `g++` since Macs don't have a well-defined universal location for the compilers. 

<!--
FIXED: in some Mac systems gcc/G++ are put in /usr/bin/. Need variables for that. Fixed

older macs use bash -> zsh doesn't work -> .bash_profile
-->

```
temp_gcc=`which gcc`
temp_g++=`which g++`

cmake .. -DCMAKE_C_COMPILER=${temp_gcc}   -DCMAKE_CXX_COMPILER=${temp_g++} -DGMX_BUILD_OWN_FFTW=OFF -DREGRESSIONTEST_DOWNLOAD=OFF -DCMAKE_INSTALL_PREFIX=${HOME}/CHEM3300G/gmx -DREGRESSIONTEST_PATH=${HOME}/CHEM3300G/gromacs/regressiontests-2020.4
````

````{tabbed} Linux with NVIDIA GPU:
In this case you must check which precise version of CUDA is present (command: `nvidia-smi`) and the path to it. Here, the version is 11.2

```
cmake .. -DREGRESSIONTEST_DOWNLOAD=OFF -DCMAKE_INSTALL_PREFIX=${HOME}/CHEM3300G/gmx \
         -DREGRESSIONTEST_PATH=${HOME}/CHEM3300G/gromacs/regressiontests-2020.4 \
         -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ \
         -DGMX_BUILD_OWN_FFTW=ON -DGMX_GPU=ON -DGMX_USE_OPENCL=off \
         -DGMX_CUDA_TARGET_COMPUTE=75 \
         -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda-11.2  \
         -DGMX_SHARED_LIBS=ON -DGMX_DOUBLE=off -DGMX_DEFAULT_SUFFIX=ON
```
````

There should be no errors.


````{admonition} If building failed: General instructions
:class: dropdown

1. Scroll up the screen and find the error messages. They tell what went wrong. Most likely, a library or package was missing. That is easy to fix by installing those packages or libraries.
1. If the build failed or it had to be interrupted, the build directory must be cleaned before re-building. In other words, the build directory must be totally empty for the new build. Check the contents and if the directory is not empty, clean the directory using the `command rm -r *`. 

After that, run `cmake` again. 



```{warning}
`rm -r *` is a very powerful and potentially dangerous command as it *deletes everything* in the current directory.

It does the following: `rm` removes. The option `-r` instructs `rm` to remove everything *recursively* under the current directory. The argument star is a so-called *wildcard* character and means 'everything'. So the command removes all files and directories under the current directory. We could remove them one-by-one, of course, but that would be very time consuming. Here we use `rm` since for the build to be successful, it has to be done in an empty directory. 
```
````

````{admonition} If building failed on Mac:
:class: dropdown

Here are a few points:

1. In addition to what is said under the general problems (=that you must clean the build directory), here are a few issues that have come up with Macs.
1. The error messages that appear often during building were related to `fftw`. The easy solution to that was to have `-DGMX_BUILD_OWN_FTTW=OFF` and install `fftw` using `brew`. 
1. In my case, the default compiler (`clang` version 11) on MacOS Catalina didn't build Gromacs properly. It seems that the issues are related to Xcode. The solution that worked was to force the building and compilation processes to use the `gcc` compiler. This can be done using the `cmake` directives as shown below. 

**Here's what worked:**

- As discussed above, install `fftw` and let's add some other packages that were missing (but not critical).

```
brew install fftw sphinx pygments 
```

Then, let's turn FFTW building off (we have it now) and force the `gcc`/`g++` compilers:

```
cmake .. -DCMAKE_C_COMPILER=/usr/local/bin/gcc   -DCMAKE_CXX_COMPILER=/usr/local/bin/g++ -DGMX_BUILD_OWN_FFTW=OFF -DREGRESSIONTEST_DOWNLOAD=OFF -DCMAKE_INSTALL_PREFIX=${HOME}/CHEM3300G/gmx -DREGRESSIONTEST_PATH=${HOME}/CHEM3300G/gromacs/regressiontests-2020.4
```

<!--
```
cmake .. -DCMAKE_CXX_FLAGS=-stdlib-libc++ -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=OFF -DCMAKE_INSTALL_PREFIX=${HOME}/CHEM3300G/gmx -DREGRESSIONTEST_PATH=${HOME}/CHEM3300G/gromacs/regressiontests-2020.4
```
If the compilation worked with `clang`, then that is perfectly good.
-->

The `gcc` compiler version was 8.


```{warning}
`rm -r *` is a very powerful and potentially dangerous command as it *deletes everything* in the current directory.

It does the following: `rm` removes. The option `-r` instructs `rm` to remove everything *recursively* under the current directory. The argument star is a so-called *wildcard* character and means 'everything'. So the command removes all files and directories under the current directory. We could remove them one-by-one, of course, but that would be very time consuming. Here we use `rm` since for the build to be successful, it has to be done in an empty directory. 
```
````



```{warning}
The process below is intensive and takes computing resources. It is very important to ensure that you have not blocked the ventilation as that may cause overheating and even damage. 

```

We are now read to build Gromacs. That is an intensive process but we can make it faster by using all the cores we have available. Note that on a PC/Mac, one physical CPU typically has two cores. Below, we will get the number of cores, assign it to a variable and then run `make`


````{tabbed} Linux & WSL/WSL2 only: 

The command to get the number of cores is `nproc` and we assign it a temporary variable.

```
TEMP=`nproc`
echo $TEMP
make -j${TEMP}
```
````

````{tabbed} Mac:

The commands are  different from Linux:

```
sysctl -n hw.physicalcpu
sysctl -n hw.ncpu
```

The former gives the  number of physical CPUs and the latter the number of cores, the number of cores is what we need:

```
TEMP=`sysctl -n hw.ncpu`
echo $TEMP
make -j${TEMP}
```
````

This process can take a bit of time. If you want to know how long the process takes, just put the command `time` before `make` in the above. Here are some timings:

- 9$^\mathrm{th}$ generation 2.6 GHz i7 (6 cores with option `-j12`, gcc9 compiler): 5 minutes
- 7 years old 2.6 GHz i7 (2 cores with option `-j4`, gcc9 compiler): 20 minutes
- 7 years old 1.3 GHz i7 (2 cores with option `-j4`, gcc9 compiler): 68 minutes
- On 3.6 GHz i7 iMac (4 cores with option `-j8`, gcc8 compiler): 4 minutes


```{admonition} If compilation failed: Click this for instructions
:class: dropdown


In the case something went wrong: Look for the error messages. They are they key to solving the problem. Warning messages, on the other hand, are usually not critical.

If you had to stop the process for some reason ([that can be done with `ctrl +c` for example if you need to do something else with the computer and simply cannot wait for this process to finish): When restarting the procedure, first ensure that you are in the build directory and then execute `make clean`, and only after that the above `make` command. You can also clean the build directory, re-build and re-make.


There are many possible reasons for errors. For example, it may be that your compiler is not compatible, you may be missing dependencies or libraries, maybe the new version of Gromacs has some problems or maybe you made a mistake in using the `make` command above (for example giving too large a number after the option `-j`). The task is to figure out why compilation failed. To do that, scroll back in the terminal window to see what was the first error message (*error*, not *warning*; there is a big difference). There are some more and less rigorous ways of finding the cause(s) of the error(s). If the source is not obvious (like a missing library or dependency), the most pragmatic is simply to copy the essential parts of the first error message and use google. In the above case, I had accidentally typed `-j6` instead of `-j4`. How did I found out the reason? I rechecked the command I had given, then I followed the advice above and cleaned the directory using `make clean` and I re-ran the command with the proper `-j4` (using just `make` instead of `make -j4` would have been the safest way).

```


## Regression tests
<hr>

Next, we will run the checks as provided by regression tests that were downloaded above. Note that this can take time since the tests are first built and then executed. All tests should be passed (=no error messages at the end). Notice also that some tests take longer than others. 


```
make check  -j${TEMP}
```

You can again time this very easily by putting the command `time` in front of `make`

- 7 years old 2.6 GHz i7 (2 cores with option `-j14`, gcc9 compiler): 26 minutes
- 9$^\mathrm{th}$ generation 2.6 GHz i7 (6 cores with option `-j12`, gcc9 compiler): Total time: 5 minutes
- 7 years old 1.3 GHz i7 (2 cores with option `-j4`, gcc9 compiler): 38 minutes
- On 3.6 GHz i7 iMac (4 cores with option `-j8`, gcc8 compiler):  7 minutes


**Important:** These tasks are CPU intensive: Ensure that you are not blocking the vents of your computer. 


## Final installation
<hr>

It is time to install. This puts the files in the installation directory we defined above. Simply execute

```
make install
```
This is very quick, takes about 10 seconds. 


## Let the system know where Gromacs is

Installation is now complete, but we are not done yet. To be able to use the software, we have to make sure that the system knows about it. 

<!--
For that we have to `source` it by running


```
source ${HOME}/CHEM3300G/gmx/bin/GMXRC
```

We can check the *environment variables* to see if `GMX` and `GROMACS` are there (use `printenv` to see all of the *environment variables*).


Just to be 100% sure, let’s check that your installation is seen by the system by running the commands below. The first one shows where the Gromacs executable (`gmx`) it is located and the second one shows you the Gromacs version and some technical details,

```
which gmx
gmx –version
```

There is one more issue to notice: The command:
```
source ${HOME}/CHEM3300G/gmx/bin/GMXRC
```	
works only during the *current session* and you have to re-run it every time you open a new terminal; try it out, open a new terminal and see if it can find `gmx` by using `which gmx`. 


You have three choices and they are all fine, choose to your liking:



1. Choose to re-run the command every time when you run a gromacs session. 
2. You put the `source` command in your `.profile` file. This means that it is automatically executed every time you open a new session. That way Gromacs is available without running `source` every time. To do this, you simply have to edit the file `.profile` in your home directory and add the line
```
source ${HOME}/CHEM3300G/gmx/bin/GMXRC
```		
at the end of it. Important: you must edit the file with an ASCII editor such as `vi`, `emacs`, `nano` or `pico`. *Do not edit `.profile` or any of the system files with Word or such as it can potentially prevent you from using your system*.
3. You can write an alias and put it your `.profile` file. This is quite handy if you have several versions of Gromacs available. For example, put
```
alias gmx2020.4=’source ${HOME}/CHEM3300G/gmx/bin/GMXRC’
```

-->

````{tabbed} Linux & WSL/WSL2:

Copy the line

```
source ${HOME}/CHEM3300G/gmx/bin/GMXRC
```	

at the end of your `.profile` file. This enables the command `gmx` and puts Gromacs available in your $PATH variable. The file `.profile` is one of the hidden files in your home directory. You can edit it using, for example, `vi`:

```
vi ${HOME}/.profile
```

and just copy the line above as the last line in there.

````

````{tabbed} Mac: 



Since Mac uses `zsh` instead of `bash`, there are some differences. First, let's make sure that the autocompletion systems is enabled (strictly speaking, that is not necessary but it is convenient and reduces some error/warning messages). Execute
```
autoload -Uz compinit
compinit
```

In addition, in the hidden dot files are different in `zsh`. There is no file called `.profile` as there is in Linux. Instead, we can use a file called `.zshenv`. Let's first check if the file exists 

```
test -f ${HOME}/.zshenv && echo "Exists" || echo "Does NOT exist"
```

**If it exist**, then add
```
source ${HOME}/CHEM3300G/gmx/bin/GMXRC
```
at the end of it.

**If it doesn't exist**, let's create it and then simply copy the line above in it and save:

```
vi ${HOME}/.zshenv
```
````

Now we are done and have Gromacs and all the tools it provides installed, tested and available. Let's double check: Simply open a new terminal and in Linux & WSL/WSL2 execute the command `printenv` or in Mac the command `env` and look for the lines that begin with `GMX`. They are the lines that are related to Gromacs. To double-check, give the commands

```
which gmx
gmx –version
```

These show where the Gromacs executable is and which version of Gromacs is installed.

<!--

````{admonition} The installation process in a condensed form
:class: dropdown


Below is the installation process in a nutshell. Use this shortcut only of you know exactly what you are doing. This also assumes that all of Gromacs' dependencies are present.

```
cd
mkdir CHEM3300G
cd CHEM3300G
mkdir gromacs
mkdir gmx
cd gromacs
wget http://ftp.gromacs.org/pub/gromacs/gromacs-2020.4.tar.gz
wget http://gerrit.gromacs.org/download/regressiontests-2020.4.tar.gz
cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=OFF -DCMAKE_INSTALL_PREFIX=${HOME}/CHEM3300G/gmx
TEMP=`nproc`
echo $TEMP
make -j${TEMP}
make -j${TEMP} check
make install
```


````

-->
