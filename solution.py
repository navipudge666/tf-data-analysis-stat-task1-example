import pandas as pd
import numpy as np


chat_id = 475225606

def solution(x: np.array) -> float:
    return np.log(x-223).mean()
