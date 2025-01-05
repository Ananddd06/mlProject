# Student Exam Performance Prediction

This project is an end-to-end machine learning application designed to predict a student's math exam score based on various features such as gender, ethnicity, parental level of education, lunch type, test preparation course, writing score, and reading score.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Web Application](#web-application)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The objective of this project is to build a predictive model that estimates a student's math exam score based on input features. The project encompasses data preprocessing, feature engineering, model training, evaluation, and deployment of a web application for user interaction.

## Features

- **Data Preprocessing**: Handling missing values, encoding categorical variables, and feature scaling.
- **Model Training**: Training machine learning models to predict math scores.
- **Model Evaluation**: Assessing model performance using appropriate metrics.
- **Web Application**: A user-friendly interface for inputting student data and obtaining predictions.
- **Deployment**: Hosting the web application using Vercel for accessibility.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Ananddd06/mlProject.git
   cd mlProject
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Activate the Virtual Environment**:

   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Run the Application**:

   ```bash
   python app.py
   ```

3. **Access the Web Application**:

   Open a web browser and navigate to `http://localhost:5000` to use the application.

## Model Training

The model training process involves the following steps:

1. **Data Loading**: Load the dataset containing student information and exam scores.
2. **Data Preprocessing**: Clean the data, handle missing values, encode categorical variables, and scale features.
3. **Feature Engineering**: Select relevant features for model training.
4. **Model Selection**: Choose appropriate machine learning algorithms for prediction.
5. **Model Training**: Train the models using the preprocessed data.
6. **Model Evaluation**: Evaluate model performance using metrics such as Mean Absolute Error (MAE) and R-squared.
7. **Model Selection**: Select the best-performing model based on evaluation metrics.

The trained model is then saved and integrated into the web application for real-time predictions.

## Web Application

The web application provides an interface for users to input student data and receive predicted math exam scores.

**Key Components**:

- **Home Page (`index.html`)**:
  - A landing page with a "Learn More" button that navigates to the prediction form.

- **Prediction Page (`home.html`)**:
  - A form where users can input student details.
  - Upon submission, the application displays the predicted math score.

**Navigation**:

- The "Learn More" button on the home page directs users to the prediction form.

## Deployment

The application is deployed using Vercel, providing a live URL for users to access the prediction tool.

**Deployment Steps**:

1. **Install Vercel CLI**:

   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**:

   ```bash
   vercel login
   ```

3. **Deploy the Application**:

   ```bash
   vercel
   ```

4. **Set Up Environment Variables**:

   Configure any necessary environment variables in the Vercel dashboard to ensure the application functions correctly.

**Live Application**:

Access the deployed application at: [ml-project-lemon.vercel.app](https://ml-project-lemon.vercel.app)

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**.
2. **Create a New Branch**:

   ```bash
   git checkout -b feature-branch
   ```

3. **Make Changes and Commit**:

   ```bash
   git commit -m "Description of changes"
   ```

4. **Push to the Branch**:

   ```bash
   git push origin feature-branch
   ```

5. **Create a Pull Request**.

--------->

This README provides an overview of the Student Exam Performance Prediction project, including setup instructions, usage guidelines, and deployment details. For more information, visit the [GitHub repository](https://github.com/Ananddd06/mlProject).
