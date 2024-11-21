# ml-service-template

# Getting Started

This a template for FastApi services.

1. Uncomment .github/workflows/build=image.yaml, build-images.yaml, and push-main.yaml. You can do that like this: 
```
Select the entire file:
Press Ctrl + A (or Cmd + A on macOS) to select all lines of the YAML file.

Toggle the comment off:
Press Ctrl + / (or Cmd + / on macOS).
```

2. .github/workflows/push-main.yaml: adjust `-R manifests/repo-name` to be the name of this repo.
3. app/api/endpoints/yourservice.py: change this file name to properly reflect your service.
4. app/schemas/yourservice.py: change this file name to properly reflect your service.

Typically, the filename across api/endpoints, crud, models, schemas, will have the same name. For example if you endpoint file name is `pricing.py` then models, schemas, and crud will aslo be named `pricing.py`.


## Local Development

### Prerequisites

1. Prepare a  `.env` file in root of this repo for environment variables (Your service may have different variables):

```
APP_ENV=
OPENAI_APIKEY=
PINECONE_APIKEY=

```


## Run the Service

If your service relies on private Python packages hosted on CodeArtifact:

### The Easy Way Beta

1. Install AWS CLI 

run `brew tap aws/tap`
  `brew install awscli`
`brew install aws-sso-cli`
  `brew install aws-sso-util`

2. run `./sso.sh`

3. Setup a virtual environment.

anaconda recommended

run `conda create --name [YOUR_NAME] python=3.10`

run `pip install -r requirements.txt`

run `conda activate [YOUR_NAME]`

## Run Tests Locally

Run `pytest tests`

2. Install Lefthook pre-commits, run: `./setup.sh`

3. run `./docker.sh`

This will build the supplier-recommendations docker image.

3. Run the image: `./run.sh`

You may sometimes run into build issues with Docker, one possible reason is not enough free disk space.
To clean up images, run:

`docker system prune`

ETC ETC ETC

