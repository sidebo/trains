import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import json

NROWS = None #100
MAX_MINUTES_DELAY = 10
YEARS_FROM = 2017

def load_data():
    data = json.load(open('data.json', 'rb'))
    return data

def preprocess(data: dict, nrows=None) -> pd.DataFrame:
    row_data = data["Rows"]
    nrows = nrows or len(row_data)
    df = pd.concat([pd.json_normalize(row["Cell"]).transpose().loc[["Value"]] for row in row_data[:nrows]], axis=0)
    df.columns = ["year", "hour", "punctuality_level", "value"]
    df["year"] = df["year"].astype(int)
    df["value"] = df["value"].map(lambda v: v.replace(",", ".")).astype(float)
    df["max_minutes_delay"] = None
    mask_on_time = df["punctuality_level"] == "Ankomna enligt tidtabell"
    df.loc[mask_on_time, "max_minutes_delay"] = 0
    df.loc[~mask_on_time, "max_minutes_delay"] = df.loc[~mask_on_time, "punctuality_level"].map(lambda pl: int(re.findall(r"\d{1,2}", pl)[0])) 
    df = df[["year", "hour", "max_minutes_delay", "value"]]
    df = df.reset_index(drop=True)
    return df

data = load_data()
df = preprocess(data, nrows=NROWS)
df = df[df["year"] >= YEARS_FROM]
print(df)


sns.lineplot(data=df[df["max_minutes_delay"]==MAX_MINUTES_DELAY], 
             x="year", y="value", hue="hour", marker="o").set(
                title=f"Sammanvägt tillförlitlighetsmått (STM), max {MAX_MINUTES_DELAY:2d} minuter försening",
                xlabel="År",
                ylabel="STM"
             )
plt.legend(loc='upper left', title="Ankomsttimme")
plt.show()


