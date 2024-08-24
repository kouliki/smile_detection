# Smile Detection Project

Welcome to the Smile Detection Project! This project uses computer vision techniques to detect smiles in images using OpenCV and Haar Cascade classifiers. The aim is to demonstrate how machine learning can be used to recognize facial expressions, specifically smiles, in photographs.

## Features

- **Smile Detection**: Automatically detects and highlights smiles in an uploaded image.
- **Easy to Use**: Simple user interface built with Streamlit for quick testing.
- **Pre-trained Models**: Uses OpenCV's pre-trained Haar Cascade classifiers for face and smile detection.

## Demo

Try out the smile detection app live: [Live Demo](link-to-your-hosted-app)

![Smile Detection Demo](link-to-demo-image-or-gif)

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
