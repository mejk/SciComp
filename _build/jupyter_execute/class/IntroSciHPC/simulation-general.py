#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
from IPython.display import Markdown as md
updated = datetime.now()
now = updated.strftime("%A, %B %d %Y at %H:%M" )


# # General aspects of modeling and computer simulations
# 

# In[2]:


md(f"-Last updated on {now}")


# 
# ````{panels}
# :column: col-lg-12 p-2
# 
# 
# **Learning goals:** 
# 
# - To have an overview of the *process* involved in modeling and simulation. This is illustrated by a concrete example. Please notice that although the example is taken from a particular field, the process itself doesn't depend on the application field.
# - To understand how modeling even simple systems can be a very challenging and interdisciplinary problem.
# 
# **Keywords:** physical phenomena, algorithm, code, model, analysis, debugging, comparison to experiments, visualization
# 
# 
# ````

# <small>
# 
# ```{epigraph}    
# Big Science. Hallelujah. Big Science. Yodellayheehoo. <br>
# You know. I think we should put some mountains here. <br>
# Otherwise, what are all the characters going to fall off of? <br>
# And what about stairs? Yodellayheehoo. Ooo coo coo.
# 
# -- Laurie Anderson, Big Science 
# ```
#     
#     
# </small>    
# 
# ```{dropdown} Music: Laurie Anderson, Big Science
# 
# <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/vTHiN6Qwdgs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# 
# ```
# 

# ## General approach
# 
# Let's discuss a few general and important aspects that relate to all computer simulations and modeling. {numref}`modeling-schema` shows the general idea - this is independent of the application field. 

# <!--
# <table class="lblue">
#     <tr>
#         <td>
#             <img src="./img/modeling-schema.svg" width="100%"/>
#         </td>
#     </tr>    
#     <tr>
#         <td colspan="1">
#         Figure: Some general aspects about modeling and computer simulations. Building a model and setting up simulations is a complex process and each stage needs to be considered carefully and validated extensively.  Mistake at any level can render the whole process wrong with heaps of meaningless data. That happens more frequently that one would expect; that the software doesn't crash doesn't imply anything about the correctness of the results.   
#         </td>
#     </tr>
# </table>    
# -->
# 
# ````{panels}
#     :column: col-lg-12 p-2
#     :card: no-shadow
# ```{figure} img/modeling-schema.svg
# :width: 800px
# :name: modeling-schema
# :align: left
# *Some general aspects about modeling and computer simulations. Building a model and setting up simulations is a complex process and each stage needs to be considered carefully and validated extensively.  Mistake at any level can render the whole process wrong with heaps of meaningless data. That happens more frequently that one would expect; that the software doesn't crash doesn't imply anything about the correctness of the results. The figure is based on {cite}`Eastwood:88yh`* 
# ```
# ````

# ## Example: Modeling water
# 
# 
# Let's consider the items in {numref}`modeling-schema` using a concrete example. The procedure and considerations below are, by necessity, simplified but should give an idea the type of considerations one has to take. Some of the choices and decisions are also coupled.
# 
# 
# ````{panels}
# :card: shadow-none, border-0 
# :column: col-9 p-0 m-0
# 
# **Physical phenomenon/phenomena:** Let's use the behavior of bulk water as an example. We need to decide what we wish to model. Liquid-gas or liquid-ice phase transition? Structure of water? Or perhaps diffusion of water or the dynamics of the hydrogen bond network? Or hydrophobic hydration? One also needs to review previous research to know what kind of problems there have been and what are the undisputed correct results (if any). 
# 
# **Example:** Water dynamics is complex & has practical importance:
# 
# ```{figure} img/water-jumping.png
#    :width: 100%
#    :name: water-jump-jumping
#    :align: left
# ```
# <small>
# 
# **Some interesting previous results:** 
# - *A molecular jump mechanism of water reorientation* {cite}`Laage2006a`
# - *Observation of Immobilized Water Molecules around Hydrophobic Groups* {cite}`Rezus2007`
# 
# </small>
# 
# 
# ---
# :column: col-3
# :card: border-1
# 
# ```{figure} img/modeling-schema-small-physical.svg
#    :width: 100%
#    :name: schema-small
#    :align: right
# ```
# ````
# 
# 
# ````{panels}
# :card: shadow-none, border-0
# :column: col-9 p-0 m-0
# 
# **Construct/choose a model:** We need to decide what is the level, that is, the level of detail, and time and length scales that we are interested in. Do we need quantum mechanics? Is a classical atomistic model enough or should we use a coarse-grained model? Even at the classical level there are tens of existing models including acronyms such as ST2, TIP3P, TIP4P, TIP4P/2005, TIP5P, TIP5P/2008, SPC, SPC/E and so on. How do we know which one(s) to choose? Should one use more than one model? What has been done with these models? Is it/are they able to capture the phenomena of interest? 
# 
# **Here:** A quantum level model was needed. The basic model didn't include van der Waals interactions (density functional theory doesn't) so they needed to be added. This may sound odd, but [inclusion of van der Waals interactions in a quantum level simulation](https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/dft-d3/) is a non-trivial task.
# 
# ---
# :column: col-3
# :card: border-1
# 
# ```{figure} img/modeling-schema-small-construct.svg
#    :width: 100%
#    :name: construct-small
#    :align: right
# ```
# 
# ````
# 
# ````{panels}
# :card: shadow-none, border-0
# :column: col-9 p-0 m-0
# 
# **Choose numerical algorithm(s):** Even in the case we are planning to use a software package, we need to decide which one of the algorihms the package offers we should use. For example, for integration of the equations of motions each package offers several options. If we are going to write our own code, then we need to decide which one to implement. How do we deal with interactions? They need to be truncated but what is the most reliable way to do it? Does the system have long-range interactions? If so, do we wish to use Fourier transform-based algorithms or real space ones? In either case, there are several choises that one needs to understand. If we are writing out own code, we need to decide how to speed up the simulations - normal MD scales as $\mathcal{O}(N^2)$ where $N$ is the number of particles (the so-called [big-O](https://en.wikipedia.org/wiki/Big_O_notation) notation is used to express how well algorithms scale). We can do better using tables or multisteping. Which one to choose? Do we need constant temperature or pressure constant pressure to better mimic experimental conditions? Which method to choose? What kind of boundary conditions do we need? How can we simulate bulk conditions with a relatively small number of particles? If one uses a method that is part of an existing code, then the choice of the algorithm comes with the software. 
# ---
# :column: col-3
# :card: border-1
# 
# ```{figure} img/modeling-schema-small-numerical.svg
#    :width: 100%
#    :name: numerical-small
#    :align: right
# ```
# ````
# 
# ````{panels}
# :card: shadow-none, border-0
# :column: col-9 p-0 m-0
# 
# **Write/choose a simulation program:** Do we need to write our own code or can we use one the existing packages? This problem is very general and we could choose a software package. There are lots of possibilities including CPMD, CP2K, Gromacs, NAMD, Amber, CHARMM, DL Poly, LAMMPS and others. Or should we write your own code? If so, which programming language to use? Fortran, C, C++, python, CUDA or something else? Will this program be used in other projects? How much time will it take to write a code, debug and verify it? Do we wish to provide as open source? If so, how will it be maintained? Debugging is the most time consuming and important part!
# 
# **In this case,** we are interested in the picosecond-level dynamics and wish to use a quantum mechanical model. Of the many possible choices, let's choose the [CPMD package](https://www.cpmd.org/wordpress/) (Car-Parrinello Molecular Dynamics). It also turned out that the code needed some additions. They were tested and verified against previous simulations and experiments.
# ---
# :column: col-3
# :card: border-1
# 
# ```{figure} img/modeling-schema-small-program.svg
#    :width: 100%
#    :name: prgm-small
#    :align: right
# ```
# ````
# 
# 
# ````{panels}
# :card: shadow-none, border-0
# :column: col-9 p-0 m-0
# 
# **Perform computer simulations:** Before starting simulations: Have you debugged your code or/and 
# checked that the package that you have chosen is appropriate and has no errors in the parts relevant
# for you? Do you understand the input data and parameters, and the simulation protocol? Important: even the most well-established codes have errors and problems, but the biggest error source of all is the user! Finally, how to run very long runs in batches? 
# 
# **Here:** We can prepare the systems on local workstations, but the production simulations need large-scale resources with lot of memory. [Compute Canada](https://www.computecanada.ca/) comes to help.
# 
# ---
# :column: col-3
# :card: border-1
# 
# ```{figure} img/modeling-schema-small-simulation.svg
#    :width: 100%
#    :name: sim-small
#    :align: right
# ```
# ````
# 
# ````{panels}
# :card: shadow-none, border-0
# :column: col-9 p-0 m-0
# **Analyze data and interpret:** This is where the interesting part starts - provided we have confidence in our simulations. Do we need to write software to analyze the data or do appropriate tools exist? If the former, there are also practical questions such as how to read in the data; the data files may be massive and they may use some specific format(s), or they may be compressed.
# 
# **Here,** we can analyze hydrogen bonding in bulk water and in the solvation shell of a small hydrophobic group in a molecule. It is not all
# four-coordinated. Some of the analysis software needed to be written.
# 
# ```{figure} img/water-bonds.png
#    :width: 100%
#    :name: water-jump
#    :align: left
# ```
# 
# <small>
# 
# 
# - *Hydrophobicity: effect of density and order on water's rotational slowing down* {cite}`Titantah_2015`
# 
# 
# </small>
# 
# ---
# :column: col-3
# :card: border-1
# 
# ```{figure} img/modeling-schema-small-analyze.svg
#    :width: 100%
#    :name: analyze-small
#    :align: right
# ```
# ````
# 
# **And one should always create visualizations:**
# 
# The video below shows a close-up from an *ab initio* simulation of water. Hydrogen bonds that form and break are shown as dashed lines. See also how the vibrations of the bonds change when the bonding changes. This is a closeup from a simulation of 54 water molecules using [Born-Oppenheimer Molecular Dynamics](https://en.wikipedia.org/wiki/Born%E2%80%93Oppenheimer_approximation) (BOMD). Visualization using VMD (Visual Molecular Dynamics) {cite}`Humphrey1996a`, simulation using the CPMD (Car-Parrinello Molecular Dynamics) software.
# 
# <!--
# <div style="padding:100% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/152805742?autoplay=1&loop=1&title=0&byline=0&portrait=0" style="position:absolute;top:0;left:0;width:70%;height:70%;" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>
# -->
# <div style="float: center;">
# <iframe src="https://player.vimeo.com/video/152805742?title=0&byline=0&portrait=0" width="640" height="426" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
# </div>
#     
# <p></p>
# 
# **Additional questions:** What kind of resources are available? How long will the simulations take, that is, how large systems and for how long time can be simulated. Is that enough? How about data storage abd backup, is there enough? Do we need long term data storage?
# 
# 

# ## Summary
# 
# In the above, there are several terms and concepts that are new. We will encounter them when we set up and perform simulations. The aim here has been to give a rough idea of the process of modeling works: Simply downloading a well-known software package and using the default parameters and inputs is not acceptable. The software will run, but there is no guarantee that the results will be correct if one doesn't understand the inputs and outputs. In addtion, the results will not be relevant (even if correct) if one doesn't have a good research question. Reproducing data is not research. The software is not to blame for any of those matters, it does what the user tells it do. The user is the source of most errors; even if/when there is a bug/are bugs (and there are always are some), it is the user's responsibility to test and ensure the validity of results. If bugs are found in a published software, one should notify the developers with precise information including test results.

# ## Additional information for those interested: Water models
# 
# To put the example above to further perspective and to give an idea how complex water the simple looking humble water molecule is, below are lists of water models at different levels of description. None of the lists are by no means exhaustive and its purpose is simply to give an idea of the complexity of the problem - textbooks tend to give a simplified view. Water, as simple as it is, remains to be very difficult to model correctly. Some recent reviews are provided for example by {cite}`Ghoufi2018,Palmer2018,Brini2017,Onufriev2017,PetterssonHenchmanNilsson2016`
# 
# 
# ### Historical: 
# 
# [W.C. Röntgen](https://en.wikipedia.org/wiki/Wilhelm_R%C3%B6ntgen) - the same person who discovered x-rays (and was the recipient of the [1901 Nobel Prize in Physics](https://www.nobelprize.org/prizes/physics/1901/rontgen/facts/)), developed a two species model (1897). The water molecules were classified into fluid-like and ice-like. [J.D. Bernal](https://en.wikipedia.org/wiki/J._D._Bernal) and [R.H. Fowler](https://en.wikipedia.org/wiki/Ralph_H._Fowler) developed a model with tetrahedral geometry (1933). This is the model that forms the basis of current understanding. [Linux Pauling's](https://en.wikipedia.org/wiki/Linus_Pauling) ([Nobel Prize in Chemistry 1954](https://www.nobelprize.org/prizes/chemistry/1954/pauling/facts/) and [Nobel Prize in Peace 1962](https://www.nobelprize.org/prizes/peace/1962/pauling/facts/))) model established clathrate structure (1935) and the model of [John Pople](https://en.wikipedia.org/wiki/John_Pople) ([Nobel Prize in Chemistry 1998](https://www.nobelprize.org/prizes/chemistry/1998/summary/)) showed hydrogen bond bending (1951).
# 
# ### Quantum mechanical: 
# All the approaches have their own models. Importantly, however, van der Waals interactions are *not* part of the standard quantum mechanical approach and they have to be added separately. As a side note the van der Waals interactions are named after [J.D. van der Waals](https://en.wikipedia.org/wiki/Johannes_Diderik_van_der_Waals), the recipient of the [1910 Nobel Prize in Physics](https://www.nobelprize.org/prizes/physics/1910/waals/biographical/). 
# 
# ### Classical MD level:
# 
# There are two main families of water models:
# 
# - TIP = Transferrable Intermolecular Potential
# - SPC = Simple Point Charge
# 
# To given an idea of the abundance of models, here are some without explanations: BF, ST2, TIPS, TIPS2,  TIP3P, TIP3Pm, TIP3P/Fs TIP4P, TIP4P-Ew, TIP4P/2005, TIP4P/2005f, TIP4P/$\varepsilon$, TIP4P/FQ, TIP4P-HB, TIP4P-i, TIPTP/ice, TIP4P-pol, TIP4PQ, TIP4P-QDP, TIP4P-D, TIP5P, TIP5P-E, TIP5P/2019, OPC, SPC, SPC/E, SPC/$\varepsilon$, SPC/A, SPC/F, SPC/F2, SPC/FQ, SPC/Fw, SPC-pol, SPC/HW.
# 
# We will use some of these models during this course.
# 
# ### Coarse-grained:
# 
# There are also models that descrive water in a larger scale. The idea is that one so-called coarse-grained molecule somehow approximates a bundle of 3 or 4 actual water molecules. Here are some:
# MARTINI, MARTINI polarized, ELBA, SIRAH, DPD, Mercedes-Benz, BMW, mW.
# 
# 
# ## References
# 
# 
# 
# 
# ```{bibliography} ../../references.bib
# :filter: docname in docnames
# :style: plain
# ```
# 
