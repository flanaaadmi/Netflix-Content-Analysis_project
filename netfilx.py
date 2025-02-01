# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:37:37 2025

@author: DELL
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("C:\\Users\\DELL\\Downloads\\netflix_titles22.csv")

# Set figure size for all plots
plt.figure(figsize=(10, 6))

# 1. **Pie Chart** - Distribution of Movies and TV Shows
plt.subplot(2, 2, 1)
type_counts = data['type'].value_counts()
ex = [0.2,0.0]
plt.pie(type_counts, labels=type_counts.index, autopct='%1.0f%%', colors=['red', 'blue'], startangle=90 , explode=ex,textprops={"fontsize":8})
plt.title("Movies vs TV Shows")

# 2. **Bar Chart** - Top 10 Countries with Most Content
plt.subplot(2, 2, 2)
country_counts = data['country'].value_counts().head(10)
country_counts.plot(kind='bar', color='purple')
plt.xlabel("Country")
plt.ylabel("Count")
plt.title("Top 10 Countries with Most Netflix Content")

# 3. **Histogram** - Release Year Distribution
plt.subplot(2, 2, 3)
data['release_year'].hist(bins=20, color='green', edgecolor='black')
plt.xlabel("Release Year")
plt.ylabel("Frequency")
plt.title("Distribution of Content Release Years")

# 4. **Bar Chart** - Top 10 Directors with Most Content
plt.subplot(2, 2, 4)
director_counts = data['director'].value_counts().head(10)
director_counts.plot(kind='bar', color='orange')
plt.xlabel("Director")
plt.ylabel("Count")
plt.title("Top 10 Directors with Most Content")

# Adjust layout and show the plots
plt.tight_layout()
plt.show()
