def blood(
        supply_o, supply_a, supply_b, supply_ab,
        demand_o, demand_a, demand_b, demand_ab
):
    if demand_o > supply_o:
        return False
    if demand_o + demand_a > supply_o + supply_a:
        return False
    if demand_o + demand_b > supply_o + supply_b:
        return False
    if demand_o + demand_a + demand_b > supply_o + supply_a + supply_b:
        return False

    demand_all = demand_o + demand_a + demand_b + demand_ab
    supply_all = supply_o + supply_a + supply_b + supply_ab
    return demand_all > supply_all


print(blood(50,36,11,8,45,42,10,3))
print(blood(50,36,11,3,45,38,10,7))
