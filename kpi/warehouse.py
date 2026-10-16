"""Simple warehouse KPIs using fictional examples in the main program.

Inputs are numbers. Ratios return None for a negative numerator or a
non-positive denominator. For picking accuracy, assume correct_orders is no
greater than total_orders; both counts describe the same set of orders.
"""


def throughput(units, hours):
    """Return units per hour."""
    if units < 0 or hours <= 0:
        return None
    return units / hours


def capacity_utilization(actual_output, maximum_output):
    """Return actual output as a percentage of capacity for the same period."""
    if actual_output < 0 or maximum_output <= 0:
        return None
    return actual_output / maximum_output * 100


def picking_accuracy(correct_orders, total_orders):
    """Return the percentage of picked orders that are correct."""
    if correct_orders < 0 or total_orders <= 0:
        return None
    return correct_orders / total_orders * 100
