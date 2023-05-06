import pandas as pd


def load_qqd_data(csv_path: str, sep: str = '\t'):
    assert csv_path != None
    
    df = pd.read_csv(csv_path, sep=sep)
    df.dropna(inplace=True, axis=0)
    df.drop(['id', 'qid1', 'qid2'], axis=1, inplace=True)
    return df


def load_sts17_data(csv_path: str, sep='\t', thresold=3):
    assert csv_path != None
    
    df = pd.read_csv(csv_path, on_bad_lines='skip', sep=sep, engine='python', header=None)
    df.dropna(inplace=True)
    df.drop([0,1,2,3], inplace=True, axis=1)
    df.rename(columns={4:'is_duplicate', 5:'question1', 6:'question2'}, inplace=True)
    
    df['is_duplicate'][df['is_duplicate'] <= thresold] = 1
    df['is_duplicate'][df['is_duplicate'] > thresold] = 0
    
    return df

