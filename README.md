# Smile Detection Project

Welcome to the Smile Detection Project! This project uses computer vision techniques to detect smiles in images using OpenCV and Haar Cascade classifiers. The aim is to demonstrate how machine learning can be used to recognize facial expressions, specifically smiles, in photographs.

## Features

- **Smile Detection**: Automatically detects and highlights smiles in an uploaded image.
- **Easy to Use**: Simple user interface built with Streamlit for quick testing.
- **Pre-trained Models**: Uses OpenCV's pre-trained Haar Cascade classifiers for face and smile detection.

## Demo

Try out the smile detection app live: [Live Demo](link-to-your-hosted-app)

![Smile Detection Demo]()

## How It Works

The smile detection app works by using OpenCV's Haar Cascade classifiers, which are trained to detect various facial features. The following steps outline how the smile detection algorithm operates:

1. **Face Detection**: The algorithm first detects faces in the uploaded image.
2. **Smile Detection**: Within the detected face region, the algorithm looks for a smile using a separate classifier.
3. **Display Results**: The faces and smiles are highlighted with rectangles on the output image.

## Installation

To run this project locally, you'll need to have Python installed. Follow the steps below to get started:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smile-detection.git
   cd smile-detection

1. Installation:
   ```bash
   pip install -r requirements.txt

## Usage

Follow these steps to use the Smile Detection app:

1. **Upload an Image**: Once the app is running, use the file uploader provided on the Streamlit interface to upload an image.
   
2. **Detect Smiles**: After uploading, the app will automatically process the image and detect faces and smiles using the trained Haar Cascade classifiers.
   
3. **View Results**: The processed image will be displayed with rectangles around detected faces and smiles, allowing you to see where smiles have been identified.





