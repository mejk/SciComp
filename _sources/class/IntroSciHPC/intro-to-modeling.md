---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-input]

#import sys
#sys.path.append('./helpers')

#from helpers import settings
#import settings

###
from myst_nb import glue
from IPython.display import IFrame
from IPython.display import Markdown
# Additional styling ; should be moved into helpers
#from IPython.core.display import display, HTML
#HTML('<style>{}</style>'.format(open('styler.css').read()))
#import pandas as pd
from datetime import datetime
from IPython.display import Markdown as md
updated = datetime.now()
now = updated.strftime("%A, %B %d %Y at %H:%M" )
```

# Introduction to scientific computing & computational modeling

```{code-cell} ipython3
:tags: [remove-input]

md(f"-Last updated on {now}")
```

````{panels}
:column: col-lg-12 p-2

```{image} img/sna-pop-3.png
:width: 300px
:name: cglipid
:align: right
:class: rounded-circle
```

**Learning goals:** 
- To have a basic idea of what scientfic computing and computational modeling are.
- To get some historical background on computing.
- To understand the relation between experiments, theory and computation.
- To understand the need for different models and their relations. Several methods and models that will be discussed later in the course will be mentioned. The aim is to make the students acquainted to the terminology and make them comfortable in using the terms and termonology a litte-by-little over the course. 

**Keywords:** scientific computing, multiscale modeling, high performance computing, history of computing 
<!--
**Associated material:**
-->

**Note:** To be more concrete, some of the examples are drawn from physics, chemistry and chemical engineering. The discussion is quite general and doesn't assume background in them. 

````

<hr>

+++

## Computing and computers


**More:**
- Video: [Computer Pioneers: Pioneer Computers Part 1](https://www.youtube.com/watch?v=qundvme1Tik) by Computer History Museum
- Video: [Computer Pioneers: Pioneer Computers Part 2](https://www.youtube.com/watch?v=wsirYCAocZk) by Computer History Museum

+++

## Background

<!-- Computational chemistry and physics are relatively young fields -->  
Scientific computing and computational modeling are relatively young fields -
this is easy to understand since the first digital (in contrast to mechanical) computers were developed in the late 1930's. The first programmable computer, the [Z1](https://en.wikipedia.org/wiki/Z1_(computer)), was developed by [Konrad Zuse](https://en.wikipedia.org/wiki/Konrad_Zuse) in Germany in the late 1930's. The early developments in programmable digital computers were largely driven by military applications in 1940's and 1950's. 

The earliest computers were not reliable or stable, or were built more as calculators for a single purpose. ENIAC (Electronic Numerical Integrator and Computer) that was built in 1946 is often said to be the first real computer. Transistors did not exist at that time and [ENIAC](https://en.wikipedia.org/wiki/ENIAC) (in Philadelphia) had 17,480 vacuum tubes. Its original purpose was to determine trajectories for ballistic missiles, but due to the war ending it was used to study nuclear reactions. Nuclear warhead and storage related simulations are still one of the main uses of the largest supercomputers. One additional notable aspect of ENIAC is that, unlike modern computers, it was not able to store programs. 

ENIAC was followed by [MANIAC I](https://en.wikipedia.org/wiki/MANIAC_I) (Mathematical Analyzer Numerical Integrator And Computer Model I at Los Alamos) and it was used in the landmark paper *"Equations of State Calculations by Fast Computing Machines"*{cite}`Metropolis1953` by Metropolis et al. that introuced the Metropolis Monte Carlo method, one of the most used and important algorithms even today. MANIAC was also used in the development of the hydrogen bomb. Generalization of the Metropolis Monte Carlo method is known as the [Markov Chain Monte Carlo](https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo) and it is important in fields such as optimization and machine learning. On pure chemistry side, the earliest computational papers appeared in the 1960's and the term computational chemistry was (probably; hard to trace) first used in 1970's.

Historically, scientific computing and computational modeling have their roots in physics and chemistry, but independent if one talks about physics, chemistry or some other field, the development can be divided roughly in the theoretical developments in the field, developments of numerical methods and algorithms, and hardware. The development of numerical methods cannot be over-emphasized as it is critical to be able to model and simulate larger systems and for longer times. This will become clear as we discuss various methods and how they scale in terms of the number of degrees of freedom.

Currently, computational approaches such as hybrid methods that combine quantum mechanical and classical molecular dynamics and coarse-grained methods have gained a lot of popularity. Methods that combine different time and/or length scales can in general be called *[multiscale methods](https://en.wikipedia.org/wiki/Multiscale_modeling)* and this will be discussed in more detail later. In addition, methods that go under the term *[machine learning](https://en.wikipedia.org/wiki/Machine_learning)* are perhaps the most rapidly growing family of methods and they are applied in almost all imaginable fields from medicine to digital humanities and computational chemistry. Machine learning is not a simulation method as such, but rather a class of methods that allows classification (clustering), analyses and model building using large data sets. Machine learning methods rely heavily on statistics, linear algebra and stochastic methods such as [Markov processes](https://en.wikipedia.org/wiki/Markov_chain). We will discuss such methods later.

<!-- <table class="lblue" style="float: right" width="400">
  <tr>
    <td>
       <img src="img/compsci.svg" width="400px" />     
     </td>
    </tr>    
    <tr>
     <td colspan="1">
         Figure: Computational modeling in chemistry, physics and engineering require deep background knowledge from a number of fields.
     </td>
   </tr>
</table>
-->

<!--
:::{figure} compsci
<img src="img/compsci.svg" alt="fishy" width="600px">
Computational modeling in chemistry, physics and engineering require deep background knowledge from a number of fields.
:::
-->



```{figure} img/compsci.svg
---
width: 700px
name: compsci
---
In addition to programming and numerical methods, computational modeling and scientfic computing require deep background knowledge from a number of fields.
```

<!--

![](img/compsci.svg) 
-->


**More:**

- [Simulating Physics with Computers Richard P. Feynman](https://web.archive.org/web/20170812065758/http://www.mrtc.mdh.se/~gdc/work/ARTICLES/2014/3-CiE-journal/Background/SimulatingPhysicsWithComputers.pdf)
- [Metropolis, Monte Carlo and the MANIAC](http://www-star.st-and.ac.uk/~kw25/teaching/mcrt/MC_history_4.pdf)
- [Computing and the Manhattan Project](https://www.atomicheritage.org/history/computing-and-manhattan-project)
- [A Trilogy on Errors in the History of Computing](https://ieeexplore.ieee.org/document/4392895)
<!--
- [The Development of Computational Chemistry in Germany](http://www.quantum-chemistry-history.com/Pey_ff_Dat/CompGerm/Pey_ff_CompGerm.htm)
- [The Development of Computational Chemistry in the United Kingdom](http://www.chilton-computing.org.uk/acl/applications/qc/p001.htm)
- [Computational Chemistry in the 1950s](http://curation.cs.manchester.ac.uk/computer50/www.computer50.org/mark1/Huw-Pritchard/history.html)
-->

+++

##  Example: Computational chemistry

It is difficult to define what exactly computational chemistry is or is not. Wikipedia defines quite broadly (and one could say adeqately) as follows:

<blockquote>
"Computational chemistry is a branch of chemistry that uses computer simulation to assist in solving chemical problems. It uses methods of theoretical chemistry, incorporated into efficient computer programs, to calculate the structures and properties of molecules and solids. It is necessary because, apart from relatively recent results concerning the hydrogen molecular ion (dihydrogen cation, see references therein for more details), the quantum many-body problem cannot be solved analytically, much less in closed form. While computational results normally complement the information obtained by chemical experiments, it can in some cases predict hitherto unobserved chemical phenomena. It is widely used in the design of new drugs and materials. "    
</blockquote>    

Although the field of computational chemistry didn't exist in the 1830's, [Auguste Comte](https://en.wikipedia.org/wiki/Auguste_Comte), the philosopher behind [positivism](https://en.wikipedia.org/wiki/Positivism), stated that it is impossible and destructive to try to study chemistry using mathematics (and as an extrapolation by computers):

<blockquote>
"Every attempt to employ mathematical methods in the study of chemical
questions must be considered profoundly irrational and contrary to the
spirit of chemistry.... if mathematical analysis should ever hold a
prominent place in chemistry - an aberration which is happily almost
impossible - it would occasion a rapid and widespread degeneration of that
    science."<p></p>
&nbsp; &nbsp; -Auguste Comte, <a href="http://www.gutenberg.org/ebooks/31881">Cours de philosophie positive</a>, 1830
</blockquote>    

This view is, if course, very fitting with the idea of [positivisim](https://en.wikipedia.org/wiki/Positivism) and wrong (or '[not even wrong](https://en.wikipedia.org/wiki/Not_even_wrong)') in terms of science as it defies the existence of predictive theories. 

<!--
It is also somewhat curious given that in Comte's own hierarchy of sciences, mathematics was the most fundamental meaning that all the other sciences use it.
-->

Rather than trying to provide a strict defintion or classification as what computational chemistry is, let's rather list methods and approaches use by computational chemists - after all computational chemistry includes various simulation techniques, structural analysis, using computers to design or predict new molecules or/and molecular binding, and data mining from experimental and/or computational results. It is also hard - and unnecessary - to draw strict defintion between computational chemistry, physics or, say, chemical engineering or pharmacy/drug design. Although these fields all have their own special characteristics, from the computational perspective they share the same methods and methodologies many of them, especially when it come to algorithms and computational techniques, come from applied mathematics and computer science. Right now, we restrict ourselves just to provide and a list and we will discuss some of them in detail later. For most part here, we focus on simulation and we will also discuss some analysis and machine learning techniques. What is also common to the computational disciplines is that one needs in-depth knowledge across traditional disciplines.    

- Quantum mechanical methods: *ab initio* methods, density functional theory, Car-Parrinello simulations
- Classical molecular dynamics, steered molecular dynamics, non-equilibrium molecular dynamics
- Coarse-grained molecular dynamics
- Lattice-Boltzmann simulations
- Phase field simulations
- Finite element methods
- Monte Carlo techniques
- Optimization techniques
- Machine learning methods, Bayesian techniques, Markov models, deep learning
- Free energy calculations

... and the list goes on. This (by necessity incomplete) list aims to convey the idea that the field is very broad with no clear boundries.

+++

See also the short interview of one of the pioneers of computational chemistry / physics / chemical engineering:



**Beauty in Science: Biophysicist Klaus Schulten & his Computational Microscope**

<div class="container youtube">
<iframe class="responsive-iframe" src="https://www.youtube-nocookie.com/embed/iqcG4P-lTa0" frameborder="0" allow="accelerometer; autoplay="0"; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

+++

## Nobel Prizes to Computational Chemistry: 1998 and 2013

To date, the Nobel Prize is Chemistry has been awarded twice to computational chemists - thus far no Nobel Prizes have been granted directly to computational physics. The first computational chemistry Nobel was [1998](https://www.nobelprize.org/prizes/chemistry/1998/summary/), when 
[Walter Kohn](https://en.wikipedia.org/wiki/Walter_Kohn) (see also his [biographical notes](https://www.nobelprize.org/prizes/chemistry/1998/kohn/biographical/)), "for his development of the density-functional theory", and John A. Pople (see also his [biographical notes](https://www.nobelprize.org/prizes/chemistry/1998/pople/biographical/)), "for his development of computational methods in quantum chemistry", were the recipients. Kohn was born in Austria, escaped the nazis to Canada and received his BSc in Applied Mathematics at the University of Toronto. He moved to study physics at Harvard for his PhD. His PhD supervisor was [Julian Schwinger](https://en.wikipedia.org/wiki/Julian_Schwinger), [1965 Nobel Laureate in Physics](https://www.nobelprize.org/prizes/physics/1965/summary/). He was at the University of California in Santa Barbara at the time of his Prize. Kohn passed away in 2016 at the age of 93. [Sir John Pople](https://en.wikipedia.org/wiki/John_Pople) received his PhD in Mathematics from Cambridge. He was at Northwestern University at the time of the Nobel Prize. He passed away in 2004 at the age of 78. Pople is one of the authors of the first version of the software suite [Gaussian](https://en.wikipedia.org/wiki/Gaussian_(software)). Pople's PhD supervisor was [Sir John Lennard-Jones](https://en.wikipedia.org/wiki/John_Lennard-Jones), the [Lennard-Jones potential](https://en.wikipedia.org/wiki/Lennard-Jones_potential) used in almost all classical molecular dynamics simulations is named after him.

The second Nobel Prize to computational chemistry came in [2013](https://www.nobelprize.org/prizes/chemistry/2013/summary/) when it was awarded to [Martin Karplus](https://en.wikipedia.org/wiki/Martin_Karplus), [Michael Levitt](https://en.wikipedia.org/wiki/Michael_Levitt) and [Arieh Warshel](https://en.wikipedia.org/wiki/Arieh_Warshel) "for the development of multiscale models for complex chemical systems." The press release of the [Royal Swedish Academy of Science](https://en.wikipedia.org/wiki/Royal_Swedish_Academy_of_Sciences) stated the importance of computational chemistry very clearly:

<blockquote>
"Today the computer is just as important a tool for  chemists as the test tube. Simulations are so realistic that they predict the outcome of traditional experiments." 
<p></p>
&nbsp; &nbsp; -<a href="https://www.nobelprize.org/uploads/2018/06/press-22.pdf">Pressmeddelande, Kungliga Vetenskapsakademien</a>
</blockquote>    
 
Like Kohn, Martin Karplus was born in Vienna, Austria and moved to the USA to escape the nazis. He did his PhD in chemistry at Caltech with the two-time Nobel Laureate [Linus Pauling](https://en.wikipedia.org/wiki/Linus_Pauling). He is the originator of the [CHARMM](https://www.charmm.org/) molecular simulation package. Karplus was at Université de Strasbourg and Harvard at the time of the Prize. Arieh Warshel was postdoc (1970) with Karplus' at Harvard in Chemical Physics. He went to the Weizmann Institute in Isreal for a faculty job but moved later to the University of Southern California after [Weizmann didn't grant him tenure](https://www.ynetnews.com/articles/0,7340,L-4438751,00.html). [Michael Levitt](https://en.wikipedia.org/wiki/Michael_Levitt) was born in Pretoria, South Africa and he did his PhD in Biophysics at Cambridge. At the time of the Prize he was at Stanford where he is a professor of Structural Biology. As a side note on tenure and Nobel Prizes, Nobel winners that were not given tenure include at least [Tom Sargent](https://en.wikipedia.org/wiki/Thomas_J._Sargent) (Economics 2011; University of Pennsylvania didn't give tenure), [Lars Onsager](https://en.wikipedia.org/wiki/Lars_Onsager) (Chemistry 1968; dismissed/let go by both John's Hopkins and Brown universities).
 
<!-- 
````{margin}
The Nobel Laurates in computational chemistry. <a href="https://doi.org/10.1073/pnas.1320569110">The 1998 Nobel winners</a> Walter Kohn (UC Santa Barbara) and John Pople (Nortwestern), and the 2013 ones <a href="https://www.nobelprize.org/prizes/chemistry/2013/karplus/biographical/">Martin Karplus</a> (Harvard & Strasbourg), <a href="https://www.nobelprize.org/prizes/chemistry/2013/warshel/biographical/">Arieh Warshel</a> (Southern California), <a href="https://www.nobelprize.org/prizes/chemistry/2013/levitt/biographical/">Michael Levitt</a> (Stanford). Photos from Wikipedia, Creative Commons license.
```{figure} img/kohn-cc.jpg
   :height: 150px
   :name: figure-example
   [Walter Kohn](https://www.nobelprize.org/prizes/chemistry/1998/kohn/biographical/).
 ```
 ```{figure} img/pople-cc.png
   :height: 150px
   :name: figure-example
   [John Pople](https://www.nobelprize.org/prizes/chemistry/1998/pople/biographical/).
 ```
  ```{figure} img/karplus-cc.jpg
   :height: 150px
   :name: figure-example
   [Martin Karplus](https://www.nobelprize.org/prizes/chemistry/2013/karplus/biographical/).
 ```
  ```{figure} img/warshel-cc.jpg
   :height: 150px
   :name: figure-example
   [Arieh Warshel](https://www.nobelprize.org/prizes/chemistry/2013/warshel/biographical/).
 ```
  ```{figure} img/levitt-cc.jpg
   :height: 150px
   :name: figure-example
   [Michael Levitt](https://www.nobelprize.org/prizes/chemistry/2013/levitt/biographical/).
 ```
```` 

-->

````{panels}
:card: shadow-none, border-0
:column: col p-0 m-0

```{figure} img/kohn-cc.jpg
   :width: 200px
   :name: figure-kohn
   [Walter Kohn](https://www.nobelprize.org/prizes/chemistry/1998/kohn/biographical/). Photo from Wikipedia, Creative Commons license.
 ```
---
```{figure} img/pople-cc.png
   :width: 200px
   :name: figure-pople
   [John Pople](https://www.nobelprize.org/prizes/chemistry/1998/pople/biographical/). Photo from Wikipedia, Creative Commons license.
 ```
---
```{figure} img/karplus-cc.jpg
   :width: 200px
   :name: figure-karplus
   [Martin Karplus](https://www.nobelprize.org/prizes/chemistry/2013/karplus/biographical/). Photo from Wikipedia, Creative Commons license.
 ```
---
```{figure} img/warshel-cc.jpg
   :width: 200px
   :name: figure-warshel
   [Arieh Warshel](https://www.nobelprize.org/prizes/chemistry/2013/warshel/biographical/). Photo from Wikipedia, Creative Commons license.
 ```
---
```{figure} img/levitt-cc.jpg
   :width: 200px
   :name: figure-levitt
   [Michael Levitt](https://www.nobelprize.org/prizes/chemistry/2013/levitt/biographical/). Photo from Wikipedia, Creative Commons license.
 ```
````

<!--
````{panels}
:card: shadow-none, border-1
:column: col-12 p-0 m-0
**Figure:** The Nobel Laurates in computational chemistry. <a href="https://doi.org/10.1073/pnas.1320569110">The 1998 Nobel winners</a> Walter Kohn (UC Santa Barbara) and John Pople (Nortwestern), and the 2013 ones <a href="https://www.nobelprize.org/prizes/chemistry/2013/karplus/biographical/">Martin Karplus</a> (Harvard & Strasbourg), <a href="https://www.nobelprize.org/prizes/chemistry/2013/warshel/biographical/">Arieh Warshel</a> (Southern California), <a href="https://www.nobelprize.org/prizes/chemistry/2013/levitt/biographical/">Michael Levitt</a> (Stanford). Photos from Wikipedia, Creative Commons license.
````
-->

**More:**

- [Models of success](https://www.chemistryworld.com/features/models-of-success/6701.article) from [Chemistry World](https://www.chemistryworld.com/)
- [Lindau Nobel Laureate Meetings](https://www.lindau-nobel.org/)
- [Nobel Prize facts from the Nobel Foundation](https://www.nobelprize.org/prizes/facts/nobel-prize-facts/). Includes a lot of interesting information including prizes to married couples, mother/father & child and so on.
- [Nobel Prize controversies](https://en.wikipedia.org/wiki/Nobel_Prize_controversies)

 
### Other notable prizes in computational chemistry & physics

Since we got into the Nobel Prizes, let's list a few others.
Probably the best know is the [Berni J. Alder CECAM Prize](https://www.cecam.org/awards), the acronym [CECAM](https://www.cecam.org/) comes from  *Centre Européen de Calcul Atomique et Moléculaire* and it is currently headquartered at the École polytechnique fédérale de Lausanne (EPFL) in Switzerland. CECAM is a pan-European organization and on the practical side it is well-known for its [workshops, summer schools and conferences](https://www.cecam.org/program?type=all&month=all&location=all). The Prize, named after [Berni Alder](https://en.wikipedia.org/wiki/Berni_Alder) one of the pioneers of molecular simulations, is granted every three years. The prize was established in 1999 and has thus far been granted to

- 2019: [Sauro Succi](https://en.wikipedia.org/wiki/Sauro_Succi), Italian Institute of Technology, Center for Life Nanosciences at La Sapienza in  Rome, [for his pioneering work in lattice-Boltzmann (LB) simulations](https://www.cecam.org/award-details/2019-sauro-succi).
- 2016: [David M Ceperley](https://en.wikipedia.org/wiki/David_Ceperley), Department of Physics, University of Illinois at Urbana-Champaign and Eberhard Gross, Max Planck Institute of Microstructure Physics, Halle for "[fundamental ground-breaking contributions to the modern field of electronic structure calculations](https://www.cecam.org/award-details/2016-david-m-ceperley-and-eberhard-k-u-gross)".
- 2013: [Herman J.C. Berendsen](https://en.wikipedia.org/wiki/Herman_Berendsen) and [Jean-Pierre Hansen](https://en.wikipedia.org/wiki/Jean-Pierre_Hansen), Groningen and Cambridge for ["outstanding contributions to the developments in molecular dynamics and related simulation methods"](https://www.cecam.org/award-details/2013-herman-jc-berendsen-and-jean-pierre-hansen)
- 2010: [Roberto Car](https://en.wikipedia.org/wiki/Roberto_Car) (Princeton) and [Michele Parrinello](https://en.wikipedia.org/wiki/Michele_Parrinello) (ETH Zürich) for ["their invention and development of an ingenious method that, by unifying approaches based on quantum mechanics and classical dynamics, allows computer experiments to uncover otherwise inaccessible aspects of physical and biological sciences"](https://www.cecam.org/award-details/2010-roberto-car-and-michele-parrinello)
- 2007: [Daan Frenkel](https://en.wikipedia.org/wiki/Daan_Frenkel), Cambridge. [](https://www.cecam.org/award-details/2007-daan-frenkel)
- 2004: [Mike Klein](https://en.wikipedia.org/wiki/Michael_L._Klein), Temple University. The committee wrote: ["Mike Klein’s leadership has been crucial in the development of a variety of computational tools such as constant-temperature Molecular Dynamics, Quantum simulations (specifically path-integral simulations), extended-Lagrangian methods and multiple-timestep Molecular Dynamics"](https://www.cecam.org/award-details/2004-mike-klein)
- 2001: [Kurt Binder](https://en.wikipedia.org/wiki/Kurt_Binder), University of Mainz ["for pioneering the development of the Monte Carlo method as a quantitative tool in Statistical Physics and for catalyzing its application in many areas of physical research"](https://www.cecam.org/award-details/2001-kurt-binder)
- 1999: [Giovanni Ciccotti](https://en.wikipedia.org/wiki/Giovanni_Ciccotti), University of Rome La Sapienza for [" pioneering contributions to molecular dynamics"](https://www.cecam.org/award-details/1999-giovanni-ciccotti)

Other prizes include:

- The APS [Aneesur Rahman Prize for Computational Physics](https://www.aps.org/programs/honors/prizes/rahman.cfm)
- [ACS Award for Computers in  Chemical and Pharmaceutical Research](https://www.acscomp.org/awards/acs-award-for-computers-in-chemical-and-pharmaceutical-research)

The reason for listing all these is simply to indicate how diverse the field is.

+++

## A few examples

Before going any further, let's take a look some examples from simulations to get a more concrete view of what simulations can do. Further examples will be provided as we progress. These are taken from our own simulations to avoid any copyright issues. Use the blue arrow to see more movies.
<!--
All of the simulations and visualizations shown in the examples were made with the tools we use in this course.
-->

```{code-cell} ipython3
---
slideshow:
  slide_type: skip
tags: [remove-input]
---
from IPython.display import HTML
#import IPython.display as display
from IPython.display import IFrame
from IPython.display import FileLink
from IPython.display import display_pdf
from IPython.display import display_markdown
from IPython.display import IFrame
#from IPython.core.display import display

#display.IFrame('https://en.wikipedia.org/wiki/Chocolate_chip_cookie_dough_ice_cream', 700, 500)
#display.IFrame('https://mikko.slides.com/mka/chem3300g-winter-2020/fullscreen?token=gBWSLGtb', 600, 300)
display(IFrame('https://mikko.slides.com/mka/chem3300g-winter-2020/fullscreen?token=gBWSLGtb', 700, 400))
```

## Theory and experiment vs computation

### Experiments and *in silico* modeling


**Computational microscope.** The term *computational microscope* was probably introduced first by Walker and Mezey in 1995 in their article "A new computational microscope for molecules: High resolution MEDLA images of taxol and HIV-1 protease, using additive electron density fragmentation principles and fuzzy set methods"{cite}`Walker1995`. This combined imagining and [density functional theory (DFT)](https://en.wikipedia.org/wiki/Density_functional_theory) calculations. The term was then re-introduced in the context of MD simulations by Lee et al. in their 2009 article "Discovery Through the Computational Microscope"{cite}`Lee2009`. The analogy is a very good one: molecular simulations can mimic behvior of systems in the atomic scale and they allow one to see, analyze and track the atoms. Lee et al. conclude their article by saying{cite}`Lee2009`

<blockquote><em>
Overall, simulations can cast light on the basic architectural principles of molecules that explain fundamental cellular mechanics and might eventually direct the design of proteins with desired mechanical properties. Most importantly, beyond the understanding gained regarding the molecular mechanisms of force-bearing proteins, these examples serve to demonstrate that incessant advancements of MD methodology bring about discoveries stemming from simulation rather than from experiment. Molecular modeling, while useful as a means to complement many experimental methodologies, is rapidly becoming a tool for making accurate predictions and, thereby, discoveries that stand on their own. In other words, it is becoming a computational microscope.    
    </em>
    </blockquote>    
    
This summarizes the situation very well. Although computation has finally gained the recognition as an independent paradigm of research with theory and experiments, every now and then one still hears the comment *but it is just a simulation* or *it is just a model*. While that can be politely dismissed, such an ignorant comment deserves an equally polemic answer: *utter rubbish from a petrified mind.* Independent if one is a theorist, experimentalist or computational scientist, it is imperative to have a reasonable understanding what the other methods of research can and cannot do. 

<!--
Ultimately, of course, results by computation and theory must be tested experimentally, but simulations and theory are the sources of quantitative and predictive results, framework and theories.     
-->


## Modeling & simulations: The 3rd paradigm of research

```{image} img/heart-simplified.svg
:width: 300px
:name: heart
:align: right
```

<!--
Relations between experiments and simulations. 
Slightly modified from the original of Dr. Markus Miettinen.
-->

With the above potentially provoking statements, it is important to keep in mind that while we are dealing with *empirical sciences* and any prediction has to be proven by experiments, theory and computation provide predictions and explanations for observations in a manner that is often impossible for experimentation alone. In addition, experiments have their own problems and to get a signal out of any system, one must poke it, that is, one has to perturb the system to get a response. Simulations don't have such a limitation but can actually be used to study what the effects of probes or peturbations are on a given system. All in all, experiments, theory and simulations all have their advantages and problems and one should not consider any of them to be more superior than the others. With the rise of big data, one could even extend the methods of research to *data-intensive analysis*.

- Simulations can be predictive and guide experiments.
- Can tell what kind of perturbations experimental probes cause.
- Like any other approach: has its own problems



<!--
<table class="lblue" style="float: right" width="400">
  <tr>
    <td>
       <img src="../../images/heart-simplified.svg" width="400px" />     
     </td>
    </tr>    
    <tr>
     <td colspan="1">
         Figure: Relations between experiments and simulations. Slightly modified from the original of Dr. Markus Miettinen.
     </td>
   </tr>
</table>  
-->



<!--
**Molecular models in scattering and NMR:**

Molecular models are used for associating molecular structures from scattering and NMR. Conceptually, this is fitting to a model and not a simulation.

-->


**More:**

- [Deep Data Dives Discover Natural Laws](https://cacm.acm.org/magazines/2009/11/48443-deep-data-dives-discover-natural-laws/fulltext)
- [Vision 2020: Computational Needs of the Chemical Industry](https://www.ncbi.nlm.nih.gov/books/NBK44988/)

+++

## Good practices

The list below repeats some of the matters discussed earlier, but it is well worth going through them again.


* Keep notes, that is have a lab book. That saves a lot of time and reduces the number of errors. Document the procedures and commands (and they can sometimes be somewhat tricky and finding them quickly without proper notes may be difficult or/and lead to errors. Lab book will help you to avoid mistakes and help you to speed up your work tremendously. One good way is to use something like a github document. That is easy to maintain and it is available from any computer. Other reasonable ways: Google docs, OneDrive, Dropbox, etc. 

* Always remember to back up you critical files! There are great tools for doing that including GitHub, Zenodo and such.
* When running simulations, ensure that you will not fill your computer (estimate the amount of data that will be generated and is needed for analysis).
* Check for viruses
* Always, always, always visualize
* Always, always, always verify your simulations & system setup against known results from theory, other simulations and experiments.
* Let the computer do the work! Use [shell scripts](https://en.wikipedia.org/wiki/Shell_script), python, and so on to let the computer to do the repetitive work.

+++

## Dangers

The biggest problem of any computational modeling is the user, the computer will do what it is told to do.

We have stated in our paper "The good, the bad and the user in soft matter simulations"{cite}`Wong_ekkabut_2016`:

<blockquote><em>
It may sound absurd and somewhat provoking, but available simulation 
software (i.e., not home grown programs) becoming very user friendly and easy to 
obtain can almost be seen as a negative development!
    </em>
    </blockquote>
    
Not that long ago all simulations were based on house-written programs. Such programs had obvious limitations: They were not available to others, the codes were not maintained for longer periods of time, they were often difficult to use for all but the person who wrote code. It was also difficult to improve their performance due to very limited number (often one) developers. Modern codes are well maintained, have long-term stability, extensive error checking due to large number of users and they offer excellent performance that is impossible reach for any individual developer or even a small group. They are also very easy to use.     

Similarly to experiments, it is easy train a person to use the software and even produce data using the built-in analysis methods. That is, however, a precarious path. It is absolutely imperative to have a very strong background in the application field and its underlying theories and methods to be able to produce something meaningful. One should never use a software package as a black box!

**More on the topic:**

- [Rampant software errors may undermine scientific results](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4629271/)
- [Three ways researchers can avoid common programming bugs](https://www.natureindex.com/news-blog/three-ways-researchers-science-can-avoid-common-programming-bugs-errors)
- [Computational science: ...Error](https://www.nature.com/news/2010/101013/full/467775a.html)
- [A Scientist's Nightmare: Software Problem Leads to Five Retractions](https://www.semanticscholar.org/paper/A-Scientist%27s-Nightmare%3A-Software-Problem-Leads-to-Miller/dcbf02005884bf79d80315b250b8d70b7a021a21)
- [Scientists Make Mistakes. I Made a Big One.](https://elemental.medium.com/when-science-needs-self-correcting-a130eacb4235)

+++

<!-- 
## The need for different models


Just like with experiments, there is no single correct choice for a computational method. Choosing the most appropriate method for the task at hand depends on various issues. First and foremost, what is the phenomenon/phenomena that is being studied. For example, if one is interested in the behavior of electrons, then quantum mechanical methods are the obvious candidates. This immediately brings in additional questions such as are we interested in band structure, chemical reactions, excited states or something else. Such questions are very important since they again narrow down the choice of methods. For example, if one is studied excited states, the usual methods from density functional theory are not enough. On the other hand, if one is interested in formation of micelles or diffusion of molecules, quantum mechanical methods are useless and the more reasonable choices would be classical MD or coarse-grained MD. Why? Collective phenomena such aggregate formation doesn't  depends directly on quantum mechanical properties (although some of them are implicitly integrated in the higher level models such as classical MD). One may also be interested in static or dynamic phenomena. In the former case, optimization methods may be method of choice whereas in the latter case one needs an equation of motion that is integrated in time. 

-->


```{figure} img/1280-scales-fs.svg
:width: 700px
:name: scales1
:align: left
*Some common computer simulation methods and typical their time scales. Rough idea of systems sizes in terms of atoms and lengths is given when appropriate. The typical time steps in classical molecular dynamics and coarse-grained MD are also shown.*
```

## Terminology: Scales


The figure aboves show different methods and typical time scales associated with them. It is common to use the following terminology when talking about them. It is also important to notice that the physical time and length scales given below are somewhat arbitrary and depend on the field and there is some overlap: 

**Macroscale:** Roughly speaking, denotes time and length scales observable by plain eye.

- Typical times >0.1 sec and lengths >1 mm
- Topical associated phenomena: instabilities, pattern formation, phase separation
- Some simulation methods often used to study these scales: phase field models, FEM, Monte Carlo
 
**Mesoscale:** Intermediate scales that are not quite observable directly by eye, but typically accessible by many experimental techniques. This is a very broad concept.
- Typical times from $10^{-7}$ sec up to $10^{-1}$ sec and lengths ~$10^{-7}$-$10^{-3}$ m.
- Typical phenomena: instabilities, pattern formation, aggregation 
- Some commonly used simulation methods: phase field models,  lattice Boltzmann, coarse-grained molecular dynamics, Monte Carlo

**Atomistic scale:** Typically indicates molecular scales.
- Are in the range of $10^{–12}$ – $10^{-7}$ sec and $10^{-9}$ - $10^{-7}$m.
- Typical phenomena: microscopic mechanisms and interactions such as hydrogen bonding
- Some commonly used methods: classical molecular dynamics, Monte Carlo

**Subatomistic scale:** Typically used to denote quantum scales.
- Time and length scales below the atomistic
- Typical phenomena: electronic structure, excitations, chemical reactions
- Some commonly used methods: *ab initio* methods, Green's functions, Monte Carlo, density functional theory



<!--
 <table class="lblue" style="float: right" width="680">
  <tr>
    <td>
       <img src="../../images/1280-scales-fs.svg" width="680px" />     
     </td>
    </tr>    
    <tr>
     <td colspan="1">
         Figure: Some common computer simulation methods and typical their time scales. Rough idea of systems sizes in terms of atoms and lengths is given when appropriate. The typical time steps in classical molecular dynamics and coarse-grained MD are also shown.
     </td>
   </tr>
</table>
-->


 
### Hybrid models

{numref}`scales1` lists some common models. It is important to notice that it is possible to combine, or hybridize them. The most common hybridization is perhaps the QM/MM methods, that is, combination of a quantum mechanical  method with a method from the classical MD level; the acronym MM stands for molecular mechanics and it is often used synonymously with classical MD although strictly speaking that is not the case. The principle is simple: In QM/MM, a small part of the system is treated using quantum mechanics and the rest with classical (Newtonian) mechanics. Although the idea is simple, there are many complications and limitations.

Similarly to QM/MM, it is possible combine classical MD and coarse-grained MD. Another fairly common combination is [lattice-Boltzmann](https://en.wikipedia.org/wiki/Lattice_Boltzmann_methods) (LB) and molecular dynamics. There, the difficulties are different since the lattice-Boltzmann method uses a grid to solve fluid motion using densities (=no explicit particles), but classical MD brings in particles. This means that the two must coupled in consistent way. Often that means using composite particles instead of 'normal' atoms.

### Implicit vs explicit water

When simulating biomolecular systems as well as many others, water is present. Water is very challenging for simulations since in practise most of the simulation times goes in simulation water as it is the most abundant component in any given system. This is quite easy to understand: In addition to the molecules of interest, say, proteins, lipids or polymers, for example, the simulation box needs to be filled with water at the *correct density* and to reach proper *solvation*, enough water is needed. It is not uncommon that over 90% of the simulation time goes to simulating water. 

While keeping water in is naturally the most correct choice, methods have been developed to include water only implicitly - such models are called implicit solvent models. There are several strategies for doing but the *Generalized Born model* is probably the most commonly used one.

### Coarse-graining

<!-- 
<table class="lblue" style="float: right" width="220">
  <tr>
    <td>
       <img src="../../images/cgfig.png" width="220px" height="100px"/>
     </td>
    </tr>    
    <tr>
     <td colspan="1">
         Figure: In coarse-graned MD, atoms can be considered as 'bundled' such that a cluster of atoms forms a 'superatom' or a coarse-grained bead.
     </td>
   </tr>
</table>



```{figure} img/cgfig.png
---
height: 100px
name: heart
---
In coarse-graned MD, atoms can be considered as 'bundled' such that a cluster of atoms forms a 'superatom' or a coarse-grained bead.
```
-->

Coarse-graining is a process in which one tries to reduce the number of *degrees of freedom* in order to be able to simulate larger systems for longer times. There many approaches to coarse-grain but as a general idea, one can consider a molecule such as a lipid in the Figure and somehow determine new larger *superatoms*. It may sound like magic, but there is a solid theoretical procedure do that (Henderson's theorem) but - like with everything - there are limitations and complexities. 

Here is a brief list of some coarse-grained  MD methods:

- Direct coarse graining using the Henderson theorem.
- Adaptive Resolution Simulations (AdResS). 
- The MARTINI model. This is the most popular approach. The name MARTINI does not refer to the drink, but the Gothic style church steeple in the city of Groningen, the Netherlands. The tower was completed in 1482 and it is the most famous landmark in the city. The developers of the model, Marrink and co-workers are based at the University of Groningen. As an unrelated note (but Canadian connection), the city of Groningen was librated by Canadian troops in World War II.
- Dissipative Particle Dynamics (DPD). The DPD method is an other popular coarse-grained method. It was originally developed as a fluid flow solver at Shell laboratories by Hoogerbrugge and Koelman in 1991. The original method had, however, an error: It could not produce the correct equilibrium state with Boltzmann distribution; this is a strict requirement that arises from statistical mechanics (and it will discussed in detail later). This problem was fixed through the theoretical work of Espanol and Warren in 1995, and their formulation is the one that is universally used. 
- PLUM model. The PLUM model resembles MARTINI in the sense that the level of coarse-graining is the same. The philosophies of the two models are, however, different. PLUM was developed by Bereau and Deserno. 
- ELBA model. The ELBA model was developed by Orsi and Essex in 1991 primarly for lipid simulations. Whereas many other CG models igonre electrostatic interactions (or most of them), ELBA is unique in including them. The name ELBA comes from 'electrostatics-based'.
- SIRAH model. The name comes from 'Southamerican Initiative for a Rapid and Accurate Hamiltonian' and it has its origin in the Institute Pasteour de Montevideo in Urugay. SIRAH is based on a top down approach.


### Concurrent vs sequential coarse-graining

As the number of different models and the existence of various hybrid models suggests, there are different approached to coarse-graining. These will not be discussed in detail, but it is good to understand the there are two philosophies: *sequential* and *concurrent*. Sequential means that data is first extracted from a higher accuracy model. That data is then used construct a coasre-grained model. In *concurrent* coarse-graining, CG is done on-the-fly.

<!--
```{sidebar} Coarse-grained molecule
In coarse-graned MD, atoms can be considered as 'bundled' such that a cluster of atoms forms a 'superatom' or a coarse-grained bead.
 ![](img/cgfig.png)
```

 <table class="lblue" style="float: right" width="220">
  <tr>
    <td>
       <img src="../../images/logos/gromacs-logo.png" width="220px"/>
     </td>
    </tr>    
    <tr>
     <td colspan="1">
         Figure: Gromacs is one of the world's most popular molecular simulation packages. It is open source and it can perform both atomistic and coarse-grained simulations.
     </td>
   </tr>
</table>

-->


### Coarse-graining and software compatibility

It is not possible to run all of the above (or others) using just any software. Below are some notes. The list is not extensive but is updated regularly.

- Direct coarse graining: There is no unified tool.
- AdResS: Works with Espresso++
- MARTINI: Works with Gromacs
- DPD: Works with LAMMPS
- PLUM: Works with a special version of Gromacs
- ELBA: Works with LAMMPS
- SIRAH: Works with Gromacs and Amber

+++

### Beyond particles: Different representations and methods

Not all coarse-grained simulation methods use particles. The most common ones are the finite element method (FEM), phase field models and the lattice-Boltzmann method. In all of these cases the space is meshed, that is, the space is discretized. This discretization is typically regular such as based on squares, cubes, triangle or something else, but it can also be random or adaptive. 

**Monte Carlo:** Purely stochastic, total momentum is not conserved. This is a general methodology and does not imply the anything about the application. Monte Carlo can be used for problems as different as optimizing railway network traffic and to study quantum phenomena.


**FEM:** The finite element method is essentially a method for solving partial differential equations (PDE). The idea is simple: discretize the space *elements*. It then uses methods based on calculus of variations to solve the problem at hand. As the above implies, it is a very general method and not limited to any particular field. Typical application fields include structural analysis and heat flow. The idea of elements in obvious if one considers a bridge: To model various designs, one can consider the trusses to be the finite elements that have, for example, elastic properties. The elements are meshed and the PDEs (what exactly they are depends on the problem at hand) are then solved numerically.

**Phase field:** In the case of phase field models, the space is typically discretized using a regular grid and the relevant PDEs are solved using *finite differebce methods* on a grid. The PDEs arise from the physical proprties of the system: The system is described by an *order parameter*. The order parameter is a central concept in fields such as *physical chemistry* and *condensed matter physics* and it describes the emergence of order in a system. In the disorder state (high temperature), the order paramater is zero. When the system undergoes a phase transition (temperature is lowered), the order parameter becomes small and finite, and it is bounded from above to the value of one. Thus, order parameter of one describes full order. The difficulty is that there is no unique way of determining the order parameter but its choice depends on the system. One thus needs deep knowledge of ths system and its behavior. Examples of order parameter are the density in the case of a liquid-gas transition and the wavefunction in the case of superconductivity. 

**Lattice-Boltzmann:** In this case the space is again meshed using a regular mesh. Then a fluid is described a density at each of the nodes. The idea is to then solve for the density and flow by approximating the Boltzmann transport equation. The simplest single-relaxation time approx to Bolzmann transport equation is the so-called Bhatnagar-Gross-Krook (BGK) equation and it is commonly used in LB.  This method can be hybridized with particle models. 

<!--
 <table class="lblue" style="float: none" width="680">
  <tr>
    <td>
       <img src="../../images/water-molecule.svg" width="130px" />    
       <img src="../../images/cgfig.png" width="100px" height="100px"/>
       <img src="../../images/cdw-snap.png" width="100px"/>
       <img src="../../images/lb.jpg" width="100px"/>
       <img src="../../images/phase.jpg" width="100px"/>
       <img src="../../images/fem.jpg" width="100px"/>    
     </td>
    </tr>    
    <tr>
     <td colspan="1">
         Figure: Quantum. The systems are described by the Schrödinger equation and wave functions. In classical molecular dynamics, there are no electrons.  Individual atoms are the smallest single entity. Molecules such as water do have properties such partial charges. Their dynamics is generated by Newton's equations of motion. In coarse-graned MD, atoms can be considered as 'bundled' such that a cluster of atoms forms a 'superatom' or a coarse-grained bead. In lattice-Boltzmann simulations, computation is done on a grid and atoms can be included as coarse-grained composite entities. In phase field models, there are no individual atoms. Instead, density is used. Finally, the finite element method (FEM) uses elements that typically have elastic (and other properties). 
     </td>
   </tr>
</table>  

-->

+++

## Why do we need so many methods?

The above examples and discussion are mostly from computational chemistry / physics / chemical engineering. Even when restricted to those fields and just simulations, the number of methods is very large - and we haven't even talked about algorithms and data analysis yet! Why do we need some many methods? There are various reasons, so let's take a look at some. First, let's look at the number of atoms/components - after all, in the context of computational chemistry / physics / chemical engineering they are fundamental units. Analogously, in other problems one has to identify the basic units and behaviours to be modelled and analyzed.

A typical classical MD simulation has 10,000-100,000 atoms. The atoms are treated as entities interacting via pair potentials, and electrons (or nuclei) are not taken into account separately. Without considering technical details, let's naively assume that that there is some relatively straightforward way of treating electrons and nuclei. A system of 10,000 atoms would then contain many more entities. If the system has only hydrogens, then the total number of particles would be 20,000. Let's consider carbon-12. It has 6 protons, 6 neutrons and 6 electrons: Each atom has 18 smaller entities. This would make the 10,000 atom system to a 180,000 atom system. How about gold? It has 79 protons, 118 neutrons and 79 electrons. This means that each Au atom has 276 smaller entities and a system of 10,000 atoms would then consist of 2,760,000 particles. The number alone is overwhelming and the methods to treat them make it an even tougher problem. Here are some issues that one needs to consider. 

- Classical treatment: [Newton's equation of motion](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion), positions and velocities 
- Quantum mechanics: [Schrödinger equation](https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation), [wavefunction](https://en.wikipedia.org/wiki/Wave_function)
- Discrepancy in velocities: The fastest motion determines time step.
  - Consider this: In hydrogen, electrons (1s) move at about 0.7% speed of light!
  - In classical MD, the time step is typically 1-2 fs (or $1-2 \times 10^{-15}$ s)
  - In coarse-grained MD, the time step depends on the level of description: In the popular MARTINI model the time step is usually 10-40 fs, in dissipative particle dynamics about 10 ps.

+++

## Programming languages

One typical question is: Does one need to be able to program? The simple answer is yes. One needs to know some programming independent if one does computation, theory or experiments. Below is a brief discussion.

**Which programming language should I use/learn?** Depends on the needs, the level of knowledge and application(s). For example, Python is a general purpose language that can be used for many purposes and it is particularly useful for analyzing and visualzing data indpendent if the data is from simulations, experiments or some database. Python is very quick to learn and it has amazing amount of libraries and routines for almost any imaginable task, and the community is large and very supportive. Python is an interpreted language. Python is a language that has become a must learn independent of field and application, and it is particularly important in machine learning. We will also use Python.

C and C++ have a different nature than Python. They have to be compiled and they have a much more rigidily defined structure. C/C++ codes are great for writing high-performance simulation codes and, for example in the field of molecular simulations, Gromacs, LAMMPS and NAMD are written in C/C++. As for syntax, C/C++ and Python have lots of similarities.

Fortran is an older programming language and it was originally designed to be very efficient for numerical calculations. The name Fortran comes from *For*mula *Tran*slation. Although there has been a shift to C/C++, many HPC codes such as CP2K, Orca and Gaussian are written in Fortran.

Graphics processing units (GPU) are used increasingly in high performance computing. They use languages such as CUDA for NVIDIA GPUs, HIP for AMD GPUs and OpenCL that is GPU agnostic. In high performance computing CUDA is the dominant one while HIP is starting to gain ground. Syntactically, they have a very high resemblance to C/C++.

As for computers,  the Linux operating system is the dominant in the world of higher performance computing. As for programming, it can be done in any of the common environments, that is, Windows, Mac OSX and Linux, or even Android or Chrome.

+++

## Bibliography

```{bibliography} ../../references.bib
:filter: docname in docnames
:style: plain
```

+++

<!--
## Summary
-->
