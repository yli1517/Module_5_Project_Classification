import_info = {'demographics' : {
                    # accessible at: https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Demographics&CycleBeginYear=2015
                    'path' : "data/DEMO_I.xpt",
                    'map' : {
                        'SEQN': {
                            'Import' : True ,
                            'Label' : 'Respondent sequence number'
                                },
                        'SDDSRVYR' : {
                            'Import' : False ,
                            'Label' : 'Data release cycle'
                                },
                        'RIAGENDR' : {
                            'Import' : True ,
                            'Label' : 'Gender'
                                },
                        'RIDAGEYR' : {
                            'Import' : True ,
                            'Label' : 'Age'
                                },
                        'RIDRETH3' : {
                            'Import' : True ,
                            'Label' : 'Race'
                                },
                        'DMDEDUC2' : {
                            'Import' : True ,
                            'Label' : 'Education'
                                },
                        'INDHHIN2' : {
                            'Import' : True ,
                            'Label' : 'Annual household income'
                        }}},

              'blood_pressure' : {
                  #accessible at: https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BPX_I.htm
                    'path' : "data/BPX_I.xpt",
                    'map' : {
                        'SEQN': {
                            'Import' : True ,
                            'Label' : 'Respondent sequence number'
                                },
                        'BPXSY1' : {
                            'Import' : True ,
                            'Label' : 'Systolic Blood Pressure (mm Hg) 1st time'
                                },
                        'BPXDI1' : {
                            'Import' : True ,
                            'Label' : 'Diastolic Blood Pressure (mm Hg) 1st time'
                                },
                        'BPXSY2' : {
                            'Import' : True ,
                            'Label' : 'Systolic Blood Pressure (mm Hg) 2nd time'
                                },
                        'BPXDI2' : {
                            'Import' : True ,
                            'Label' : 'Diastolic Blood Pressure (mm Hg) 2nd time'
                                },
                        'BPXSY3' : {
                            'Import' : True ,
                            'Label' : 'Systolic Blood Pressure (mm Hg) 3rd time'
                                },
                        'BPXDI3' : {
                            'Import' : True ,
                            'Label' : 'Diastolic Blood Pressure (mm Hg) 3rd time'
                        }}},

                'body_measure' : {
                  #accessible at: https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/BMX_I.htm
                    'path' : "data/BMX_I.xpt",
                    'map' : {
                        'SEQN': {
                            'Import' : True ,
                            'Label' : 'Respondent sequence number'
                                },
                        'BMXWAIST': {
                            'Import' : False ,
                            'Label' : 'Respondent waist circumference'
                                },
                        'BMXBMI' : {
                            'Import' : True ,
                            'Label' : 'BMI'
                        }}},

               'insulin' : {
                  #accessible at: https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/INS_I.htm
                    'path' : "data/INS_I.xpt",
                    'map' : {
                        'SEQN': {
                            'Import' : True ,
                            'Label' : 'Respondent sequence number'
                                },
                        'LBDINSI': {
                            'Import' : True ,
                            'Label' : 'Insulin (pmol/L)'
                        }}},
               
                'glucose' : {
                  #accessible at: https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/GLU_I.htm
                    'path' : "data/GLU_I.xpt",
                    'map' : {
                        'SEQN': {
                            'Import' : True ,
                            'Label' : 'Respondent sequence number'
                                },
                        'LBXGLU': {
                            'Import' : True ,
                            'Label' : 'Fasting glucose level (mg/dL)'
                        }}},

               'diet' : {
                  #accessible at: https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/DBQ_I.htm
                    'path' : "data/DBQ_I.xpt",
                    'map' : {
                        'SEQN': {
                            'Import' : True ,
                            'Label' : 'Respondent sequence number'
                                },
                        'DBQ700' : {
                            'Import' : True ,
                            'Label' : 'Healthy of the diet'
                        }}},

                'physical_activity' : {
                  #accessible at: https://wwwn.cdc.gov/Nchs/Nhanes/2015-2016/PAQ_I.htm
                    'path' : "data/PAQ_I.xpt",
                    'map' : {
                        'SEQN': {
                            'Import' : True ,
                            'Label' : 'Respondent sequence number'
                                },
                        'PAQ650' : {
                            'Import' : True ,
                            'Label' : 'VIPA for at least 10 minutes continuously in a typical day'
                                },
                        'PAQ665' : {
                            'Import' : True ,
                            'Label' : 'MIPA for at least 10 minutes continuously in a typical day'
                                },
                        'PAD680' : {
                            'Import' : True ,
                            'Label' : 'Sedentary activity of a typical day (min)'
                        }}},
              }