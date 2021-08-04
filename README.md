# Fastapi Boilerplate

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Contact](#contact)

<!-- ABOUT THE PROJECT -->
## About

### Built With
* [Python](https://python.org)
* [FastAPI](https://github.com/zalando/connexion)
* [Peewee](http://docs.peewee-orm.com/en/latest/)

<!-- GETTING STARTED -->
## Getting Started with Development
This is a development setup guide for this project. Please follow the instructions to setup
project locally.

### 🤚 **Requirements**
- Docker 

### ⏳ **Running locally**
- Pull the repo
    ```bash
    docker compose up -d --build
    ```
  
    Application will run on [0.0.0.0:8000/v1](http://0.0.0.0:8000/v1)
    Swagger ui will run on [0.0.0.0:8000/docs](http://0.0.0.0:8000/docs)

## Troubleshooting
### 🧪 **Testing**
- Run pytest
    ```bash
    docker compose exec web pytest 
    ```
