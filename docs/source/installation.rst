Installation
============



1. Install via pip (recommended)
################################

The easiest way to install **SpecOneD** is via pip:

.. code-block::

  pip install speconed


Known issues
************

In some cases the pytables (pip install tables) package cannot find the hdf5 installation. This happens specifically on some python versions run on the new Mac M1 (arm64) chips. In this case, you need to follow the following steps:

.. code-block::

    pip install cython
    brew install hdf5
    brew install c-blosc
    export HDF5_DIR=/opt/homebrew/opt/hdf5
    export BLOSC_DIR=/opt/homebrew/opt/c-blosc

After these steps, you can continue to install **SpecOneD** via pip.

2. Clone the github repository
##############################

This document describes how to install Sculptor and its dependencies. For now the project has not been published on PyPi, yet. Therefore, the first step is to clone the Sculptor repository from `github <https://github.com/jtschindler/sculptor>`_.

To do this simply clone the repository to your folder of choice.

.. code-block::

  git clone https://github.com/jtschindler/sculptor.git



2.3 Installing requirements via pip
***********************************
In the speconed github repository you will find a 'requirements.txt', which allows you to install the necessary requirements using pip from the main sculptor directory:

.. code-block::

  pip install -r requirements.txt


2. Install requirements
#######################

Navigate to the main folder of sculptor. It should contain the *setup.py* file as well as *requirements.txt*, *conda_requirements.yml*, and *environment.yml*.

2.1 Installing requirements with a new conda environment (Recommended)
**********************************************************************

The sculptor github repository provides an environment.yml file. It automatically creates the  *sculptor-env* environment installing all necessary dependencies with the following command:

.. code-block::

  conda env create --file environment.yml

2.3 Install sculptor from the cloned repository
###############################################

With all requirements fulfilled, install Sculptor via

.. code-block::

  pip install -e .

