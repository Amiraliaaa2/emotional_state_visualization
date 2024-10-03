# @amirali.aaa_

import matplotlib.pyplot as plt
import numpy as np

# Data
emotions = ['Happiness', 'Sadness', 'Anger', 'Fear', 'Confusion', 'Numbness']
values = [5, 85, 40, 30, 70, 90]  # Percentage of different emotions

# Graph settings
fig, ax = plt.subplots(figsize=(10, 6))

# Draw pie chart
ax.pie(values, labels=emotions, autopct='%1.1f%%', startangle=90, colors=plt.cm.viridis(np.linspace(0, 1, len(emotions))))
ax.axis('equal')  # Display circle as a round shape
plt.title('Current Emotional State')

# Draw bar chart to describe emotions
fig, ax2 = plt.subplots(figsize=(10, 6))
ax2.bar(emotions, values, color=['#f39c12', '#e74c3c', '#c0392b', '#8e44ad', '#3498db', '#2ecc71'])
ax2.set_ylim(0, 100)
ax2.set_ylabel('Percentage (%)')
ax2.set_title('Emotional Breakdown')

# Show graph
plt.show()
