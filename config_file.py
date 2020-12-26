from import_modules import *

if os.path.exists("/remote_parent_path/"):  # if I am working on remote server
    data_path = "/remote_parent_path/data"
    src_path = "/remote_parent_path/src/"
    output_path = "/remote_parent_path/output/"

    # Optional: I have list of function I use from my past Kaggle competition

    # kaggle_path = "/remote_parent_path_Kaggle/Kaggle_API"
else:  # if I am working on local machine
    data_path = "/local_parent_path/data"
    src_path = "/local_parent_path/src"
    output_path = "/local_parent_path/output/"
    # kaggle_path = "/path_to/Kaggle/Kaggle_API/"


sys.path.insert(
    0, kaggle_path
)  # keep always config_file called before setting kaggle_api path
from handy_kaggle import *
