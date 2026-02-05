from tui import (
    display_title,
    main_menu,
    submenu_view_data,
    submenu_visualise_data,
    submenu_export_format
)
from process import (
    load_data,
    view_all_reviews_for_park,
    number_of_reviews_for_park_from_location,
    average_rating_for_park_in_year,
    average_score_per_park_by_reviewer_location,
    most_reviewed_parks,
    park_ranking_by_nationality,
    most_popular_month_by_park
)
from process import ParkDataExporter


def main():
    display_title("Disneyland Review Analyser")

    path = "disneyland_reviews.csv"
    header, dataset = load_data(path)

    if not dataset:
        return

    while True:
        choice = main_menu()

        if choice == "A":
            sub = submenu_view_data()

            if sub == "A":
                view_all_reviews_for_park(dataset)
            elif sub == "B":
                number_of_reviews_for_park_from_location(dataset)
            elif sub == "C":
                average_rating_for_park_in_year(dataset)
            elif sub == "D":
                average_score_per_park_by_reviewer_location(dataset)

        elif choice == "B":
            sub = submenu_visualise_data()

            if sub == "A":
                most_reviewed_parks(dataset)
            elif sub == "B":
                park_ranking_by_nationality(dataset)
            elif sub == "C":
                most_popular_month_by_park(dataset)

        elif choice == "C":
            fmt = submenu_export_format()
            exporter = ParkDataExporter(dataset)

            if fmt == "A":
                exporter.export_txt("park_aggregates.txt")
                print("\n[System] Export complete: park_aggregates.txt")
            elif fmt == "B":
                exporter.export_csv("park_aggregates.csv")
                print("\n[System] Export complete: park_aggregates.csv")
            elif fmt == "C":
                exporter.export_json("park_aggregates.json")
                print("\n[System] Export complete: park_aggregates.json")

        elif choice == "X":
            print("\nExiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()
