import pandas as pd
from image_processing import colorImage

def open_removeUnnamed_df(path_csv):
    df = pd.read_csv(path_csv)
    df.drop(columns = "Unnamed: 0", inplace = True)
    display(df.head())
    return df

def addColumn_imageArray(df, name_column, path, debug):
    df["image_array"] = df[name_column].apply(colorImage, args=(path,debug))
    df = df.reset_index().drop(columns="index")
    if debug == False:
        print("Column with arrays from images in gray scale has been added")
    else:
        print("Column with arrays from images in RGB has been added")
    display(df.head())
    return df

def calculateSize(value):
    return value.shape

"""
def addColumn_shape(df, name_column, path, debug):
    df = addColumn_imageArray(df, name_column, path, debug)
    df["shape"] = df["image_array"].apply(calculateSize)
    print("Column with image sizes has been added")
    display(df.head())
    return df

def checkSize(df, name_column, path, debug):
    df = addColumn_shape(df, name_column, path, debug)
    subset["shape"][subset["shape"]!=size].value_counts()
"""

def addColumn_shape(df, name_column):
    df["shape"] = df[name_column].apply(calculateSize)
    print("Column with image sizes has been added")
    display(df.head())
    return df

def checkSize(df, name_column, debug):
    if debug ==False:
        size = (224,224)
    else:
        size = (224,224,3)
    df_shape = df[name_column][df[name_column]!=size].shape
    if  df_shape == (0,):
        print(f"All images are the same size: {size}")
    else:
        print(f"There are images with different size: {size}")
        display(df[df[name_column]!=size])
        return df[df[name_column]!=size]

def saveDFtoPickle(df, column_names, name_file, debug):
    df = df[column_names]
    display(df.head())
    if debug == False:
        df.to_pickle(f"../output/{name_file}_BnW.pkl")
    else:
        df.to_pickle(f"../output/{name_file}_Color.pkl")
