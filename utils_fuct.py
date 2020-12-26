from import_modules import *
from config_file import *


def util_fct_1(filename):
    df = pd.read_csv(os.path.join(data_path, filename))
    df.columns = df.columns.str.strip()
    return df


def get_cat_count(df):
    rm_cols = []
    for col in df.columns:
        if df[col].nunique() < 20 and df[col].nunique() > 1:
            print(col, "............")
            print(df[col].unique())
        else:
            rm_cols.append(col)
    return np.array(rm_cols)


funct = lambda x: "-".join(str(x).split(" ")[0].split("-")[1:])


def select_date_range(df, date_column="", start_date=None, end_date=None):
    return df.set_index(date_column)[start_date:end_date].reset_index()
