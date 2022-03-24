# Jupyter Notebook / Jupyter Lab

````{panels}
:column: col-lg-12 p-2

```{image} ../../images/logos/Jupyter_logo.svg
:alt: Jupyter
:width: 150px
:align: right
```

**Learning goals:** 

- To understand what Jupyter Notebook and Jupyter Lab are
- To be able to use Jupyter and understand its basic structure with code and markdown cells

**Keywords:** Python, Anaconda, conda, Project Jupyter, Jupyter Lab, Jupyter Notebook, Jupyter notebook, `.ipynb`, interactive environment for scientific computing, markdown cell, code cell

**Note:** Since Python and Jupyter are core components of the course, it is imperative that the installation works.


**Associated material:** 


- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/en/stable/)
- [The JupyterLab Interface](https://jupyterlab.readthedocs.io/en/stable/user/interface.html)
- [Frequently Asked Questions (FAQ)](https://jupyterlab.readthedocs.io/en/stable/getting_started/faq.html)
- [A gallery of interesting Jupyter Notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks)
- [Markdown basics](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working%20With%20Markdown%20Cells.html)



````

## What is Jupyter Lab / Notebook?

[Jupyter notebook](https://jupyter.org/)  can be described as a web browser-based document that has the ability to combine live code with plotting, interactions, text and multimedia. In addition to Python, it can handle many other programming languages as well. It is better to call it a platform or an environment rather than a document since it provides an interactive browser-based environment for scientific computing, analysis and documentation.  Jupyter notebooks have the file extension `.ipynb`. The files are in [ASCII](https://en.wikipedia.org/wiki/ASCII) format and do not depend on the operating system one uses. Importantly, Jupyter notebooks provide the possibility to create live lab books that are reproducible. Jupyter notebooks are used extensively in a broad range of fields such as analysis of simulation data, machine learning, digital humanities, meteorology, and so on.

The applications that can open, execute and save Jupyter notebooks are called *Jupyter Notebook* and *Jupyter Lab*. The former is older but has more extensions for handling different types of data. 

There is also *Jupyter Book* that uses markdown and Jupyter notebooks to create live textbooks that can even execute code. This document was made using Jupyter Book. There are also several other related projects, see the [Project Jupyter page](https://jupyter.org/). Jupyter is open source software.

Please see the links in the header for information.

## Jupyter Lab or Notebook?

There are two applications that can open Jupyter notebook (`.ipynb`) files, Jupyter Notebook and Jupyter Lab. Below are some of the main differences between the two:

- Both of them run in a web browser. 
- *Jupyter Lab* is newer. Due that, not all the extensions that work with *Jupyter Notebook* work with *Jupyter Lab.* This is, however, changing rapidly. 
- The user interface of *Jupyter Lab* is very versatile. One can open simultaneously many notebook (`.ipynb`) files, even terminal windows and stand-alone Python (or other programming language) windows. 
- With *Jupyter Notebook* one works with a single notebook (`.ipynb`) file at a time. 

So which one to choose? Here, we prefer Jupyter Lab. However, everything works in Jupyter Notebook as well so the choice is yours. For the advanced users, Jupyter Notebook has some features that are not yet available on Jupyter Lab such as the use of variables in markdown cells. We won't be using such features here and it is highly likely that they get implemented in Jupyter Lab as well.

## How to start Jupyter Notebook / Lab?

Click on the tab that corresponds to your operating system. Independent of your operating system, launching Jupyter Lab (we'll use Lab from now on) opens a new web browser or tab using your default browser. 

````{dropdown} Windows 10 and Mac

On both Windows and Mac, simply run the Anaconda Navigator from your program menu. The interface is the same in both cases and it looks like this:

<P></p>

```{figure} ../../images/ana-interface.png
:alt: Anaconda Mac/Windows interface
:class: bg-light
:width: 100%
:align: center
```
<P></p>

Simply clicking `Launch` on Jupyter Lab or Jupyter Notebook starts it. Similarly, one can start any of the other applications that come bundled with Anaconda.

````

````{dropdown} Linux & WSL/WSL2

On Linux and WSL/WSL2, Jupyter Lab and Jupyter Notebook must be started on the command line. The following commands start Jupyter Lab and Jupyter Notebook, respectively.

```
jupyter-lab
jupyter-notebook
```

If needed, you can get help with the following commands:

```
jupyter-lab --help
jupyter-notebook --help
```

<P></p>

````

## Jupyter interface

The initial web browser window is identical in all operating systems. Note that the Jupyter window (or tab) is *not* connected to internet. Instead, it runs locally on your computer. The figure below shows the initial browser window when starting Jupyter Lab. There are a few points to here:

- The web address: `localhost:8888/lab`. This is a local address, this means that the application (Jupyter Lab) is running on your computer (`localhost`) and connected to port `8888`.
- The window has tabs on the left hand side for listing files, extensions, help etc.
- The top menus offer functionality such as starting and stopping kernels, running selected cells and so on.
- The icons on top of the left hand side pane have the options to open new Launchers,  create new folders, upload files and refresh the current list. In the figure below, no files are present in the current directory (the list is empty).

The initial Launcher Window in a web browser looks like this:


```{figure} ../../images/j-notebook-interface.svg
:alt: Anaconda Mac/Windows interface
:class: bg-light
:width: 100%
:align: center
```
<P></p>


## Code and markdown cells


Clicking the Python 3 notebook icon opens the Jupyter workspace window. It is the same in all operating systems. The figure below shows some of the important features:

```{figure} ../../images/j-notebook-interface-2.svg
:alt: Anaconda Mac/Windows interface
:class: bg-light
:width: 100%
:align: center
```
<P></p>

One of the very useful features on Jupyter notebooks is that there are different types of cells (the white area inside the blue rectangle). The two basic types are *markdown cells* and *code cells*. The cell type can be easily changed from the dropdown menu as indicated in the figure. This separation makes it very convenient and easy to write interactive, reproducible and well-documented notebooks.

### Code cells

As the name suggests, these are the cells in which one writes (live) code. Here, we use Python 3 and that is also clearly indicated in the workspace. Once code is written, it has to be executed. One can use the icons or the 'Run' and 'Kernel' tabs. The 'Kernel' tab contains several very useful options including 'Restart Kernel and Clear All Outputs'. This is very useful if one wants to make sure that everything is consistent (remember, the cells are sequential and sometimes cell-wise execution of commands using different variables may lead to problems). 

Code cells can also be executed by clicking `Ctrl-Enter` (this does not advance the cursor to the next cell) or `Shift-Enter` (advances the cursor to the next cell).


### Markdown cells

*Markdown* means that one can enter normal text, but there is no executable code. *Markdown* is language that is simple and quick to use for documentation (link to the preference is provided in the header). It allows for titles, lists, figures, mathematics and so on. Even markdown cells must be executed for the text (and other markup such as mathematics) is rendered properly. Execution works just like for code cells.

Below is a figure that demonstrates some of the above matters and also the multi-window feature of Jupyter Lab (if it is too small, click on it to see it full size).



```{figure} ../../images/j-lab-1.svg
:alt: Anaconda Mac/Windows interface
:class: bg-light
:width: 100%
:align: center
```

## Finally...

There is much more to the Jupyter notebooks (see the links in the header) but the above provides the fundamentals. When working with them, always *remember to save your work.*
