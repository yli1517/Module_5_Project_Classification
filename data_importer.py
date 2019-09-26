import pandas as pd

def set_index(df_selected):
    """For the NHANES study, participants are given a 'Sequence Number'.
    This function sets the index of disparate datasets as the 'SEQN' in anticipation of a DataFrame join."""

    df_selected = df_selected.set_index('SEQN')
    return df_selected

def data_import(path, import_dict):
    """Imports a NHANES dataset using a pre-specified dictionary to guide the process."""
    dataset = pd.read_sas(path)
    variables_of_interest = []

    for variable in import_dict:
        if import_dict[variable]['Import'] == True:
            variables_of_interest.append(variable)

    selected = dataset[variables_of_interest]
    selected = set_index(selected)

    return selected


def data_complier(import_info):
    """Compiles disparate NHANES datasets into a single dataframe"""
    dataframes = []
    for dataset in import_info:
        dataframe = data_import(import_info[dataset]['path'],import_info[dataset]['map'])
        dataframes.append(dataframe)
    compiled_raw_data = dataframes[0].join(dataframes[1:])
    return compiled_raw_data


def variables_to_be_imported(import_info):
    """Useful code for listing which variables in the pre-specified dictionary are slated for import versus exclusion."""
    included_variables = []
    excluded_variables = []
    for dataset in import_info:
        for variable in import_info[dataset]['map']:
            if import_info[dataset]['map'][variable]['Import'] == True:
                included_variables.append(import_info[dataset]['map'][variable]['Label'])
            else:
                excluded_variables.append(import_info[dataset]['map'][variable]['Label'])

    print("*** Included Variables: {} ***".format(str(len(included_variables))))
    print(included_variables)
    print("\n*** Excluded Variables: {} ***".format(str(len(excluded_variables))))
    print(excluded_variables)
    print("\n*** Note: modify import status of individual variables directly in .py file. ***")

    return included_variables, excluded_variables