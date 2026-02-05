import csv
import json
from collections import Counter, defaultdict

# CSV indexes
IDX_REVIEW_ID = 0
IDX_RATING = 1
IDX_YEAR_MONTH = 2
IDX_LOCATION = 3
IDX_BRANCH = 4


def load_data(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if row:
                rows.append(row)

    print("\n[System] Dataset loaded successfully.")
    print(f"[System] Total rows loaded: {len(rows)}")
    return header, rows


def choose_park():
    while True:
        print("\n1. Disneyland Hong Kong\n2. Disneyland California\n3. Disneyland Paris")
        c = input("Enter 1-3: ").strip()
        return {
            "1": "Disneyland_HongKong",
            "2": "Disneyland_California",
            "3": "Disneyland_Paris"
        }.get(c)


def view_all_reviews_for_park(dataset):
    park = choose_park()
    for r in dataset:
        if r[IDX_BRANCH] == park:
            print(r)


def number_of_reviews_for_park_from_location(dataset):
    park = choose_park()
    loc = input("Enter reviewer location: ").lower()
    count = sum(
        1 for r in dataset
        if r[IDX_BRANCH] == park and loc in r[IDX_LOCATION].lower()
    )
    print(f"\nNumber of reviews: {count}")


def average_rating_for_park_in_year(dataset):
    park = choose_park()
    year = input("Enter year: ")
    ratings = [
        int(r[IDX_RATING]) for r in dataset
        if r[IDX_BRANCH] == park and r[IDX_YEAR_MONTH].startswith(year)
    ]
    if ratings:
        print(f"Average: {sum(ratings)/len(ratings):.2f}")
    else:
        print("No data found.")


def average_score_per_park_by_reviewer_location(dataset):
    data = defaultdict(lambda: defaultdict(list))
    for r in dataset:
        data[r[IDX_BRANCH]][r[IDX_LOCATION]].append(int(r[IDX_RATING]))

    for park, locs in data.items():
        print(f"\n{park}")
        for loc, ratings in locs.items():
            print(f"{loc}: {sum(ratings)/len(ratings):.2f}")


def most_reviewed_parks(dataset):
    c = Counter(r[IDX_BRANCH] for r in dataset)
    for park, n in c.most_common():
        print(f"{park}: {n}")


def park_ranking_by_nationality(dataset):
    loc = input("Enter reviewer location: ").lower()
    totals = defaultdict(list)

    for r in dataset:
        if loc in r[IDX_LOCATION].lower():
            totals[r[IDX_BRANCH]].append(int(r[IDX_RATING]))

    for park, ratings in sorted(
        totals.items(),
        key=lambda x: sum(x[1])/len(x[1]),
        reverse=True
    ):
        print(f"{park}: {sum(ratings)/len(ratings):.2f}")


def most_popular_month_by_park(dataset):
    park = choose_park()
    c = Counter(
        r[IDX_YEAR_MONTH] for r in dataset if r[IDX_BRANCH] == park
    )
    for ym, n in c.most_common():
        print(f"{ym}: {n}")


class ParkDataExporter:
    def __init__(self, dataset):
        self.dataset = dataset

    def build(self):
        data = defaultdict(lambda: {"sum": 0, "count": 0, "locs": set()})
        for r in self.dataset:
            d = data[r[IDX_BRANCH]]
            d["sum"] += int(r[IDX_RATING])
            d["count"] += 1
            d["locs"].add(r[IDX_LOCATION])

        return [
            {
                "park": k,
                "avg": round(v["sum"]/v["count"], 2),
                "reviews": v["count"],
                "countries": len(v["locs"])
            }
            for k, v in data.items()
        ]

    def export_txt(self, path):
        for d in self.build():
            with open(path, "w") as f:
                f.write(str(d))

    def export_csv(self, path):
        with open(path, "w", newline="") as f:
            w = csv.DictWriter(f, self.build()[0].keys())
            w.writeheader()
            w.writerows(self.build())

    def export_json(self, path):
        with open(path, "w") as f:
            json.dump(self.build(), f, indent=2)
