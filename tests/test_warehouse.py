from kpi.warehouse import capacity_utilization, picking_accuracy, throughput


def test_example_values():
    assert throughput(60, 2) == 30
    assert capacity_utilization(18, 24) == 75
    assert picking_accuracy(95, 100) == 95


def test_zero_output():
    assert throughput(0, 2) == 0
    assert capacity_utilization(0, 24) == 0
    assert picking_accuracy(0, 100) == 0


def test_zero_denominators():
    assert throughput(60, 0) is None
    assert capacity_utilization(18, 0) is None
    assert picking_accuracy(95, 0) is None


def test_negative_values():
    assert throughput(-1, 2) is None
    assert throughput(1, -2) is None
    assert capacity_utilization(-1, 24) is None
    assert capacity_utilization(18, -24) is None
    assert picking_accuracy(-1, 100) is None
    assert picking_accuracy(95, -100) is None
