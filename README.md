<div class="hero-icon" align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</div>

<h1 align="center">
AI Powered OpenAI Request Wrapper - MVP
</h1>
<h4 align="center">A Python Backend API for Streamlined OpenAI Integration</h4>
<h4 align="center">Developed with the software and tools below.</h4>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Framework-FastAPI-blue" alt="Framework: FastAPI">
  <img src="https://img.shields.io/badge/Backend-Python-red" alt="Backend: Python">
  <img src="https://img.shields.io/badge/Database-PostgreSQL-blue" alt="Database: PostgreSQL">
  <img src="https://img.shields.io/badge/LLMs-OpenAI-black" alt="LLMs: OpenAI">
</div>
<div class="badges" align="center">
  <img src="https://img.shields.io/github/last-commit/coslynx/AI-Powered-OpenAI-Request-Wrapper-MVP?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/coslynx/AI-Powered-OpenAI-Request-Wrapper-MVP?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/coslynx/AI-Powered-OpenAI-Request-Wrapper-MVP?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Hosting
- 📄 API Documentation
- 📜 License
- 👏 Authors

## 📍 Overview

This repository houses the Minimum Viable Product (MVP) for an "AI Powered OpenAI Request Wrapper," a Python backend API designed to simplify interactions with OpenAI's powerful language models. This MVP serves as a foundational layer for developers and businesses to seamlessly integrate AI capabilities into their applications.

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The API follows a robust and modular architecture, utilizing FastAPI for efficient API development, PostgreSQL for data storage and retrieval, and the OpenAI Python library for secure and seamless integration with OpenAI's API. |
| 📄 | **Documentation**  | This README file provides a comprehensive overview of the MVP, its functionality, and how to set it up and use it effectively.                                   |
| 🔗 | **Dependencies**   | The codebase relies on external libraries such as FastAPI, Uvicorn, OpenAI, Pydantic, SQLAlchemy, psycopg2-binary, python-dotenv, and pytest. |
| 🧩 | **Modularity**     | The API is designed with modularity in mind, separating different functionalities into distinct files and modules for easier maintainability and scalability.  |
| 🧪 | **Testing**        | Comprehensive unit tests and integration tests using pytest ensure the API's functionality, robustness, and adherence to best practices.       |
| ⚡️  | **Performance**    | The API utilizes asynchronous programming and optimized libraries for efficient handling of requests, minimizing latency and maximizing performance.  |
| 🔐 | **Security**       | Security is a top priority, with HTTPS for secure communication, API key authentication, rate limiting, and input validation to prevent unauthorized access. |
| 🔀 | **Version Control**| The project uses Git for version control, allowing for easy tracking of changes and collaboration between developers. |
| 🔌 | **Integrations**   | The API seamlessly integrates with OpenAI's API using the OpenAI Python library, enabling access to a range of language models for various AI tasks. |
| 📶 | **Scalability**    | The architecture allows for easy scalability, with a scalable database (PostgreSQL) and a performant framework (FastAPI).  |

## 📂 Structure

```text
AI-Powered-OpenAI-Request-Wrapper-MVP
├── requirements.txt
├── .env
├── main.py
├── config
│   └── settings.py
├── database
│   └── database.py
├── routes
│   ├── generate_text.py
│   ├── models.py
│   └── usage.py
└── tests
    └── unit
        └── test_utils.py

```

## 💻 Installation

### 🔧 Prerequisites
- Python 3.9+
- PostgreSQL 13+
- Docker 20.10+

### 🚀 Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/coslynx/AI-Powered-OpenAI-Request-Wrapper-MVP.git
   cd AI-Powered-OpenAI-Request-Wrapper-MVP
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```bash
   docker-compose up -d postgres
   ```
4. Configure environment variables:
   ```bash
   cp .env.example .env
   # Replace placeholders in .env with your OpenAI API key and PostgreSQL connection details
   ```

## 🏗️ Usage

### 🏃‍♂️ Running the MVP
1. Start the development server:
   ```bash
   uvicorn main:app --reload
   ```
2. Access the API:
   - Make API requests using tools like Postman or curl.

## 🌐 Hosting

### 🚀 Deployment Instructions

1. Build the Docker Image:
   ```bash
   docker-compose build
   ```
2. Deploy to a Container Orchestration Platform:
   - Follow the specific deployment instructions for your preferred platform (e.g., Docker Hub, AWS ECS, Kubernetes).

## 📄 API Documentation

### 🔍 Endpoints

- **POST /generate_text**
    - Description: Generate text using OpenAI's API.
    - Body: 
      ```json
      {
        "prompt": "Write a short story about a cat who can talk.",
        "model": "text-davinci-003",
        "temperature": 0.7,
        "max_tokens": 100
      }
      ```
    - Response: 
      ```json
      {
        "response": "The cat sat on the windowsill, gazing out at the world with its bright, green eyes. 'I wish I could talk,' it thought to itself, 'then I could tell everyone about my adventures in the garden.'",
        "model": "text-davinci-003",
        "tokens": 80
      }
      ```
- **GET /models**
    - Description: Retrieve a list of available OpenAI models.
    - Response: 
      ```json
      {
        "models": [
          "text-davinci-003",
          "text-curie-001",
          "text-babbage-001",
          "text-ada-001",
          "gpt-3.5-turbo"
        ]
      }
      ```
- **GET /usage** 
    - Description: Get API usage statistics (optional).

### 🔑 Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key.
- `DATABASE_URL`: Connection string for the PostgreSQL database.

## 📜 License & Attribution

### 📄 License
This Minimum Viable Product (MVP) is licensed under the [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) license.

### 🤖 AI-Generated MVP
This MVP was entirely generated using artificial intelligence through [CosLynx.com](https://coslynx.com).

No human was directly involved in the coding process of the repository: AI-Powered-OpenAI-Request-Wrapper-MVP

### 📞 Contact
For any questions or concerns regarding this AI-generated MVP, please contact CosLynx at:
- Website: [CosLynx.com](https://coslynx.com)
- Twitter: [@CosLynxAI](https://x.com/CosLynxAI)

<p align="center">
  <h1 align="center">🌐 CosLynx.com</h1>
</p>
<p align="center">
  <em>Create Your Custom MVP in Minutes With CosLynxAI!</em>
</p>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Developers-Drix10,_Kais_Radwan-red" alt="">
  <img src="https://img.shields.io/badge/Website-CosLynx.com-blue" alt="">
  <img src="https://img.shields.io/badge/Backed_by-Google,_Microsoft_&_Amazon_for_Startups-red" alt="">
  <img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4,_v6-black" alt="">
</div>

```