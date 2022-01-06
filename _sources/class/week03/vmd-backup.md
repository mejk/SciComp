# Molecular visualization and VMD


````{panels}
:column: col-lg-12 p-2

```{image} ../../images/logos/vmd_logo.gif
:alt: VMD
:class: bg-primary
:width: 250px
:align: right
```
```{image} ../../images/1ubq-cropped.jpg
:alt: 1UBQ
:class: bg-primary
:width: 250px
:align: right
```

<!--
**This file:** 
- Provides instructions for installing VMD and links to additional plugins.
-->

**Learning goals:** 
- To learn the importance and utility of molecular visualization
- To learn the basic use of VMD

**Keywords:** visualization, physical model, molecular graphics, VMD, VMD Plugins, atomistic simulations

**Associated material:**
- [VMD installation](../../extras/vmd-install)
- [VMD plugins](../../extras/vmd-plugins)

**More on VMD:**

- [VMD Home Page](https://www.ks.uiuc.edu/Research/vmd/)
- [VMD tutorial](https://www.ks.uiuc.edu/Training/Tutorials/vmd/tutorial-html/index.html) from the VMD web site
- [VMD documentation and tutorials](https://www.ks.uiuc.edu/Research/vmd/current/docs.html) from the VMD web site
- [VMD plugin library and documentation for extensions](https://www.ks.uiuc.edu/Research/vmd/plugins/)
- [VMD programmer's guide](http://www.ks.uiuc.edu/Research/vmd/doxygen/)

<!--
**Alternatives to VMD:** Pymol
-->

**Note:** This visualization was done with [VMD](https://www.ks.uiuc.edu/Research/vmd/) using its internal Tachyon rendering with high resolution settings. The molecule is the structure [1UBQ](https://www.rcsb.org/structure/1UBQ) (ubiquitin) from the PDB database. The visualization combines several different representations.

````


## Why visualize?

Visualization is a key part of any data analysis, computational or experimental. It can quickly reveal important features or problems. Using simulation data to produce movies is particular powerful as it allows one to focus the time evolution of  particular part(s) of any molecule(s) or molecular property. One can also easily overlay properties/structures for comparison.

### Physical models: The model of Watson and Crick

The *physical* molecular model of Watson and Crick for the double stranded DNA is probably the most famous such a model. Although a physical model, it is a visualization based on (in this case experimental) data. Molecular graphics, that is, molecular visualization using computers, can of course produce different representations based on both experimental and computational data. Even in the case of experimental data, a *molecular model* is required to create a representation.

```{figure} ../../images/img-wiki/DNA_Model_Crick-Watson.jpg
:alt: Crick-Watson
:width: 250px
:align: left

*The physical molecular model (National Science Museum, London, UK) that [Crick](https://en.wikipedia.org/wiki/Francis_Crick) and [Watson](https://en.wikipedia.org/wiki/James_Watson) built for DNA in 1953. The individual nucleobases were cut out of aluminum. In terms of molecular models, they used rods or licorice for bonds and sheets for nucleobases.   The model itself was based on experimental data of [Rosalind Franklin](https://en.wikipedia.org/wiki/Rosalind_Franklin), [Maurice Wilkins](https://en.wikipedia.org/wiki/Maurice_Wilkins) and [Alexander Stokes](https://en.wikipedia.org/wiki/Alec_Stokes). The model allowed Crick and Watson to model how the helical structure and hydrogen bonding emerges based on the data. The DNA is a [double helix](https://en.wikipedia.org/wiki/Nucleic_acid_double_helix) and around the same time (1953), [Linus Pauling](https://en.wikipedia.org/wiki/Linus_Pauling) proposed a [triple-helical model](https://en.wikipedia.org/wiki/Obsolete_models_of_DNA_structure) for DNA.  Figure: Wikipedia, public domain.*

```

### Molecular graphics

The term [*molecular graphics*](https://en.wikipedia.org/wiki/Molecular_graphics) is most commonly used to refer to computer-based visualization of molecules although the term can be interpreted more broadly. It dates back to an MIT project on interactive molecular structures in the 1960's and in particular to [Cyrus Levinthal](https://en.wikipedia.org/wiki/Cyrus_Levinthal) who applied computer graphics to show protein structures. Levinthal is also known for [Levinthal's paradox](https://en.wikipedia.org/wiki/Levinthal%27s_paradox). Interestingly, Levinthal got his PhD in physics but later moved on to Molecular Biology. 

The difficulty with molecular graphics is that one has two dimensional representations of 3D objects (molecules). There are very interesting developments in using virtual reality applications for molecular modeling, see for example {cite}`Cassidy2020`.

One of the strengths of visualization software is to apply different representations at the same time. That allows one to visualize different aspects and their relations. 

### Experiments and visualization

Data from [x-ray scattering](https://en.wikipedia.org/wiki/X-ray_scattering_techniques), [NMR](https://en.wikipedia.org/wiki/Nuclear_magnetic_resonance) (Nuclear Magnetic Resonance; [Nobel Prize in Chemistry 1991](https://www.nobelprize.org/prizes/chemistry/1991/summary/) to [Richard Ernst](https://www.nobelprize.org/prizes/chemistry/1991/ernst/biographical/)) and [CryoEM](https://en.wikipedia.org/wiki/Cryogenic_electron_microscopy) (Cryogenic Electron Microscopy; [Nobel Prize in Chemistry in 2017](https://www.nobelprize.org/prizes/chemistry/2017/summary/) to [Jacques Dubochet](https://www.nobelprize.org/prizes/chemistry/2017/dubochet/biographical/), [Joachim Frank](https://www.nobelprize.org/prizes/chemistry/2017/frank/biographical/) and [Richard Henderson](https://www.nobelprize.org/prizes/chemistry/2017/henderson/biographical/) ).

### More reading

- [Molecular graphics](https://en.wikipedia.org/wiki/Molecular_graphics) from Wikipedia
- [History of Visualization of Biological Macromolecules](http://www.umass.edu/microbio/rasmol/history.htm) by Eric Martz and Eric Francoeur
- [History of Visualization of Biological Macromolecules: On-line Museum](http://www.umass.edu/molvis/francoeur/index.html)

### Videos discussing visualization

````{dropdown} **Movie: Molecular Visualization: Principles and Practice by Stuart Jantzen**

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/G5FxPdBMUHE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


````

````{dropdown} **Molecular visualization with VMD: Westgrid / Compute Canada workshop**

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/_skmrS6X4Ys" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


````

````{dropdown} **Virtual Reality Molecular Dynamics Visualization**

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/zzrBcHMWL3U" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

````

````{dropdown} **Cecilia Clementi: Learning molecular models from simulation and experimental data**

This is a full research talk by [Prof. Cecilia Clementi](https://en.wikipedia.org/wiki/Cecilia_Clementi) in "Machine Learning for Physics and the Physics of Learning."

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/WVSy8bdD4Gg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

````

````{dropdown} **Scalable Molecular Visualization and Analysis Tools with VMD by John Stone, UIUC**

[Dr. John Stone](http://www.ks.uiuc.edu/~johns/) is the lead developer of VMD.

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/EZwzzr5XS8Q" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

````

### Visualization and the PDB database

<!--
[History of Visualization of Biological Macromolecules](http://www.umass.edu/microbio/rasmol/history.htm)
-->


The [PDB database](https://www.rcsb.org/) (Protein Data Bank)) uses visualization very effectively for  the deposited structures. Each molecule has 3D representations that can be rotated and changed on-line. In addition, PDB has the *Molecule of the Month*. For example, see the entry for [*Sars-CoV-2 Spike protein*](http://pdb101.rcsb.org/motm/246) in [*Molecule of the Month*](http://pdb101.rcsb.org/motm). The static images use different representations and colors to express chosen features and at the bottom of the page it is possible to explore the structure and change representations on-line (the JSmol tab). This shows how much information visualization can convey more or less immediately. 

See for example:

````{dropdown} **Example PDB web page with visualization**
<iframe width="800" height="650" src="https://www.rcsb.org/3d-view/ngl/6wgs"></iframe>

````

## Molecular visualization software: VMD

Here, we use VMD for visualization. It is one of the world's most popular visualization and analysis software for molecular systems. 

### List of some popular visualization software

Before start with VMD, let's list some alternatives. There are, of course, lots of excellent software packages for visualization. Below is a list of some of the popular ones and choice often depends on the purpose, that is, is the aim to visualize (and analyze) data from experiments or simulations and produce figures for publications and reports or perhaps have live demonstrations on web page or even interactive web pages. For example, VMD and PyMol are great choice for the former but not suitable for latter purpose. For web based visualization one could use software such as Jmol/JSmol or NGL, but they are not as well suited for complex visualization and analysis as VMD or PyMol. 

- [VMD - Visual Molecular Dynamics](https://www.ks.uiuc.edu/Research/vmd/)
   - Linux, MacOS and Windows
- [PyMol](https://pymol.org)
- [Jmol](http://jmol.sourceforge.net/)
- [Avogadro](https://avogadro.cc/)
   - Avogadro's is somewhat different from VMD and PyMol in that, besides visualization, it is primarily a molecule editor, that is, it can be used to construct molecules. Avogadro is not the software of choice for generating movies, but it has unique capabilities in molecular design. It has also extension for geometry optimization, molecular orbitals, [QTAIM](https://en.wikipedia.org/wiki/Atoms_in_molecules) (Quantum Theory of Atoms in Molecules) calculations, calculation of spectra and other features.
   - Open source
   - GUI driven and has capability for plugins
   - Linux, MacOS and Windows
- [List of molecular graphics systems](https://en.wikipedia.org/wiki/List_of_molecular_graphics_systems) from Wikipedia
- [List of molecular design software](https://en.wikipedia.org/wiki/Molecular_design_software) from Wikipedia.


## What is VMD


VMD - Visual Molecular Dynamics - is a general purpose  software for 3D molecular visualization and data analysis of molecular systems. Together the [NAMD](https://www.ks.uiuc.edu/Research/namd/) simulation software, it can also be used to run interactive MD simulations and for setting up NAMD simulations. Both VMD and NAMD are developed in Theoretical and Computational Biophysics Group at the University of Illinois at Urbana-Champaign. 

VMD  was originally designed for visualization and analysis of biological systems, but it is a general purpose software that is not limited to any particular system.  It can read essentially all common molecular file formats and data produced by most common software including PDB, XYZ, NAMD, Gromacs, Amber, CPMD, and it can be used to visualize and analyze data from classical, coarse-grained and quantum simulations. VMD includes a lot of various analysis tools and it  has a plugin system for developers. VMD is also able to use CUDA acceleration if an NVIDIA GPU is present.


### Operating systems

VMD is available for Linux, Windows and OSX. VMD has both a GUI and a command line interface. 

## VMD: Basic operation


Here, only the basic operations of VMD are reviewed. It is impossible to provide all its details as VMD has extremely feature set for both visualization and analysis. The focus here is on visualization only. The aim of the examples below is to show some of VMD's capabilities and the demonstrate some of the features of its user interface. 


### Example: Visualizing human islet amyloid polypeptide

Let's start with a simple example. For that,  we download a molecule from the [PDB database](https://www.rcsb.org). In this case, the PDB ID [5MGQ](https://www.rcsb.org/structure/5MGQ) was selected. The molecule 5MGQ is an oxidized and amidated human islet amyloid polypeptide (IAPP) and it is an important molecule in diabetes II. 

The structure in that file contains 20 frames and we will use the last frame. The term *frame* means a snapshot of the molecule. Frames can come, for example, from repeated experiments or from different times steps of a simulation. In the case of VMD, the number of frames contained in a file is indicated in the VMD Main window as will be shown in the next section where the VMD user interface is demonstrated. 

The figure below shows five different representations of the molecule 5MGQ created by VMD. The figures show the same molecule form the exact same angle; nothing else has been changed except the representation, that is, coloring method, drawing method and material. What exactly these terms mean will be come apparent shortly, at this time the important thing is to see that one can convey different information by different representations. The names of the drawing methods (VMD uses these names as do many other software) are provided under each of the images. 

It is also important to notice that one can very easily (and we will see how this works) overlay representations. This is illustated in the third image from the left where two representations, *new cartoon* and *licorice*, have been overlayed. The number of ways of selecting atoms and molecules and how they are represented is extremely versatile. We will see how that works in the second example in thee next section. As it is clear from the figure, VMD can produce high-quality publication level graphics. It can also be used to render very high quality molecular movies as will be dicussed later. 



````{figure} ../../images/vmd-rendering-example.svg
:width: 700 px
:align: left

*Different representations of the PDB ID [5MGQ](https://www.rcsb.org/structure/5MGQ) (final structure out of 20 frames)),  oxidized and amidated human islet amyloid polypeptide (IAPP). This peptide is involved in the human diabetes II. Different representations are useful different purposes. From left to right: Lines with the residues show in different color, New Cartoon with coloring using secondary structure, New Cartoon and Licorice representations superposed, van der Waals, and Bonds. These and many others are available in VMD in `Graphics ->  Representations`. Rendering using `Tachyon`. Click the image to see it in high resolution.*

````




### VMD's user interface


The user interface of VMD does not depend on the operating system. Starting VMD opens three windows: The VMD Main window, the Display window and VMD console. The best way to get familiar with VMD is to use it. 

When VMD is started, the screen looks like below (with the exception that your Display window will have black background as I have changed mine to white in my default settings). In the examples below, the file `spc216.gro` that comes with Gromacs is used. If/when you have Gromacs installed, the file is located under the Gromacs installation directory in `share/gromacs/top`. As the name indicates, the file is in Gromacs' `.gro` format and VMD knows how to read the format (as it did with the above PDB case). The file is a small box (size of 1.86206 nm as shown on the last line of the file) of 216 SPC water molecules. I strongly encourage you to download the above PDB file ([5MGQ](https://www.rcsb.org/structure/5MGQ)), or any other PDB file, as well as try `spc216.gro` once Gromacs has been installed. 

Below are an example of a `.gro` file and a picture of the VMD opening screens.


````{dropdown} **Example of the .gro format**

The output below has been extracted (5 water molecules out of 216 were selected) from the file `spc216.gro` that comes with Gromacs. The `.gro` format but during a simulation binary formats are used since they take much less space to store. If you don't have Gromacs installed yet and hence no access to `spc216.gro`, you can copy and save the example below and visualize it in VMD (example is shown below). Notice that to save the date, you must use an ASCII text editor such as `vi` or comparable. 

- The 1st line has comments. Arbitrary information can be included and this line is ignored by analysis software. In this case is says: 5 water molecules, SPC model, temperature of 300K and box size of 1.86206. 
- The 2nd line: The total number of atoms. This information is required by the `.gro` format.
- The lines starting with number and SOL: 1SOL is the 1st solvent molecule. 2SOL: second solvent molecule and so on. Each solvent/water molecule consist of three atoms: OW, HW1, HW2. 
   - OW: Water oxygen
    - HW1 and HW2: Water hydrogens 1 and 2. 
- The 3rd column: Numbering of individual atoms. Each atom must have a unique identifier.
- Columns 4-6: x, y and z coordinates in nanometers.
- The last line: the size of the simulation box in nanometers. 

For example, VMD understand this format and can read and visualize the data. Notice also that formatting is strict (column position do matter)..

```
5H2O,SPC-MODEL,300K,BOX(M)=1.86206
  15
    1SOL     OW    1    .230    .628    .113
    1SOL    HW1    2    .137    .626    .150
    1SOL    HW2    3    .231    .589    .021
    2SOL     OW    4    .225    .275   -.866
    2SOL    HW1    5    .260    .258   -.774
    2SOL    HW2    6    .137    .230   -.878
    3SOL     OW    7    .019    .368    .647
    3SOL    HW1    8   -.063    .411    .686
    3SOL    HW2    9   -.009    .295    .584
    4SOL     OW   10    .569   -.587   -.697
    4SOL    HW1   11    .476   -.594   -.734
    4SOL    HW2   12    .580   -.498   -.653
    5SOL     OW   13   -.307   -.351    .703
    5SOL    HW1   14   -.364   -.367    .784
    5SOL    HW2   15   -.366   -.341    .623
     1.86206   1.86206   1.86206
```	 


The output, when visualized using VMD, looks like this:

```{figure} ../../images/5spc-waters.png
:alt: 5spc
:class: bg-light
:width: 350px
:align: left
```

````


````{figure} ../../images/vmd-start-annot.svg
:width: 850px
:align: left

*Upon opening VMD, three windows are displayed. The option `Save Visualization State...` is very useful as it allows one to save the visualization project and read it with *Load Visualization State* when restarting. Another great feature is that saved state can be used cross-platform, that is, it doesn't matter if it was saved on a Mac, it can be used on Windows or Linux as well (file path may need to adjusted, however). The console allows one to execute commands directly. The downside with the console is that one cannot use the arrow keys to move back and forth or recall previous commands. There is, however, a remedy: Under `Extensions` there is the option `Tk Console` that has all those features.*

````

#### Load a molecule

As the next step, the file  `spc216.gro` was loaded (`File -> New Molecule`). The Display window (not shown here) first shows the molecules using `Line` representation; the default represntation can be changed but lines are very quick to render so there is no need to change that setting. 

Let's first focus on `VMD Main window` and `Graphical Representations`. The figure below shows some of the key feature including the molecule name, the number of frames (the file `spc216.gro` has only one frame), the number of atoms and so on. 
The window `Graphical Representations` is opend through `VMD Main -> Graphics -> Representations`. That windows shows the selected molecule; here we have only one molecules but it is possible to have more althogh the most typical situation ist  to work with a single molecule. `Graphical Representations`. 

Some of the other important features `Graphical Representations` include the `Representations panel`. Here, it shows that the `Drawing Method` (red circle) or `Style` (in the  `Representations panel`) is `Lines`, `Coloring Method` or `Color` is `Name` and the all atoms have been selected. The buttons `Create Rep` and `Delete Rep` allows creation deletion of representations. This is also how different representations can be overlayed: Simply by creating new representations. The `Material` selector has the material/texture for representation. In addition there are the tabs `Draw style` (the currently seleced one) , `Selections` (it has the keywords and keys for selecting atoms and molecules by different criteria), `Trajectory` (when one has multiple frames especially for movies and analysis, this tab has update options for the frames)) and `Periodic` (allows selection of periodic images of the system). 


````{figure} ../../images/vmd-representations-annot.svg
:width: 850px
:align: left

The `VMD Main` window and `Graphical Representations` (under `Graphics`). Some of key features are indicated. The `Drawing Method` selector has been opened to denonstrate the different methods for representing molecules. In the above figrure showing 5MGQ, lines, new cartoon, licorice, van der Walls (VDW) and bonds were used. Coloring allows to empahsize, for example, atoms, groups or strutures. In the 5MGQ, the second image from the left used `New Cartoon` as the `Drawing Method` and `Secondary Structure` as the `Coloring Method`. The `Selections` tab shows the different standard selections.

````


#### Representations and rendering


Now that we have a better understanding of how to load a molecules/molecules and the interface, let's take a more detailed look into representations and discuss rendering (=how save images on the disk). The figure below shows the `VMD Main`, ` window, `Graphical Representations`, `File Render Controls` (accessible under `VMD Main -> File -> Render`) and the system in the `Display` window.

Here, we have *overlayed representations*. The different representations are listed in `Representations panel`. Two different arbitrary residues have been selected and they are represented using different styles and coloring methods. The rest of the molecules are show using `CPK` representation; the name [CPK](https://en.wikipedia.org/wiki/Space-filling_model) comes from the creators of this model, Robert Corey, Linus Pauling and Walter Koltun.

To save the figure, one has the *render* it. VMD has different methods for rendering. The most basic one is the one that is open in the `File Render Controls` window: The snapshot method. This method does exactly what the name suggests: It takes an exact snapshot of the Display window. There are no controls for resolution - it is deterimined by the window size. This method offers a quick way to create figures, but the quality is not good enough for publications. 

*High-quality figures* require a different rendering method, such as `Tachyon` that is available from the selector. 

**More on the topic:**

- [Molecular Representations in VMD](https://www.ks.uiuc.edu/Research/vmd/allversions/repimages/) from the VMD web site


#### Image rendering practicals

VMD supports a large number of high-quality rendering methods including `Tachyon` (comes with VMD) and `povray` (installation of PovRay is required for that). 


One important point with the different rendering methods is that they use [ray tracing](https://en.wikipedia.org/wiki/Ray_tracing_(graphics)) and thus the basic rendering on screen may (and typically does) look different than the final high-resolution picture saved into a file. This simply means that one has to find the proper settings for a given syste, somply by trying out the different options.  High resolution rendering may also take significant amount of time as the process is computationally intensive. 

Summary of the above and some additional practical points:

- The screen capture mode for rending gives *exactly* what is on the screen including the screen size. That is, the screen size determines the resolution. Thus, for high quality publication level images, other methods have to be used. 
- `Graphics -> Representations -> Material`: The choice of material has a significant effect on rendering in the high quality rendering modes (=other than screen capture). Importantly, the ray tracing methods like Tachyon and PovRay produce significantly different output as compared to the screen display.
- Pay attention to the resolution for objects such as bonds and spheres when rendering. The settings are in `Graphics -> Representations`
- Lights can be adjusted under `Display -> Lights`: There are 4 options
- For the high quality rendering options using ray tracing methods (such as Tachyon and PovRay), the options under `Display setting -> Ray tracing options` should be adjusted as necessary.
- Under `Display`, there are several important options such as using `Perspective` and `Orthographic` view. The latter is often the most suitable. 


#### Rendering with Tachyon

When using `Tachyon` rendering, the following options work in many cases:

```
Display -> Rendermode -> GLSL
Display --> Display Setting --> Shadow ON, Ambient Occl. ON
```

then, when selecting the rendering method

The following options *after the render command* work well. Adjust the resolution appropriately, the line below produces large (1024 x 1024 px) high quality pictures.


```
-aasamples 12 %s -auto_skylight 0.7 -format TARGA -res 1024 1024 -o %s.tga
```

Currently, Tachyon rendering can produce the following three formats: `TARGA`, `PSD48` (photoshop) and `BMP`. The common 
`JPEG` and `PNG` do not work.



````{figure} ../../images/vmd-render-annot.svg
:width: 850px
:align: left

VMD rendering. If the text  seems small, click for full resolution.

````


````{figure} ../../images/vmd-selections-annot.svg
:width: 850px
:align: left

VMD rendering. If the text  seems small, click for full resolution.

````

````{figure} ../../images/vmd-query-annot.svg
:width: 850px
:align: left

VMD rendering. If the text  seems small, click for full resolution.

````






### Data analysis

VMD has a wide range of built-in analysis tools. Importantly, there is no preset limit for the length of a trajectory. The available memory is the only limitation.

### Scripting and extensions

VMD also offers a very powerful scripting interface using Tcl/Tk. It has also an interface to [PLUMED](https://www.plumed.org/) collective variable analysis (requires separate installation of PLUMED).

**But I am an experimentalist:** Besides reading all the major file formats, VMD has plugins that are intended for experimental data. These include MDFF for Cryo-EM data and others.

### Special

- VMD has  some [NAMD](https://www.ks.uiuc.edu/Research/namd/)-specific tools for setting up molecular simulations. 
- VMD has an interface for reading PDB entries by accession number directly from the [PDB database](https://www.rcsb.org/). Read more [background information](https://www.rcsb.org/pages/about-us/index) about the PDB database. 
- VMD also has an interface to [APBS](http://www.poissonboltzmann.org/) (Adaptive Poisson Boltzmann Solver) for calculations of continuum electrostatics.
- VMD has a toolkit for force field parameterization called [Force Field Toolkit](http://www.ks.uiuc.edu/Research/vmd/plugins/fftk/) plugin (ffTK)

Note that many of the plugins require installation of additional software or/and libraries.

### PDB database

VMD has the capability to download  PDB files directly from the PDB database.

The PDB database is available at 

- [RCSB Protein Databank (PDB)](https://www.rcsb.org/)

### Movies with VMD

#### Problems with PDB with version 1.9.3

Version 1.9.3 has a problem of downloading files directly from the PDB database using

```
Extensions -> Data -> PDB Database Query
```

Thus, at this time one has to retrieve  PDB files by direct download.

The ability to download has been fixed in the 1.9.4-alpha41 versions (at this time there is no stable release of 1.9.4; the alpha51 works on MacOS Catalina and Linux, but crashes on Windows 10).



As an example, let's retrieve (from PDB) the COVID-19 spike protein, PDB accession code `6ZB4`

Here's the PDB web site entry for it:

- [SARS CoV-2 Spike protein, Closed conformation, C1 symmetry](https://www.rcsb.org/structure/6ZB4).


Movie showing some basic VMD operations using `6ZB4`. These include zooming, rotating and resetting the view, switching between the perspective and orthographic modes, creating representations, using selections, changing colors, querying for information about a selected residue and some other simple tasks. 

#### Orthographic vs perspective mode

### Loading and viewing a trajectory

Trajectory and structure


### Saving and re-loading a visualization

### Customizing VMD

In older versions of VMD, one could simply edit the `.vmdrc` file located in the home directory. That is, however, not recommended. The better (and also very easy way) to change the initial settings is to use the `VMD Preferences` menu under `Extensions` and from there saving the settings by clicking `Write Settings to VMDRC`. This works in Windows, Linux and Mac. For example, my preferences are white background, orthographic viewing and not showing waters.



### Rendering and tuning its quality

Resolution settings

Colors and materials

Axes on/off

Orthographic vs perspective

Depth cueing

Clipping plane

Volumetric rendering


http://mgltools.scripps.edu/downloads#msms




This is how the display size can be chosen from the VMD command shell:

```
display resize 100x100
```

#### Tachyon


Display -> Rendermode -> GLSL
Display --> Display Setting --> Shadow ON, Ambient Occl. ON



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


**High resolution movie:**

Before rendering any movies, ensure that you have enough storage space available. 


    first create the .dat file for each frame by choosing the following

    Extension -> Visualization -> Movie Maker

    Change the Movie Maker settings as

    Renderer -> Tachyon
    Name of the movie frame
    Movie Settings -> Trajectory with ‘4. Delete image files’ unchecked
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




### Using the Tcl/Tk  command shell

Tcl stands for  Tool Command Language and Tk is the graphical user interface toolkit for Tcl. Tcl/Tk is supported across the different operating systems (Windows, Linux, OSX). 











