import pandas as pd
import matplotlib.pyplot as plt

# Sample engagement data (time vs. engagement)
data = {
    'Time': ['8 AM', '9 AM', '10 AM', '11 AM', '12 PM'],
    'Likes': [150, 150, 20, 180, 160],
    'Comments': [20, 25, 40, 28, 22]
}


avg_likes = sum(data['Likes']) / len(data['Likes'])
avg_comments = sum(data['Comments']) / len(data['Comments'])

# Convert data to DataFrame
df = pd.DataFrame(data)

# assume 1 comment = 10 likes

df['Engagement'] = df['Likes'] + df['Comments'] * 10

# 2. Find out the best time slot with highest engagement
best_time = df[df['Engagement'] == df['Engagement'].max()]['Time'].values[0]

# 3. Find out the best day to post
# Find the day with the highest engagement
# Add a new column 'Day' to the DataFrame
df['Day'] = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

best_day = df[df['Engagement'] == df['Engagement'].max()]['Day'].values[0]

print(f'The best time to post is {best_time} and the best day to post is {best_day}')

# Plot engagement metrics
plt.figure(figsize=(10, 6))
plt.plot(df['Time'], df['Likes'], marker='o', label='Likes')
plt.plot(df['Time'], df['Comments'], marker='x', label='Comments')
plt.xlabel('Time')
plt.ylabel('Engagement')
plt.title('Engagement vs. Time')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()
