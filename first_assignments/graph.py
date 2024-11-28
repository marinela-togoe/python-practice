import matplotlib.pyplot as plt

# Data for the SANS Maturity Model
years = ["Current", "Year 1", "Year 2", "Year 3"]
maturity_levels = [1, 2, 3, 4]  # Levels corresponding to Initial, Managed, Defined, Optimized

# Mapping years to their objectives
objectives = [
    "Current Level: Initial (Level 1)",
    "Year 1: Managed (Level 2) - Standardize policies, Improve patch management",
    "Year 2: Defined (Level 3) - Formalize incident response, Continuous monitoring",
    "Year 3: Optimized (Level 4) - Advanced threat detection, Forensic readiness"
]

# Creating the plot
plt.figure(figsize=(10, 6))
plt.plot(years, maturity_levels, marker='o', linestyle='-', color='b')

# Annotating the plot with objectives
for i, txt in enumerate(objectives):
    plt.annotate(txt, (years[i], maturity_levels[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Setting plot labels and title
plt.xlabel('Timeline')
plt.ylabel('Maturity Level')
plt.title('Maturity Assessment Using the SANS Maturity Model for INGKA Group')
plt.yticks([1, 2, 3, 4, 5], ["Initial (1)", "Managed (2)", "Defined (3)", "Optimized (4)", "Adaptive (5)"])

# Display the plot
plt.grid(True)
plt.show()
