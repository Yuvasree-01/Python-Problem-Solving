import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    result = logins[logins["time_stamp"].dt.year == 2020]
    result= result.groupby("user_id")["time_stamp"].max().dropna().reset_index().rename(columns={"time_stamp":"last_stamp"})
    return result
