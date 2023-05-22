# TikTok Analytics Web App <font color="blue">[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)</font>
https://user-images.githubusercontent.com/90381570/185801856-48475c57-2bcf-432b-9aba-d7814830219f.mp4

This project is an online analytical dashboard for analyzing TikTok data, developed as part of the Software Engineering Course at the University of Zanjan. The main idea behind this web app was inspired by Nicholas Renotte, and I have implemented and enhanced it from scratch.

### Problem Definition
The goal of this project is to analyze trending tiktoks data using machine learning techniques. By leveraging a dataset extracted from TikTok and performing exploratory data analysis (EDA) tasks, the project aims to preprocess the data and train a regression model. The selected model for training is the Extra Trees Regressor, chosen based on my experience with different models.

### Dataset
The latest TikTok dataset from Kaggle was gathered for this project. Raw data was subjected to EDA tasks to gain insights and understand the underlying patterns and characteristics of the dataset. This enabled effective preprocessing of the data for subsequent steps.


# Solution Approach
- Identified the problem of tumor detection.
- Extracted use cases and requirements.

## Data Gathering and Exploration:
- Gathered the latest TikTok dataset from Kaggle.
- Conducted exploratory data analysis (EDA) on the raw data.
- Performed necessary data preprocessing steps.

## Model Selection:
- Determined that the task is regression based on the problem definition.
- Considered the data format and volume to choose the Extra Trees Regressor model.
- Leveraged experience working with different models to make an informed selection.

## Model Training and Evaluation:
- Trained the Extra Trees Regressor model on the preprocessed dataset.
- Evaluated the model's performance and adjusted parameters as needed.

## Web App Deployment:
- Utilized Streamlit to deploy the web application on the internet.
- Provided an interactive interface for users to detect tumors using the trained model.

## Usage
To run the web app locally, follow these steps:

- Clone the repository:
```bash
git clone https://github.com/your-username/tumor-detection-web-app.git
```
- Install the required dependencies:
```bash
pip install -r requirements.txt
```
- Run the application:
```bash
streamlit run app.py
```
## Acknowledgements
I would like to express my gratitude to Nicholas Renotte for inspiring this project. His initial idea served as a foundation for my own implementation, allowing me to enhance the web app further.
