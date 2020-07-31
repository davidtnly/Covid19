import os
import pandas as pd

def merge_files():
    """
    Merge all files into a single data frame
    """

    # Move to directory with csv files to merge
    os.chdir("Merge")

    # Current directory
    merge_folder = os.getcwd()
    merge_files = os.listdir(merge_folder)

    unclean_df = pd.DataFrame()
    for file in merge_files:
        if file.endswith(".csv"):
            unclean_df = unclean_df.append(pd.read_csv(file), ignore_index=True)
            print(file, "has been merged.")

    return unclean_df

def clean_files(df):
    """
    Clean columns
    """

    df["replace_ps"] = df["Admin2"].fillna("1")
    df["Country_Region"] = df["Country_Region"].replace("Taiwan*", "Taiwan")
    df["cleaned_province_state"] = df["Admin2"] + ", " + df["Province_State"]
    df["cleaned_province_state"] = df["cleaned_province_state"].fillna(df["Province_State"], axis=0)
    df["cleaned_province_state"] = df["cleaned_province_state"].fillna(df["Country_Region"], axis=0)

    col_list = ["cleaned_province_state", "Country_Region", "Last_Update",
                "Confirmed", "Deaths", "Recovered", "cleaned_province_state",
                "Lat", "Long_"]

    cleaned_df = df[col_list]
    cleaned_df = cleaned_df.rename(columns={"cleaned_province_state": "Province_State",
                                            "Country_Region": "Country",
                                            "Last_Update": "Last_Update",
                                            "Confirmed": "Confirmed",
                                            "Deaths": "Deaths",
                                            # "cleaned_province_state": "Province_State",
                                            "Lat": "Lat",
                                            "Long_": "Lon"
                                            })

    cleaned_df["Last_Update"] = pd.to_datetime(cleaned_df["Last_Update"]).dt.date
    # cleaned_df["Province_State"] = cleaned_df["Province_State"].str.replace("*", "")

    return cleaned_df

def save_files(df, filename):
    """
    Save file to csv
    """
    # Go back to main directory
    os.chdir("..")

    df.to_csv(filename, index=False)

def run_all():
    """
    Run, Merge, & Save Final Output
    """

    # Run merge_files() and clean_files()
    unclean_df = merge_files()
    cleaned_df = clean_files(unclean_df)

    # Save file
    save_files(cleaned_df, "cleaned_dataset.csv")

if __name__ == "__main__":
    run_all()
