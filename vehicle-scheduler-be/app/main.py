from app.api import get_depots, get_vehicles
from app.scheduler import schedule_tasks


def main():
    depots = get_depots()["depots"]
    vehicles = get_vehicles()["vehicles"]

    for depot in depots:
        print("=" * 50)
        print(f"Depot ID : {depot['ID']}")
        print(f"Mechanic Hours : {depot['MechanicHours']}")

        selected, hours, impact = schedule_tasks(
            vehicles,
            depot["MechanicHours"]
        )

        print(f"Hours Used : {hours}")
        print(f"Total Impact : {impact}")

        print("\nSelected Vehicles:")

        for task in selected:
            print(
                task["TaskID"],
                "| Duration:",
                task["Duration"],
                "| Impact:",
                task["Impact"]
            )


if __name__ == "__main__":
    main()