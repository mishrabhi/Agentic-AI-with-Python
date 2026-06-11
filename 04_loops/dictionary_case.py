# dictionary in case of match-case

users = [
        {"id": 1, "total": 100, "coupon": "P20"},
        {"id": 1, "total": 150, "coupon": "F20"},
        {"id": 1, "total": 200, "coupon": "D20"}
]

discounts = {
    "P20": (0.2, 0),
    "F20": (0.5, 0),
    "D20": (0, 10)
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0,0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got doscount for next visit of rupees {discount}")