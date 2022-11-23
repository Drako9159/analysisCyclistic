import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


results = pd.read_csv("./csv/survey_results_public.csv", index_col="ResponseId")
resultsSchema = pd.read_csv("./csv/survey_results_schema.csv")


print(results.head(15))
