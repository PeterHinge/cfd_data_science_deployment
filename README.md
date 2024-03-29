<a name="readme-top"></a>

# BLUEPRINT: Cookiecutter + FastAPI + Docker for Data Science Deployment

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Stargazers](https://img.shields.io/github/stars/peterhinge/cfd_data_science_deployment.svg)](https://github.com/peterhinge/cfd_data_science_deployment/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/peterhinge/cfd_data_science_deployment.svg)](https://github.com/peterhinge/cfd_data_science_deployment/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/peterhinge/cfd_data_science_deployment.svg)](https://github.com/peterhinge/cfd_data_science_deployment/pulls)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](https://github.com/peterhinge/cfd_data_science_deployment/blob/master/LICENSE)
[![Contributors](https://img.shields.io/github/contributors/peterhinge/cfd_data_science_deployment.svg)](https://github.com/peterhinge/cfd_data_science_deployment/graphs/contributors)

Disclaimer: I didn't make this blueprint from scratch - I simply combined some of my favorite frameworks for DS model deployment. 1) Cookiecutter framework for project structure. 2) FastAPI for deploying model/program as a RESTful webservice. 3) Docker for having the model/program containerized.

Credit for this idea goes to my colleague <a target="_blank" href="https://github.com/simonkamronn">Simon Kamronn</a>

--------

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── Dockerfile         <- Dockerfile for building image
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │   │                     the creator's initials, and a short `-` delimited description, e.g.
    │   │                     `1.0-jqp-initial-data-exploration`.
    │   └── 0.1-api-test.ipynb
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── app            <- API application
    │   │   ├── api
    │   │   │   └── routes 
    │   │   ├── core       <- API configs, event-handlers, messages, security etc.
    │   │   ├── models     <- The models for payload, prediction-result, heartbeat etc.
    │   │   ├── services
    │   │   └── main.py    <- FastAPI app
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- Tox file with settings for running tox; see tox.readthedocs.io


<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

--------

## Model deployment
Serving machine learning models production-ready, fast, easy and secure powered by the great FastAPI by [Sebastián Ramírez]([)](https://github.com/tiangolo).

To experiment and get a feeling on how to use this skeleton, a sample regression model for house price prediction is included in this project. Follow the installation and setup instructions to run the sample model and serve it aso RESTful API.

## Requirements
Python 3.6+

## Installation
Install the required packages in your local environment
```bash
conda install --file requirements.txt -c conda-forge
``` 
or 
```bash
pip install -r requirements.txt
``` 

## Setup
1. Make `.env` file.

2. In the `.env` file configure an `API_KEY`. The key is used for authenticating our API. <br>
   A sample API key can be generated using Python REPL:
```python
import uuid
print(str(uuid.uuid4()))
```

3. Install the package in the environment
```bash
python setup.py develop
```

4. Train and save the model
```bash
python src/models/train_model.py
```
This will download the data, train the model and save it to `models/`.

## Run locally

1. Start your  app with: 
```bash
uvicorn src.app.main:app
```
2. Go to [http://localhost:8000/docs](http://localhost:8000/docs).
   
3. Click `Authorize` and enter the API key as created in the Setup step
   
4. You can use the sample payload from the `tests/test_service/test_models.py` file when trying out the house price prediction model using the API.

## Run with Docker
1. Edit `Dockerfile` if necessary
2. Build the docker image
```bash
docker build -t src .
```

3. Deploy the image in a container
```bash
docker run -d --name src -p 8000:80 src
```

## Test in Notebook
1. Run `jupyter lab` in a terminal
2. Open the notebook in `notebooks/0.1-api-test.ipynb`

## Run Tests

If you're not using `tox`, please install with:
```bash
conda install -c conda-forge tox pytest
```

Run your tests with: 
```bash
tox
```

This runs tests and coverage for Python 3.6 and Flake8, Autopep8, Bandit.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

