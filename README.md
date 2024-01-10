# Terrain Classification Web App

## Overview

This web application allows users to explore and classify different terrains from images. It utilizes a Convolutional Neural Network (CNN) to analyze uploaded images and predict the terrain type, such as grassy, marshy, rocky, or sandy.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Model](#model)
- [File Structure](#file-structure)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [Dataset](#dataset)   

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Mahesh062003/Terrain_classification-using-ML.git

    ```
1.Install the required Python packages:
```bash
pip install -r requirements.txt
```
## Usage 
1.Run the Flask application:
```bash
Pythhon app.py
```
2.Open your web browser and go to http://localhost:5000.

3.Explore the different sections:

Home: Explore the terrains with captivating videos.
Upload: Upload an image to classify the terrain type.
About: Learn more about the application and how it works.

# Dependencies 

Dependencies
Flask
TensorFlow
NumPy
Install all dependencies using:

```bash

pip install -r requirements.txt
```
# Model
The application uses a pre-trained CNN model for terrain classification. The model file (`model.h5`) is stored in the `model` directory. Update the class names in the model based on your requirements.

# File Structure
- **static:** Contains video files for the landing page.
- **templates:** Contains HTML templates for rendering web pages.
- **model:** Stores the pre-trained CNN model.
- **app.py:** Flask application script.
- **index.html:** Main HTML file for the web app.
- **README.md:** Documentation file.


## Screenshots 
![image](https://github.com/mahesh062003/Terrain_classification/assets/92420298/af137767-7e5a-424f-9db9-87b65d7f85ce)
![image](https://github.com/mahesh062003/Terrain_classification/assets/92420298/5d1524f9-9bcf-4f68-a632-8285d0473977)
![image](https://github.com/mahesh062003/Terrain_classification/assets/92420298/38f680f2-d9d6-404f-8a15-e72d90498739)


## Contributing 
Feel free to contribute to the project. Create a fork, make your changes, and submit a pull request.

## Dataset
Find the dataset link below 

  https://drive.google.com/drive/folders/1OOc-ceo7eF1stmN8JTUL4JNnnqNDklQ-?usp=drive_link
