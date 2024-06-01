import pandas as pd
import numpy as np
from tabulate import tabulate

# Function to extract days from the diff column
def extract_days(diff):
    if 'days' in diff:
        days = int(diff.split(' days')[0])
    else:
        days = 0
    return days

# Function to calculate retention rates
def calculate_retention(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Apply the function to the diff column
    data['days'] = data['diff'].apply(extract_days)
    
    # Total number of users (sample space)
    total_users = len(data)
    
    # Number of users in each retention cohort
    retention_d1 = np.sum(data['days'] >= 1)
    retention_d7 = np.sum(data['days'] >= 7)
    retention_d30 = np.sum(data['days'] >= 30)
    retention_d60 = np.sum(data['days'] >= 60)
    retention_d90 = np.sum(data['days'] >= 90)
    
    # Calculate the percentage retention for each cohort
    percentage_retention_d1 = (retention_d1 / total_users) * 100
    percentage_retention_d7 = (retention_d7 / total_users) * 100
    percentage_retention_d30 = (retention_d30 / total_users) * 100
    percentage_retention_d60 = (retention_d60 / total_users) * 100
    percentage_retention_d90 = (retention_d90 / total_users) * 100
    
    return {
        "total_users": total_users,
        "retention_d1": retention_d1,
        "retention_d7": retention_d7,
        "retention_d30": retention_d30,
        "retention_d60": retention_d60,
        "retention_d90": retention_d90,
        "percentage_retention_d1": percentage_retention_d1,
        "percentage_retention_d7": percentage_retention_d7,
        "percentage_retention_d30": percentage_retention_d30,
        "percentage_retention_d60": percentage_retention_d60,
        "percentage_retention_d90": percentage_retention_d90,
    }

# Function to print the retention rates in a table format
def print_retention_table(retention_data, dataset_name):
    headers = ["Metric", "Value"]
    table = [
        ["Total Users", retention_data["total_users"]],
        ["Retention D1", retention_data["retention_d1"]],
        ["Retention D7", retention_data["retention_d7"]],
        ["Retention D30", retention_data["retention_d30"]],
        ["Retention D60", retention_data["retention_d60"]],
        ["Retention D90", retention_data["retention_d90"]],
        ["Percentage Retention D1", f'{retention_data["percentage_retention_d1"]:.2f}%'],
        ["Percentage Retention D7", f'{retention_data["percentage_retention_d7"]:.2f}%'],
        ["Percentage Retention D30", f'{retention_data["percentage_retention_d30"]:.2f}%'],
        ["Percentage Retention D60", f'{retention_data["percentage_retention_d60"]:.2f}%'],
        ["Percentage Retention D90", f'{retention_data["percentage_retention_d90"]:.2f}%'],
    ]
    print(f"\n{dataset_name} Retention Table:")
    print(tabulate(table, headers, tablefmt="pretty"))

# File paths
file_path_views = 'data/views.csv'  
file_path_friends = 'data/friends.csv'
file_path_messages = 'data/messages.csv'  

# Calculate and print retention for the views dataset
views_retention = calculate_retention(file_path_views)
print_retention_table(views_retention, "Views Dataset")

# Calculate and print retention for the friends dataset
friends_retention = calculate_retention(file_path_friends)
print_retention_table(friends_retention, "Friends Dataset")

# Calculate and print retention for the friends dataset
messages_retention = calculate_retention(file_path_messages)
print_retention_table(messages_retention, "Messages Dataset")