import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelBinarizer

def average_blood_pressure(data):
    """get the blood pressure means"""
    data['BPXDI'] = round((data.BPXDI1 + data.BPXDI2 + data.BPXDI3) / 3 , 2)
    data = data.drop(['BPXDI1', 'BPXDI2', 'BPXDI3'], axis=1)
    data['BPXSY'] = round((data.BPXSY1 + data.BPXSY2 + data.BPXSY3) / 3 , 2)
    data = data.drop(['BPXSY1', 'BPXSY2', 'BPXSY3'], axis=1)
    return data

def new_indhhin2(data):
    """create new binary variable INDHHIN2_new to replace the problematic coding of original INDHHIN2. Code income below $20,000 to 1 and income over $20,000 to 2"""
    data.loc[((data.INDHHIN2 > 0) & (data.INDHHIN2 < 5)), 'INDHHIN2_new'] = 1
    data.loc[(data.INDHHIN2 == 13), 'INDHHIN2_new'] = 1
    data.loc[((data.INDHHIN2 > 4) & (data.INDHHIN2 < 11)), 'INDHHIN2_new'] = 2
    data.loc[((data.INDHHIN2 == 12) | (data.INDHHIN2 == 14) | (data.INDHHIN2 == 15)), 'INDHHIN2_new'] = 2
    data = data.drop('INDHHIN2', axis=1)
    return data

def create_binaries(data):
    """Creates dataframe where selected variables are turned into binaries. In NHANES, generally goes from (1,2) to (0,1)"""
    lb = LabelBinarizer()
    variables_to_convert = ['PAQ650', 'PAQ665', 'RIAGENDR', 'INDHHIN2_new']
    dummy_dict = {}
    for variable in variables_to_convert:
        lb.fit(data[variable])
        dummy_dict[variable] = lb.fit_transform(data[variable])
        data[variable] = dummy_dict[variable]
    return data

def create_dummies(data):
    """Creates dataframe where selected variables are turned into dummies"""
    variables_to_convert = ['RIDRETH3', 'DMDEDUC2', 'DBQ700']
    list_of_dummies = []
    for variable in variables_to_convert:
        dummies = pd.get_dummies(data[variable], prefix=variable, drop_first=True)
        list_of_dummies.append(dummies)
    data = data.drop(variables_to_convert, axis=1)
    dummies_df = pd.concat(list_of_dummies, axis=1)
    data = pd.concat([data, dummies_df], axis=1)
    return data

def fasting_glucose_categories_binary(data):
    """create 2 categories for y variable--fasting glucose"""
    data.loc[((data.LBXGLU > 0) & (data.LBXGLU < 100)), 'GLU'] = 0
    data.loc[(data.LBXGLU >= 100), 'GLU'] = 1
    data = data.drop('LBXGLU', axis=1)
    return data

def fasting_glucose_categories_binary_2(data):
    """create 2 categories for y variable--fasting glucose"""
    data.loc[((data.LBXGLU > 0) & (data.LBXGLU < 126)), 'GLU'] = 0
    data.loc[(data.LBXGLU >= 126), 'GLU'] = 1
    data = data.drop('LBXGLU', axis=1)
    return data

def fasting_glucose_categories(data):
    """create 3 categories for y variable--fasting glucose"""
    data.loc[((data.LBXGLU > 0) & (data.LBXGLU < 100)), 'GLU'] = 0
    data.loc[((data.LBXGLU >= 100) & (data.LBXGLU <= 125)), 'GLU'] = 1
    data.loc[((data.LBXGLU > 125)), 'GLU'] = 2
    data = data.drop('LBXGLU', axis=1)
    return data

def remove_outliers(data):
    """remove outliers based on IQR"""
    numeric_variables = ['BPXSY', 'BPXDI', 'BMXBMI', 'GLU', 'LBDINSI', 'PAD680']
    data_no_outliers = data[['BPXSY', 'BPXDI', 'BMXBMI', 'GLU', 'LBDINSI', 'PAD680']]
    Q1 = data_no_outliers.quantile(0.25)
    Q3 = data_no_outliers.quantile(0.75)
    IQR = Q3 - Q1
    data_no_outliers = data_no_outliers[~((data < (Q1 - 1.5 * IQR)) |(data_no_outliers > (Q3 + 1.5 * IQR))).any(axis=1)]
    data[['BPXSY', 'BPXDI', 'BMXBMI', 'GLU', 'LBDINSI', 'PAD680']] = data_no_outliers
    data = data.dropna()
    return data