import pandas as pd
import matplotlib.pyplot as plt

# Read csv
df = pd.read_csv('medications.csv')

# Convert date columns to datetime format
df['START'] = pd.to_datetime(df['START'])
df['STOP'] = pd.to_datetime(df['STOP'])

# Get unique patient IDs
patient_ids = df['PATIENT'].unique()

patient_id = '8d4c4326-e9de-4f45-9a4c-f8c36bff89ae'
patient_data = df[df['PATIENT'] == patient_id].sort_values(by=['START'])

# Plot patient trajectory over time
plt.plot(patient_data['START'], patient_data['DESCRIPTION'])
plt.title('Patient Trajectory for {}'.format(patient_id))
plt.xticks(rotation=8.5, fontsize=4.6)
plt.yticks(rotation=65, fontsize=5.6)
plt.show()

# Loop through each patient and create a plot
'''
for patient_id in patient_ids:
    # Select data for a single patient
    patient_data = df[df['PATIENT'] == patient_id].sort_values(by=['START'])
    
    # Plot patient trajectory over time
    plt.plot(patient_data['START'], patient_data['DESCRIPTION'])
    plt.title('Patient Trajectory for {}'.format(patient_id))
    plt.xlabel('Date')
    plt.ylabel('Description')
    
    # Resize x and y axis labels
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Save the plot as an image file
    plt.savefig('patient_{}.png'.format(patient_id))
    
    # Clear the plot for the next patient
    plt.clf()
'''


# Find the three most common conditions
condition_counts = df.groupby(['DESCRIPTION']).size().reset_index(name='count')
top_3_conditions = condition_counts.nlargest(3, 'count')

# Plot bar chart of the three most common conditions
plt.bar(top_3_conditions['DESCRIPTION'], top_3_conditions['count'], width=0.2)
plt.title('Top 3 Most Common Conditions')
plt.xlabel('Condition')
plt.ylabel('Number of Patients')
plt.xticks(rotation=10.5, fontsize=5.6)
plt.yticks(fontsize=5.6)
plt.show()

# Select data for the three most common conditions
top_3_condition_data = df[df['DESCRIPTION'].isin(top_3_conditions['DESCRIPTION'])]

# Plot boxplots of base cost by condition
top_3_condition_data.boxplot(column=['BASE_COST'], by=['DESCRIPTION'], vert=False)
plt.title('Base Cost by Condition')
plt.xlabel('Base Cost')
plt.xticks(rotation=15.5, fontsize=5.6)
plt.yticks(rotation=65, fontsize=4.6)
plt.show()

# Find the most common reason codes
reason_counts = df.groupby(['REASONDESCRIPTION']).size().reset_index(name='count')
top_3_reasons = reason_counts.nlargest(3, 'count')

# Plot bar chart of the three most common reason codes
plt.bar(top_3_reasons['REASONDESCRIPTION'], top_3_reasons['count'], width=0.2)
plt.title('Top 3 Most Common Reason Codes')
plt.xlabel('Reason Code')
plt.ylabel('Number of Patients')
plt.xticks(rotation=10.5, fontsize=5.6)
plt.yticks(fontsize=5.6)
plt.show()