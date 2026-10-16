"""Run this file from the project folder to display the example KPIs."""

from kpi.warehouse import capacity_utilization, picking_accuracy, throughput


def main():
    print("Throughput:", throughput(60, 2), "units/hour")
    print("Capacity utilization:", capacity_utilization(18, 24), "%")
    print("Picking accuracy:", picking_accuracy(95, 100), "%")


if __name__ == "__main__":
    main()
