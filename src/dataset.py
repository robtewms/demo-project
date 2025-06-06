import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [24, 27, 22, 32],
    "city": ["new york", "los angeles", "chicago", "houston"],
}

df = pd.DataFrame(data)
print(df.head(2))
