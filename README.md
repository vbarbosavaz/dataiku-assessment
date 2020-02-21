# Dataiku assessment

Dataiku Machine Learning test for interviewees.

**Keywords:** Machine learning, Data Visualization

**Author:** Vincent Barbosa Vaz

**Date:** February 21, 2020

## Run the project

**Clone the project**

```bash
git clone https://github.com/v-barbosavaz/dataiku_assessment
cd dataiku_assessment
```

**Unzip data archive**

In **data** folder unzip **us_census_full.zip**

Move every files from **us_census_full** folder in **data** folder (parent directory). Delete the empty folder **us_census_full**.

**Create the environment**

```bash
python3 -m venv venv
```

**Activate the environment and install libraries**

```bash
source venv/bin/activate
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
