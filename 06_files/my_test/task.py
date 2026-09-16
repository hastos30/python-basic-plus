count = 0
total_amount = 0

with open("leads.txt", "r", encoding="utf-8") as source_file, open(
    "hot_leads.txt", "w", encoding="utf-8"
) as result_file:

    for line in source_file:
        name, amount = line.strip().split(",")
        amount = int(amount)
        if amount >= 10000:
            result_file.write(f"{name},{amount}\n")
            total_amount += amount
            count += 1


print(f"Горячих лидов: {count}")
print(f"Общая сумма: {total_amount}")
