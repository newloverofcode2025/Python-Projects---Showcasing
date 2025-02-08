# src/data_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

def analyze_data():
    # Sample DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [50000, 60000, 70000]
    }
    df = pd.DataFrame(data)

    print("Data Analysis:")
    print(df)

    # Plotting
    df.plot(kind='bar', x='Name', y='Salary', color='skyblue')
    plt.title('Salary Distribution')
    plt.xlabel('Name')
    plt.ylabel('Salary')
    plt.show()

if __name__ == "__main__":
    analyze_data()