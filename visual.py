import matplotlib.pyplot as plt
from collections import Counter, defaultdict


IDX_RATING = 1
IDX_YEAR_MONTH = 2
IDX_LOCATION = 3
IDX_BRANCH = 4


def _safe_int(value):
    try:
        return int(value)
    except Exception:
        return None


def pie_reviews_by_park(dataset):
    """
    Section C - Task 10:
    Pie chart showing number of reviews each park has received.
    """
    counts = Counter()

    for row in dataset:
        park = row[IDX_BRANCH] if len(row) > IDX_BRANCH else ""
        if park:
            counts[park] += 1

    if not counts:
        print("[Visual] No data available for pie chart.")
        return

    labels = [p.replace("_", " ") for p in counts.keys()]
    sizes = list(counts.values())

    plt.figure()
    plt.title("Number of Reviews per Park")
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.show()


def bar_top10_locations_highest_avg(dataset, park):
    """
    Section C - Task 11:
    Ask user to enter a park (feito no main/process) and display a bar chart
    showing the top 10 locations that gave the HIGHEST average rating for that park.
    """
    totals = defaultdict(int)
    counts = defaultdict(int)

    for row in dataset:
        if len(row) <= IDX_BRANCH:
            continue
        if row[IDX_BRANCH] != park:
            continue

        loc = row[IDX_LOCATION] if len(row) > IDX_LOCATION else ""
        rating = _safe_int(row[IDX_RATING] if len(row) > IDX_RATING else None)

        if not loc or rating is None:
            continue

        totals[loc] += rating
        counts[loc] += 1

    if not counts:
        print("[Visual] No data found for this park.")
        return

    averages = [(loc, totals[loc] / counts[loc]) for loc in counts]
    averages.sort(key=lambda x: x[1], reverse=True)
    top10 = averages[:10]

    locations = [x[0] for x in top10]
    avg_scores = [x[1] for x in top10]

    plt.figure()
    plt.title(f"Top 10 Locations by Highest Average Rating\n({park.replace('_', ' ')})")
    plt.xlabel("Reviewer Location")
    plt.ylabel("Average Rating")
    plt.bar(locations, avg_scores)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def bar_avg_rating_by_month(dataset, park):
    """
    Section C - Task 12:
    Bar chart showing average rating for each MONTH of the year (ignore year).
    Months must be ordered by month.
    """
    # month number -> list of ratings
    month_ratings = defaultdict(list)

    for row in dataset:
        if len(row) <= IDX_BRANCH or row[IDX_BRANCH] != park:
            continue

        ym = row[IDX_YEAR_MONTH] if len(row) > IDX_YEAR_MONTH else ""
        rating = _safe_int(row[IDX_RATING] if len(row) > IDX_RATING else None)

        if rating is None or not ym:
            continue

        # Expect format like "2018-05" or "2018-5" (we handle both)
        # Extract month part after '-'
        if "-" in ym:
            parts = ym.split("-")
            if len(parts) >= 2 and parts[1].isdigit():
                month_num = int(parts[1])
            else:
                continue
        else:
            continue

        if 1 <= month_num <= 12:
            month_ratings[month_num].append(rating)

    if not month_ratings:
        print("[Visual] No month data found for this park.")
        return

    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    months = list(range(1, 13))
    averages = []
    for m in months:
        ratings = month_ratings.get(m, [])
        avg = sum(ratings) / len(ratings) if ratings else 0
        averages.append(avg)

    plt.figure()
    plt.title(f"Average Rating by Month (All Years)\n({park.replace('_', ' ')})")
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.bar(month_names, averages)
    plt.ylim(0, 5)
    plt.tight_layout()
    plt.show()

