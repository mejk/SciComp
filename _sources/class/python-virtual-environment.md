# Python virtual environments

There is a vast number of python packages both distributed with the basic installation and contributed by the users. When packages are updated or/and changed, compatibility may break. That is not a problem between packages that belong to the main distribution but some of the contributed ones, including ones that may be your own ones, may also need to be updated to be compatible with the new distribution. The solution to this is the so-called *virtual environment.*

The idea of a *virtual environment* is provide a sandbox - an isolated environment - for a project. This allows the project to have its own dependencies without interfering with the other projects. Here is a practical example (this was the case in Nov 2020 but may have changed since then): The molecular simulations analysis package MDAnalysis requires a specific version of the plotting package Matplotlib. The latest Matplotlib version leads to some unexpected errors. Using virtual environments helps to circumvent the problem since creating a an environment specific for MDAnalysis allows it to have its own version of Matplotlib. 



**More:**

- [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)


In our little example above, we’d just need to create a separate virtual environment for both ProjectA and ProjectB, and we’d be good to go. Each environment, in turn, would be able to depend on whatever version of ProjectC they choose, independent of the other.

The great thing about this is that there are no limits to the number of environments you can have since they’re just directories containing a few scripts. Plus, they’re easily created using the virtualenv or pyenv command line tools.
