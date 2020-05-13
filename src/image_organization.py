import re
import pandas as pd

def createDic(filesName, label, dictionary):
    for file in filesName:
        if re.search(fr"^{label}", file):
            #print(file, label)
            if label in dictionary:
                #print(file, label, "if")
                dictionary[label].append(file)
            else:
                #print(file, label, "else")
                dictionary[label] = [file]
    return dictionary
"""
def createDic(images, dictionary):
    for image in images:
        pic = image.split("images/")[-1]
        label = pic.split("_")[0]
        if label in dictionary:
            dictionary[label].append(pic)
        else:
            dictionary[label] = [pic]
    return dictionary
"""
def createDF(dictionary):
    label_images = []
    for label,images in dictionary.items():
        for image in images:
            label_images.append([label,image])
    return pd.DataFrame(label_images, columns=["label","image"])