import os
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

import numpy as np
import pandas as pd
from dotenv import load_dotenv

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

from langchain_dartmouth.llms import DartmouthLLM, ChatDartmouth

svm_df = pd.read_csv("data/cleaned_merged_seasons.csv")