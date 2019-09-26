def adults_only(unclean_data):
    """Only consider adults >= 20 years old. Since kids and youth their body are still growing, so their hormone level tends to fluctuate, which may lead to biased data"""
    clean_data = unclean_data.loc[unclean_data['RIDAGEYR'] >= 20]
    observations_removed = len(unclean_data) - len(clean_data)
    print("{} observations removed because age of participant is twenty or less.".format(observations_removed))
    print("{} observations remaining.".format(len(clean_data)))
    return clean_data


def remove_nonresponse_codes(unclean_data):
    """This function removes 'non-response' or 'refuse to response' values"""
    unclean_data_length = len(unclean_data)
    coding_map = {'single_digit' : {
                        'variables' : ['DMDEDUC2', 'DBQ700', 'PAQ650', 'PAQ665'],
                        'codes' : (7, 9)
                                    },
                  'four_digit' : {
                        'variables' : ['PAD680'],
                        'codes' : (7777, 9999)
                                    },
                    }
    for code_length in coding_map:
        for variable in coding_map[code_length]['variables']:
            unclean_data = unclean_data.loc[(unclean_data[variable] != coding_map[code_length]['codes'][0]) & (unclean_data[variable] != coding_map[code_length]['codes'][1])]
    clean_data = unclean_data
    observations_removed = unclean_data_length - len(clean_data)
    print("{} observations removed because data was coded as respondent 'refused to answer' or 'don't know'.".format(observations_removed))
    print("{} observations remaining.".format(len(clean_data)))
    return clean_data


def remove_missing(unclean_data):
    """Remove all missing values"""
    unclean_data_length = len(unclean_data)
    variables_to_clean = ['INDHHIN2_new', 'BPXSY', 'BMXBMI', 'PAQ650', 'PAQ665', 'PAD680', 'LBXGLU', 'LBDINSI']
    for variable in variables_to_clean:
        unclean_data = unclean_data[unclean_data[variable].isna() == False]
    clean_data = unclean_data
    observations_removed = unclean_data_length - len(clean_data)
    print("{} observations removed because data was missing.".format(observations_removed))
    print("{} observations remaining.".format(len(clean_data)))
    return clean_data

def data_full_cleaner(unclean_data):
    """Runs the entirety of the library's data cleaning functions on the unclean NHANES data, like a metaphorical premium car wash option of data."""
    somewhat_cleaner_data = adults_only(unclean_data)
    even_cleaner_data = remove_nonresponse_codes(somewhat_cleaner_data)
    clean_data = remove_missing(even_cleaner_data)
    return clean_data
