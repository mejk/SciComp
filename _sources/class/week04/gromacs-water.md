#  MD simulation of bulk water

## Preparations

For the examples below, I created directory 

	MDCOURSE

under my home directory (in my case username is mine, in your case yours) and a couple of subdirectors in there to keep things clear: 

```
/home/username/MDCOURSE/
/home/username/MDCOURSE/Assignments/
/home/username/MDCOURSE/Assignments/Water-1
```

If unsure, here’s how you can do this (=execute the following commands in your terminal window) but as said, your work directory can be pretty anywhere:

```
cd
mkdir MDCOURSE
cd MDCOURSE
mkdir Assignments
cd Assignments
mkdir Water-1
cd Water-1
```

And just to make sure that you can access Gromacs: remember this from installation:

```
source ${HOME}/MDCOURSE/gmx/bin/GMXRC
```

Do that again. What it does is this: it puts Gromacs’ environmental variables in your system so that you can access Gromacs. Either you have to do that every time, or you can edit the `.profile`  in your home directory and put that as the last line in there.


## Background information

    • The standard Gromacs (> version 5.0) provides several 3-point models: SPC, SPC/E and TIP3P. For all 3-point models spc216.gro (located in $GMXDATA/gromacs/share/top) can be used, that is, there are no separate tip3p.gro and other files. The file spc216.gro contains 216 pre-equilibrated SPC (3-point) molecules. 
    • One 4-point model is provided (in that same location as the 3-point model): TIP4P. For a quick start, the above directory contains the file tip4p.gro which has 216 pre-equilibrated (at 300 K) TIP4P water molecules.
    • One 5-point model is provided (again at the same location as the tow above): TIP5P. For a quick start, the above directory contains the file tip5p.gro which has 512 pre-equilibrated (at 300 K) TIP5P water molecules.
    • There are lots of other water models. If you use them, you just have to build the topologies, pay attention to force fields and compatibility with possible solutes and their force fields.
    • You can, of course, build your system starting from a single H2O.
    • There are force field directories, such as 
          gromos54a7.ff
          
      within the above directory. Each of these force field directories have their respective .itp files for the water models to be used with them. In addition, each of these directories has a file 
          watermodels.dat 
          
      which contains some info regarding the force field and the recommended water models.
    • Coarse-grained models: Must be obtained/built separately.


While there are several possible ways to set up a simulation for a water box, we will follow the following procedure: 1) Insert (`gmx editconf`) the pre-equilibrated 216 water molecules from the `spc216.gro` file (648 atoms) centered in a box of chosen geometry (we will use cubic and rhombic dodecahedron). 2) After setting up the initial systems and defining the size (`gmx editoconf`), 3) the simulation box is then filled with more water (`gmx solvate`). These steps constitute the setup process.

There are a few things worth repeating before we start: Use descriptive file names. That is particularly useful if you need to trace back your steps, start new simulations using the same structures, and in finding errors. Pay attention to the error messages and other messages the software produces. Keep also in mind that at almost each step, a new `.gro` file is created. Using unique and descriptive file names helps to keep track of the `.gro` files created at various stages.

What's the deal with 216 SPC molecule file and the box vectors?


Where does it come from?

Let's figure it out:

1. Normal density of water is 1 g/cm3
1. We have 216 water molecules
1. Mass of a water molecule is:
1. 216 water molecules weigh:
1. The last line says: This gives a box of volume:
1. Let's try it out: 216*x/volume


## Step 1. Generate the simulation box(s) with desired geometries depending on boundary conditions (we'll use PBC).

- Note 1: Remember the command `source`.
- Note 2: Below: replace username by your own username 
- Note 3: Unless otherwise said, the commands must be on one line


1. Generate a cubic box with side of length 10 nm with the system of 216 waters centered inside it using the command below. Important: this must be on one contunuous line so be careful if you are copy-pasting (and remember to replace username by your actual username!):

Notes: The box size of 5 nm will give roughly 3,800 water molecules (as you will in the next step). This should be ok even with older computers. You can also change it to a smaller number to speed up computations later on, but it should be larger than 2.8. If you change the number, it may be a good idea to change the name so that it describes what the file contains/


```
gmx editconf -f /home/username/MDCOURSE/gmx/share/gromacs/top/spc216.gro -o spc216-for-filling-cubic-5.gro -bt cubic -box 5
```


````{dropdown} Explanation of the procedure
What is happening above: you must have the input file spc216.gro. The 216 water molecules are put inside a new cubic simulation of size 5 nm. You should check both the original `spc216.gro` and the new file  `spc216-for-filling-cubic-5.gro` using VMD). The file `spc216.gro` is the only input file here. A new file is generated as specied by the option `-o` (stands for output). This new file is called `spc216-for-filling-cubic-5.gro`. The number after -box determines the vector length (remember that Gromacs’ units are in nanometers), that is, `-box 5` generates a cubic box with a size of 5 nm. In detail: 

```
-f: input file. Typically .gro, .pdb or .tpr. We use .gro
-o: output file. Typically .gro
-bt: box type. 
-box: Vector length(s) [box size]. For cubic and dodecahedral boxes only one value is needed. Centers the system (no -c needed). Gromacs uses nanometers.
```
````


```{dropdown} What can go wrong?
Many things of course. 1) Gromacs didn’t find `spc216.gro`. One possibility is then to copy it from `$GMXDATA/top` to your current work directory or refer to it directely (that’s what we are doing above). 2) The above commands must be on a single line so be careful when you copy-paste. The same applies to the rest.
```


````{dropdown} For afficionados: Rhombic dodecahedral box
```
gmx editconf -f /home/username/MDCOURSE/gmx/share/gromacs/top/spc216.gro -o water-box-econf-dode.gro -bt dodecahedron -box 5
```
````

### Step 2: The simulation box needs to be filled with water.


1. Generate a cubic water box, that is, let’s fill the box generated above:

```
gmx solvate -cp spc216-for-filling-cubic-5.gro -cs spc216.gro -o spc216-solvated-noff-cubic-5.gro
```

Gives: 383 SOL (water molecules; this number may be slightly different for you) at density of 970.323 g/l	

````{dropdown} Rhomibc dodecahedral water box
Generate a rhombic dodecahedron water box:
```
gmx solvate -cp water-box-econf-dode.gro -cs spc216.gro -o water-box-solvated-dode.gro
```
Gives: 3838 SOL (water; this number may be slightly different for you) molecules at density of 970.323 g/l.

````

The number of molecules will most likely be slightly different for you (and everyone for that matter). Why? Because the process of solvation involved random numbers. You should check that the density is reasonable.

Notes: 
```
-cp: 	input file. This contains the solute. Box size is included in 	this (we defined this with editconf above).
-cs: 	input file. This contains the solvent.
-o: 	output file. The part noff just tells that no force field has 	been incorporated yet
```. 

After completing Step 2, we have the initial structures ready. We have not, however, associated force fields with them or any other parameters for that matter – if you have used Gromacs before to, say, solvate a protein, you notice that we did not specify a topology file above. This is what we will do next. You should open the file `spc216-solvated-noff-cubic-5.gro` in VMD and see how the system looks like.

Although the small 216 water molecule system was equilibrated, these larger new systems are not; we used the small 216 system since it was pre-equilibrated with a densigty close to real water density. By multiplying that system, we obtained a new larger one that has density close to what the density of water should be. The new system, is however, not in equlibrium and that is what we aim to do shortly.

### Step 3. Generate the topology and index files

The above procedure defined the initial coordinates but not the force fields and topologies. This is done with gmx pdb2gmx. When run, it asks for force field and the specific water model – so far we have only defined the water model to be a 3-site model instead of 4- or 5-site model but we have not defined if the model is SPC, SPC/E or TIP3P. Topology: the molecular connections.
Note: gmx pdb2gmx produces 3 files: topology, positition restraints and .gro (or other specified).
	1. Generate a cubic simulation box:
gmx pdb2gmx -f spc216-for-filling-cubic-5.gro -o spc-oplsaa-solvated-cubic.gro -p spc-oplsaa-solvated-cubic.top -n spc-oplsaa-solvated-cubic.ndx

When prompted, select OPLS-AA (option 15) for the force field and SPC (option 6) for the water model. The output files above have been named with that assumption. Change the names if you change the force field / water model. Pay attention to the messages if there are any errors or warnings.

	2. Generate a rhombic dodecahedron. Proceed as above:

gmx pdb2gmx -f water-box-solvated-dode.gro -o water-box-solvated-dode-complete.gro -p water-box-solvated-dode-complete.top -n water-box-solvated-dode-complete.ndx

Again, select OPLS-AA for the force field and SPC for the water model.

Notes: 
```
-f: 	input file. 
-o: 	output file.
-p: 	output file. Topology.
-n: 	output file. Contains reordered groups.
```

### Step 4: Run the grompp pre-processor. This generates the run file for relaxation

This is the first time we use grompp and we do need a .mdp file. This must be done before executing the commands below. The .mdp file contains all the runtime parameters and protocols. However, for the minimization step, very little is needed.
The .mdp file for energy minimizatio can look as simple as the one below and it must be plain ASCII. Generate this file now – otherwise the command below will not work. Name the em.mdp:


````{dropdown} The `.mdp` file for minimzation: 'em.mdp`
```
;=======================================================================
; FILENAME: em.mdp
;==================================================================
; 
; Note: emtol and emstep may limit convergence. They
; can be commented out. In that case the criterion is set
; by nsteps and machine precision whichever is met first
;
integrator		= steep	; steepest descents, cg for conjugate grad.
; emtol   		= 1000.0 	; Stop when max force < 1000.0 kJ/mol/nm
;emstep  		= 0.01  	; Energy step size
nsteps		 	= 1000		; max # of steps unless process converges 1st
;
; Interactions and neighbours:
;------------------------------
;
nstlist		= 1		; doesn't matter with verlet (next)
cutoff-scheme		= verlet	; works for GPU too. 
vdw-type		= cut-off	; how to handle van der Waals interactions
rvdw			= 1.0		; van der Waals cutoff
coulombtype		= pme		; safe and good. Avoid cutoffs.
rcoulomb		= 1.0		; cutoff for real-space part of PME
pbc			= xyz		; periodic boundary conditions
;=======================================================================
```
````

This is an energy minimization step (not a true simulation) and since we are using deterministic optimization, some of the above parameters are not critical. It is, however, good to set the correctly from the beginning (pme, etc.). 
Notice: The same .mdp file is good for both of the cubic and dodecahedral cases (as well as others).
Important: The grommp command below combines information from em.mdp and the solvated system we created above and generates a run input file (.tpr)
Notice: When you execute the commands below, pay attention to possible errors / warnings.

1. Cubic:
```
gmx grompp -v -f em.mdp -c spc-oplsaa-solvated-cubic.gro -p spc-oplsaa-solvated-cubic.top -o spc-oplsaa-solvated-cubic-minimize
```

````{dropdown} Rhombic dodecahedron
```
gmx grompp -v -f em.mdp -c water-box-solvated-dode-complete.gro -p water-box-solvated-dode-complete.top -o water-dode-minimize

```

````

Notes: 
```
-v: 	verbose mode. Show all the messages. 
-f: 	input: the .mdp file.
-c: 	input file. Structure as generated above.
-o: 	output file. The run input file of .tpr type.
```

What can go wrong: This should be a straightforward step: information is just collected into the run input file (`.tpr`) to be used in the next step.


### Step 5: Step 5: Relaxation using energy minimization (steepest descents or conjugate gradient)

Now that we have our run input files (.tpr), we can perform energy minimization, that is, to relax the systems. This process is there to ensure that possible steric conflicts will be take care of. In other words: it may have happened that during solvation some of the molecules were put in too close contact or too far way from each other. The former leads to enormous energies (atoms cannot overlap) and the latter can lead to the molecules accelerating too fast when the actual simulation starts. 
We have now defined the initial structures, topologies and force field. In thi step we apply the method of steepest descents (conjugate gradient would work as well) to relax the system. Notice that both steepest descents and conjugate gradient are methods of deterministic optimization, they are not real simulations (that sounds like an oxymoron...). In other words, the process will stop when they the first local energy minimum is found. This means that 1) it is sometimes a good idea to repeat this after the Equilibration (next) and 2) increasing the number of relaxation steps does not lead to better convergence since these algorithms stop after they find the first local minimum.
Important: If you for some reason wish to change the parameters in the .mdp file at this time, you must return to previous stage and rerun it.
1. Cubic
gmx mdrun -v -deffnm spc-oplsaa-solvated-cubic-minimize

2. Rhombic dodecahedron:

gmx mdrun -v -deffnm water-dode-minimize
	
The syntax: 
	mdrun 		# obvious
	-v		# verbose output so that you can follow what is happening
-deffnm	# file names for input and output (all files will be named using this)

The following files will be generated by mdrun:
    • [filename].log		# log file
    • [filename].edr		# energy. Binary file
    • [filename].trr		# Trajectory. Full precision, binary format.
    • [filename].gro		# Energy minimized structure

where [filename] is either water-cubic-minimize or water-dode-minimize.

What can go wrong: Many things of course. The most common is that the minimization procedure gives errors like this:

step 14: One or more water molecules can not be settled. 
Check for bad contacts and/or reduce the timestep if appropriate.

Whether or not that is serious depends. It means, that the minimzation procedure could not find an energy-minimized position for an atom (or atoms). When this happens, the program writes a .pdb file which allows one to go back and fix things. The file is named according to the step when this happned. In this case the file is called step14.pdb. (if you got such files, take a look at them using VMD). At the end, the process gives a warning messsage that it didn’t mange to minimize energy:

Energy minimization reached the maximum number of steps before the forces 
reached the requested precision Fmax < 10.

Should you worry about this? The answer is that it depends. What you should do is this: open VMD and see that everything is at least superficially (visually ok). Second, you should run gromacs’ energy analysis to see if there was convergence. For this the .edr file is used. For example,

gmx energy -f spc-oplsaa-solvated-cubic-minimize -o energy-check.xvg

This gives you a menu you can use to select which quantitie(s) you want to plot. The very least you should look at the potential energy. You can view the xvg file with xmgrace (if you use Matlab or something else, you may need to change the comment style in the file; if you do so, you must again use an ASCII editor). If everything looks more or less ok, you can proceed to the next step (=the problem was not a serious one). In the not so fortunate case, you have two choices: try to produce a new file starting from the beginning or use one of the pdb files produced during the minimization, identify the problematic molecule and rotate or move it slightly and try again (either by editing the file, using VMD or other software).

BUT: Even if you got such an error message, you can try the next step. If it doesn’t crash, there is no need to return this is minimization step – and you should try to convince yourself why that is the case.


### Step 6: Run grompp to combine structure, topology and parameters for mdrun in NVE ensemble


If you skipped the section preceding this step, read it. If you did read even the last bit, good, let’s continue. In this step, we will perform an NVE simulation – this is a real MD simulation unlike the minimization step above. In this simulation, we keep the number particles (N), volume (V) and energy (E) constant. To be able to do all that, a new .mdp file is needed, the previous one cannot be used. You must create a new file (the one below) and I suggest you name it nve-equib.mdp. Remember that it must be an ASCII file. Notice also how there are comments in the .mdp file. Always put in comments, they are very helpful.

````{dropdown} `.mdp` file for NVE equilibration
```
;=================================================================
; Fairly minimal mdp file for NVE equilibration
; Name: nve-equib.mdp
; If in doubt: http://manual.gromacs.org/online/mdp_opt.html
;==================================================================
;
;  No position restraints in this one. If needed, add them here.
;
;== RUN CONTROL. Time in ps.  =================================
;
title		= NVE equilibration of SPC water
integrator 	= md 		; standard leap-frog. others are available incl. vv
dt		= 0.001		; time step in ps. No constraints: 0.001, w/: 0.002.
nsteps		= 20000 	; # of steps. This would mean 20 ps for MD (20000*0.001). 
comm-mode	= linear	; removes both translation and rotation of COM (center of mass).
nstcomm		= 100		; frequency (in steps) to remove COM motion
;
;== NEIGHBOR LISTS ============================
;
cutoff-scheme 	= Verlet	; Verlet is needed for GPU. Works with CPUs too
nstlist 	= 20		; neighbor list update frq. Verlet: 20-40, group <10. 20 fs.
ns_type		= simple	; method for constructing neighbor lists. Grid is faster
pbc		= xyz		; Full periodic boundary conditions
verlet-buffer-tolerance = 0.005 ; May have to use smaller value for NVE but let’s start with this
;
;== OUTPUT CONTROL ===================================================
;
nstxout		= 500		; write out coordinates every 0.5 ps. Standard: 1.0 ps
nstvout		= 500		; frq for writing out velocities
nstenergy	= 500		; frq for writing out energies
nstlog		= 1000		; frq for updating the log file
; 
;== Electrostatics. Default order: 4, tol: 1e-5, spacing: 0.12 nm, geom: 3d ==
;
coulombtype	= pme		; you really do want to use PME instead of cutoff
rcoulomb	= 1.0		; Coulomb real space cutoff
;
;== Van der Waals interactions.================================
;
; rvdw MUST be chosen to be commensurate with rcoulomb
;
vdwtype		= cut-off	; 
rvdw		= 1.0		; vdW cutoff. NOTE: 
dispcorr	= EnerPres	; Dispersion correction applied to energy & pressure
;
;== TEMPERATURE COUPLING: NVT / NpT RUNS=======================
;
tcoupl		= no		; NVE RUN
;
;== PRESSURE COUPLING: NpT RUNS =====================
;
pcoupl		= no		; NVE RUN (use this also for NVT)
;
;== GENERATE VELOCITIES: NEEDED FOR EQUILIBRATION AND SET UP =======================
;
; NOTE: gen_vel = no if the run is a continuation! 
;
gen_vel		= yes		; generate velocities from a Maxwell distribution
gen-seed	= -1		; random seed for random number generation 
gen_temp	= 300		; temperature for the above Maxwell distribution
;
;== Continuing a previous simulation? ======================================
;
; Also needed when running back-to-back equilibration runs! (NVT-> NpT)
; IMPORTANT: You may need to set gen_vel=no above. 
; 
continuation	= no 		; restarting a previous run?
;
;====================================================================================

```

````

Now that you have nve-equib.mdp generated, we must grompp again. As above, grompp takes the parameter file (), the file after minimization and created a run input file. 

### Grompp to set up and NVE run


Let’s grompp. This again combines the input parameters (nve-equib.mdp), topology and the minimized structure from the last step: 

```
gmx grompp -f nve-equib.mdp -c spc-oplsaa-solvated-cubic-minimize.gro -p spc-oplsaa-solvated-cubic.top -o spc-oplsaa-cubic-nve.tpr

	-f nvt.mdp	; input, not modified. Uses posres.top
	-c em.gro	; the structure for energy minimization as input. not modified
	-p topol.top	; topology
	-o nvt.tpr	; trajectory. Output. Modified	
```

Again, you should take a look at what is going on using VMD. You can even seen an on-screen movie: first load the .gro file (`spc-oplsaa-solvated-cubic-minimize.gro`) in VMD and then use the “Load data into molecule” option in VMD to load the `.trr` file (`spc-oplsaa-cubic-nve.trr` that is, the trajectory; the trajectory contains the coordinates at different times as defined by the parameter `nstxout` in the `.mdp` file). You should also take a look at the different quantities, at the very least the potential energy using

```
	gmx energy -f spc-oplsaa-solvated-cubic-minimize -o energy-check.xvg
```

As above, plot it with `xmgrace`. 

### Equilibration NVE run

Grompping macht spaß! Now we are set to simulate. The following command runs a short (20 ps) real NVE molecular dynamics simulation:
```
	gmx mdrun -s spc-oplsaa-cubic-nve.tpr -o -x -deffnm spc-oplsaa-cubic-nve-run
```
```
mdrun 		# obvious
-s 		# run input file. Typically .tpr (the one created in the above step)
-x 		# produces compressed trajectory (xtc)
-o 		# produces full precision trajectory
	-deffnm	# file names (all files will be named using this)
```

Again, you should take a look at what is going on using VMD. You can even seen an on-screen movie: first load the .gro file (spc-oplsaa-cubic-nve-run.gro) in VMD and then use the “Load data into molecule” option in VMD to load the .trr file (spc-oplsaa-cubic-nve-run.trr that is, the trajectory; the trajectory contains the coordinates at different times as defined by the parameter nstxout in the .mdp file). You should also take a look at the different quantities, at the very least the potential energy using

```
gmx energy -f spc-oplsaa-cubic-nve-run -o energy-check.xvg
	
```	

As above, plot it with `xmgrace`. 

**Note 1:** if you have a faster computer, you can change the nsteps parameter in the mdp file and run longer. You just need to re-grompp. If you do that, use VMD to make a movie. 

**Note 2:** If you want to explore VMD, it can even analyze and visualize hydrogen bonds.


### Let’s grompp again to set up an equilibration NVT run.

After the brief NVE run, let's perform an NVT run. For this, the .mdp file needs the following modifications in the respective sections. Let’s save a copy of the file under the name `nvt-equilib.mdp` and make in that file. Then make the changes as indicated below. As you see, some new parameters come into play.

```
tcoupl		= v-rescale	; NVT RUN
ref_t		= 300		; temperature in Kelvin
tau_t		= 0.1		; time constant for coupling. 0.1 ps
tc_grps	= System	; Let's put the whole system on single thermostat
gen_vel	= no		; we continue our previous run
continuation	= yes 		; restarting a previous run
gen_vel	= no		; we continue our previous run
continuation	= yes 		; restarting a previous run
```

Important: If you took a look at the directory, you noticed that there is also a new file, a .cpt file. That is a checkpoint file (binary) and it will be used when restarting. There is also a .gro file that was written at the same time. That contains the coordinates from the final stage of the simulations and they will be used for the restart.

Below is the grompp command. Notice that the topology file is still the same. Makes sense since the molecular connectivity has not changed.

gmx grompp -f nvt-equib.mdp -c spc-oplsaa-cubic-nve-run.gro -t spc-oplsaa-cubic-nve-run.cpt -p spc-oplsaa-solvated-cubic.top -o spc-oplsaa-cubic-nvt-run.tpr

-f 			; input, not modified. Uses posres.top
	-c 			; the structure from energy minimization. not modified
	-p			; topology
	-o nvt.tpr		; trajectory. Output. Modified	
-t			; continuation for a previous run (.cpt file) 

Again, you should take a look at what is going on using VMD. You can even seen an on-screen movie: first load the .gro file (spc-oplsaa-cubic-nvt-run.gro) in VMD and then use the “Load data into molecule” option in VMD to load the .trr file (spc-oplsaa-cubic-nvt-run.trr that is, the trajectory; the trajectory contains the coordinates at different times as defined by the parameter nstxout in the .mdp file). You should also take a look at the different quantities, at the very least the potential energy using

```
gmx energy -f spc-oplsaa-cubc-nvt-run -o energy-check.xvg
```

### Start the equilibration run using mdrun. NVT run.

We can now run an NVT simulation. We just continue where we left off after NVE:

```
gmx mdrun -s spc-oplsaa-cubic-nvt.tpr -o -x -deffnm spc-oplsaa-cubic-nvt-run
```
```
mdrun 		# obvious
-s 		# run input file. Typically .tpr (the one created in the above step)
-x 		# produces compressed trajectory (xtc)
-o 		# produces full precision trajectory
	-deffnm	# file names for input and output (all files will be named using this)
```

### Grompp again to set up an NpT run.

Now we will perform and NpT run starting from where we left off after the NVT run but first we need to grommp again. This also means that the mdp file needs to be modified again since NpT has its own requirements. Remember: the letter p means constant pressure. This allows the simulation box to adjust to the pressure (and hence density will fluctuate). That means we have to let the systems size to change and for that we have to have a barostat (Parrinello-Rahman below). Here are the changes, make the in your file and name it `npt-equilib.mdp`
	
```
pcoupl			= parrinello-rahman	; sets a parrinello-rahman barostat
pcoupltype		= isotropic		; isotropic coupling
tau_p			= 2.0			; coupling time, 2 ps
ref_p			= 1.0			; pressure in bars
refcoord-scaling 	= all			; all coords scaled
compressibility	= 4.5e-5		; as it says, compressibility
```

Let's grompp. Note that the topology file remains the same.

```
gmx grompp -f npt-equib.mdp -c spc-nvt.gro -t spc-nvt.cpt -p water-box-solvated-cubic-complete.top -o spc-npt.tpr
```

### Run an NpT simulation

After all that grompping, we are now in a position to run an NpT simulation:

```
	gmx mdrun -deffnm spc-npt
```
```
mdrun 		# obvious
	-deffnm	# file names for input and output (all files will be named using this)
```

## Visualization and data analysis


As pointed out above after each step: Always, always, always take a look at what is going on in the system! Use VMD, Pymol or whatever your favourite is. 

Energy, temperature, pressure, box dimensions, and other global properties:
    • gmx energy in Gromacs manual
Quick interactive analysis using the module energy and plotting the properties using xmgrace and gnuplot. Simply type

```
gmx energy -f filename.edr -o filename.xvg
```

and choose the property you want to plot. Then, plot it

either using `xmgrace` (from command line):	`xmgrace spc-npt.xvg`
or using `gnuplot` (open gnuplot first):	`plot “spc-npt.xvg” using 1:2`

The module energy gives access to energies, temperatures, distance restraints and the like from the .edr file. These are properties that must be monitored to determine equilibration and if the system is behaving as expected, but rarely shown in publication (since these are basic properties). The gmx energy tool is interactive.

The energy module has capabilities well beyond computing simple energies, see more on extracting data from energy files.  In addition to the energy module, Gromacs has a whole array of various analysis tools for analyzing trajectory analysis, kinetic properties, electrostatics, and so on. Let's look at some of them next. More info: Gromacs commands by topic. 
