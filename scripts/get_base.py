import json
import pandas as pd
with open("data/data.json", encoding="utf-8") as f:
    raw = json.load(f)
df = pd.DataFrame([
    {"nivel_m": float(nivel.removesuffix("m").replace("_", ".")), "bairro": bairro, **valores}
    for nivel, bairros in raw.items()
    for bairro, valores in bairros.items()
    ])
print(df.shape) # deve dar (6674, 7)