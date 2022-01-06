

# Helpful software

<small>

```{epigraph}
“There are only two industries that refer to their customers as ‘users’.”

-- Edward Tufte, Professor of Political Science, Computer Science and Statistics, Yale.
```

</small>

````{panels}
:column: col-lg-12 p-2

**Goals:** 
- To provide a list of some potentially useful software for various purposes.

**Keywords:** Word processors, LaTeX, Jabref, Inkscape

**Associated material:** 

- [Random computer stuff](https://github.com/mejk/computer-stuff). Lists of software, installation instructions for some random things and solutions to some problems.
- [A brief list of cross-platform software](https://github.com/mejk/computer-stuff/blob/master/cross-platform-software.md). This is a list of software that can be be installed on Windows, Mac and Linus (and in some cases on mobile platforms as well. Some of the stuff below was extracted from this link. In particular, if you want to have more than listed below & to install `flatpack` that provides convenient access to install software such as Spotify etc. on Linux, then take a look.


````

The listings of different software are not exhaustive and reflect my personal preferences and I use most of them more or less continuously. The software listed below are mostly with GPL or comparable license.




## Typesetting

If you use Word, WordPerfect, etc.. you  are on your own. Below is a list of some software stuff that I have found useful & use. 

### LibreOffice

LibreOffice is a free multiplatform full-featured office package. Most Linux distributions are shipped with LibreOffice installed. If not, you can get it from here (also for Windows and Mac): [LibreOffice](https://www.libreoffice.org/).

#### LibreOffice and math

If you are a LaTeX user, Libreoffice has a wonderful plugin called [TexMaths by Roland Baudin](http://roland65.free.fr/texmaths/). With TexMaths you can copy-paste your LaTeX equations into LibreOffice documents and presentations. The equations remain editable (numbering is also provided) and one can choose either SVG or PNG as the output format. The use of TexMaths requires a LaTeX 
installation, `dvipng` (for PNG output) or `dvisvgm` (for SVG output).

Installation of `dvipng` and `dvisvgm` using Ubuntu:

```
sudo apt install dvipng dvisvgm
```

LibreOffice works great in Linux, Windows and OSX systems. To be able to the TeXMaths plugin, you need to have LaTeX installed independent of the operating system. LibreOffice has also a built-in equation editor that is very similar to what Word has. However, LaTeX + TexMaths are superior to any other current solution.

#### LibreOffice and references: 

Another great feature of LibreOffice is that it can link directly to the [Jabref](https://www.jabref.org/) reference manager. [Jabref](https://www.jabref.org/) is available for Linux, Windows and Mac.

 - Summary of Jabref:
     - Has BibTeX and BibLaTeX support
     - Has browser extensions from Chrome, Firefox and Vivaldi
     - Can also connect directly to various LaTeX editors AND LibreOffice.
     - Can import directly using ISBN, DOI, PubMed-ID and arXiv-ID
     - On Linux: Download and install using 
	    ```
		 sudo dpkg -i <package name>
		``` 


#### Linux notes:

  - If you want to use TexMaths, and you don't have LaTeX installed, the following gives the full LaTeX installation (it's over 4 GB, if you want the a lighter installation, replace `texlive-full` by `texlive-recommended`):

```  
sudo apt install texlive-full
```


Here's how to install the `dvipng` and `dvisvgm` packages for rendering maths:

  - Open a terminal window and give the following commands (the latter gives `dvisvgm`)

```
sudo apt install dvipng
sudo apt install texlive-extra-utils
```

### WPS Office 

WPS Office advertises itself as a "cross-platform office suite". It is available for MaC, Windows, Linux, Android and iOS. It is free. The main advantage for WPS Office is its compatibility with MS Office. On a personal note, I have used it for editing different types of Word documents as well as PowerPoint files and thus far to my great surprise everything has worked perfectly - even in PowerPoint with embedded movies. The interface and functionalities are also *very* familiar for an MS Office users.

#### WPS installation: 
This is one of those cases when you do need the command line as WPS Office must be downloaded as a debian package and installed using the command line. That part is very simple. 


#### Proprietary Microsoft fonts: 

The other slight complication is that one needs to install separately the proprietary Microsoft Arial and Times New Roman Fonts. You probably want these for other applications as well, this issue is general and not limited to WPS Office. The installation procedure below makes the fonts available system-wide for all applications. You probably also want the symbol font and the instructions for it are provided as well. 

**Procedure:** We first install the fonts and then WPS Office.

1. Let's first ensure that the **Microsoft proprietary fonts** (gives Times New Roman and Arial) are installed. 
 
  - Open a terminal window and give the following command
```
sudo apt install ttf-mscorefonts-installer  
```
A pop-up window will ask you to agree with the terms of license. Accept and 
   now you have Times New Roman and Arial fonts available for all applications system-wide.


#### Symbol font:

This is slightly more complex. We download the fonts to the `Downloads` directory and then install them from there. 

  - Open a terminal window and execute

```
cd
cd Downloads
mkdir tmp
cd tmp
```

  - Check if you have git installed
```  
which git
```  
  If git was found skip the next step. In case git was not found, execute
  Install git (if you don't have it) and get the fonts:

```  
sudo apt install git
```

  - Now we can get the Symbol fonts using `git`. This creates a directory `ttf-wps-fonts`. We move in there:

```  
git clone https://github.com/IamDH4/ttf-wps-fonts
cd ttf-wps-fonts
```  

  - Let's create a subdirectory for the new fonts in the font directory. Typically (at least in my Ubuntu 20.04 LTS and 18.04 LTS) the main fonts directory is at `/usr/share/fonts`. Create a subdirectory `wps-fonts` in there:

```
sudo mkdir /usr/share/fonts/wps-fonts
```

  - Now that we have retrieved the Symbol font, copy (or move) the fonts in the new directory and change the file permissions:

```  
sudo cp *.ttf /usr/share/fonts/wps-fonts
sudo chmod 644 /usr/share/fonts/wps-fonts/*
```  
  
  - We are almost done. We need to rebuild the font cache to make the fonts available:
```  
sudo fc-cache -vfs
```  

  - Remove the temporary directory if you want to (but it is not necessary).


#### Install WPS Office:

Now that we have all the fonts, let's install WPS

  - Download it from [WPS Office 2019 For Linux](https://linux.wps.com/)
  - The file should go to your Downloads directory. If not, move it there after downloading
  - Once downloaded (and if necessary moved to the Downloads directory), go to the Downloads directory:
  
  - Check the name of the `.deb` file using (for example)

```
ls -lt *.deb
```
  -  Install using the Debian package manager dpkg. Below, replace `<package_name>` by the name of the actual `deb` file.
   
```
sudo dkpg -i package_name
```

Done!

Here is more: [Word processors](https://github.com/mejk/computer-stuff/blob/master/ubuntu/word-processors-with-gui.md)
  

### LaTeX and BibTeX

LaTeX is not an editor, it is a page description, or a markup, language. It was designed to be able to produce high quality mathematical typesetting - and there is no contest, LaTeX is by far the best. It offers a huge amount of extensions and *very versatile* cross-referencing and handling of bibliographical data with BibTeX. The catch is that there is a bit of a learning curve, but it pays off. Most articles in science and engineering are produced with LaTeX.

- LaTeX for Windows: [MiKTeX](https://miktex.org/)
- LaTeX for OSX: [TeXShop](https://pages.uoregon.edu/koch/texshop/)
- LaTeX for Linux: with package manager. The full installation:
   ```
   sudo apt install texlive-full
   ```

To use LaTeX you need to choose a word processor separately. Since all LaTeX files must be saved as ASCII, almost any editor will work. Some of them have built in capabilities or have plugins for LaTeX. Such editors include [Atom](https://atom.io/), Emacs, Notepad++, gedit and kate, to mention some. There are also text editors that have been designed particularly for LaTeX, for example [TeXShop](https://pages.uoregon.edu/koch/texshop/) (OSX only), [TeXStudio](https://www.texstudio.org/) (Win, Linux, OSX), TeXworks (Linux, Windows), [Texmaker](https://www.xm1math.net/texmaker/) (Linux, OSX, Windows), and LyX (Linux, Windows, OSX). Basically any editor capable of saving your files in ASCII, such as the venerable vi, will do, but the editors such as Emacs, TeXShop, Atom, gedit, kate and TeXStudio offer a lot of extra goodies. Atom is available for all major operating systems.

## Illustrations

[Inkscape](https://inkscape.org/) for vector graphics and [GIMP](https://www.gimp.org/) for everything else. Both are extremely powerful and available for all operating systems. On Linux, they are available through the software center (direct download works, of course, as well). Almost all the graphics in the course notes have been done using Inkscape. 

## Plotting

There are a lot of options. The recommended option for this course - and also for producing production quality plots is to use one/some of the Python packages in Jupyter Lab/Notebook. Options include [matplotlib](https://matplotlib.org/), [seaborn](https://seaborn.pydata.org/), [Plotly](https://plotly.com/) and so on. As for [matplotlib](https://matplotlib.org/), it provides a Matlab-like command set with very versatile 2D and 3D plotting properties. It lives on top of Python and hence you can plug in almost any Python library you like - that makes Matplotlib very useful as the there is a Python library for almost any imaginable task. And if you don't care about Python, Matplotlib handles numerics in a very Matlab-like fashion, it is free and runs on top of almost any operating system.


Below are some other options. 

### Gnuplot

[Gnuplot](http://www.gnuplot.info/) is capable of production quality 2D plotting & fitting and it has some 3D capabilities  as well.  It runs under almost any operating system (Linux, Unix, OSX, Windows, VMS, ...). It is not a program for data analysis, but it is a plotting front-end.

## Grace

[Grace](https://en.wikipedia.org/wiki/Grace_(plotting_tool)) is a menu-driven plotting package for high quality 2D plotting. It has also data fitting capabilities, Fourier transforms, and regression. Very easy to use and can be installed in most systems. In addition, for those performing molecular simulations using Gromacs’:  The Gromacs analysis tools generate files in Grace's `.xvg` format.

