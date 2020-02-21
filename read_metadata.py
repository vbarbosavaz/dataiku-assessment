import re
import numpy as np
import pandas as pd

file = 'data/census_income_metadata.txt'

def top():
    """
    Parse top of file.
    """
    metadata = []
    with open(file, 'r') as filehandle:
        filecontent = filehandle.readlines()

        for cursor,line in enumerate(filecontent):
            if cursor > 22 and cursor < 68:
                splitted = re.split(r'\t+', line.lstrip("| ").rstrip('\n'))
                
                feature = splitted[0]
                unique_values = splitted[1]
                metadata.append([feature, unique_values])
        
        cols = np.array(metadata)
        print('Shape: {}'.format(cols.shape))
    
    df = pd.DataFrame(cols, columns=['feature', 'code'])

    return df

def middle():
    """
    Parse middle of file.
    """
    metadata = []
    with open(file, 'r') as filehandle:
        filecontent = filehandle.readlines()

        for cursor,line in enumerate(filecontent):
            if cursor > 80 and cursor < 121:
                values = int(re.split(r' ', line.lstrip("| ").rstrip('\n'))[0])
                feature = line[line.find("(")+1:line.find(")")]
                
                metadata.append([feature, values])
        cols = np.array(metadata)
        print('Shape: {}'.format(cols.shape))
        
        df = pd.DataFrame(cols, columns=['feature', 'nunique'])
        
    return df

def bottom():
    """
    Parse bottom of file.
    """
    metadata = []
    with open(file, 'r') as filehandle:
        filecontent = filehandle.readlines()

        for cursor,line in enumerate(filecontent):
            if cursor > 141:
                splitted = line.lstrip("| ").rstrip('\n').split(":", 1)
                
                feature = splitted[0]
                unique_values = [x.strip() for x in splitted[1].rstrip('.').split(",")]
                if "ignore" not in splitted[1]:
                    metadata.append([feature, unique_values])
        cols = np.array(metadata)
        print('Shape: {}'.format(cols.shape))
        
    df = pd.DataFrame(cols, columns=['feature', 'unique values'])

    return df

if __name__ == '__main__':
    print("Metadata reader module")