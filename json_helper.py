import json
import os
import pandas as pd

def json_to_df(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        df = pd.DataFrame(data['results'])
        return df
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return pd.DataFrame()

def read_all_json(file_path):
    json_files = pd.DataFrame()
    for files in os.listdir(file_path):
        full_path = os.path.join(file_path, files)

        try:
            with open(full_path, 'r') as file:
                data = json.load(file)
            json_df = pd.DataFrame(data['results'])
            json_df['source'] = files
            json_files = pd.concat([json_files, json_df], ignore_index=True)
        except Exception as e:
            print(f"Error reading {full_path}: {e}")
    return json_files