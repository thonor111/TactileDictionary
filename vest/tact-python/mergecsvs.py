import pandas as pd
import numpy as np


columns = ['ParticipantNumber', 'TrialNumber', 'ActualLocation', 'GuessedLocations', 'LocationCorrect',
       'ActualCategory', 'GuessedCategory', 'CategoryCorrect']

data = None

for i in range(13):
    df_no_vest = pd.read_csv(f'data/trial{i+1}noVest.csv')
    df_vest = pd.read_csv(f'data/trial{i + 1}Vest.csv')
    df_no_vest.insert(0, "ParticipantNumber", ([i] * df_no_vest.shape[0]), True)
    df_vest.insert(0, "ParticipantNumber", ([i] * df_vest.shape[0]), True)
    df_no_vest.insert(1, "Vest", ([False] * df_no_vest.shape[0]), True)
    df_vest.insert(1, "Vest", ([True] * df_vest.shape[0]), True)
    if i == 0:
        data = pd.concat([df_vest, df_no_vest])
    else:
        data = pd.concat([data, df_vest, df_no_vest])
    print(data.shape)
data.to_csv("Category_Guesses.csv", index=False)