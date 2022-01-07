#  VMD installation

````{panels}
:column: col-lg-12 p-2

```{image} ../images/logos/vmd_logo.gif
:alt: VMD
:class: bg-primary
:width: 250px
:align: right
```
```{image} ../images/1ubq-cropped.jpg
:alt: 1UBQ
:class: bg-primary
:width: 250px
:align: right
```

**This file:** 
- Provides instructions for installing VMD



<!--
![VMD](../images/logos/vmd_logo.gif)
-->

**Keywords:** VMD,  visualization, atomistic simulations

**About VMD:** 

Humphrey, W., Dalke, A. and Schulten, K., *"VMD - Visual Molecular Dynamics"*, 
J. Molec. Graphics, 1996, vol. 14, pp. 33-38. 

**Associated material:** 

- [VMD plugins]()
- [VMD selections]()
- [VMD documentation](https://www.ks.uiuc.edu/Research/vmd/current/docs.html) from the VMD Home Page

````




## Installation

Choose the operating system for your VMD installation. 
In all of the cases, you must download the software from 
[VMD Home page](https://www.ks.uiuc.edu/Research/vmd/). 
Select the version that is compatible with your operating system. At this time (Dec. 2020) the latest stable version is 1.9.3. There is also 1.9.4-alpha51. Version 1.9.3 is recommended, but it is also very easy to install both. If you haven't registered before, you will be asked to register during the process (it's free).


```{tabbed} Windows 10:

- [Download from VMD Home Page](https://www.ks.uiuc.edu/Research/vmd/). 
- Installation using `.exe` file. 
   - Simply install like any other package.
   - Note: 1.9.4-alpha51 is not stable on Windows 10

```

```{tabbed} Mac:

- [Download from VMD Home Page](https://www.ks.uiuc.edu/Research/vmd/). 
- Installation is done using a `.dmg` package. 
   - Simply install like any other package.
   - Make sure that you pick the correct package (64 bit for `Catalina` - the version for `Catalina` and `Big Sur` are also different); you can check the version of your MacOS using the Apple logo on the top left corner and then selecting `About this Mac`.

```

````{tabbed} Linux & WSL/WSL2:

- [Download from VMD Home Page](https://www.ks.uiuc.edu/Research/vmd/). 
- Download one of the `.tar.gz` packages. 
- Installation instructions are provided below. 


**Unpack:**

After downloading (it is assumed that the `.tar.gz` package was downloaded in the `Downloads` directory), unpack and move into the new directory:

```
tar xzf vmd-1.9.3.bin.LINUXAMD64-CUDA8-OptiX4-OSPRay111p1.opengl.tar.gz
cd vmd-1.9.3
```

Read the `README` file!

After reading the `README` file, edit the file called `configure` if you want to change the default name or the location into which vmd will be installed. Here's how:

**Change name if you want to have multiple versions:**

If you want to install different versions of VMD, look for the line that has the variable 

```
install_name = "vmd"
```

To distinguish between the different versions, you have to give them different names. For example, for `vmd-1.9.3` it might be a good idea to do the following:

```
install_name = "vmd-1.9.3"
```

and for `vmd-1.9.4-alpha51`

```
install_name = "vmd-1.9.4-a51"
```

where the part `a51` is to indicate the particular alpha version that was available at the time; it is useful to have the version name in case one wants to install another version later. 


**Install & library directories:**

The default install and library directories are given by the variables `install_bin_dir` and `install_library_dir`. The defaults are:

```
install_bin_dir="/usr/local/bin"
install_library_dir="/usr/local/lib/$install_name
```

If you have root privileges and want to install VMD system-wide, then nothing needs to be done. If you don't have root rights or/and want to have a private installation, change the above to whatever you want.

**Configure:**

Run `./configure` to generate a `Makefile`:

```
./configure
```

The output looks something like 

```
sam@linux:~/Downloads/vmd-1.9.3$ ./configure 
using configure.options: LINUXAMD64 OPENGL OPENGLPBUFFER FLTK TK ACTC CUDA IMD LIBSBALL XINERAMA XINPUT LIBOPTIX LIBOSPRAY LIBTACHYON VRPN NETCDF COLVARS TCL PYTHON PTHREADS NUMPY SILENT ICC
```

**Final step: The actual installation:**

The above puts the new `Makefile` in the directory `./src`. Move there 

```
cd src
```

Pick one of the installation commands below depending on if you want a system-wide installation or if you modified the installation and library directories to local ones that do not require root access:

For system-wide installation:
```
sudo make install
```

For private installation (requires that installation and library directories were changed as discussed above):
```
sudo make install
```

The output looks something like

```
sam@linux:~/Downloads/vmd-1.9.3/src$ sudo make install
[sudo] password for sam: 
Info: /bin/csh shell not found, installing Bourne shell startup script instead
Make sure /usr/local/bin/vmd is in your path.
VMD installation complete.  Enjoy!
```

If you changed the name as above, start vmd from the command line using 

```
vmd-1.9.3
```
and otherwise using

```
vmd
```
````


