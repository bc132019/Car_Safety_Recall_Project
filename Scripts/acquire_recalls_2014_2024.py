import requests
import requests, json, time
from pathlib import Path

# Directories
RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = RAW_DIR / "recalls_2014_2024.json"

# APIs
VPIC_BASE = "https://vpic.nhtsa.dot.gov/api/vehicles"
RECALLS_BASE = "https://api.nhtsa.gov/recalls/recallsByVehicle"

# Makes of interest
MAKES = ["ford", "chevrolet", "chrysler", "toyota", "honda", "hyundai"]
YEARS = range(2014, 2025)


def get_models_for_make_year(make, year):
    """Use vPIC to get all models for a given make + year."""
    url = f"{VPIC_BASE}/GetModelsForMakeYear/make/{make}/modelyear/{year}"
    resp = requests.get(url, params={"format": "json"})
    resp.raise_for_status()
    return resp.json().get("Results", [])


from requests.exceptions import HTTPError

def get_recalls(make, model, year):
    """Get recall data for a given make-model-year from NHTSA."""
    params = {"make": make, "model": model, "modelYear": year}
    try:
        resp = requests.get(RECALLS_BASE, params=params)
        resp.raise_for_status()
    except HTTPError as e:
        print(f"    Skipping {make} {model} {year} because of error: {e}")
        return []

    data = resp.json()
    return data.get("results") or data.get("Results") or []


def main():
    all_recalls = []

    for make in MAKES:
        print(f"\n=== Processing {make.upper()} ===")
        for year in YEARS:
            print(f"Getting models for {make} {year}...")
            models = get_models_for_make_year(make, year)
            model_names = {m["Model_Name"] for m in models if m.get("Model_Name")}

            for model in model_names:
                print(f"  Fetching recalls for {make} {model} {year}...")
                recalls = get_recalls(make, model, year)

                for rec in recalls:
                    rec["Make"] = make
                    rec["Model"] = model
                    rec["ModelYear"] = year

                all_recalls.extend(recalls)
                time.sleep(0.2)

    print(f"\nCollected {len(all_recalls)} recall records.")

    OUTPUT_FILE.write_text(json.dumps(all_recalls, indent=2))
    print(f"Saved raw recall data to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
