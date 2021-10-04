# Cloud Computing | Side project 1

#### Screenshot
![screenshot](https://raw.githubusercontent.com/Youplala/API-webapp/master/webapp/screenshot.png)


# API & Web App links
- [Web app](https://streamlit-webapp1.herokuapp.com/)
- [API](https://api-qx6f75jsla-ew.a.run.app/run) (accessible using POST requests only)

## Introduction

Using the classification deep learning model ```beto-emotion-analysis``` available at [HuggingFace](https://huggingface.co/finiteautomata/beto-emotion-analysis), we detect an emotion from a sentence. An inference API is running on Google Cloud Run, taking a text input and returning the emotion and score. Using a web app made with Streamlit, we call the API in a easy and interactive way.

## How it works
API is called using a POST request. It requires an API key, which is `mysupersecret` in this demo.

### Request
Request must be like: 

#### Header

```
{"Content-Type": "application/json"}
```

#### Data

```
{
    "api_key": "mysupersecret",
    "input": "I am so happy right now"
}
```



## API cost estimation

The API container is deployed on a Google Cloud Run instance with the following specifications: 

#### Cloud Run
- 1 CPU
- 1GB memory
- 80 concurrent requests
- 0ms response
- 10k requests per month
- 1 instance minimum

Total: **13.14 $ / month**

#### Artifact Registry

~ 3GB storage

Total: **0.25 $ / month**

## Contributors

Elie Brosset & Julien Assuied



