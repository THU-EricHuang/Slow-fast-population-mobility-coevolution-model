# Slow-fast-population-mobility-coevolution-model

Thank you for reviewing our manuscript **"Population-mobility coevolution drives the emergence of spatial heterogeneity in cities”**.

The repository contains the source code for the simulations and analysis presented in the manuscript. The source code is implemented in Python.

## System requirements

The code has been tested on the following specific environment. We recommend using Anaconda to replicate this environment.

* `python == 3.8.11`
* `numpy == 1.21.6`
* `scipy == 1.7.3`
* `matplotlib == 3.5.0`

## Installation Guide

1. Install Anaconda: [https://docs.anaconda.com/anaconda/install/index.html](https://docs.anaconda.com/anaconda/install/index.html)

2. Create a virtual environment:conda create -n mobility_coevolution python=3.8.11
conda activate mobility_coevolution

3. Install necessary packages:


conda install numpy=1.21.6 scipy=1.7.3 matplotlib=3.5.0


This installation should take less than 10 minutes.

## Demo and Reproduction

The main simulation logic is contained within `main.py`.

1. Activate the experimental environment:

```bash
conda activate mobility_coevolution
```

2. Run the main simulation script:

```bash
python main.py
```

3. To generate visualizations from the simulation results, run the visualization script:

```bash
python Visualization_pop_2D_Batch processing_unifiedlegend.py
```

The expected output will be the simulation data and corresponding figures presented in the manuscript.

## File Description

* `main.py`: The main script to run the slow-fast population-mobility co-evolution model.
* `Cal_distance.py`: Utility script for calculating distances.
* `Cal_functionsimilarity.py`: Utility script for calculating functional similarity.
* `Visualization_pop_2D_Batch processing_unifiedlegend.py`: Script to process simulation results and generate 2D population visualizations with a unified legend.
