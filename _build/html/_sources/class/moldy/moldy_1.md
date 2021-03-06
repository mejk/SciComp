# What is Molecular Dynamics (MD)

This module focuses on  molecular dynamics (MD) simulations. The aim is to learn the what MD is, to install Gromacs, the software that we will use for our simulations and to install VMD (Visual Molecular Dynamics). We start the explorations of molecular systems with VMD as visualization is one of the key components. Importantly, VMD is not only for visualization, it also provides a framework for data analysis and it can be used for both simulational and experimental data.



<!--
One the main aims this week is to understand the basic protocol and concepts of MD simulations. The actual simulations will be started next week.
-->


````{panels}
:column: col-lg-12 p-2

```{image} ../../images/boundary-conditions-snap.png
:alt: boundary
:class: bg-primary
:width: 250px
:align: right
```

**Learning goals:**
- To learn the basic MD workflow
- To understand the concept of boundary conditions
- To understand the process of initialization in MD simulations
- To understand the concepts of energy minimization, pre-equilibration, equilibration and production run
- To be able to estimate the number of molecules or/and atoms that can be put in a simulation box.

**Keywords:** Molecular dynamics, workflow, molecular topology, force field, boundary conditions, initialization, equilibration, simulation box

<!--
**Associated material:** Cheat sheet of the most common Linux commands.
-->

````

Now it is time to discuss some of the basic concepts of MD. 
As this is the first description, it  does not aim to be complete, but rather practical in the sense that basic concepts and terminology is introduced. The aim is that this knowledge helps us to start analyzing some data and setting up simulations. These concepts (as we well as several new ones) will be elaborated as we progress.


## Workflow in MD simulations

The basic workflow can be described as follows:


````{panels}
   :column: col-lg-12 p-2
   :card: 
```{figure} ../../images/molecular-simulation-workflow-simplified.svg
:width: 750px
:name: heart
:align: left
*General MD workflow independent of software. First, one must define the components, that is, the atoms and molecules and their interactions. The atoms and molecules are then used to create the simulation system. After the simulation system has undergone relaxation and pre-equilibration, the actual MD simulation can be started. The simulation produces a trajectory - the coordinates (velocities and forces can be also saved) of all of the particles as a function of time. This trajectory is used for data analysis.*
```
````


## MD workflow refined

The previous figure showed the basic parts. However, each of the parts consists of small parts that are vital in setting up MD simulations. The figure below shows some of the most important parts. Importantly, these are not specific to any particular software. The same workflow and issues are present independent of software. Which part involves the most work depends on various matter such as if new molecules need to be parameterized, is the system multicomponent, are special techniques required and so on.

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


<!--



### Integration of the equations of motion



###Boundary conditions

Impractical to contain system with a real boundary
Enhances finite-size effects
Artificial influence of boundary on system properties

Instead surround with replicas of simulated system
???Periodic Boundary Conditions??? (PBC)


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



#### Minimum image convention

Minimum image convention

Consider only nearest image of a given particle when looking for collision partners


-->

## Initialization

The system needs to be set up before the actual simulation can start. Assuming that a force field has been chosen, one needs to set up the simulation system. 1) This means assembling the system in a simulation box and 2) choosing the boundary conditions. The first part involves assigning initial coordinates for the atom and molecules. There are several possibilities for doing that. What is the most appropriate method depends on the system. For example: To create a system resembling a liquid or a gas, random generation of coordinates may be a good choice whereas for a solid-state system one may want to choose a lattice. For protein simulations, the most convenient choice may be to download a PDB file from the PDB database (PDB files have molecular coordinates). Such data may come, for example, from X-ray diffraction or NMR. Similarly, one may generate the homology models based on experimental data and use the initial coordinates from one/some of the homology model(s). Finally, a very common choice is to use coordinates data from a previous simulation.

## Energy minimization vs equilibration vs production simulation

There is an often overlooked major difference between integration of the equations of motion and energy minimization: Integration is the propagation of the equations of motion in time with a time step given in terms of real time. Thus, it involves updates of the particles' positions and velocities.     Energy minimization using [steepest descents](https://en.wikipedia.org/wiki/Method_of_steepest_descent) or the [conjugate gradient](https://en.wikipedia.org/wiki/Conjugate_gradient_method) method is a mathematical (deterministic) optimization process that involves minimization of the potential energy, that is, only positions are needed. Second, even though ones gives a number of steps for the optimization process, the number of steps does not correspond to physical time but only gives an upper limit for the number of steps to be taken in case the process doesn't converge earlier. We will not discuss these methods in detail here, but it is important to understand that optimization using these methods does not involve time or velocities, it is simply minimization of the potential energy. This is a general feature of these methods are not specific to Gromacs or any other simulation/modeling package.


**Further considerations:**

1. If one has to assemble a system consisting of several different molecules, it is usually a good idea to start from the largest molecule first. For example, take the protein and put in the simulation box. After that, solvate the system with water molecules and add the ions (if needed) last. 
1. If one continues one's own previous simulation of the same system, then one can jump directly to the production phase and the time is continued from the end of the previous simulations. Most software provide mechanisms for that
1. It is generally a good idea to use a previous simulation as a starting point since it has been already run for possibly a long time. It may still be a good idea to go through the equilibration phase and double-check that the system is indeed in equilibrium. 


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


<!--

## Initial velocities

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

#### Thermostats 

#### Barostats


## Basic concepts: Hamiltonian

Typically, the system is described by a model Hamiltonian that depends on the degrees of freedom the system has. 

The Hamiltonian expresses the total energy of an isolates system as a function of coordinates & momenta. 


\begin{equation}
\mathcal{H} \equiv \mathcal{H}(\vec{q}, \vec{p})
\end{equation}

\begin{equation}
\mathcal{H} = T +V
\end{equation}


## Basic concepts: Statistical mechanics

```{epigraph}
The object of statistical mechanics is to provide a molecular theory or interpretation of equilibrium properties of macroscopic systems.

-- T.L. Hill
```

It answers the question ???why???? in thermodynamics.


### Phase space

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
If in some cataclysm all scienti???c knowledge were to be destroyed and only one sentence passed onto the next generation of creatures,what statement would contain the most information in the fewest words? I believe it is the atomic hypothesis that all things are made of atoms???little particles that move around in perpetual motion,attracting each other when they area little distance apart,but repelling upon being squeezed into one another. In that one sentence,you will see there is an enormous amount of information about the world, of just a little imagination and thinking is applied.

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

-->

## Boundary conditions: Open, closed and periodic

Computational systems have a very limited number of particles compared to macroscopic systems. This is one of the reasons why 
it is very difficult and impractical to simulate systems that have real walls or  boundaries. In addition, one is often interested in bulk systems, such as bulk solutions of polymers or colloids, or proteins in solution. One additional difficulty in having walls is that they tend to give rise to *finite-size effects*.

The most common solution is to apply *Periodic Boundary Conditions* (PBC). The figures below explain the concept.

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
Particle motions in system with periodic boundary conditions.
```
````

<!--


### Energy minimization

### Pre-equilibration

### Equilibration

### Production run

### Trajectory / data analysis

-->



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
 To get the mass of a $^{12}$C atom, we have to divide by Avogadro???s number:

 $$
 m_\mathrm{^{12}\mathrm{C}} = \frac{12} {6.0221 \times 10^{23}}\, \mathrm{g} \approx 
 1.993 \times 10^{-23} \, \mathrm{g} =  1.993 \times 10^{-26} \, \mathrm{kg} 
 $$
```

<P></p>

### Historical notes:

[Avogadro???s number](https://en.wikipedia.org/wiki/Avogadro_constant) is named after [Amadeo Avogadro](https://en.wikipedia.org/wiki/Amedeo_Avogadro), an Italian scientist (who started out as a lawyer). Avogadro's number was originally proposed by [Jean Perrin](https://en.wikipedia.org/wiki/Jean_Baptiste_Perrin) who was also the first to determine it and was awarded the [Nobel Prize in Physics in 1926](https://www.nobelprize.org/prizes/physics/1926/perrin/biographical/). Avogadro studied gases and proposed that under given thermodynamic conditions, the volume is proportional to the constituents of that gas *independent* of the precise nature of that gas. In earlier German literature, Avogadro???s number has the name [Loschmidt number](https://en.wikipedia.org/wiki/Loschmidt_constant).

The first standard was the mass of the hydrogen atom ([Stanislao Cannizzarro](https://en.wikipedia.org/wiki/Stanislao_Cannizzaro)). The problem with this was the lightness of hydrogen which lead to large experimental errors (Perrin also used the hydrogen mass standard). In 1903, the German Chemical Society (Deutsche Chemische Gesellschaft) set the $^{16}$O scale. 

### How to estimate the number of molecules and box size


The mole (mol) is defined as the amount of substance that contains Avogadro???s number ($N_A$) of constitutive particles ($N_A \approx 6.0221 \times 10^{23}\,\mathrm{mol}^{-1}$). The constitutive particles may be molecules or atoms. Importantly, $N_A$ makes no reference to the their precise nature. The mole is one of the seven SI base units. The older, pre-2019, definition of mole is that it is the amount of chemical substance (atoms, molecules) contained in 12 grams of $^{12}$C. The molar mass is defined as mass (typically grams) divided by the amount of substance (in moles). It is thus given in units of g/mol. With this, the unified atomic mass unit can be defined as

$$
1\,\mathrm{u} = 
\frac{\mathrm{molar\,mass\,constant}}{\mathrm{Avogadro's\, constant}} =
\frac{M_\mathrm{u}}{N_\mathrm{A}} \approx 
\frac{1\,\mathrm{g/mol}}{6.022\times 10^{23}\,\mathrm{mol}^{-1}} =
1.661 \times 10^{-24}\,\mathrm{g} =
1\,\mathrm{Dalton} = 1\,\mathrm{Da},
$$		

where $M_\mathrm{u}$  is the molar mass constant. In the above, we gave the unified atomic mass in grams since that is the common notation although kilogram would be the more appropriate unit as it is one of the base SI units. In addition, it is good to keep in mind that the atomic radii are about 1 ?? while the nuclear radius is about $10^{-5}$ ??. 

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






### Example: Estimate for the number of water molecules and the size of the simulation box

The above formulas can now be used to estimate the number of water molecules and the size for the simulation box. 

````{panels}
   :column: col-lg-12 p-2
   :card: 

**Step 1:** Determine the weight of the molecule in grams. For that, its mass in unified atomic mass is needed together with Avogadro???s constant:


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

To get the weight of a water molecule in grams, we have to divide by Avogadro???s constant:

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

1. The Gromacs unit system uses *u* ($1.6605402 \times 10^{-27}$ kg) and nanometers so the above can be applied directly.
1. If you have no table available, Gromacs provides unified atomic masses in the file

```
$GMXDATA/top/atommass.dat
```

and toward the end of the file there is an entry for water with the following values for oxygen and hydrogen (of course you can check these from elsewhere as well):

``` 
SOL OW ??15.9994
SOL HW ????1.008
```
