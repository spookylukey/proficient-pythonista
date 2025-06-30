import csv

def read_spanners_csv(filename: str) -> list[dict], list[str]:
    valid_items = []
    errors = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not validate_spanner
            print(row['first_name'], row['last_name'])
