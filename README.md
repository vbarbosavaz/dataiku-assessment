# Dataiku assessment

Dataiku Machine Learning test for interviewees.

**Keywords:** Machine learning, Data Visualization, Plotly

**Author:** Vincent Barbosa Vaz

**Date:** February 21, 2020

## Note

I added a PDF version for convenience.

I strongly recommend not to use the PDF rendered version of the notebook (the **rendering is poor** and **does not exploit the interactive functionality of Plotly**) but rather run the notebook and have fun with graphics.

## Run the project

**Clone the project**

```bash
git clone https://github.com/v-barbosavaz/dataiku-assessment
cd dataiku-assessment
```

**Unzip data archive**

In **data** folder unzip **us_census_full.zip**

Move every files from **us_census_full** folder in **data** folder (parent directory). Delete the empty folder **us_census_full**.

**Create the environment**

```bash
python3 -m venv env
```

**Activate the environment and install libraries**

```bash
source env/bin/activate
pip install -r requirements.txt
```

**Note**

You may have to deactivate conda base:

```bash
conda deactivate
```

**Run Jupyter Notebook**

```bash
jupyter notebook
```

## Development utils

**Deactivate the environment**

```bash
deactivate
```

**Output installed packages in requirements format (alternative *pip list*)**:

```bash
pip freeze
```

**Generate a requirements file:**

```bash
pip freeze > requirements.txt
```

## Datasets

- List of State Abbreviations, [http://worldpopulationreview.com/states/state-abbreviations](http://worldpopulationreview.com/states/state-abbreviations/)
- US Census, extracted from the census bureau database found at : [https://www.census.gov](https://www.census.gov/)
