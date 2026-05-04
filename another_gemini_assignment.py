employees = ["Иван", "Мария", "Петър", "Елена"]
performance = [85, 92, 78, 95]

results_list = []

for employee, score in zip(employees, performance):
    if score > 90:
        result = f'{employee}: Excellent rating with ({score}).'
    elif 80 <= score <= 90:
        result = f'{employee}: Standard rating with ({score}).'
    else:
        result = f'{employee}: No bonus.'

    results_list.append(result)

print(results_list)

# based_on_performance = [
#     f'{emp}: Excellent Bonus with ({perf}).' if perf > 90
#     else (f'{emp}: Standard bonus with ({perf}).' if perf >=80
#     else f'{emp}: No bonus.')
#     for emp, perf in zip(employees, performance)
# ]
#
# print(based_on_performance)