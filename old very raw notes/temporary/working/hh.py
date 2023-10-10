"""
interesting tests using linting
"""
import pandas as pd

data = [['tom', 10], ["nik", 15], ["juli", 14]]
df = pd.DataFrame(data, columns=["Name", "Age"])
print(df)