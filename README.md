# JupyterBook Course Template and Material for SciComp

This is a repository the Scientific Computing course intended for advanced undergraduates and early graduate students.

## Course Website

To access the rendered version of this course, visit 

https://mejk.github.io/SciComp

If you wish to use it as such, you're most welcome to do so.

## How to use the material for your own course or such

Just clone the site (as you see below, this is CC licensed). It is expected that you know how git and friends work. The lectures are written as both markdown and Jupyter notebooks depending on the type of material. Should be easy to modify and adjust. 

## Updates and contributions

- This material is updated continuously and new modules are added.
- If you wish to contribute, just contact us! Contributions are very welcome. The one requirement is that all the material is original or Creative Commons licensed.
- If you find typos or errors, let us know.


## How to make a copy

If you want to copy the material for your own course, simply clone the site and push it to your own git repository. There are several ways to make create the web site but maybe the simplest way is to build it on your local computer and the push to your own github pages.

The material has been tested under Linux, MacOS and Windows 10.

### Dependencies

Install the dependencies first, The material uses 

- Python. You also need
  - Scipy, numpy, seaborn, matplotlib, and some others. Anaconda installation takes care of all the dependencies.
  
- [git tools](https://github.com/git-guides/install-git)
- [ghp-import](https://github.com/c-w/ghp-import)
- [Jupyter Lab/Notebook](https://jupyter.org/)
- [Jupyter Book](https://jupyterbook.org/start/overview.html)
- [sphinx-proof](https://github.com/executablebooks/sphinx-proof)

### Annotations, pdf and such

- The [course web site](https://mejk.github.io/SciComp/) uses [https://hypothes.is](https://hypothes.is) that allows for both private and public annotations. This is a useful feature for both the teacher and the student.
-  The [course web site](https://mejk.github.io/SciComp/) allows saving the source code of each page as well as producing a PDF file of the page 

### Here's one possible way using the command line:

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

## Important!!!

- Use at your own risk. We take no responsibility or liability of any kind. 
- The various installations have all been tested and tried, but if you choose to follow the notes, the risk is entirely yours. Please be aware that computer software and operating systems develop rapidly: Pay attention to the version numbers.

## Copyright 

- By [Mikko Karttunen](https://www.softsimu.net/mikko/) and [Colin Denniston](https://publish.uwo.ca/~cdennist/group.html).  All content on this site (unless otherwise specified) is licensed under the [CC BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).
- We do wish that if you use the material, please include an acknowledgement. 


## Acknowledgements

This project is made possible with funding by the Government of Ontario and through eCampusOntario???s support of the Virtual Learning Strategy. To learn more about the Virtual Learning Strategy visit: [https://vls.ecampusontario.ca](https://vls.ecampusontario.ca.).

![Ontario](./images/logos/ON_POS_LOGO_RGB-sm-2.png)


- The [Jupyter Project](https://jupyter.org/)
- The [JupyterBook community](https://github.com/executablebooks/jupyter-book/graphs/contributors).
- [Dr. Firas Moosvi](https://github.com/firasm) for the initial inspiration. Check his pages, there's more cool Jupyter Book stuff!

