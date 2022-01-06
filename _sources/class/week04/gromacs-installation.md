# Gromacs installation

## Preparations

Let's check that we have the compilers and cmake. If not, install them
```
gcc --version
```
replace `gcc` by `clang` or `icc` if you use clan or intel compiler instead
```
cmake --version
g++ --version
```
this checks if c++ compiler was also installed. It should have been but it appears in some Windows 10 systems that was not the case but `g++` (the c++ compiler) had to be installed separately. If not found, execute `sudo apt-get install g++`

Everything found? Then let't move on.


## Installation

### Step 1: Create the necessary directories

Open a terminal window (Linux, OSX or Ubuntu shell in Windows 10). We will take the following approach: we will create separate locations for downloading the source file and for the fina installation. While this is not really necessary, it is helpful since if we have to reinstall it for any reason, it will then be very easy use the downloaded source file(s) again. The actual installation will be done in a local directory and we will create a separate directory for that. That directory is where the exectuables and other files of the software will be put.

Let's ensure that we are in the home directory. We then create the main directory for the course called `MDCOURSE` and under that directories gromacs where we will download the files and a second directory called `gmx` where will install the software. Execute the following commands:


```
cd
mkdir MDCOURSE
cd MDCOURSE
mkdir gromacs
mkdir gmx
```

### Step 2: Download the Gromacs source file


If you followed Step 1, you should now be in the `MDCOURSE` directory. Move to the
download directory (the directory called gromacs we created) and download gromacs
using the command line as follows.

```
cd gromacs
wget http://ftp.gromacs.org/pub/gromacs/gromacs-2019.tar.gz
ls -lt

```

### Step 3. Check the authenticity (digital fingerprint) of the Gromacs source file:

Now that we have source file downloaded, we should check that the digital fingerprint (`md5sum`) matches the one given on the download page (fcd283dd0fe5ceb54dd9d735d75cbc65; check this at http://manual.gromacs.org/documentation/2019/download.html ). The numbers should be exactly the same. Run the command

```
md5sum gromacs-2019.tar.gz
```

**Note for Mac users:** The command `md5sum` is not present on a mac. Try `md5` instead.If it doesn't work, install it with Brew:

```
brew install md5sha1sum
md5 gromacs-2019.tar.gz
```


### Step 4. Unpack, uncompress and create a build directory.

The next step is to uncompress and unpack the file and to create a build directory. The latter is where the software is built (=a temporary directory for setting up various things for the actual installation). Note, you can omit the letter `v` in the `tar` command below: The option `v` produces verbose output and shows what is being produced (so use it if you want to see what is going on). Without it, no messages will be printed on screen. After unpacking, check that a new directory called `gromacs-2019` has been created. Below, we also list the contents but you can skip that, of course. We then move in there, create a build directory and move in there:

```
tar xzfv gromacs-2019.tar.gz
ls -lt
cd gromacs-2019
mkdir build
cd build
```


### Step 5: Building gromacs.


Using Ubuntu Shell on Windows 10 on my small 1.3 GHz (i7) laptop, this step took 3 minutes.

In this is very important to you are located inside the build directory where we just moved. This is also emphasized below. The steps have two parts: building the software with cmake and then compilation with make. Cmake is a general the tool for building software. When software is built, the process
checks, among other things, that all the dependencies (=software, libraries etc that the new software be installed depends on) are present and sets the paths (=directories) for the actual installation. We can
pass arguments such as the installation directory to cmake and that is what we will do; the default installation directory define in the software source files is in the system. We want to have a local installation instead. We can define that in when we run cmake.
The command looks like this but don't execute it run it yet, we will first walk through the different parts of the command and then execute it

```
cmake .. -DGMX_BUILD_OWN_FFTW=ON \
-DREGRESSIONTEST_DOWNLOAD=ON \
-DCMAKE_INSTALL_PREFIX=/pathtohome/username/MDCOURSE/gmx
```

The two dots tell cmake to get the source files from a directory above the current one. Then, the part
```
-DGMX_BUILD_OWN_FFTW=ON
```

says that the we build our own fftw. In other words, during the process the lastest source files for fftw are fetched and built. If you change it to OFF, then the process uses the one from your system (if it doesn't exist an error will be produced). The second one,

```
-DREGRESSIONTEST_DOWNLOAD=ON
```
downloads the regression tests. The are needed to check that everything is ok. The third part

```
-DCMAKE_INSTALL_PREFIX=/pathtohome/username/MDCOURSE/gmx
```

defines the location for the installation. This is very important. Remember, we created directory gmx under `MDCOURSE` (`MDCOURSE/gmx`) as the installation location. You have to change the first part after the equal sign as follows (we will do this below when execute the command): 1) we check where your home is to replace the part /pathtohome/username . This can vary depending on if you are on Mac, Linux or Ubuntu bash shell in Windows. There are several ways of doing that, but let's use the command echo and check the system variable for home (`$HOME`). The neat part is that this work on all
operating systems. You can see that yourself, just execute
```
echo $HOME
```
and that tells where your home directory is.

We are now ready to execute the cmake command but let's play it very safe (this makes it also quicker to check that everything is ok) to see that building will work. By this, I mean that we make a test build without downloading the regression tests as downloading them takes a extra time (can take 5-10 minutes). If the test build works, we then clean the directory using the command `rm -r *`. WARNING: this is a very powerful and potentially dangerous command. It does the following: `rm`
removes. The option `-r` instructs it to remove everything recursively under the current directory. The argument star is a so-called wildcard character and means 'all files'. So the command removes all files and directories under the current directory. We could remove them one-by-one, of course, but that would be very time consuming. Here we must use rm since for the build to be successful, it has to be done in an empty directory. Since we will first do a test build, we must clean the directory to do the actual build. But you have been warned about the dangers of the rm command.


The commands below do the following: 1) double-check that you are in the build directory (if not move there but you should be there unless you didn't follow the above), 2) perform the test build, 3a) if there were no errors listed at the end of the build, then clean dirctory or 3b) if there were errors, check the error messages and try to fix the errors and clean the directory

```pwd
```

let's double-check that we are in the build directory. If not, move there.

```
cmake .. -DGMX_BUILD_OWN_FFTW=ON \
-DREGRESSIONTEST_DOWNLOAD=OFF \
-DCMAKE_INSTALL_PREFIX=${HOME}/MDCOURSE/gmx
```
perform a test build. Note the backslash allows dividing the command over separate lines. You can copy-paste that on your terminal. If there were no errors, then we clean the directory with the next command
and do the actual build and retrieve the regressionstests that we need.
`rm -r *`
We must clean the directory after the test build. The actual build must be done in an empty directory.

```
cmake .. -DGMX_BUILD_OWN_FFTW=ON \
-DREGRESSIONTEST_DOWNLOAD=ON \
-DCMAKE_INSTALL_PREFIX=${HOME}/MDCOURSE/gmx
```

No errors? Then move on the next step.

### Step 6: "Making" gromacs

Using Ubuntu Shell on Windows 10 on my small 1.3 GHz (i7) laptop, this step took 25 minutes.

Using Linux on 3.9 GHz (i7) laptop, this step took 4 minutes.

Now that we have a build, we finally compile the software. That is done using make. Since this process takes computing resources, make sure you have not blocked the ventilation. Your computer/laptop is most likely a multicore computer. Let's check that too using the command `nproc`. For example, for a dual core system it gives 4 (2 CPUs and 2 virtual computing cores). I doesn't matter if you don't have that command. Execute

```
nproc
```

gives the number of available computing cores. If you don't have the command use plain
make instead of `make -j`

```
make -j4
```

replace 4 by the number that nproc have or use plain make instead. This can take quite some time depending on your system (anything from minutes to an hour or so). Important: if you have to stop the process for some reason (for example if you need the computer and simpy cannot wait for this process to finish): first make sure yo come back to the build directory and then you must execute make clean and after that the above make command.

Assuming everything went fine without errors, we will run the checks in the next step.



### Step 7: Running regressions tests (=checking that everything works)


Using Ubuntu Shell on Windows 10 on my small 1.3 GHz (i7) laptop, this step took 18 minutes.
Using Linux on 3.9 GHz (i7) laptop, this step took 4 minutes.


This process is also instensive and computing resources. It is very important to ensure that you have not blocked the ventilation. Compile and run the tests. This make take time anything from a few minutes to an hour depending on your computer. All tests should be passed (=no error message at the end). 

```
make check
```
this performs all the checks. This can take some time. Note: you can also use the `-j` option here. All tests should be passed (=no error message at the end). When the process ends, there is a listing of how many tests were passed or failed. The number of failures should be zero. If that is the case, we can finally install.

### Step 8: Finally: installation


It is time to install. This puts the files in the installation directory we defined above. Execute

```
make install
```

This is very quick.

Finally, to be able to use the software, we have to make sure that the system knows about it. For that we
have to 'source' it by running

```
source ${HOME}/MDCOURSE/gmx/bin/GMXRC
```

Now you're ready to go. Just to 100% sure, let's check that your installation is seen by the system by running the commands below. The first one shows where the Gromacs executable (`gmx`) it is located and the second one shows you the Gromacs version and some technical details,

```
which gmx
gmx --version
```

### For afficionados:

If you want to install another version of gromacs

There are also many other arguments that can be used. In addition, the process also checks if you have a GPU present in your system and if it can be used to speed up computations (NVIDIA only) but let's not worry about that at this time. You can see some of additional options for `cmake` at
http://manual.gromacs.org/documentation/2019/install-guide/index.html
