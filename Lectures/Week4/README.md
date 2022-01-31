# Week 4

## Running Project

### Running on Kaggle (Suggested)

1. Sign-In or create an account on Kaggle (Required)
2. Go to <https://www.kaggle.com/uysimty/keras-cnn-dog-or-cat-classification>
3. At the top right of the website, copy this notebook
4. Unzip the files using python zip library and change where files are being accessed as running.
5. Go through the code, and change train and test directories accordingly

```python
import zipfile

def unzip_file(path_to_zip_file, directory_to_extract_to):
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
        
unzip_file("../input/train.zip", "./train")
unzip_file("../input/test1.zip", "./test")
```

### Running Locally

1. Download files from Kaggle <https://www.kaggle.com/uysimty/keras-cnn-dog-or-cat-classification/data>
2. Copy and unzip files in Resources/Lectures/Data
3. Open and step through Week4.ipynb

## Model Preformance

### Training Accuracy and Loss Over 50 Epochs

Loss = Top | Accuracy = Bottom

![Training Accuracy and Loss Over Time](./TrainingOutput.png)

### Example Predictions From model

0 = cat, 1 = dog

![18 Example Predictions From Model](ExamplePredictions.png)