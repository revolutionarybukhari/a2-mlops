# Data Version Control with Apache Airflow

## Project Overview

This project implements an automated data pipeline that extracts data from BBC's homepage, processes the data, saves it in JSON format, and uploads it to Google Drive. We use Data Version Control (DVC) to manage versions of our datasets and Apache Airflow to schedule and automate the data processing workflows.

## Setup Instructions

### Prerequisites

- Python 3.x
- Git
- Apache Airflow
- DVC
- Access to Google Drive API

### Installation

1. _Clone the repository:_

```bash
   git clone https://github.com/revolutionarybukhari/a2-mlops.git
   cd a2-mlops
```

2. _Install the required Python libraries:_

```bash
pip install -r requirements.txt
```

3. _Initialize DVC:_

```bash
dvc init
dvc remote add -d myremote gdrive://<Your-Google-Drive-Folder-ID>
```

4. _Start Apache Airflow:_

```bash
airflow webserver -p 8080
airflow scheduler
```

Navigate to localhost:8080 in your web browser to access the Airflow UI.

_Configuration_
Ensure you have set up your Google Drive credentials and saved them in your project directory. Follow the Google Drive API documentation to obtain credentials.json and configure pydrive.
