from datetime import datetime

# 1. User input
birth_input = input("તમારી જન્મ તારીખ લખો (dd-mm-yyyy): ")
birth_date = datetime.strptime(birth_input, "%d-%m-%Y")

# 2. Current date
current_date = datetime.now()

# 3. Difference
age_days = (current_date - birth_date).days
age_years = age_days // 365
age_months = (age_days % 365) // 30
remaining_days = (age_days % 365) % 30

# 4. Output
print(f"તમારું ઉંમર છે: {age_years} વર્ષ, {age_months} મહિના અને {remaining_days} દિવસ")
