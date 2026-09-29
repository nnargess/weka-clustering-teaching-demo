"""Optional Python comparison of standardised k-means cluster profiles."""
from pathlib import Path
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

DATA = Path(__file__).parent / "data" / "crop_fields_synthetic.csv"

def main():
    frame = pd.read_csv(DATA)
    features = frame.drop(columns=["field_id"])
    scaled = StandardScaler().fit_transform(features)
    model = KMeans(n_clusters=3, random_state=2026, n_init=10)
    frame["cluster"] = model.fit_predict(scaled)
    print("Cluster sizes:")
    print(frame.groupby("cluster").size().to_string())
    print("\nCentroids in original measurement units:")
    print(frame.groupby("cluster")[features.columns].mean().round(2).to_string())
    print("\nWithin-cluster sum of squares (standardised scale):", round(model.inertia_, 2))

if __name__ == "__main__":
    main()
