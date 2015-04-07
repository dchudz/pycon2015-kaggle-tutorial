# Instructions

These are instructions for recommended preparation for students in the PyCon 2015 Kaggle Tutorial.

If possible, try to check back Wednesday night for any minor updates to the data set or `environment.yml`. I'll add a note here if anything is updated.

## Download dataset

The tutorial will be based on the data [here](https://inclass.kaggle.com/c/pycon-2015-tutorial/data). 

## Download Anaconda or Miniconda

If you don't have Anaconda or Miniconda installed in your laptop, you can download them from here:

- [Miniconda](http://conda.pydata.org/miniconda.html): Python distribution with conda package manager.
  [Recommended]
- [Anaconda](http://continuum.io/downloads): Free enterprise-ready Python distribution with 270+ data and
  scientific packages.

For step-by-step instructions, visit [Anaconda Install](http://docs.continuum.io/anaconda/install.html)

Alternatively, command line download instructions for UNIX systems:

    $ wget http://bit.ly/miniconda
    $ bash miniconda


## Setup your environment

Once you have either Miniconda or Anaconda, you can just run the following commands to setup your environment:

    $ conda env create
    $ source activate kaggletutorial

*Note: Windows users should run `activate kaggletutorial` instead.*

## Running the notebooks

    $ ipython-notebook


## Add more libraries

The tutorial will include lots of time for working on your own and in groups, so feel free to add any additional tools (e.g. for machine learning, text processing, data visualizaton, and data manipulation) you like to your environment.