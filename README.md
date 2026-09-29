# WEKA clustering teaching demonstration

A small, reproducible classroom example for explaining k-means clustering to students beginning data analytics. The crop-field measurements are **synthetic** and do not represent real farms or research findings.

## What the project demonstrates

- Prepare a CSV dataset for WEKA Explorer.
- Load the data in WEKA, select `Cluster`, then choose `SimpleKMeans`.
- Set `numClusters` to 3, run the model, and inspect cluster centroids and assignments.
- Visualise clusters by rainfall and yield while explaining that clustering uses **all selected attributes**, not just the two plotted axes.
- Discuss feature scale and why standardising inputs can change Euclidean-distance results.

## Files

- `data/crop_fields_synthetic.csv`: generated example data with 60 fields and eight numeric measurements.
- `generate_data.py`: deterministic generation of the synthetic CSV.
- `analysis.py`: optional Python comparison using scikit-learn. It standardises features and fits k-means with a fixed random seed.
- `requirements.txt`: Python dependencies for the optional analysis.

## WEKA classroom walkthrough

1. Open WEKA Explorer > Preprocess > Open file and choose the CSV.
2. Inspect the eight measurement columns. `field_id` is only an identifier: remove it before clustering.
3. For a scale-sensitive comparison, use the `Standardize` filter on the measurements before clustering. Keep a copy of the unstandardised data to discuss the difference.
4. In Cluster, choose `SimpleKMeans`, click its name, and set `numClusters` to `3`.
5. Choose `Use training set`, then click `Start`. The result list appears in the lower-left panel.
6. Right-click the result and choose `Visualize cluster assignments`. Select rainfall for X and yield for Y. Colours show the groups obtained from all eight input measurements.
7. Examine the centroids in the text output. These are the mean attribute values of the fields currently assigned to each cluster; they update until assignments stabilise.

**Teaching note:** The numerical cluster labels have no inherent meaning. Interpret clusters using centroid profiles. K-means does not guarantee that clusters are distinctly separated in a two-dimensional plot.

## Separate WEKA analysis supplied by the author (41,592 records)

The following results come from a **different crop dataset** supplied for analysis. That dataset is **not included** in this repository; The 60-record synthetic dataset does not reproduce this separate 41,592-record analysis. Its original source, licence and any preprocessing performed before import should be documented before the dataset or its screenshots are published.

**Method.** WEKA `SimpleKMeans` was run on the training set with `numClusters = 3`, Euclidean distance, a maximum of 500 iterations and random seed 10. The run contained 41,592 records and eight attributes: soil type, rainfall, temperature, fertiliser use, irrigation use, weather condition, days to harvest and yield. WEKA reported that missing values were globally replaced with the mean or mode. The model took 14 iterations; within-cluster sum of squared errors was 78,522.992 (in WEKA's distance calculation). This is a descriptive clustering result, not a predictive test on unseen data.

| Cluster | Records | Share | Rainfall centroid (mm) | Yield centroid (t/ha) | Modal soil | Modal fertiliser | Modal irrigation | Modal weather |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| 0 | 15,540 | 37% | 560.86 | 4.00 | Clay | No | No | Cloudy |
| 1 | 10,736 | 26% | 449.98 | 3.88 | Chalky | No | Yes | Sunny |
| 2 | 15,316 | 37% | 609.59 | 5.84 | Peaty | Yes | Yes | Sunny |

**Interpretation.** Cluster 2 has the highest average rainfall and yield, while cluster 1 has the lowest averages for both. Cluster 0 lies between them for rainfall and yield. For numeric attributes, a centroid reports a mean; for categorical attributes, WEKA displays a modal category. These profiles describe groups in this dataset. They do not establish that fertiliser, irrigation, soil or rainfall caused differences in yield. Yield itself was included as a clustering attribute, so the yield differences are part of how the groups were formed.

The dataset source and preprocessing history are not yet documented here. Cluster labels are arbitrary, and changing the selected attributes, scaling, seed or number of clusters can change the result. Do not use the 60-record synthetic plot above as a visualisation of this separate 41,592-record run.

## Optional Python run

```bash
python -m pip install -r requirements.txt
python generate_data.py
python analysis.py
```

Python and WEKA can yield different assignments because preprocessing, initialisation, distance settings and random seeds may differ. Compare the method and interpretation rather than expecting identical cluster numbers.

## Portfolio context

Prepared as a teaching demonstration for introductory Big Data and machine-learning concepts. This repository does not claim an original research dataset, clinical data, bioinformatics workflow, or production deployment.
