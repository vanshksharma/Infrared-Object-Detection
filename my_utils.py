import pandas as pd
import os
import shutil

def open_file(filename: str,label_dir:str) ->pd.DataFrame:
    
    full_path=os.path.join(label_dir,filename)
    df=pd.read_csv(full_path,delimiter="\t",names=["image_id","Track","classes","x","y","w","h"])
    return df


def reshape_dataframe(df:pd.DataFrame) ->pd.DataFrame:
    
    df["x_center"]=(df['x']+df['w'])/2
    df['y_center']=(df['y']+df['h'])/2
    return df[['image_id','x','y','w','h','x_center','y_center','classes']]
    
    
def get_name(full_name:str)->int:
    
    return int(full_name.split(".")[0])

def rename_label(old_name:int, new_name:int, df:pd.DataFrame) ->pd.DataFrame:
    
    df["image_id"].replace(old_name,new_name,inplace=True)


def combine_labels(parent:pd.DataFrame,child=pd.DataFrame)->pd.DataFrame:
    
    return pd.concat([parent,child],ignore_index=True)

def move_and_rename_image(old_name:str,new_name:str) ->None:
    
    shutil.copy(old_name,new_name)
    
def files_to_int(files:list) ->list:
    
    return sorted(list(map(lambda x: int(x.split(".")[0]),files)))

def get_file_name(im_id:int,seq_num:int,extension: dict) ->str:
    
    return "0"*(6-len(str(im_id)))+str(im_id)+extension[seq_num]

def seq_to_int(sequences:list) ->int:
    
    return sorted(list(map(lambda x: int(x.split("-")[1]),sequences)))