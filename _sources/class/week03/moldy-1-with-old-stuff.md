# First look into particle simulations

````{panels}
:column: col-lg-12 p-2

**Learning goals:** 
- To learn the basic terms and terminology of particle simulations
- To have a basic understanding of molecular topologies 
- To understand the difference between particle and continuum models
- To understand the concept of force field

**Keywords:** Particle simulations, molecular dynamics, Monte Carlo, continuum simulations, molecular topology, force field, interactions

**Note:** The links are provided for additional information for those interested, not as required reading.

````

It is finally the time to discuss some of the basic concepts of particle simulations. As this is the first description, it  does not aim to be complete, but rather practical in the sense that basic concepts and terminology are introduced. This information will be needed and elaborated later and this knowledge will help in setting up simulations and in data analysis. 

<hr>

## Particle vs continuum simulations

Although *particle simulations*  seems almost too obvious a term, it needs some attention. The most common basic object in a particle simulation is an atom or, rather, a *generalized atom*. In this course we are mostly dealing with atoms in the sense that they don't have electrons. Their overall averaged properties are included in the *force fields* as we will discuss. 

<blockquote>
<b>Force field:</b> The parameters and functions that describe interactions in simulations.
</blockquote>


These electron-less atoms do, however, have many other properties allowing for comparisons between the simulation results and experiments as long as one is in the same atomistic scales (for example energies, diffusion coefficients and such). The important concept here is that by *particle simulations* we refer to a system which is composed of *discrete entities*.

<blockquote>
<b>Atom:</b> From the Greek word atomos, which means "uncuttable".
</blockquote>

These discrete entities may also be *coarse-grained atoms* (sometimes also called *superatoms*). The concept of a coarse-grained atom can be thought of as follows: Assume that there is some method that allows us to average over some chosen physical properties of a group of atoms, for example a group of atoms in a polymer, and combine them to a single larger entity. That new entity is then a *coarse-grained* atom. At first sight such a procedure may sound like that may sound like heresy or nonsense, but there are some well-justified and rigorous methods for such procedures. Such methods will not be discusses here but in case interested, see for example references{cite}`Murtola2009d,Fritz2011`. An example of such an approach is the so-called MARTINI force field{cite}`Marrink2013` in which four 'atomistic' atoms are a coarse-grained into one larger unit. 

````{figure} ../../images/water-coarse-grain.svg
:alt: coarse-grained atoms
:class: bg-light
:width: 450px
:align: left

*Examples of coarse graining. Left: A single water molecule with its hydrogens and oxygens coarse grained to a single new coarse-grained water. Right: Four water molecules coarse-grained to a single coarse-grained water molecule. This approach is used in the very popular MARTINI model{cite}`Marrink2013`. Note that the size of a water molecule is about 2.8  Å.*

````

Simulations of even large non-atomistic entities such as planets are in the category of particle simulations since they are *discrete entities*. In such simulations, the internal structure of planets or celestial bodies is not included in the simulated properties. This is similar in  spirit to not taking electrons into account in atomic-level molecular dynamics simulations.  Other examples that may not be so obvious at first sight are entities such as lattice defects in solid state systems. Defects can be treated as discrete entities and they have properties such as size and they interact over distances. Here, we use 'atomistic' atoms and the term *atomistic* is used for describing systems at the atomic scale of Ångströms and nanometers.

````{figure} ../../images/lattice-hexagonal.svg
:alt: continuum modeling
:class: bg-light
:width: 700px
:align: left

*Two examples of a lattice. Left: A hexagonal lattice with one lattice site highlighted in red. The nearest neighbors (6) of the site are marked in blue. Midle: A square lattice. The nearest neighbors (4) of a selected site (red) are marked in blue. When simulating continuum models, the partial differential equations are solved using finite difference methods on a lattice. Thus, the space is not continuous like in a particle simulation (right).*
````

In contrast to *particle simulations*, in *continuum modeling* one often uses a fixed underlying *lattice* or grid in which one solves *finite difference* equations. In such simulations the material (say, a liquid, gas or a solid) is described by a *continuous field* instead of an atom. This means that, unlike in an atomistic simulations, the material no longer has internal structure but it is described by a field or several fields. The field(s) is (are)  placed on a discrete grid and the evolution of the field(s) is (are) solved on a computer; the corresponding equations of motion are solved on a lattice or using finite element methods (FEM). Such approaches are commonly used in the fields of materials research and reaction-diffusion systems.


````{figure} ../../images/rayleigh-benard-cell.png
:alt: continuum modeling
:class: bg-light
:width: 450px
:align: left

*Example of continuum modeling. Assume a situation in which fluid is placed between two plates. The lower plate is kept at a higher temperature than the upper one (left). As the warmer and lighter fluid raises to the top, the top layer cools and becomes denser and heavier. This can lead to rotation of water as indicated by the arrows: the heavier fluid drops and lighter rises. The picture on the right shows a top view of such a situation using continuum modeling (*phase-field model*). Model this type of a system would require too many particles and hence one has to use continuum models. In this case, the equations of motion (partial differential equations) were solved on a square lattice. This type of physical situation occurs, for example in oceans and is called Rayleigh-Benard convection.*
````

````{dropdown} **Movie a simulation of a reaction-diffusion system using a field**

A movie showing an example of *continuum modeling*. The model (the so-called Gray-Scott model) describes chemical reactions between two species. The reaction starts from the lower left hand corner and as the time progresses, the whole system is covered leading to a stripy patters; this pattern describes one density of one of the chemical components, the other component has a complementary pattern. After the stripes have formed, one can observe slower evolution of the pattern. That is called *coarsening*. In this case, the partial differential equations describing the system were solved on a square lattice in two dimensions.

<div style="padding:102.78% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/501235656?title=0&byline=0&portrait=0" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>
<p><a href="https://vimeo.com/501235656">Gray-Scott model</a> from <a href="https://vimeo.com/softsimu">mikko karttunen</a>.</p>



````

<!--
It is also noteworthy that *electronic structure calculations* do not belong to the category of particle simulations either as the positions of the nuclei are fixed and the electronic structure is determined by a *minimization process*. Minimization is very different from an actual simulation as will be discussed later.
-->


## Simulation methods for particle systems

The main simulation methods for particle systems are Monte Carlo and Molecular Dynamics (MD). 

### Monte Carlo 

In this course the focus is on the molecular dynamics method, but for completeness, let's briefly discuss the Monte Carlo (MC) method since it is one the most widely used simulation techniques (if not *the most widely used*) with applications ranging from social sciences, to optimizing public transport networks to particle simulations.

The MC method does *not* solve any equations of motion, instead it is a *stochastic optimization* method using an energy function: No time integration is involved but one uses random numbers for optimizing selected properties. In the case molecular systems, one typically optimizes (minimizes) the potential energy. This also means that, in its basic form, MC cannot measure any dynamical properties (there are variants like the kinetic Monte Carlo but even that doesn't have time integration). Instead, MC uses [*ensemble averaging*](https://en.wikipedia.org/wiki/Ensemble_average_(statistical_mechanics)) to compute the system's properties. 

The basic idea of MC simulation is that it uses [*pseudo-random numbers*](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) to overcome local energy barriers to reach the minimum energy state. Ranodm numbers are used to give the system a small probability to move in the direction that is energetically unfavorable. That is, in a crude sense the system 'gambles' to find the global minimum state; the name Monte Carlo comes from the [Monte Carlo Casino](https://en.wikipedia.org/wiki/Monte_Carlo_Casino) in the city of [Monaco](https://en.wikipedia.org/wiki/Monaco) in Southern France.
In terms of an atomistic system, only the positions of the atoms are used and there are no velocities. Since the particles have mutual interactions described by a potential energy, minimization of potential energy yields the equilibrium configuration of the system.  The part that sometimes causes confusion is that in MC, term *Monte Carlo steps* is used. The term indicates the number of so-called *Monte Carlo sweeps* and it is sometimes falsely equated to the *time steps* in MD simulations. In MD, there is a real time step (typically in terms of femtoseconds) but the MC step does not correspond to any physical time.


````{figure} ../../images/energy-minimum.svg
:alt: energy-minimum
:class: bg-light
:width: 650px
:align: left

*The concept behind the [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method). Consider that a system's state is described the green sphere and the that the [energy landscape](https://en.wikipedia.org/wiki/Energy_landscape) is given by the dashed line. Deterministic optimization finds the closest minimum as indicated by the arrow in the left hand side figure. Once the minimum has been reached, the system stays there. Monte Carlo is a stochastic optimization method. It uses random numbers to enable the system to move uphill in the energetically unfavorable direction as indicated by the arrow in the right hand side figure. Once the system crosses the saddle point, it can find the global minimum.*

````


Technically, a Monte Carlo simulation is the evaluation of statistical mechanical *configuration integral* and we will discuss this point later and it generates *representative samples* of the system.The key ingredients are the application of a *probability distribution* and the use of random numbers. In the case of physical systems, the equilibrium state has a unique distribution: the *Boltzmann distribution*. 

Although it may not be clear from the above, one of the great advantages of the MC method is its flexibility. In terms of atoms or particles, it can be used to simulate classical and quantum mechanical systems. It can also be applied to systems of very different nature such as optimizing train scheduling for railway networks and to numerically solve complex mathematical integrals that have no analytical solution. 

### Classical Molecular Dynamics

Now that we have an idea of the Monte Carlo, let's move on our main interest, the MD method. 
We can define classical Molecular Dynamics the following way: 

```{admonition} Definition of Molecular Dynamics (MD)
Molecular Dynamics is the evolution of Newton’s equations motion in time. 
<!-- In short, the problem is simply to solve numerically `F=ma`. -->
```

This definition has several important points: 
1. We have a *dynamical system* that evolves in time. That is, it provides *time-resolved* information. This is in contrast to the Monte Carlo method.
1. The evolution of the system in the [*phase space*](https://en.wikipedia.org/wiki/Phase_space) is determined by solving Newton's equations of motion for all the particles that comprise the system.
1. In the absence of external forces and fields, the system must evolve toward *equilibrium*, that is, the state of minimum free energy. *Statistical mechanics* tells us that equilibrium described by a unique distribution, the [*Boltzmann distribution*](https://en.wikipedia.org/wiki/Boltzmann_distribution). 


The first published article using classical MD simulations titled "*Phase Transition for a Hard Sphere System*" was published by Alder and Wainwright in 1957{cite}`Alder1957`. They simulated systems of 32 hard particles and also shorter simulations with 108 particles.  As already discussed, the first MC simulations were performed a few years before in 1952 by Metropolis et al.{cite}`Metropolis1953`. Other landmarks include the paper of Gibson et al., *"Dynamics of Radiation Damage"* which is the first time for using continous potentials in an MD simulation the same sprit as we do today{cite}`Gibson1960`. Another interesting point is the number of time steps taken in their simulation. They had 500 atoms and reported a total 219 steps which took over 3.5 hours. Keep this number in mind for the time when we set up our own simulations. Another landamark in MD simulations is the emergence of force fields and the first QM/MM simulations which can be traced to the articles of Warshel, Karplus and Lifson in the late 1960's and early 1970s{cite}`Lifson1968,Warshel1972`. 



### What is the output of a particle simulation?

The basic result of a particle simulation is a *trajectory*, that is, the positions of atoms written at a requested output interval (the output interval is typically given as an input parameter for the simulation). In the case of an MD simulation, it is also possible to output the velocities and forces together with the positions. MC simulation, however, does not have velocities or forces. Instead, it has energies. They can be written out at the the requested interval. Once shoudl also notice that whereas MD simulation has time and output interval is given in terms of time (or steps that can be easily convered to time), in a Monte Carlo simulation the MC step has no relation to real time. 

Most simulations programs also output other quantities such as energies, pressures, the size of the simulation box and so on. However, the trajectory is the most fundamental outcome of a particle simulation and it is the basis of more detailed analyses.


````{dropdown} **Example output from an MD simulation**
The actual output format varies depends on the software, but in the most typical case positions of all atoms are stored. It is also possible to store velocities and forces in the case of MD simulations. The example below shows an output in the format of Gromacs `.gro` file. 

The output below has been extracted (5 water molecules out of 216 were selected) from the file `spc216.gro` that comes with Gromacs; the full file will be used when we set up simulations that include water. Notice also that most software, including Gromacs can output trajectory data in multiple formats. The example below is the human-readable `.gro` format but during a simulation binary formats are used since they take much less space to store. File formats will be discussed in detail in later lectures. 

- The 1st line has comments. Arbitrary information can be included and this line is igonred by analysis software. In this case is says: 5 water molecules, SPC model, temperature of 300K and box size of 1.86206. 
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

### System sizes

Let's start with atoms. The size of an atom is in the scale of Ångströms (10$^{-10}$ m). Thus, it is quite easy to see that describing anything in *macroscopic* length scales is simply impossible; just make a simple estimate of how many water molecules would it take to fill a nanoscopic container of size 10 nm$\times$10 nm$\times$10 nm! For reference, if you look at the example `.gro` file from the `dropdown` above, the last line gives the dimensions of the *simulation box* in nanometers: the box length is 1.86206 nanometers. When using the more or less correct density of water, the box can fit a maximum of about 216 water molecules. Since each water has (using the SPC model) three atoms, the total number of atoms is 648.


One advantage of continuum simulations using fields is that it is possible to describe systems in much larger length scales since one is not limited to atoms. What one loses is the atomic specificity and its consequences. There are approaches that allow continuum methods to be more material specific but such a techniques are outside the scope of this course. For those interested, such methods include phase-field{cite}`Steinbach2009` and phase-field crystal methods{cite}`Provatas2007Using`.



## Summary

This section introduced a number of concepts related particle modeling. In the next sections, we will make these concepts more quantitative and put them into practise when we set up and analyze simulations and simulation data.



### Random numbers in MC

## Classical MD

## Simulation methods for particle systems

### Monte Carlo 

In this course the focus is on the molecular dynamics method, but for completeness, let's briefly discuss the Monte Carlo (MC) method since it is one the most widely used simulation techniques with applications ranging from social sciences to particles.

The MC method does not solve any equations of motion, instead it is a *stochastic optimization* method: No time integration is involved but one uses random numbers for optimizing selected properties. In the case molecular systems, one typically optimizes the potential energy. This also means that, in its basic form, MC cannot measure any dynamical properties (there are variants like the kinetic Monte Carlo but even that doesn't have time integration). Instead, MC uses *ensemble averaging* to compute the system's properties.

The basic idea of MC simulation is that it uses *pseudo-random numbers* to generate *representative samples* of the system. In terms of an atomistic system, only the positions of the atoms are used and there are no velocities. The part that sometimes causes confusion is that in MC, term *Monte Carlo steps* is used. The term indicates the number of so-called *Monte Carlo sweeps* and it is sometimes falsely equated to the *time steps* in MD simulations. In MD, there is a real time step (typically in terms of femtoseconds) but the MC step does not correspond to any physical time.


Technically, a Monte Carlo simulation is the evaluation of statistical mechanical *configuration integral* and we will discuss this point later. The key ingredient the application of a *probability distribution*. In the case of physical systems, the equilibrium state has a unique distribution: the *Boltzmann distribution*. 

Although it may not be clear from the above, one of the great advantages of the MC method is its flexibility. In terms of atoms or particles, it can be used to simulate classical and quantum mechanical systems. It can also be applied to systems of very different nature such as optimizing train scheduling for railway networks and to numerically solve complex mathematical integrals that have no analytical solution.


We can define classical Molecular Dynamics the following way: 

```{admonition} Definition of Molecular Dynamics (MD)
Molecular Dynamics is the evolution of Newton’s equations motion in time. 
<!-- In short, the problem is simply to solve numerically `F=ma`. -->
```

This definition has several important points: 
1. We have a *dynamical system* that evolves in time. That is, it provides *time-resolved* information. This is in contrast to the to Monte Carlo method.
1. The evolution of the system in the *phase space* is determined by solving Newton's equations of motion for all the particles that comprise the system.
1. In the absence of external force and fields, the system must evolve toward *equilibrium*. *Statistical mechanics* tells us that equilibrium described by a unique distribution, the *Boltzmann distribution*. 


The first published article using classical MD simulations titled "*Phase Transition for a Hard Sphere System*" was published by Alder and Wainwright in 1957{cite}`Alder1957`. They simulated systems of 32 hard particles and also shorter simulations with 108 particles. 

### Newton's laws:

Let's remind ourselves of Newton's laws of motion.

#### Newton's first law:

Possibly the simplest way of expressing Newton's first law is the following: In the absence of an external net force, an object that is at rest will remain at rest and and object that is in motion will remain in motion. 

This can be also stated as follows: Consider a single object. We can write

$$
\vec{F} = m \vec{a} = m \frac{d\, \vec{v}}{d\,t}
$$

Then, if the net force is zero, 

$$
\vec{F} = 0. 
$$

As an immediate consequence

$$
m \frac{d\, \vec{v}}{d\,t} = 0. 
$$

This means that the velocity remains constant in time: An object as rest will remain at rest and an object in motion will remain in motion.

#### Newton's second law:


This is the famous $\vec{F}= m\vec{a}$ law. We can write this as

$$
\vec{F} = m \vec{a} = \frac{d\, \vec{p}}{d\,t} m \vec{a} = m \frac{d\, \vec{v}}{d\,t}
$$

#### Newton's third law:

The third law is the law of equal magnitude and opposite direction: Any force between two objects is equal in magnitude and opposite in direction.

This is has practical consequences for simulations: When forces between any two particles are computed, we need to do it only once. For example, if we have particles A and B, then the force exerted by A on B is of equal magnitude as the force exerted by B on A but of opposite directions. Thus, using Newton's third law helps to cut the computational cost quite significantly. 




### Equations of motion

\begin{equation}
m_i \frac{d^2 \vec{q}(t)}{d\,t^2} 
= - \nabla_i U(\vec{q}) 
= - \frac{\partial \, U(\vec{q})}{\partial \vec{q_i}} 
\label{eq:newton}
\end{equation}



### Energy conservation

Conservation laws are fundamental properties of nature. In the case of MD, it is very important to notice that in its basic form MD has constant energy. In terms of *thermodynamic ensembles* this corresponds to the *microcanonical ensemble*. If $E$ is the total energy of the system, $T$ the kinetic energy and $V$ the potential energy, we have

$$
E=T+V = \mathrm{constant}
$$

Since energy is conserved, it cannot change over time. Why is that the case? Let's think what a classical MD simulation is: Assume that we have $N$ particles (let's assume them to be free and identical for simplicity). When the system is initialized, the particles are put in the simulation box. That is, we assign *initial coordinates* for each of the particles. If the system is an *ideal gas*, then there are no interactions of any kind between the particles. This means that the at after the coordinate assignment the *total energy* of the system is zero. It is zero because there are *no interactions* (meaning $V=0$) and we have *not assigned velocities* to the particles. This situation would correspond to *zero temperature* and, obviously, none of the particles can move anywhere no matter how long one waits. 

Let's impose a *finite temperature*. Since temperature means kinetic energy ($T$, we simply assign *initial velocities* to the particles. How do we do that? From thermodynamics and statistical mechanics we know that *in thermal equilibrium* particle velocities follow a particular distribution, the *Maxwell distribution*. So let's assume that we can now assign a velocity (or rather, a momentum) to each of the particles using a Maxwell distribution at temperature $T$. 

````{figure}
:alt: ideal gas
````


Now that we have the initial velocities (or momenta), the kinetic energy is then given as

$$
T = \sum_{i=1}^{N} \frac{1}{2} m_i v_i^2 
= \sum_{i=1}^{N} \frac{p_i^2}{2m_i}
= N \underbrace{\frac{3}{2} k_\mathrm{B} T}_{\mathrm{from\\equipartition\\ theorem}}.
$$

This is also the total energy the system has at the beginning, that is, $E = T$, where $E$ is the total energy (remember that we have an ideal gas with no interactions). Since the system is isolated from the rest of the world, this energy can not change in time. Thus, at any later time the *total energy*, which in this case is equal to the kinetic energy, remains constant. Thus, the total energy of the system is conserved.

Let's make the system more realistic and assume that the particles have pairwise interactions described a potential energy term $U(\vec{q}_i, \vec{q}_j)$. Then, at the beginning, we must also compute the potential energy. Since it is pairwise and depends on the positions ($q_i$) only, it can be written as

$$
V = \sum_{i=1}^{N-1} \sum_{j=i+1}^N U(\vec{q}_i, \vec{q}_j
$$

What are the consequences of this to the total energy $E$? Is in the case of ideal gas, the *total energy* ($E$) must remain constant over time. Since particles interact and move, the distribution between the kinetic and potential energy may change with the restriction that the total energy *must remain constant*.

In a simulation, we solve the equations of motion numerically and this brings in some practical problems. For example, the integration method has to be selected carefully such that it does not break the above conservation. There are also other issues but we will discuss them later when we set up simulations.

Notice there are small fluctuations. In general, such fluctuations should be a few percent only and there can not be any systematic drift.

````{figure}
:alt: energy conservation in a microcanonical system
````

<!--
and the potential energy needs to be truncated for distance shorter than some cutoff radius.
-->


#### But experimental system are at constant temperature, not constant energy

That is indeed the case. To be able to simulate constant temperature, that is, the *canonical ensemble*, we need to introduce a mechanism how to keep the temperature constant. That is done by a *thermostat*. 



### Integration of the equations of motion


### Boundary conditions

Impractical to contain system with a real boundary
Enhances finite-size effects
Artificial influence of boundary on system properties

Instead surround with replicas of simulated system
“Periodic Boundary Conditions” (PBC)


Problems:

Correlations
new artificial correlations
suppressed long-range correlations

Other geometries possible
any space-filling unit cell
hexagonal in 2D
truncated octahedron in 3D
rhombic dodecahedron in 3D
surface of a (hyper)sphere
variable aspect ratio useful for solids
relieves artificial stresses



### Minimum image convention

Minimum image convention

Consider only nearest image of a given particle when looking for collision partners


### Initialization

The system needs to be set up before the actual simulation can start. Assuming that a force field has been chosen, one needs to set up the simulation system. 1) This means assembling the system in a simulation box and 2) choosing the boundary conditions. The first part involves assigning initial coordinates for the atom and molecules. There are several possibilities for doing that. What is the most appropriate method depends on the system. For example: To create a system resembling a liquid or a gas, random generation of coordinates may be a good choice whereas for a solid-state system one may want to choose a lattice. For protein simulations, the most convenient choice may be to download a PDB file from the PDB database (PDB files have molecular coordinates). Such data may come, for example, from X-ray diffraction or NMR. Similarly, one may generate the homology models based on experimental data and use the initial coordinates from one/some of the homology model(s). Finally, a very common choice is to use coordinates data from a previous simulation.

### Energy minimization vs equilibration vs production simulation

There is an often overlooked major difference between integration of the equations of motion and energy minimization: Integration is the propagation of the equations of motion in time with a time step given in terms of real time. Thus, it involves updates of the particles' positions and velocities. Energy minimization using [steepest descents](https://en.wikipedia.org/wiki/Method_of_steepest_descent) or the [conjugate gradient](https://en.wikipedia.org/wiki/Conjugate_gradient_method) method is a mathematical (deterministic) optimization process that involves minimization of the potential energy, that is, only positions are needed. Second, even though ones gives a number of steps for the optimization process, the number of steps does not correspond to physical time but only gives an upper limit for the number of steps to be taken in case the process doesn't converge earlier. We will not discuss these methods in detail here, but it is important to understand that optimization using these methods does not involve time or velocities, it is simply minimization of the potential energy. This is a general feature of these methods are not specific to Gromacs or any other simulation/modeling package.


**Further considerations:**

1. If one has to assemble a biomolecular system consisting of several different molecules, it is usually a good idea to start from the largest molecules first. For example, take the protein and put in the simulation box. After that, solvate the system with water molecules and add the ions (if needed) last. 
1. If one continues one's own previous simulation of the same system, then one can jump directly to the production phase and the time is continued from the end of the previous simulations. Most software provide mechanisms for that. For house-written programs that is an essential feature to have.
1. It is generally a good idea to use a previous simulation as a starting point since it has been already run for (possibly) a long time. It may still be a good idea to go through an equilibration phase and double-check that the system is indeed in equilibrium. 


````{panels}
   :column: col-lg-12 p-2
   :card: 
```{figure} ../../images/molecular-simulation-initialization.svg
:width: 750px
:name: init
:align: left
Energy minimization, pre-equilibration (or relaxation), equilibration, production
```
````


#### Initial velocities

Random direction
randomize each component independently
randomize direction by choosing point on spherical surface

Magnitude consistent with desired temperature.  Choices:

Maxwell-Boltzmann:
Uniform over (-1/2,+1/2), then scale so that 
Same for y, z components

Be sure to shift so center-of-mass momentum is zero

### Integration: finite differences

Criteria:
it should be simple; easy to write and to debug
it should be stable; energy conservation 
it should be efficient; how fast it can advance the system
it should be reliable; can it handle temperatures, pressures, densities
special properties; does it vectorize, etc.


Other factors:
Almost all of the CPU time goes into computing the forces 
Memory consideration are not a major issue nowadays. However, one should beware of cache misses (what is a cache miss?)
it should be efficient; how fast it can advance the system
Energy conservation is important. The (constant) energy surface becomes a little bit rough is energy is not conserved. Rule of thumb (Ceperley): allow 0.01kT fluctuation in the total energy. 
Other symmetries, such as momentum conservation may be important



Unnecessary for Monte Carlo simulations (of course)


### Cut-off radius

### Thermodynamic ensembles

### Thermostats 

#### Berendsen thermostat

Target temperature $T_0$

\begin{equation}
\frac{dT(t)}{dt} = \frac{1}{\tau} \left[ T_o - T(t) \right]
\label{eq:Berendsen}
\end{equation}
where the parameter $\tau$ describes the coupling to the heat bath. It is sometimes called the *rise time* and in a typical simulation is around 2 ps.

**Advantages:** Very fast to compute and simple.

**Problems:** The Berendsen thermostat does not yield the correct Boltzmann distribution. Thus, it should not be used in production simulations. It is, however, useful when setting up simulations.

#### Nosé-Hoover thermostat

The Nosé-Hoover method introduces a new internal variable $s$ and an associated fictitious mass $Q$


#### v-rescale thermostat

#### Andersen thermostat

#### Lowe-Andersen thermostat


### Barostats


## Basic concepts: Hamiltonian

Typically, the system is described by a model *Hamiltonian* that depends on the degrees of freedom the system has. The Hamiltonian is a function expresses the total energy of an isolated system as a function of coordinates ($\vec{q}$) and  momenta ($\vec{p}$) of the particles, 

\begin{equation}
\mathcal{H} \equiv \mathcal{H}(\vec{q}, \vec{p}) = T(\vec{p}) + V(\vec{q}),
\end{equation}
where $T$ is the kinetic energy and $V$ is the potential energy.

<!--
\begin{equation}
\mathcal{H} = T + V
\end{equation}
-->

## Basic concepts: Statistical mechanics

```{epigraph}
The object of statistical mechanics is to provide a molecular theory or interpretation of equilibrium properties of macroscopic systems.

-- T.L. Hill
```

It answers the question “why?” in thermodynamics.


### Phase space

Let's restrict the discussion here to classical (non-quantum) systems. The state of a system is defined by the positions ($\vec{q}$) and momenta ($\vec{p}$) of all of the constituent. Since (in 3-dimensional space) each particle has three position coordinates and three corresponding momenta, each particle has six degrees of freedom. Thus, if a system has a total of $N$ particles, the system has $6N$ degrees of freedom. 

With the above, we can define *phase space* and a *phase point* in that space. 

The  Hamiltonian depends on the degrees of freedom the system has, i.e.,  

The set of states constitutes the phase space available for the system.

Any observable quantity is a function of the states of the system. For the accessible states, there is a distribution function.

Any observable quantity is a function of the states of the system. For the accessible states, there is a distribution function. Now, a quantity A is given as an expectation value by

$$
\langle A \rangle = \frac{1}{Z} 
\int 
A(\vec{q}, \vec{p}) 
f( \mathcal{H}(\vec{q}, \vec{p})) \,
d\vec{q}^N \, d\vec{p}^N
$$
is called the ensemble average, where Z, the partition function, is defined as

$$
Z = \int f( \mathcal{H}(\vec{q}, \vec{p})) \,
d\vec{q}^N \, d\vec{p}^N
$$


Interpretation of the ensemble average: It is the average over all possible states of the system. However, this is not how we usually make measurements. Typically, we perform measurements over some interval of time and then compute the average over these measurements. 
This procedure is typical for both simulation and experiments and it is called time averaging.

The time average is defined as


$$
\langle A \rangle_\mathrm{time} = \bar{A} = \frac{1}{t-t_0} \int_t_0^t A(t')\, dt'
$$


Are the time average and the ensemble average the same?

To be able to proceed, we invoke the ergodic hypothesis and hence assume that we can replace the ensemble average by the time average. 

Is this a valid assumption? Does it always hold?  

The ergodic hypothesis does not always hold. Sometimes it is a practical problem and sometimes ergodicity breaking is a fundamental property of the system.


What about simulations:

Time averaging: Molecular dynamics approach; study the evolution of the system

Ensemble averaging: Monte Carlo approach; sample the phase space by using different initial conditions.

Problems:
Glasses
Systems with metastable states
Harmonic solids
Integrable systems



## Force fields

```{epigraph}
If in some cataclysm all scientiﬁc knowledge were to be destroyed and only one sentence passed onto the next generation of creatures,what statement would contain the most information in the fewest words? I believe it is the atomic hypothesis that all things are made of atoms–little particles that move around in perpetual motion,attracting each other when they area little distance apart,but repelling upon being squeezed into one another. In that one sentence,you will see there is an enormous amount of information about the world, of just a little imagination and thinking is applied.

-- Richard Feynman in Feynman Lectures in Physics
```

### Molecular interactions: Bonded and non-bonded
\begin{equation} 
\frac{d \vec{p}}{dt}
= -\nabla  U(\vec{r})
\end{equation} 

$$
\frac{d\mathcal{H}}{dt}=0
$$

$$
U_\mathrm{LJ} (r_{ij})= 
4 \epsilon
\left[
\left(
\frac{\sigma}{r_{ij}}
\right)^{12}
-
\left(
\frac{\sigma}{r_{ij}}
\right)^{6}
\right]
$$

$$
U_\mathrm{LJ} (r_{ij})= 
\left(
\frac{A}{r_{ij}}
\right)^{12}
-
\left(
\frac{B}{r_{ij}}
\right)^{6}
$$

### Interactions between unlike atoms: Lorentz-Berthelot rules

$$
\sigma_{ij} = \frac{\sigma_i + \sigma_j}{2}
$$

$$
\epsilon_{ij} = \sqrt{\epsilon_i \epsilon_j}
$$


\begin{equation} 
V = \sum_{i} U_1(\vec{r}_i) + 
    \sum_{i} \sum_{j > i} U_2(\vec{r}_i,\vec{r}_j) + 
    \sum_{i} \sum_{j > i} \sum_{k > j > i} 
         U_3(\vec{r}_i,\vec{r}_j,\vec{r}_k) + \mathrm{higher\,\,order\,\, terms}. 
\end{equation} 


\begin{eqnarray} 
\label{eq:forcefield}
V & = & \sum_{\mathrm{bonds}} 
    \frac{k_i^\mathrm{b}}{2}(l_i - l_i^{\mathrm{ref}})^2 +
    \sum_{\mathrm{angles}}\frac{k_i^\mathrm{a}}{2}
         (\theta_i - \theta_i^{\mathrm{ref}})^2 +
    \sum_{\mathrm{torsions}}\frac{V_T}{2}
         (1 + \cos(n\omega - \gamma)) + \\ \nonumber 
  & &  \sum_{i=1}^{N-1} \sum_{j=i+1}^{N} 
      \left( 4\epsilon_{ij}
          \left[ 
             \left( \frac{\sigma_{ij}}{r_{ij}}\right)^{12} - 
             \left( \frac{\sigma_{ij}}{r_{ij}}\right)^6 
          \right] + 
          \frac{q_i q_j}{4\pi \epsilon_0 r_{ij}}
      \right)  . 
\end{eqnarray} 
% 



## Boundary conditions: Open, closed and periodic

````{panels}
   :column: col-lg-12 p-2
   :card: 
```{figure} ../../images/boundary-conditions-demonstrated.svg
:width: 750px
:name: heart
:align: left
The most common boundary conditions. Left: Open boundary. The particles a free to move anywhere in space without limitations. Middle: Particles in a box with walls. Here, hard walls are assumed meaning the particles undergo elastic collisions and are reflected back from the boundary. Right: Periodic boundaries. In this case there is no physical wall, but since the system is periodic (not open), the particles have to be wrapped back into the box when they cross the  border.
```
````


````{panels}
   :column: col-lg-12 p-2
   :card: 
```{figure} ../../images/pbc.svg
:width: 750px
:name: heart
:align: left
General MD workflow.
```
````


## MD workflow

### Energy minimization

### Pre-equilibration

### Equilibration

### Production run

### Trajectory / data analysis


````{panels}
   :column: col-lg-12 p-2
   :card: 
```{figure} ../../images/molecular-simulation-workflow.svg
:width: 750px
:name: heart
:align: left
*General MD workflow independent of software. The different colors and blocks indicate the structure: First, one must define the components, that is, the atoms and molecules and their interactions. If we only individual atoms, then the topology, or connectedness is simple: there is none and the interactions between the atoms are *non-bonded*. In molecules, the atoms composing a molecule are connected and we must describe the their connectedness. This is involves numbering the atoms in a systematic way and providing information about how they are connected. This gives rise to *bonded* interactions. The force field, that is, the description of all interactions and parameters, and topology define the molecules. When a system is composed, one also needs to provide the initial coordinates.*
```
````




## Atomic and molar masses

When we set up MD simulations, we need to have estimates, for example, for the size of the simulation box, the number of molecules and the types of molecules. This may be sometimes difficult, but it is easy to get a reasonable estimate and for that atomic and molar masses are needed. As reminder, let's review the concept of mole and its relation to the mass of a an atom:  
  
 
```{panels} 
   :container: fluid
   :column: col-lg-12
  
**Chemical notation**
^^^
 

 $^{12}$C = 1 mole of $^{12}$C
 
 Using the old (pre-2019) definition, the atomic mass of $^{12}$C is 12 amu. Hence
 [mass in amu] = 12. That is, one mole of $^{12}$C has the atomic mass of 12. 
 To get the mass of a $^{12}$C atom, we have to divide by Avogadro’s number:

 $$
 m_\mathrm{^{12}\mathrm{C}} = \frac{12} {6.0221 \times 10^{23}}\, \mathrm{g} \approx 
 1.993 \times 10^{-23} \, \mathrm{g} =  1.993 \times 10^{-26} \, \mathrm{kg} 
 $$
```

<P></p>

### Historical notes:

[Avogadro’s number](https://en.wikipedia.org/wiki/Avogadro_constant) is named after [Amadeo Avogadro](https://en.wikipedia.org/wiki/Amedeo_Avogadro), an Italian scientist (who started out as a lawyer). Avogadro's number was originally proposed by [Jean Perrin](https://en.wikipedia.org/wiki/Jean_Baptiste_Perrin) who was also the first to determine it and was awarded the [Nobel Prize in Physics in 1926](https://www.nobelprize.org/prizes/physics/1926/perrin/biographical/). Avogadro studied gases and proposed that under given thermodynamic conditions, the volume is proportional to the constituents of that gas *independent* of the precise nature of that gas. In earlier German literature, Avogadro’s number has the name [Loschmidt number](https://en.wikipedia.org/wiki/Loschmidt_constant).

The first standard was the mass of the hydrogen atom ([Stanislao Cannizzarro](https://en.wikipedia.org/wiki/Stanislao_Cannizzaro)). The problem with this was the lightness of hydrogen which lead to large experimental errors (Perrin also used the hydrogen mass standard). In 1903, the German Chemical Society (Deutsche Chemische Gesellschaft) set the $^{16}$O scale. 

### How to estimate the number of molecules and box size


The mole (mol) is defined as the amount of substance that contains Avogadro’s number ($N_A$) of constitutive particles ($N_A \approx 6.0221 \times 10^{23}\,\mathrm{mol}^{-1}$). The constitutive particles may be molecules or atoms. Importantly, $N_A$ makes no reference to the their precise nature. The mole is one of the seven SI base units. The older, pre-2019, definition of mole is that it is the amount of chemical substance (atoms, molecules) contained in 12 grams of $^{12}$C. The molar mass is defined as mass (typically grams) divided by the amount of substance (in moles). It is thus given in units of g/mol. With this, the unified atomic mass unit can be defined as

$$
1\,\mathrm{u} = 
\frac{\mathrm{molar\,mass\,constant}}{\mathrm{Avogadro's\, constant}} =
\frac{M_\mathrm{u}}{N_\mathrm{A}} \approx 
\frac{1\,\mathrm{g/mol}}{6.022\times 10^{23}\,\mathrm{mol}^{-1}} =
1.661 \times 10^{-24}\,\mathrm{g} =
1\,\mathrm{Dalton} = 1\,\mathrm{Da},
$$		

where $M_\mathrm{u}$  is the molar mass constant. In the above, we gave the unified atomic mass in grams since that is the common notation although kilogram would be the more appropriate unit as it is one of the base SI units. In addition, it is good to keep in mind that the atomic radii are about 1 Å while the nuclear radius is about $10^{-5}$ Å. 

````{dropdown} **Additional information: SI Units**

The seven SI base units:

```{list-table} SI units and the defining constants
 :header-rows: 1
 :name: SI-units
 
* - quantity
  - name
  - symbol
  - defining constant
* - time
  - second
  - s
  - hyperfine transition frequency of cesium
* - length
  - meter
  - m
  - speed of light
* - mass
  - kilogram
  - kg
  - Planck's constant
* - temperature
  - kelvin
  - K
  - Boltzmann's constant
* - amount of substance
  - mole
  - mol
  - Avogadro's constant
* - electric current
  - ampere
  - A
  - elementary charge
* - luminous intensity
  - candela
  - cd
  - luminous efficacy of 540 THz radiation
```

- More information: [International System of Units (SI)](https://en.wikipedia.org/wiki/International_System_of_Units)

````






#### Example: Estimate for the number of water molecules and the size of the simulation box

The above formulas can now be used to estimate the number of water molecules and the size for the simulation box. 

````{panels}
   :column: col-lg-12 p-2
   :card: 

**Step 1:** Determine the weight of the molecule in grams. For that, its mass in unified atomic mass is needed together with Avogadro’s constant:


$$
m_\mathrm{molecule} =
\frac{
 \mathrm{mass\,in\,u}
}
 {N_\mathrm{A}}\, \mathrm{g} 
=
\frac{
 \mathrm{mass\,in\,u}
} 
{(6.0221 \times 10^{23})}
\, \mathrm{g} 
$$

**Step 2:** We need to have some approximate density ($\rho$) and number of molecules ($N_\mathrm{molecule$}). Since the simulation box is in nanometers, we should convert this to grams/nanometers: $1\,\mathrm{g/cm^3} = 10^{-21}\,\mathrm{g/nm^3}$:

$$
\mathrm{density\,in\,grams/nm^3} =
\frac
{\mathrm{mass\,in\,grams}}
{\mathrm{volume\,in\, nm^3}}
= \frac
{N_\mathrm{molecule} \times m_\mathrm{molecule}}
{\mathrm{volume\,in\, nm^3}}
$$


**Step 3:** Solve for volume and assume that the simulation box is cubic

$$
{\mathrm{volume\,in\, nm^3}}
= \frac
{N_\mathrm{molecule} \times m_\mathrm{molecule}}
{\mathrm{density\,in\,grams/nm^3}}
=
\frac
{N_\mathrm{molecule} \times m_\mathrm{molecule}}
{\rho \times 10^{-21}}
%}
\,
\mathrm{nm}^3
$$

This gives the very useful formula for the simulation box size:

$$
L = \sqrt[3]{\frac{N_\mathrm{molecule} \times m_\mathrm{molecule}}
{\rho \times 10^{-21}}}.
$$

````


**Task: Estimate the simulation box size for a given number of water molecules:**

Use the above to estimate the (cubic) box size that is needed for 3,000 water molecules. Try to solve this first on your own before seeing the solution.


```{dropdown} **Solution:**

**Step 1:** The unified atomic mass of water (using table values for the unified atomic masses of hydrogen (1.008 u) and oxygen (15.9994 u)) is 

$$
(15.994 + 2 \times 1.008) \, \mathrm{u} 
= 
18.0154 \, \mathrm{u}
$$

With this the molar mass is

$$
M(\mathrm{H_2O}) = (15.994 + 2 \times 1.008) \, \mathrm{g/mol} 
= 
18.0154 \, \mathrm{g/mol}
$$

To get the weight of a water molecule in grams, we have to divide by Avogadro’s constant:

$$
m_\mathrm{H_2O} = 18.0154 /(6.0221 \times 10^{23})\, \mathrm{g} \approx 2.9915 \times 10^{-23} \, \mathrm{g}
$$

**Step 2:** The density of water is approximately $1\,\mathrm{g/cm^3}$. We have 3,000 water molecules.


**Step 3:** Use the formula

$$
L=\sqrt[3]{
\frac
{N_\mathrm{H_2O} \times m_\mathrm{H_2O}}
{\rho \times 10^{-21}}
}
\,
\mathrm{nm}
$$

Substitution gives

$$
\underline{
\underline{
L=\sqrt[3]{
\frac{
3000 \times 2.9915 \times 10^{-23}
}
{
10^{-21}
}
} \,\mathrm{nm}
=\sqrt[3]{3000 \times  0.029915} \,\mathrm{nm}
\approx
4.48 \, \mathrm{nm}
}}
$$

```


**Gromacs notes: Number of water molecules and box size**

1. The Gromacs unit system uses grams and nanometers so the above can be applied directly.
1. If you have no table available, Gromacs provides unified atomic masses in the file

```
$GMXDATA/top/atommass.dat
```

and toward the end of the file there is an entry for water with the following values for oxygen and hydrogen (of course you can check these from elsewhere as well):

``` 
SOL OW  15.9994
SOL HW   1.008
```




## References

```{bibliography} ../../references.bib
   :filter: docname in docnames
   :style: plain
```
