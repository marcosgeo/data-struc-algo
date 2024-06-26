

# Calculate the average temperature
def average_temperature():
    num_days = int(input("How many day's temperature"))
    total = 0
    temp = []
    for i in range(num_days):
        next_day = int(input(f"Day {str(i + 1)}'s  high temp:"))
        temp.append(next_day)
        total += temp[i]

    avg = round(total / num_days, 2)
    print(f"\nAverage = {str(avg)}")

    above = 0
    for i in temp:
        if i > avg:
            above += 1

    print(f"{str(above)} day(s) above average")

