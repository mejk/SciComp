# Introduction to Gromacs

````{panels}
:column: col-lg-12 p-2

```{image} ../../images/logos/gromacs-logo.png
:alt: Gromacs
:class: bg-light
:width: 250px
:align: right
```

**Learning goals:** 
- To learn the basic structure and protocols of Gromacs
- To understand that different software employ different unit systems

**Keywords:** Gromacs, grompp, molecular dynamics, molecular topology, force field, interactions, free energy, thermostat, barostat, QM/MM, unit system, CUDA


**Associated material:** 

- [Full Gromacs documentation](https://manual.gromacs.org/)


````


<hr>



## What is Gromacs

[Gromacs](https://en.wikipedia.org/wiki/GROMACS) is simulation software package for classical MD simulations. Along with [NAMD](https://en.wikipedia.org/wiki/NAMD), [Amber](https://en.wikipedia.org/wiki/AMBER) and [LAMMPS](https://en.wikipedia.org/wiki/LAMMPS), it is one of the world's most popular MD simulation packages. Although it was originally developed for simulations of biochemical systems such as proteins, lipids and nucleic acids, it is a general purpose simulation package and has been used for nanotubes, colloids, polymers and many other systems. It has been used to simulate systems with millions of particles. Gromacs has a very rich feature set that goes far beyond what we can discuss during this course. 
<!--
It allows the user also to input interactions in tabular formats for generality.
-->

The name Gromacs is an acronym, that stands for the *Groningen Machine for Chemical Simulations*. The development started in 1991. It was originally developed in the group of [Herman Berendsen](https://en.wikipedia.org/wiki/Herman_Berendsen) at the [University of Groningen](https://en.wikipedia.org/wiki/University_of_Groningen) in the Netherlands. Since around 2001, the main Gromacs development has been done at the [Royal Institute of Technology](https://en.wikipedia.org/wiki/KTH_Royal_Institute_of_Technology) (Kungliga Tekniska högskolan, KTH) in Stockholm, [Stockholm University](https://en.wikipedia.org/wiki/Stockholm_University) and [Uppsala University](https://en.wikipedia.org/wiki/Uppsala_University), all in Sweden. Gromacs is also part of the European Union [BioExcel](https://bioexcel.eu/) (Centre of Excellence for Computational Biomolecular Research) program and it is open source. Notably, essentially all of the major simulation packages are open source.


### Relation of Gromacs to other MD simulation packages

There are many excellent software packages available for classical MD simulations. Some of the most famous ones in addition to Gromacs are 
[Amber](https://en.wikipedia.org/wiki/AMBER) (Assisted Model Building with Energy Refinement), [NAMD](https://en.wikipedia.org/wiki/NAMD) (Nanoscale Molecular Dynamics), [CHARMM](https://en.wikipedia.org/wiki/CHARMM) (Chemistry at Harvard Macromolecular Mechanics), [LAMMPS](https://en.wikipedia.org/wiki/LAMMPS) (Large-scale Atomic/Molecular Massively Parallel Simulator), [GROMOS](https://en.wikipedia.org/wiki/GROMOS) (GROningen MOlecular Simulation; one of the oldest packages as it dates back to 1978) and [DL-Poly](https://www.scd.stfc.ac.uk/Pages/DL_POLY.aspx) (not sure about the acronym, but it is likely that DL refers to [Daresbury Laboratory](https://stfc.ukri.org/about-us/where-we-work/daresbury-laboratory/) where DL-Poly originated from the group of William Smith around 1993). They all have their own particular strengths and the choice depends on the task at hand, simulation conditions, force field requirements, resources and prior experience. Gromacs, NAMD, Amber and LAMMPS offer GPU acceleration which allows for simulations of moderate size systems (10,000's of atoms) even on consumer PCs with (currently NVIDIA) graphics cards. 

The need for a particular force field is another important criterion when choosing software. Some of the above sooftware packages are restricted to only a certain family for force fields (CHARMM and NAMD software for CHARMM family of force fields and Amber software for Amber family of force fields). One particular strength of Gromacs is that it supports a very wide range of force fields including atomistic (Amber, CHARMM, OPLS, GROMOS force field families) and coarse-grained (MARTINI). There are also user-provided patches to some versions of Gromacs that support more exotic force fields such as PLUM{cite}`Bereau2014`. On the other hand, a package such as Amber may offer support to the very latest Amber-family force fields that are not yet availabe for other software. 

**Note:** When reading literature, one issue that often causes confusion is the naming of force fields and software. The names Amber, CHARMM and GROMOS can refer to either software or force field (or both). When taking about either, ones should use the software and force field version numbers as that makes the situation much clearer. This is also important from another point of view: Each of the force fields has *many* variants and it is very important to distinguish between them; to give an idea, CHARMM force fields include (and this is not a complete list) CHARMM22, CHARMM27, CHARMM36, CHARMM36m, CHARMM36 Drude, CGenFF, CHARMM27/CMAP and so on.

**More:** List of software for molecular mechanics

- [Comparison of software for molecular mechanics modeling](https://en.wikipedia.org/wiki/Comparison_of_software_for_molecular_mechanics_modeling) from Wikipedia
- A list of [Molecular dynamics software](https://en.wikipedia.org/wiki/Category:Molecular_dynamics_software) from Wikipedia

It is important to keep in mind that there is no best choice when it comes to software. The choice depends on many factors such as one needs for some specific functionality, needs for specific force fields, available hardware and so on as discussed before. The good news is that there are a lot of excellent choices such as those mentioned above (and there is more). Here, we use Gromacs. 

<!--

## Main areas of use
-->



## Main features of Gromacs

Gromacs has always been known for it is very good performance, stability and its developers have always been quick to adapt new technologies such as [SSE](https://en.wikipedia.org/wiki/Streaming_SIMD_Extensions) (Streaming SIMD extensions) and [SSE2](https://en.wikipedia.org/wiki/SSE2) in the early 2000's and later [CUDA](https://en.wikipedia.org/wiki/CUDA)-based GPU acceleration. From the user point of view, Gromacs is run from the command line (CLI) - this is the case with essentially all of the simulations software. Gromacs has been ported to various computer architectures and, importantly, both input and output files are *independent* of the hardware that was used to generate them. Input files are given in ASCII format (this is also the reason why we need an ASCII editor such as `vi`, `emacs`, `atom` or such to edit the input files).

Gromacs saves data in compressed form with two options (`.xtc` and `.trr`; we will discuss the Gromacs files in a separate section below). Gromacs also provides a very large set (>100) of built-in analysis routines. The use of these routines typically require two steps:

1. identification of the atoms and/or molecules of interest. This is called *indexing* and it produces and *index file* (`.ndx`). This *index file* is then used in 
1. running the actual analysis routine. 

Both of these steps must be done on command line or, alternatively, using Python.

There are also several independent (mostly Python-based) packages that can read and analyze Gromacs output data. Examples of such packages include [VMD](https://www.ks.uiuc.edu/Research/vmd/), [PyMOL](https://pymol.org/2/), [MDAnalysis](https://mdanalysis.org), [FATSLiM](https://fatslim.github.io/) and [PyBILT](https://pybilt.readthedocs.io/en/latest/readme.html). Importantly, [MDAnalysis](https://mdanalysis.org) can also be used to analyze trajectories produced by many other simulation software including NAMD and Amber.

Gromacs, like most of the main simulation software, can be run on serial, parallel and GPU  systems. For parallelization, it supports MPI and OpenMP and parallelization across multiple GPUs. Both NVIDIA's [CUDA](https://en.wikipedia.org/wiki/CUDA) and [OpenCL](https://en.wikipedia.org/wiki/OpenCL) are supported but former offers much better performance. There are a few consequences:

- If you have a multicore laptop or desktop, you can run parallel simulations even on your own computer.
- If you have an NVIDIA GPU, you can use it to run Gromacs simulations *provided* you are running Linux. The ability of being able to use GPUs from WSL2 is being added but it is not yet (Dec. 2020) generally available. This is also important for tasks other than molecular simulations as GPU acceleration is available for, for example, the [Tensorflow](https://www.tensorflow.org/) package for machine learning.

## Quantum mechanical / Molecular Mechanics calculations (QM/MM) 

<!--

````{figure}
:alt: QMMM
````

-->

Gromacs also allows for hybrid [QM/MM simulations](https://en.wikipedia.org/wiki/QM/MM): In QM/MM, most of the simulation is done at the classical level, but a small part of the system (that is, a subsystem) is handled quantum mechanically. This requires coupling Gromacs with a quantum mechanical simulation package. At this time Gromacs has interfaces at least with [CPMD](https://www.cpmd.org/), Gaussian and [GAMESS-UK](http://www.cfs.dl.ac.uk/). Support is also planned for [CP2K](https://www.cp2k.org/) (in 2021).

<!-- 
The package includes a fully automated topology builder for proteins,
even multimeric structures.
-->

## The `grompp` preprocessor

One particular feature of Gromacs' is the [`grompp` preprocessor](https://manual.gromacs.org/current/onlinehelp/gmx-grompp.html). `grompp` is used at several stages of building a simulation, but in general it reads the file describing molecular topologies (`.top`), it checks the validity and consistency of files and builds a binary run input file (`.tpr`) that is used for execution of the MD simulation. 


Technically, `grompp` is serial preprocessor and it is used to perform several tasks *prior* to the actual simulation. In particular, `grommp` is used for the following tasks:

– To read the molecular topology file (`.top`). Then, `grompp` checks its validity, and (if everything is ok), it expands the topology from a molecular to an atomic description. That is, it builds the molecules using the atomic data.
– To reads the coordinate file. Additionally, it can generate velocities from a Maxwellian
distribution if requested in the input (`.mdp`) file.
– To reads parameters (from the `.mdp` file). This includes the number of MD time steps, time step, cut-off and so on.
- To use some of Gromacs' utility programs. This includes generating the simulation box, addion ions, processing Protein Databank (`.pdb`) files

<!--
• Parallel MD and energy minimizing program mdrun.
– Performs simulation or minimization.
- Several analysis tools g ..., ngmx.
- Utility programs pdb2gmx, genbox, genion, ....
– Produces a binary file as the sole input for the MD program. This is is very convenient as it makes starting Gromacs very easy. 
-->


## Additional features

It is impossible to give a brief yet comprehensive description of the many features that Gromacs offers. Below, some of the common ones are listed as examples. The listed features are chosen based on what will be encountered in the simulations during this course.

For integration of Newton's equations of motion, there are a few options most notably the [velocity-Verlet](https://en.wikipedia.org/wiki/Verlet_integration#Velocity_Verlet) and the [leap-frog](https://en.wikipedia.org/wiki/Leapfrog_integration) methods. For energy minimization, the main options are the [method of steepest descents](https://en.wikipedia.org/wiki/Method_of_steepest_descent) and the [conjugate gradient](https://en.wikipedia.org/wiki/Conjugate_gradient_method) method. There is an often overlooked major difference between integration of the equations of motion and energy minimization: *Integration* is the propagation of the equations of motion in time with a time step given in terms of real time. Thus, it involves updates of the particles' positions and velocities. *Energy minimization* using [steepest descents](https://en.wikipedia.org/wiki/Method_of_steepest_descent) or the [conjugate gradient](https://en.wikipedia.org/wiki/Conjugate_gradient_method) method is a mathematical (deterministic) optimization process that involves minimization of the potential energy, that is, only positions are needed. Second, even though ones gives a number of steps for the optimization process, the number of steps does not correspond to physical time but only gives an upper limit for the number of steps to be taken in case the process doesn't converge earlier. We will not discuss these methods in detail here, but it is important to understand that *optimization* using these methods does not involve time or velocities, it is simply minimization of the potential energy. This is a general feature of these methods are not specific to Gromacs or any other simulation/modeling package.

For thermostats, Gromacs offers the choices of the [Berendsen](https://en.wikipedia.org/wiki/Berendsen_thermostat), [Nosé-Hoover](https://en.wikipedia.org/wiki/Nos%C3%A9%E2%80%93Hoover_thermostat), Nosé-Hoover chain{cite}`Martyna1992` (with some restrictions), v-rescale{cite}`Bussi2007a`, [Andersen](https://en.wikipedia.org/wiki/Andersen_thermostat) and [Langevin](https://en.wikipedia.org/wiki/Langevin_dynamics) (called stochastic dynamics in Gromacs) thermostats. Currently, the [Dissipative Particle Dynamics](https://en.wikipedia.org/wiki/Dissipative_particle_dynamics) (DPD) thermostat is not available (it is available in LAMMPS). The choice of thermostat depends on the system and properties of interest, but the Nosé-Hoover and v-rescale are the most common and recommended choices. For colloidal systems, Gromacs has also [Brownian dynamics](https://en.wikipedia.org/wiki/Brownian_dynamics). As for periodic boundary conditions, Gromacs has three options, [cuboid](https://en.wikipedia.org/wiki/Cuboid), [rhombic dodecahedron](https://en.wikipedia.org/wiki/Rhombic_dodecahedron) and [truncated octahedron](https://en.wikipedia.org/wiki/Truncated_octahedron). 

<!--

````{figure} Space filling structures
````

-->

Why those ones for periodic boundary conditions? The reason is simple: When using periodic boundaries, the simulation cell must have a structure that it is [space filling](https://en.wikipedia.org/wiki/Space-filling_polyhedron). If the simulation uses closed boundaries, any structure is fine (as long as it is available in the code or if one can code it).

For barostats, Gromacs has the Berendsen{cite}`Berendsen1984`, Parrinello-Rahman{cite}`Parrinello1981a` and Martyna-Tuckerman-Tobias-Klein{cite}`Martyna1994,Martyna1996` (with some restrictions) as the possible options. The two latter ones are the recommended options, but the Berendsen method is often useful during the pre-equilibration of the system.

For computing the long-range electrostatic interactions, one has the choices of simple cutoff (not recommended), reaction-field, plain [Ewald summation](https://en.wikipedia.org/wiki/Ewald_summation), the particle-particle particle-mesh (P3M) and the particle mesh Ewald sum (PME). The last one is the most common choice. Gromacs has also the option to use a modified PME for systems that are not fully periodic. The most additions (not in the main version at this time) is the [Fast Multipole Method](https://en.wikipedia.org/wiki/Fast_multipole_method) (FMM) of Greengard and Rokhlin.

<!--
• Shell molecular dynamics accounts for polarizability in the simulation.
• Non-equilibrium molecular dynamics options, including accelerations on
arbitrary groups of atoms and electric fields.
-->

### Free energy calculations

Gromacs also supports free energy calculations using the slow growth method, [thermodynamic integration](https://en.wikipedia.org/wiki/Thermodynamic_integration) and [umbrella sampling](https://en.wikipedia.org/wiki/Umbrella_sampling).  [Metadynamics](https://en.wikipedia.org/wiki/Metadynamics) with its many variants can be used using the [PLUMED-plugin](https://www.plumed.org/). [PLUMED](https://www.plumed.org/) is not restricted to Gromacs but it can be used with many other packages including LAMMPS, Amber, CP2K (quantum) and so on. [PLUMED](https://www.plumed.org/) was originally introduced in 2009 and its current version PLUMED2 in 214. 

## Gromacs unit system

Every MD software has its own convention to handle units. When switching between, for example, Gromacs, NAMD, LAMMPS or others, one should pay attention to the units used in each of the software. Another circumstance in which the importance of the unit convention should be give special attention is when different analysis packages such as [MDAnalysis](https://mdanalysis.org/) or such are used. They may (and often do) use different convention(s). 

Gromacs uses the following five base units:

<!--
````{panels}
   :column: col-lg-12 p-2

-->   
<!-- table-bordered, -->
```{list-table} Gromacs' five base units,
 :header-rows: 1
 :name: Gromacs-units
 :class: table-hover

 * - **Quantity:**
   - **Unit:**
   - **Numerical value:**
 * - length:
   - nanometers
   - 10$^{-9}$ m
 * - time:
   - picoseconds
   - 10$^{-12}$ s
 * - temperature:  
   - kelvin
   - absolute scale: 0 K = -273.15 $^\circ$C
 * - mass:   
   - u (atomic unit)
   - $\approx$ 1.661  $\times$ 10$^{-27}$ kg 
 * - charge
   - elementary charge (e)
   - $\approx$ 1.602 $\times$ 10$^{-19}$ C 
```
<!--
````
-->

This gives the following derived units:


<!-- table-bordered, -->
```{list-table} Gromacs' derived units
 :align: center
 :width: 100%
 :header-rows: 1
 :name: Gromacs-units
 :class: table, table-hover


 * - **Quantity:**
   - **Unit:**
 * - energy: 
   - kJ/mol
 * - force: 
   - kJ/(mol $\times$ nm )
 * - velocity:
   - nm/ps
 * - density:
   - g/mol
 * - pressure:
   - bar
 * - dipole moment:
   - e $\times$ nm
 * - electric field:
   - kJ/( mol $\times$ nm $\times$ e)
 * - electric potential:
   - kJ/( mol $\times$ e)  
 * - compressibility:
   - bar$^{-1}$
```


## Files

Files:

During the different stages, the coordinate/structure file (`.gro`), the topology file (.top) and the run input file (`.tpr`) get updated. If some of the stages must be re-run, it may become necessary to remove one/some of `.gro`, `.top`, `.tpr` files.

````{dropdown} Example of gro file
gro
```

### Binary files and ascii files

Data analysis output, files:

Gromacs’ data analysis routines produce `.xvg` files. They need the free software xmgrace. Or if you prefer, you can write a script to handle them with python. xmgrace is easier, though, and it can produce high quality plots in various formats including png, jpg, svg and pdf.

````{dropdown} Example of an xvg file
data here
````
## References

```{bibliography} ../../references.bib
   :filter: docname in docnames
   :style: plain
```

<!--
## Gromacs cheatsheet
-->


