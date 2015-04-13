## Winning code

Update: Here's the [winning code](https://github.com/justmarkham/kaggle-pycon-2015) from Kevin.

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

## Simple setup

If you have Anaconda, you are already setup to go.

If you have Miniconda you'll need the following libraries.

    $ conda install numpy pandas scipy matplotlib scikit-learn nltk ipython-notebook seaborn

## Using conda environments

It's useful to have your dependencies in environments. Conda handles environments natively and can help you manage your Data Science projects.

### Get the `environment.yml`

The the `environment.yml` file in this repository (by downloading it, pulling the repository with `git clone https://github.com/dchudz/pycon2015-kaggle-tutorial.git`, or even forking and then pulling your own copy).


### Setup your environment

Once you have either Miniconda or Anaconda, you can just run the following commands to setup your environment (from inside the directory with `environment.yml`):

    $ conda env create
    $ source activate kaggletutorial

*Note: Windows users should run `activate kaggletutorial` instead.*

## Running the notebooks

    $ ipython notebook


## Add more libraries

The tutorial will include lots of time for working on your own and in groups, so feel free to add any additional tools (e.g. for machine learning, text processing, data visualizaton, and data manipulation) you like to your environment.
