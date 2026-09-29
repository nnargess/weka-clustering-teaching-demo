"""Generate synthetic crop field measurements for a classroom clustering exercise."""
import csv
import random
from pathlib import Path

OUTPUT = Path(__file__).parent / "data" / "crop_fields_synthetic.csv"
COLUMNS = ["field_id", "rainfall_mm", "yield_t_ha", "temperature_c", "soil_ph",
           "nitrogen_mg_kg", "irrigation_mm", "sunlight_hours", "organic_matter_pct"]
# Plausible teaching profiles only; these are not agronomic estimates.
PROFILES = [
    (420, 2.8, 27, 6.2, 32, 250, 1900, 2.1),
    (690, 5.1, 23, 6.8, 58, 170, 2050, 3.4),
    (890, 7.0, 20, 7.0, 78, 105, 2150, 4.2),
]
SPREAD = (75, .65, 2.0, .25, 9, 35, 115, .45)

def main():
    rng = random.Random(2026)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(COLUMNS)
        for i in range(60):
            profile = PROFILES[i % len(PROFILES)]
            values = [round(rng.gauss(mean, sd), 2) for mean, sd in zip(profile, SPREAD)]
            writer.writerow([f"F{i+1:03d}", *values])
    print(f"Wrote 60 synthetic records to {OUTPUT}")

if __name__ == "__main__":
    main()
