# Installation of tools: WSL2/Linux etc.

- We need to set up command line terminal. It will be used extensively throughout the course.
- All of command line terminal options are either Linux or Linux-like (technically the OSX one is based on Free BSD but that doesn't make any practical difference here).


## Installation of basic tools

1. Set up command line terminal either by installing full Linux, WSL/WSL2 in Windows or Linux in a virtual machine. A decision needs to be made and we discuss these options below.
2. Learn the basics of command line and the main differences between Linux, Windows and/or Mac.
3. In this course we  Python and Jupyter Lab/Notebook:
    - They have pre-requisites and we need to install them first. This includes software such as a C/C++-compiler, Xcode for OSX users, `cmake`, and so on.
   - After the prerequisites have been installed, we install  Python and Jupyter.

The figure shows a summary of the options depending on your current OS. For Windows users the recommended choice is WSL2 (WSL2 has some advantages over WSL, but WSL works as well). Dual boot Windows 10/Linux is a good choice but requires more work and care. Virtual machine is a safe choice but requires a lot of memory. Mac users already have a command line terminal. It can be found in
```
Finder -> Applications -> Utilities -> Terminal
```
That same location has also `XQuartz` that will be needed to run GUI based applications.

```{figure} ../week01/img/linux-decision.svg
:alt: Linux vs others
:width: 700px
:align: left
*The three main operating systems and the main options.* 
```

If you are happy with the recommended choices, the move on the next section and installation. If you want more information, just click the `dropdown` below to read more.

```{important}
When you install any software *the responsibility is entirely yours*. It is important to you back up your data and essential files. Doing that ensures that in the case something goes wrong, you will be able to recover your previous work and software. While it is rare that something goes wrong, one should take the necessary precautions. And remember to do virus checks.

Recovering a crippled computer may be very hard or impossible.
```

### Additional information 

The `dropdowns` provide more information for those interested and are not required reading.

````{dropdown} **Pre-installation considerations**

**What is your operating system and what you need to do (if anything):**

The listing below should help to choose what to do. Main requirements and limitations are listed.

- **If you have pure Linux or dual boot:** You are good to go, no need to do anything at this time (...you can check that your system is up-to-date).
- **If you have Mac OSX:** OSX is based on Free BSD (Unix) and it has a command line terminal. Nothing needs to be done regarding getting a terminal. Optionally, you can install Linux in a virtual machine but we are not covering that here.
- **If you have Windows:** There are different options to choose from:
   - **The recommended choice for Windows users is to install WSL/WSL2** - with preference for WSL2. This provides you with a Linux installation and full command line tools. 
       - *Important:* to Install WSL, you must have Windows 10. For WSL2 only the following Windows 10 versions are compatible: version 2004 (May 2020), version 1909 (Nov. 2019) and version 1903 (May 2019). Check your Windows version but if you have kept your Windows 10 installation up-to-date, it is highly likely that you have one of above versions. WSL2 is the recommended option.
       -  Installation of WSL/WSL2 is straightforward and WSL/WSL2 is supported by Microsoft. WSL/WSL2 gives a CLI but no GUI. In practise you will have Windows and Linux on your system at the same time. Linux does have access to your files on the Windows side *but* Windows has no access to the files on the Linux side. All Linux CLI tools work well. 
	
  - **Dual boot is another option**. In that case you will have both Linux and Windows installed and you select at boot time which one you want to use. This works independent of which version of Windows you have, but you must have enough free space on your hard drive
     - If you have enough disk space, this is a very clean and efficient option.
     - I strongly recommend not to do this if you have Microsoft Surface. While not impossible, there are reports that the process is not necessarily straightforward.
	 - This is more risky than the very straightforward WSL/WSL2 installation.
  - **The third options is to install Linux in a virtual machine inside your Windows.** This works with all recent versions of Windows.
     - This requires that the computer must have enough RAM. In practise, one should have at least 16 Gb since the RAM has to be divided between Windows and Linux.
     -  Linux inside a virtual machine is full Linux with GUI as well as CLI. 
     - We will not cover the installation here but it is straightforward albeit more time consuming that WSL/WSL2.
	 
**GPU computing:** 

Many popular software packages such as Tensorflow for machine learning and Gromacs, NAMD and Amber for molecular simulations can use GPUs for simulations. GPUs provide a significant speedup compared to running the simulations on CPUs. Depending on your computer, you may be able to use GPUs. If not, don't worry, all the simulations have been tested with an older CPU-only laptop to ensure that the simulations will complete within reasonable time. 

 - Linux: If you have NVIDIA GPUs, you will be able to use the for simulations provided you install / have installed the CUDA drivers. If you have AMD GPUs, things are different. The concerns are the same as for MacOS below
 - WSL/WSL2: No access to GPUs. This features is, however, coming to WSL2 but it is not available at this time (Dec 2020).
 - MacOS: Apple uses AMD GPUs. They are not compatible with NVIDIAs CUDA but use OpenCL instead. 
  - Virtual machine: No access to the GPU(s).	 


**Important: The responsibility is yours.** When you install any software the responsibility is entirely yours. 
It is important to you back up your data and essential files. Doing that ensures that in the case something goes wrong, you will be able to recover your previous work and software. While it is rare that something goes wrong, one should take the necessary precautions. Recovering a crippled computer may be very hard or impossible.


````


````{dropdown} **Try Linux without installing**
If you are curious about installing Linux either as a dual boot or the only operating system, you can try it first using Live USB *without* installing.** 

This allows you try it out and see if it works on your computer. This is important since this way you can see that Wifi and other devices work properly and also check if you like the user interface. Here are the basic steps (the suggestions below are Ubuntu or Ubuntu-based for ease):

-  To make a Live USB you need a USB pen. 4GB is recommended (and often needed). If you want  to try several distributions/flavors at the same time, just have 2 or more pens ready. Note that the USB pen needs to be erased (and formatted) in the process so make sure that you copy all the important files to another USB/SD/HD/SSD.

- Browse the web pages of the different flavors/distributions and see which one pleases you visually. Functionally, they all contain the same features. 

  Suggestions:
   - [Ubuntu Desktop default](https://ubuntu.com/download/desktop)
     - Note: Pick Ubuntu 20.04 LTS (20.04.01 LTS at the time of writing this), NOT any of the newer ones.
   - [The official Ubuntu flavours](https://ubuntu.com/download/flavours).
     -  For those coming from Windows or Mac, Ubuntu Budgie may be the most familiar looking. Simply take a look at their respective pages and see what pleases you visually. 
   - [Elementary OS 5.1 Hera](https://elementary.io/)
     - Uses Ubuntu/Debian package management.
     - Beautiful Mac-like user interface design
   - [Linux Mint 20 Ulyana:](https://linuxmint.com/download.php)
     - Uses Ubuntu/Debian package management.
     - Beautiful Windows-like design

- Once you have made your choice, download the one(s) you want. The files that you download are so-called [ISO images](https://en.wikipedia.org/wiki/ISO_image). It is a standard archive format that we use to create a bootable USB. Note that the ISO images can be large, anything between 1 and 4 GB.

- Create a bootable USB. The links below contain step-by-step instructions and work for all of the above Linux flavours/versions. 

   - [Ubuntu tutorials: Create a bootable USB stick on Windows](https://ubuntu.com/tutorials/create-a-usb-stick-on-windows)
  - [Ubuntu tutorials: Create a bootable USB stick on macOS](https://ubuntu.com/tutorials/create-a-usb-stick-on-macos)


- Now you can try it out. Simply insert the USB and reboot your computer.

  - Potential problems:
     - The computer boots back to Windows (or Mac). This means that USB is not recognized as a boot device. This is easy to change:
         - Solution: Reboot the computer and enter Bios. How this is done depends on bit on your computer. When you reboot, many computers usually show (for a few seconds) what are the keys to press to enter bios. This depends on your computer, but here are a few examples:
            - The most common keys to hold down while booting are F2, F10 and F12. 
            - Lenovo: F2 
            - Not here? Then you have to search the web. It is good to know this since if there ever is a serious problem with your Windows, you may need this to be able to recover your computer and OS. 
            - Once in Bios, go into the `boot menu` and change the order of bootable devices such that USB comes first. Save and reboot. Now (provided the USB is inserted), the computer should boot to Linux. 

- Now you should be running Linux from the USB. Try it out, connect the Wifi, open software from the menus and see that everything works as expected. If everything is fine and you like the visual features, then all is good. Now you can quit or install.

- If you want to try another distribution/flavour, just repeat the steps.    
    
````

````{dropdown} **I want to try/install Linux but which version?**

**Which version/distribution of Linux should I install?**



There are a lot of great Linux distributions to choose from. 

**Recommendation regarding distribution:** The instructions in this document are for Ubuntu-based distributions to keep things simple. If you have not used Linux before, then the easiest way is use one of the Ubuntu based ones. There are many other excellent distributions and you can typically try them without installing by simply making a Live USB (see the other `dropdown`).  

**Recommendation regarding Ubuntu version:** It is strongly recommended to install an LTS (Long Term Support) version. At this time (fall 2020), the latest LTS version is 20.04 LTS. The instructions below have been tested with this particular version (as well as to some degree using 18.04 LTS). Why LTS and not the absolute latest? Ubuntu releases come in 6 month cycles (April and October), but the LTS versions are released every two years. Importantly, the LTS versions are supported and maintained for *five* years. In other words it is a stable solution without the need to upgrade. 

**Recommendation regarding Ubuntu flavor:** There are a lot of excellent choices and ultimately it depends what you like / what seems visually the most appealing to you. 

**Which distribution/version/flavor you use?** Right now, our student office computers run the default Ubuntu, my 2007 iMac runs Ubuntu Budgie and my laptop runs KDE Neon. All of the computers run LTS versions of Ubuntu (mostly 18.04 LTS and 20.04 LTS). I have used Linux since 1993 and tried many distributions including Slackware, Redhat/Fedora, SuSe, Gentoo, Arc, Elementary OS and so on.


**More information:**

- [From It's FOSS: Best Linux Distributions That are Most Suitable for Beginners](https://itsfoss.com/best-linux-beginners/)
- [From It's FOSS: Explained: Which Ubuntu Version Should I Use?](https://itsfoss.com/which-ubuntu-install/)
- [From Ubuntu Blog: What is an Ubuntu LTS release?](https://ubuntu.com/blog/what-is-an-ubuntu-lts-release)

````

Time to start the installations. The time each step takes depends on your operating system. 


## Task 1: Terminal, WSL/WSL2, Xcode and such

Based on your current operating system: Choose one of the tab options that is the most suitable for you. What we are going to do is the following independent of the operating system. 

<!--
Proceed through Tasks 1-3 in this order. As for Tasks 4-5, you can change their mutual order (but must be after Tasks 1-3).
-->


````{tabbed} Linux
Update your system if necessary. Go to the next step.

````

````{tabbed} Windows 10: Install WSL/WSL2

WSL/WSL2 is needed for command line terminal. It gives Linux distribution *without* GUI. It is possible to also use GUI with some extra software as will be indicated.


Here is the procedure:

- First: Check the [Detailed instructions from Microsoft](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
  - **Note:** If you are not in the *Windows Insiders* program (if you don't know what it is, then you aren't), you must follow the [*Manual Installation steps*](https://docs.microsoft.com/en-us/windows/wsl/install-win10#manual-installation-steps)
  - The installation  took about 20 minutes on an old 1.3 GHz laptop.
  - Requires the use of `PowerShell as Administrator`. Pay attention when the instruction ask you to open the `PowerShell as an `Administrator`. 
- For Ubuntu distribution, choose 20.04 LTS. Here's what to choose at the Microsoft App Store: [Ubuntu 20.04 LTS at MS App Store](https://www.microsoft.com/en-ca/p/ubuntu-2004-lts/9n6svws3rx71?activetab=pivot:overviewtab)
- After installation, you *must* update WSL/WSL2  

Here are the detailed steps for WSL2 (if in doubt, see the video below):

- Open PowerShell as an Administrator. In PowerShell, give the command

  ```
  dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
  ```
  
  Reboot your computer
  
  ```
  Reboot computer
  ```
  
- After rebooting, download the WSL2 package: [WSL kernel update](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)


- Next: Give the command:

  ```
  Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -NoRestart
  ```

- After this, give the command:

  ```
  wsl --set-default-version 2
  ```

- If all went fine, open Microsoft App Store and search for Ubuntu. Select, `Ubuntu 20.04 LTS` and get it. 
- Once you have it, click `Launch`.
  ```
  Launch
  ```
- The procedure will ask you to create a user account. This a user account for your `Linux shell`. You can choose any username you want.
- Once done, you *must* run `update` to get the latest updates for your syste,. This is done with the Ubuntu package manager by giving the command
  ```
  sudo apt update
  ```
- After the process finishes, run the `upgrade` procedure by giving the command
  ```
  sudo apt upgrade
  ```

This will take some time. But once it finishes, you have a new WSL2 system installed and you're good to proceed.

- **IMPORTANT:** The home directory is different from you Windows home. WSL2 can see you Windows  directories but not the other way around. Your Windows directories are located at
  ```
  /mnt/c
  ```
You will need this later.

- Optional: Do you  also want GUI with WSL2? You can install any of the following for that (not shown on the video):
  - [VcxSrv](https://sourceforge.net/projects/vcxsrv/). Free.
    - WSL2 requires some extra settings: 1) When staring XLaunch, in `Extra Settings` select also `Disable access control`.     You also need to give the commands:
	   ```
	   export DISPLAY=$(awk '/nameserver / {print $2; exit}' /etc/resolv.conf 2>/dev/null):0
	   export LIBGL_ALWAYS_INDIRECT=1
	   ```
	   Open an X-application and see that it works. If it does, then put the two above lines at the end of your `.bashrc`.
	   These instructions are from [Stackoverflow](https://stackoverflow.com/questions/61110603/how-to-set-up-working-x11-forwarding-on-wsl2). The setting have been tested and they work.
  - [Xming](https://sourceforge.net/projects/xming/). Free.
  - [X410](https://x410.dev/) from Microsoft App Store. 
     - This is not free but works well. When using with WSL2, X410 needs to be give permission to get through the firewall. See [Using X410 with WSL2](https://x410.dev/cookbook/wsl/using-x410-with-wsl2/)
  


You can also watch the following video of WSL2 installation on laptop:

The video follows the manual installation steps (=*non Windows Insiders Program* ones)

```{dropdown} **Video: Installation of WSL2 on a Windows 10 laptop**

The video shows the *full installation* of WSL2 on a Windows 10 laptop. The video is unedited so it shows the full downloads (scroll over to speed it up) as well. If the video appears too small, you can make it full screen on access it directly on another browser window. It is 1080 resolution, just select it if it seems like low resolution in the first place.

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/501562652?title=0&byline=0&portrait=0" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

```

````


````{tabbed} MacOS

- Check which version of MacOS you have (under `About this Mac`).
  - if you have `Catalina`: It is *not* advisable to update it to `Big Sur` as there are reports that some of the tools that we need may not work. This may, of course, change / have changed (Nov 2020). The installations have been tested on `Catalina` but not `Big Sur`.

Check if you have `Xcode`. If not install it, it is required. `Xcode` requires registration but it is free. It provides the necessary compilers and other tools.

- [Xcode](https://developer.apple.com/xcode/). Follow the instructions as Apple's web site. 
   - Xcode provides the compilers, libraries and other development tools
   - This may take some time depending on your internet connection.
   
````

## Task 2: Package manager

````{tabbed} Linux
You already have a package manager, so there is nothing to do.

````

````{tabbed} WSL/WSL2
When WSL/WSL2 was installed, you got a package manager. There is nothing to do at this step.

````

````{tabbed} MacOS

The next task is to install a package manager such as  [MacPorts](https://www.macports.org/) or [Homebrew](https://brew.sh/). Here, we use [Homebrew](https://brew.sh/) but MacPorts works well too. However, the instructions on these pages are for Homebrew only.

See the installation and operating instructions at the [Homebrew](https://brew.sh/) web site. Here is a copy from the web site. 

**Installation:**
- Open a terminal window and give the following command:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Once done, update Homebrew:

```
brew update
```

Now you are ready install software using Homebrew. For how to do it and further instructions, see  [Homebrew](https://brew.sh/) web site. 


````




## Task 3: Install Python and Jupyter Lab

   - See the panel on the left hand side
   

## Task 4: Try the command line terminal

Now it is time to try to command line terminal. Go to


-  [Basic Linux commands](../class/week02/linux-basic-commands-2)

go through the page and work through the commands there. 

**Important:** When there is a warning sign, take it *very* seriously as there are a few commands that are dangerous!  

If there are commands or concepts you don't understand, please ask during the next class.


## Optional: Create work directory for the course

Independent of your operating system:

- Open a terminal window and type

   ```
   cd
   ```

This changes the directory to your `home directory` (we will go through Linux commands separately, right now we just want to create a work directory for the course material).

- Then, give the command

   ```
   mkdir SciComp9502B  
   ```
This directory can be used for course related data, scrips and programs.


- Check that the directory is there by giving the command

   ```
   ls -lt
   ```
