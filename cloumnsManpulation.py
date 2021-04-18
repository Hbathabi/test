import csv
import pandas as pd


# method  replace
def replacTarget(target, fileName):
    df = pd.read_csv(fileName)
    for col in df.columns:
        if (col.endswith(target)):
            targetColumn = col[:(-1)*len(target)]
            newName = df[col][0]
            df = df.rename(columns={targetColumn: newName})
            del df[col]
    df.to_csv(fileName, index=False)

# method delete
def deleteTarget(delete, fileName):
    df = pd.read_csv(fileName)
    for col in df.columns:
        
        if (col.startswith('agent')):
            del df[col]
        # elif ("time" in col.lower() and col.lower() != "endTime".lower()):
        #     del df[col]
        elif (col.lower() in delete):
            del df[col]
    df.to_csv(fileName, index=False)
