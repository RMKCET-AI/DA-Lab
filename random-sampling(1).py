"""
1 . Implement Random sampling using python libraries and create your own population for
student details with S_ID, S_NAME, AGE, DEPT, YEAR using the dictionary.
"""

import pandas as pd

data = {
    'S_ID': [1, 2, 3, 4],
    'S_NAME': ['Hasher', 'Miner', 'Thunder', 'Harsha'],
    'AGE': [18, 19, 20, 21],
    'DEPT': ['AI', 'CSE', 'BC', 'CS'],
    'YEAR': [2021, 2022, 2023, 2024]
}

pd_dataframe = pd.DataFrame.from_dict(data)

sample_dataframe = pd_dataframe.sample(2)

print(sample_dataframe)

