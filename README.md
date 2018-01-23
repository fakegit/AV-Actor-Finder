# AV Actor Finder
Project for finding Adult Video actor with only picture but no name

# How it works?
This project composed with 3 componenets,  
- Image Crawler (Crawling with python)
- Face Auto-cropper (Google Vision API)
- Deep Learned model with CNN (Deep learning)

All components build and written by python3 (3.6), so the python 2.x cannot be used for it.

# Requirments
- High quality PC to deep learn the pictures(or you can use pre-trained model)
- Python 3
- And cups of coffee (I mean the patience)
- json based API Key for Google Vision API

# How to use
1. Run the `preprocessor.py`
2. Crawling the images
  - There's no automation for keyword input system.
  - Maybe the `Airi Suzumura, Kana Momonogi, Kirara Asuka, Koharu Suzuki, Yura Sakura` can be the good choice
  - At least 100 images(limit) should be need, because some images can be an wrong one.
3. Cropping the images
  - Be sure you have correct json file for Google Vision API!
  - Many many many of bad images will dropped or removed
  - Input `images` for `Source Directory`
  - Input `outputs` for `Destination Directory`
  - Best choice for `Max number for samples per class` should be 2/3 of total images
4. Run the `train_with_CNN.py`

# Reference
[Codes for CNN and Cropping with Google Vision API usage](https://github.com/bwcho75/facerecognition)
[Codes for image crawling from Google](https://github.com/hardikvasa/google-images-download/blob/master/google-images-download.py)

