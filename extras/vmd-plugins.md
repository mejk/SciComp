#  VMD  plugins

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
- Provides links to additional plugins that may be useful.

**Keywords:** VMD, VMD Plugins, visualization, atomistic simulations



**Associated material:** 
- [VMD installation]()
- [VMD selections]()
- [VMD documentation](https://www.ks.uiuc.edu/Research/vmd/current/docs.html) from the VMD Home Page

````




There are lots of plugins for various analyses and other tasks. Some of them are provided with the basic installation and many are provided by VMD other users. Below is a list of VMD plugins that may be useful depending on your needs.


## Povray rendering

Povray stands for *Persistence of vision*. It can be easily installed in Linux, Mac or/and Windows 10.


`povray` can used to produce very high-quality graphics. It can be  used  directly from VMD provided `povray` is installed/included in your `$PATH`.

Installation:


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

```{tabbed} Windows 10:
Download the binary from the [povray website](http://www.povray.org/download/).

```

**More:**

- [povray stuff](http://knottsgroup.groups.et.byu.net/labbook/index.php?n=Main.UsingVMD)


<!--

## APBS 

```
unzip APBS-3.0.0
```

-->

## VMD plugins from  VMD Home

- List of [VMD plugins](https://www.ks.uiuc.edu/Research/vmd/plugins/) from the VMD home page.


## Visualizing MARTINI systems


- [Martini systems using VMD](http://cgmartini.nl/index.php/tutorials-general-introduction-gmx5/cgviz-gmx5)


## Andriy Anishkin's VMD scripts

- [Here](http://science.umd.edu/biology/sukharevlab/download.htm)

## VMD Store: More plugins

[Biomolecular SIMulations Research Group](https://biosim.pt/) at the University of Porto maintains a VMD plugin repository called *VMD Store:*


- [VMD Store](https://biosim.pt/software/)
- [vmdStore and installation instructions](https://github.com/BioSIM-Research-Group/vmdStore)

**Note:** 

- The *Molecular docking plugin* requires `autodock-tools` and `autogrid`. Autodock can be installed on Mac and Linux by downloading from the [Autodoc web site](http://autodock.scripps.edu/) or on Linux from command line using:

- the *vmdMagazine plugin* needs NAMD


````{tabbed} Linux & WSL/WSL2:

```
sudo apt install autodock autodock-getdata autodock-test autodock-vina autogrid autogrid-test
```
````

````{tabbed} Mac:
```
Does not work under Mac Catalina
```
````


## Memplugin

- [Analysis of membrane properties](https://sourceforge.net/p/membplugin/wiki/Home/)

## DruGUI

- [Druggability Suite](http://prody.csb.pitt.edu/tutorials/drugui_tutorial/intro.html)
  - Requires NAMD for simulations

## CoMD

- [Collective MD](http://prody.csb.pitt.edu/comd/) 
  * COnformational energy landscapes

## VMDIce

- Computes RMSD, RMSF and Solvent Accessible Surface Area


## MultiMSMS

[Home page](http://mariovalle.name/ChemViz/multimsms.html)

## Clustering tool

- [Clustering tool](https://github.com/luisico/clustering)

## FTProd

- [Multistructural binding site characterization](https://amarolab.ucsd.edu/php/labResources/ftprodTutorial/tutorialHome.php)

## DelEnsembleElec

- [DelPhi Ensemble Electrostatics](https://amarolab.ucsd.edu/php/labResources/delensembleelec.php)
  * Requires [DelPhi](http://compbio.clemson.edu/delphi)


## Lipid Builder

- [Creation of realistic biological membranes for molecular simulations](https://lipidbuilder.epfl.ch/plugin)

## Plumed-GUI

- [A Plumed collective variable analysis tool for VMD](https://github.com/giorginolab/vmd_plumed)

## Diffusion coefficient tool

- [VMD Diffusion Coefficient Tool](https://github.com/giorginolab/vmd_diffusion_coefficient)

## Thermodynamic and kinetic models from MD data 

- [METAGUI](https://github.com/metagui/metagui3)

## Density profile tool

- [1-D projections of  atomic densities](https://github.com/giorginolab/vmd_density_profile)
