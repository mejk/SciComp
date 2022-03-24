# JupyterBook Course Template and Material for SciComp

This is a repository the Scientific Computing course intended for advanced undergraduates and early graduate students.

## Course Website

To access the rendered version of this course, visit 

https://mejk.github.io/SciComp


## How to use the material for your own course or such

Just clone the site. It is expected that you know how git and friends work. The lectrues are written as both markdown and Jupyter notebooks depending on the type of material. 

## How to make a copy

If you want to copy the material for your own course, simply clone the site and push it to your own git repository. There are several ways to make create the web site but maybe the simplest way is to build it on your local computer and the push to github pages.

The material has been tested under Linux and Windows 10.

### Dependencies

Install the depenencies first, The material uses 

- Python. You also need
  - Scipy, numpy, seaborn, matplotlib, and some others. Anaconda installation takes care of all the dependencies.
  
- [git tools](https://github.com/git-guides/install-git)
- [ghp-import](https://github.com/c-w/ghp-import)
- [Jupyter Lab/Notebook](https://jupyter.org/)
- [Jupyter Book](https://jupyterbook.org/start/overview.html)
- [sphinx-proof](https://github.com/executablebooks/sphinx-proof)



### Here's one possible way using command line:

1. Clone the material to a directory on your local computer
1. Create a github repository for the material.
1. Push the material from your computer to the new github repository. 
1. Build the jupyter book (this assumes you are inside the directory) using
  ```
  jupyter-book build .
  ```
5. Use `ghp-import` to push the built to `gh-pages`
  ```
   ghp-import -n -p -f _build/html
  ``` 
6. Check the progress from the github repository under `Actions`. Once done, go the web site (as listed under `Actions`.

## Important

Use at your own risk. We take no responsibility or liability of any kind. 

## Copyright 

By Mikko Karttunen and Colin Denniston.  All content on this site (unless otherwise specified) is licensed under the [CC BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).


## Acknowledgments


- The [Jupyter Project](https://jupyter.org/)
- The [JupyterBook community](https://github.com/executablebooks/jupyter-book/graphs/contributors).

