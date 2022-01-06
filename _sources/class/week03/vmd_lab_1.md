# VMD - Visual Molecular Dynamics


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

**Keywords:** VMD,  visualization, atomistic simulations

**About VMD:** 

Humphrey, W., Dalke, A. and Schulten, K., *"VMD - Visual Molecular Dynamics"*, 
J. Molec. Graphics, 1996, vol. 14, pp. 33-38. 

**Associated material:** 

- [VMD plugins]()
- [VMD selections]()
- [VMD documentation](https://www.ks.uiuc.edu/Research/vmd/current/docs.html) from the VMD Home Page


**Alternatives to VMD:** Pymol


````

## Background

Why visualize?

## More on VMD:

- [VMD Home Page](https://www.ks.uiuc.edu/Research/vmd/)
- [VMD tutorial](https://www.ks.uiuc.edu/Training/Tutorials/vmd/tutorial-html/index.html) from the VMD web site
- [VMD documentation and tutorials](https://www.ks.uiuc.edu/Research/vmd/current/docs.html) from the VMD web site
- [VMD plugin library and documentation for extensions](https://www.ks.uiuc.edu/Research/vmd/plugins/)
- [VMD programmer's guide](http://www.ks.uiuc.edu/Research/vmd/doxygen/)

## What is VMD

VMD - Visual Molecular Dynamics - is a general purpose  software for 3D molecular visualization and data analysis of molecular systems. It can read file formats and data produced by most common software including PDB, xyz, NAMD, Gromacs, Amber, CPMD, and it can used to visualize and analyze data from both classical and quantum simulations. VMD includes a lot of various analysis tools and it also has a plugin system for developers. VMD is also able to use CUDA acceleration of an NVIDIA GPU is present.

VMD is developed in Theoretical and Computational Biophysics Group at the University of Illinois at Urbana-Champaign. 

## Features

**Operating systems:** VMD is available for Linux, Windows and OSX. VMD has both a GUI and a command line interface. 

**Visualization:** VMD can produce publication quality graphics and movies. It supports verious rendering methods including `Tachyon` (internal) and `povray` (installation of povray is required for that). It has very powerful tools for section  atoms, molecules and groups based on various criteria. 

**Data analysis:** VMD has a wide range of built-in analysis tools. There is no set limit for the length of a trajectory apart from available memory.

**Scripting and extensions:** VMD also offers a very powerful scripting interface using Tcl/Tk. It has also an interface to [PLUMED](https://www.plumed.org/) collective variable analysis (requires separate installation of PLUMED).

**But I am an experimentalist:** Besides reading all the major file formats, VMD has plugins that are intended for experimental data. These include MDFF for Cryo-EM data and others.

**Special:** 
- VMD has  some [NAMD](https://www.ks.uiuc.edu/Research/namd/)-specific tools for setting up molecular simulations. 
- VMD has an interface for reading PDB entries by accession number directly from the [PDB database](https://www.rcsb.org/). Read more [background information](https://www.rcsb.org/pages/about-us/index) about the PDB database. 
- VMD also has an interface to [APBS](http://www.poissonboltzmann.org/) (Adaptive Poisson Boltzmann Solver) for calculations of continuum electrostatics.
- VMD has a toolkit for force field parameterization called [Force Field Toolkit](http://www.ks.uiuc.edu/Research/vmd/plugins/fftk/) plugin (ffTK)

Note that many of the plugins require installation of additional software or/and libraries.

## Basics

Movie showing the basic VMD window.  

### Loading molecular data

**PDB database:** VMD has the capability to download  PDB files directly from the PDB database. 

- [RCSB Protein Databank (PDB)](https://www.rcsb.org/)


**PDB file:**


**Note: Trouble loading from PDB directly to VMD?**

There seems to be some issues loading molecules directly from PDB to vmd-1.9.3 but the feature works in 1.9.4-alpha51. 

<!--
However, vmd-1.9.3 can still retrieve PDB files and download them. The files can then be read into VMD. 
-->

As an example, let's retrieve (from PDB) the COVID-19 spike protein, PDB accession code `6ZB4`

Here's the PDB web site entry for it:

- [SARS CoV-2 Spike protein, Closed conformation, C1 symmetry](https://www.rcsb.org/structure/6ZB4).


Movie showing some basic VMD operations usingh `6ZB4`. These include zooming, rotating and resetting the view, switching between the perspective and orthographic modes, creating representations, using selections, changing colors, querying for information about a selected residue and some other simple tasks. 

#### Orthographic vs perspective mode

### Loading and viewing a trajectory

Trajectory and structure


### Saving and re-loading a visualization

### Customizing VMD

In older versions of VMD, one could simply edit the `.vmdrc` file located in the home directory. That is, however, not recommended. The better (and also very easy way) to change the initial settings is to use the `VMD Preferences` menu under `Extensions` abd from there saving the settings by clicing `Write Settings to VMDRC`. This works in Windows, Linux and Mac. For example, my preferences are white background, orthographic viewing and not showing waters.



### Representations


- [Molecular Representations in VMD](https://www.ks.uiuc.edu/Research/vmd/allversions/repimages/) from the VMD web site

### Saving 

### Rendering and tuning its quality

Resolution settings

Colors and materials

Axes on/off

Orthographic vs perspective

Depth cueing

Clipping plane

Volumetric rendering


http://mgltools.scripps.edu/downloads#msms


### High-quality rendering

There are several ways to produce very high quality publication level graphics. Here, two of the most common ones are covered, interal `Tachyon` and `povray` rendering. Independent of teh technique - and this also applied to the screenshot method - is that the display size needs to be chosen appropriately. While with the screenshot method the screen size is exactly as it is on the display, for  `Tachyon` and `povray` rendering the proportions are preserved and the actualy resolution can be changed when calling the renderer. Thus, the proprtions must be chosen to be commensurate with the desired resolution. 

This is how the display size can be chosen from the VMD command shell:

```
display resize 100x100
```

#### Tachyon


Display -> Rendermode -> GLSL
Display --> Display Setting --> Shadow ON, Ambient Occl. ON

Select the rendering method as `tachyon`

In the 'Render command` window

```
-aasamples 12 %s -auto_skylight 0.7 -format TARGA -res 2048 2048 -o %s.tga
```

```
 -res 12460 9620 -aasamples 36 -add_skylight 1.0 %s -normalize -format PSD48 -o %s.psd
```

formats:

`TARGA`, `PSD48`, `BMP`, 
<!--
`JPEG`, `PNG`, 
-->



From VMD console:

```
render Tachyon filename.dat "/path/to/tachyon_binary" filename.dat -aasamples 12 -format TARGA -res 4096 4096 -o outfile.tga
```

Transparent molecular surfaces (value 1 seems to work well)

```
 -trans_max_surfaces 
```

Speed it up? Check the number of threads using, for example, `lscpu`. I have 4 cores and 2 threads per core, that is, 8 threads in total.


```
 -numthreads 8 -aasamples 12 %s -auto_skylight 0.7 -format TARGA  -trans_max_surfaces 1
 -res 2048 2048 -o %s.tga

```

Transparent background


**High resolution movie:**

Before rendering any movies, ensnure that you have enough storage space available. 


    irst create the .dat file for each frame by choosing the following

    Extension -> Visualization -> Movie Maker

    Change the Movie Maker settings as

    Renderer -> Tachyon
    Name of the movie frame
    Movie Settings -> Trajectory with ‘4. Delete image files’ uncheked
    Format -> Targa Frames

    Run this to generate the .dat files
    Now process the *.dat files with the following option as slurm jobs

    tachyon=/software/vmd-1.9.2-x86_64/lib64/tachyon_LINUXAMD64

    ${tachyon} -numthreads 16 -aasamples 12 frame.${a}.dat -format TGA -res 512 512 -o frame.${a}.tga;
    (Change all the numbers accordingly)
    If a huge number of frames are required, then the job can be split as multiple slurm jobs which will speed up the whole process

    Finally process all the image files with ffmpeg

    ffmpeg -threads 16 -r 30 -i frmae.%05d.tga -s 512x512 -vcodec libx264 -b 5000k movie.mpg
    (by assuming all the frames has dimension 512x512. If the frame dimension has changed by display resize command, then that value needs to be used here)
    One can also play with the ffmpeg options


<!--
pdbalias atom HOH O OH2
pdbalias residue HOH TIP3
-->

**More:**

- [How to make images for publication using VMD](https://mini.ourphysics.org/wiki/index.php/How_to_make_images_for_publication_using_VMD)
- [Simulate, analyze, plot blog](http://linuxrajib.blogspot.com/2016/03/vmd-high-resolution-image-and-movie.html)

- [Rangsiman Ketkaew](https://rangsimanketkaew.github.io/)

#### Povray rendering

<!-- 
Povray stands for *Persistence of vision*. It can be easily installed in Linux and Mac:


````{tabbed} Linux & WSL/WSL2:
```
sudo apt install povray
```
````

````{tabbed} Mac:
```
brew install povray
```
````

-->

**More:**

- [povray stuff](http://knottsgroup.groups.et.byu.net/labbook/index.php?n=Main.UsingVMD)


### Removing periodic images

### Updating every frame

## Making movies

Under *Extensions*  *Visualization*  *Movie Maker*

### The `ffmpeg` encoder


````{tabbed} Linux & WSL/WSL2:

```
sudo apt install ffmpeg
```
````

````{tabbed} Mac:

```
brew install ffmpeg
```
````

```{tabbed} Windows 10

- Download from [ffmepg](https://www.ffmpeg.org/download.html)

````


<!--
```
sudo port install ffmpeg +gpl +postproc +lame +theora +libogg +vorbis
 +xvid +x264 +a52 +faac +faad +dts +nonfree
```
-->


### Renderers

**Windows specific:**

## Advanced

## Extensions

Under the menu *Extensions*

### Using the Tcl/Tk  command shell

Tcl stands for  Tool Command Language and Tk is the graphical usner interface toolkit for Tcl. Tcl/Tk is supported across the different operating systems (Windows, Linux, OSX). 

### Showing elapsed time


## Visualization of MARTINI simulations


- [Martini tutorials: visualizing Martini systems using VMD](http://cgmartini.nl/index.php/tutorials-general-introduction-gmx5/cgviz-gmx5)





## Tips and Tricks

Put two movies on top of each other.  They must have the same dimensions.

Source:[aaa] (https://stackoverflow.com/questions/11552565/vertically-or-horizontally-stack-several-videos-using-ffmpeg)

Vertically:

```
ffmpeg -i input1 -i input2 -filter_complex vstack=inputs=2 output
```

Horizontally:

```
ffmpeg -i input0 -i input1 -filter_complex hstack=inputs=2 output
```

- [Other sources:](https://trac.ffmpeg.org/wiki/How%20to%20speed%20up%20/%20slow%20down%20a%20video)


### Convert sequentially number files to a movie

 Flags:
 
``` 
  -r :framerate
  -i : input files number sequentially (the example below has 5 digits with leading zeros)
```

```
ffmpeg -r 1 -i movie-%05d.png apl-movie.mp4
```

<!--
### COnvert svg to png using inkscape on command like.
# Flags:
#  -W  : width (if no height is given, it's computed automatically)
-->

```
inkscape -z -e output.png  -w 1000  input.svg    
```

Set the background color for transparent svg:

```
#ffffff = white
```

```
inkscape -z --export-background="#ffffff" -e $output.png  -w 1024  $input.svg
```

```
#===============================================================================
#
# Simple bash script to convert a bunch of svg's to png's and convert to a movie
#-------------------------------------------------------------------------------
#  Sets background to white (transparent svg)
#  Adjust the numbers and file names as necessary
#  Copy and save.
#-------------------------------------------------------------------------------
#
#!/bin/bash
fnbase="movie-"
for i in {0..10}
do
    printf -v ii '%05d' $i
    echo $ii
    fnsvg=${fnbase}${ii}".svg"
    fnpng=${fnbase}${ii}".png"
    echo $fnsvg
    inkscape -z --export-background="#ffffff" -e ${fnpng}  -w 1024  ${fnsvg} 
done

ffmpeg -r 1 -i movie-%05d.png apl-movie.mp4

exit

#=================================================================================

```
