# Python virtual environments

There is a vast number of python packages both distributed with the basic installation and contributed by the users and various projects. When packages are updated or/and changed, compatibility may break. That is not a problem between packages that belong to the main distribution but some of the contributed ones, including ones that may be your own ones, may also need to be modified to be compatible with the new distribution. The solution to this is the so-called *virtual environment.*

The idea of a *virtual environment* is to provide a sandbox - an isolated environment - for a project. This allows the project to have its own dependencies without interfering with the other projects. Here is a practical example from the context of molecular simualtions (this was the case in Nov 2020 but may have changed since then): The widely used molecular simulations analysis package [MDAnalysis](https://www.mdanalysis.org/) requires a specific version of the plotting package [Matplotlib](https://matplotlib.org/). The latest Matplotlib version (=the the latest at the time of writing this) leads to some unexpected errors. Using *virtual environments* helps to circumvent the problem since creating an environment specific for MDAnalysis allows it to have its own version of Matplotlib. 

In the example above, we’d simply created a separate *virtual environment*. This could be extended to any other situations. For example, let's assume that we two projects, `ProjectA` and `ProjectB`. Let's further assume that they have different and possibly conflicting dependencies. We simply need to create separete *virtual environments* for both `ProjectA` and `ProjectB`, and are  good to go. 

There are no limits to the number of environments. 


```{note}
Using virtual environments is *highly* recommended. Using them eliminates lots of potential errors and problems with package updates.
```

## Installation & practical example

````{tabbed} Using Anaconda command line

Here's how to create virtual environments with `conda` using the command line terminal. This works in Linux, WSL/WSL2 and Mac. Mac and Windows 10 have also the Anaconda GUI but using command line is quicker. Note that `conda` stores the information about environments in `${HOME}/anaconda3/envs/`. In practise that means that environments can activated and deactivated very conveniently (this is different from `pip`).



**1. Check the version and existing environments:**

  - Check the version of `conda` (command line):

    ```
    conda -V
    ```

  - Check if `conda` needs to be updated:

    ```
    conda update conda
    ```

  - List  all of your existing `conda` environments:

    ```
    conda env list
    ```

  - If you want to see the list of packages installed in your current virtual environment:

	```
    conda list
    ```

**2. Set up a virtual environment with `conda`:**


   - Create a new virtual environment. To use your current version of Python:
     ```
     conda create -n my_new_environment
     ```

   - Alternatively, if you want to use some specific version of Python, instead use
     ```
     conda create -n my_new_environment python=x.y
     ```
     and replace `x.y` by the version number accordingly


   - Activate the new virtual environment

     ```
     conda activate  my_new_environment
     ```
    
	 After this, the name of your new environment will appear in front of the prompt on your terminal.


   - Install the packages that you want for the environment called `my_new_environment`

     ```
     conda install -n my_new_environment <package name>
     ```
	 Note: the option `-n` specifies the name of the environment. That allows for easy installation of
	 packages into any environment. Leaving `-n` out installs in the current environment.

   - Deactivate the virtual environment

     ```
     conda deactivate
     ```

     After this, the text `base` will appear in front of the command prompt on your terminal.



**If you want to remove your virtual environment:** 

 ```
 conda env remove -n  my_new_environment
 ```

````

````{tabbed} Using the Anaconda GUI

- Open the Anaconda Navigator
- Click on the tab named 'Environments'
- Click on `Create` at the bottom of the Navigator menu

````

````{tabbed} Virtual environments with pip

`pip` works a bit differently, but using it is equally easy. First, install the package `virtualenv` using

```
python3 -m pip install --user virtualenv
```

This gives `venv` for settinhg up virtual environments.

**Create a virtual environment:**

There is one important thing to notice here and this is where `pip` is different from `conda`. Using `pip` creates 
a virtual environment and its directories at the location where you currently are. In the example below, the creation of the new environment that is called `my_new_env` means that a directory called `my_new_env` is created *at the current location*. This is less convenient than with `conda`. You can activate a virtul environment from any location but with `pip`, you need to know where it is located.

  - The command to create a new virtual environment (we call it here `my_new_env`):
    ```
    python3 -m venv my_new_env
    ```
  - After its creation, the environment must be activated by the command `source`
    ```
	source my_new_env/bin/activate
	```
  - To check that the virtual environment is indeed activated, type
    ```
	which python
    ```
  - Deactivation is easier: Independent of your location, simply type 
    ```
	deactivate
	```

````


## More on Python virtual environments

- [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
- [A Guide to Python’s Virtual Environments](https://towardsdatascience.com/virtual-environments-104c62d48c54)


