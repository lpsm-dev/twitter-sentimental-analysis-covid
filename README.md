<p align="center">
  <img alt="sentiment-analysis" src="https://www.networkx.nl/wp-content/uploads/2015/02/Twitter_Python_MongoDB-300x289.png" width="250px" float="center"/>
</p>

<h1 align="center">Welcome to Sentiment Analysis Repository</h1>

<p align="center">
  <strong>Python Sentiment Analysis API + Docker + Docker Compose</strong>
</p>

<p align="center">
  <a href="https://github.com/lpmatos/sentiment-analysis">
    <img alt="Open Source" src="https://badges.frapsoft.com/os/v1/open-source.svg?v=102">
  </a>

  <a href="https://github.com/lpmatos/sentiment-analysis/graphs/contributors">
    <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/lpmatos/sentiment-analysis">
  </a>

  <a href="https://github.com/lpmatos/sentiment-analysis">
    <img alt="GitHub Language Count" src="https://img.shields.io/github/languages/count/lpmatos/sentiment-analysis">
  </a>

  <a href="https://github.com/lpmatos/sentiment-analysis">
    <img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/lpmatos/sentiment-analysis">
  </a>

  <a href="https://github.com/lpmatos/sentiment-analysis/stargazers">
    <img alt="GitHub Stars" src="https://img.shields.io/github/stars/lpmatos/sentiment-analysis?style=social">
  </a>

  <a href="https://github.com/lpmatos/sentiment-analysis/commits/master">
    <img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/lpmatos/sentiment-analysis">
  </a>

  <a href="https://github.com/lpmatos/sentiment-analysis">
    <img alt="Repository Size" src="https://img.shields.io/github/repo-size/lpmatos/sentiment-analysis">
  </a>

  <a href="https://github.com/lpmatos/sentiment-analysis/issues">
    <img alt="Repository Issues" src="https://img.shields.io/github/issues/lpmatos/sentiment-analysis">
  </a>

  <a href="https://github.com/lpmatos/sentiment-analysis/blob/master/LICENSE">
    <img alt="MIT License" src="https://img.shields.io/github/license/lpmatos/sentiment-analysis">
  </a>
</p>

### Menu

<p align="left">
  <a href="#pre-requisites">Pre-Requisites</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#description">Description</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#how-to-contribute">How to contribute</a>
</p>

### By me a coffe

Pull requests are welcome. If you'd like to support the work and buy me a ☕, I greatly appreciate it!

<a href="https://www.buymeacoffee.com/EatdMck" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 100px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

### Getting Started

If you want use this repository you need to make a **git clone**:

```bash
git clone --depth 1 https://github.com/lpmatos/sentiment-analysis.git -b master
```

This will give access on your **local machine**.

### Pre-Requisites

To this project you yeed:

* Python 3.8.
* Docker and Docker Compose.
* MongoDB.

### Built with

- [Python](https://www.python.org/)
- [MongoDB](https://www.mongodb.com/)
- [Mongoku](https://github.com/huggingface/Mongoku)
- [AdminMongo](https://github.com/mrvautin/adminMongo)
- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### How to use it?

1. Set the gitlab environment variables.
2. Install python packages in requirements.txt.
2. Run this script with docker-compose, Dockerfile or into your local machine with Python command.
3. Profit.

Press CTRL + C to stop it in Docker Compose or Dockerfile.

### Description

This is a project whose focus is to address the analysis of feelings in a basic way. An api was created to perform the search for tweets and as a result returns a list with the classification: positive, neutral, negative.

### Mongo Schema

![Alt text](docs/images/MONGO_SCHEMA.png?raw=true "Mongo Schema")

### Services

![Alt text](docs/images/SERVICES.png?raw=true "Services")

### Routes

![Alt text](docs/images/ROUTES.png?raw=true "Routes")

### Architecture

![Alt text](docs/images/ARCHITECTURE.png?raw=true "Architecture Sentimental Analysis")

### Results

![Alt text](docs/images/RESULTS.png?raw=true "Results Sentimental Analysis")

### Documentation

[Project Documentation](/docs/helper.md)

### MongoDB Tools

Some MongoDB Tools that we use in this project.

#### Mongoku

MongoDB client for the web. Query your data directly from your browser. You can host it locally, or anywhere else, for you and your team.

It scales with your data (at Hugging Face we use it on a 1TB+ cluster) and is blazing fast for all operations, including sort/skip/limit. Built on TypeScript/Node.js/Angular.

#### AdminMongo

AdminMongo is a cross platform user interface (GUI) to handle all your MongoDB connections/databases needs. AdminMongo is fully responsive and should work on a range of devices.

>
> AdminMongo connection information (including username/password) is stored unencrypted in a config file, it is not recommended to run this application on a production or public facing server without proper security considerations.
>

### Environment variables

**Name**  |  **Description**
:---:  |  :---:
**TWITTER_CONSUMER_KEY**  |  Twitter Consumer Key
**TWITTER_CONSUMER_SECRET**  |  Twitter Consumer Secret
**TWITTER_ACCESS_TOKEN**  |  Twitter Access Token
**TWITTER_ACCESS_TOKEN_SECRET**  |  Twitter Access Token Secret
**LOG_PATH**  |  Just the Log Path
**LOG_FILE**  |  Just the Log File
**LOG_LEVEL**  |  Just the Log Level
**LOGGER_NAME**  |  Just the Logger name

### 🐋 Development with Docker

Steps to build the Docker Image.

#### Build

```bash
docker image build -t <IMAGE_NAME> -f <PATH_DOCKERFILE> <PATH_CONTEXT_DOCKERFILE>
docker image build -t <IMAGE_NAME> . (This context)
```

#### Run

Steps to run the Docker Container.

* **Linux** running:

```bash
docker container run -d -p <LOCAL_PORT:CONTAINER_PORT> <IMAGE_NAME> <COMMAND>
docker container run -it --rm --name <CONTAINER_NAME> -p <LOCAL_PORT:CONTAINER_PORT> <IMAGE_NAME> <COMMAND>
```

* **Windows** running:

```
winpty docker.exe container run -it --rm <IMAGE_NAME> <COMMAND>
```

For more information, access the [Docker](https://docs.docker.com/) documentation or [this](docs/docker.md).

### 🐋 Development with Docker Compose

Build and run a docker-compose.

```bash
docker-compose up --build
```

Down all services deployed by docker-compose.

```bash
docker-compose down
```

Down all services and delete all images.

```bash
docker-compose down --rmi all
```

### How to contribute

>
> 1. Make a **Fork**.
> 2. Follow the project organization.
> 3. Add the file to the appropriate level folder - If the folder does not exist, create according to the standard.
> 4. Make the **Commit**.
> 5. Open a **Pull Request**.
> 6. Wait for your pull request to be accepted.. 🚀
>
Remember: There is no bad code, there are different views/versions of solving the same problem. 😊

### Add to git and push

You must send the project to your GitHub after the modifications

```bash
git add -f .
git commit -m "Added - Fixing somethings"
git push origin master
```

### Versioning

- [CHANGELOG](CHANGELOG.md)

### License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

### Author

👤 **Lucca Pessoa**

Hey!! If you like this project or if you find some bugs feel free to contact me in my channels:

> * Email: luccapsm@gmail.com
> * Website: https://github.com/lpmatos
> * Github: [@lpmatos](https://github.com/lpmatos)
> * LinkedIn: [@luccapessoa](https://www.linkedin.com/in/lucca-pessoa-4abb71138/)

### Show your support

Give a ⭐️ if this project helped you!

### Project Status

* ✔️ Finish

---

<p align="center">Feito com ❤️ by <strong>Lucca Pessoa :wave:</p>
