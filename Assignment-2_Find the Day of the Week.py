import datetime

def find_day_of_week(date_str: str) -> str:
    d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    s = d.strftime("%A")
    return s


date_str = "2024-01-01"
s = find_day_of_week(date_str)
print(s)

# Example Test Cases
# Input: "2024-06-27"
# Output: "Thursday"

# Input: "2024-01-01"
# Output: "Monday"
