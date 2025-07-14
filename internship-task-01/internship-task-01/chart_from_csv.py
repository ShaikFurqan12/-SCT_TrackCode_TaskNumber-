import pandas as pd
import matplotlib.pyplot as plt
file_name = "population_data.csv"
data = pd.read_csv(file_name)
print("Columns in CSV:", data.columns)
age_groups = data['Height(Inches)'].astype(str)[:5]
population = data['Weight(Pounds)'][:5]
plt.figure(figsize=(10,6))
bars = plt.bar(age_groups, population, color='skyblue', edgecolor='black')
for bar, val in zip(bars, population):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f'{val}', 
             ha='center', va='bottom', fontsize=11)
plt.title("Sample Population Bar Chart from CSV", fontsize=14)
plt.xlabel("Age Groups (mocked from Height)")
plt.ylabel("Population (mocked from Weight)")
plt.tight_layout()
plt.savefig("population_chart.png")
plt.show()
