import pandas as pd

df = pd.read_csv("big-mac-full-index.csv").query("index < 20")
