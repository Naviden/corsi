# Let's create some simple datasets that can be used to demonstrate record matching.
# We'll create two datasets with some overlapping records that can be matched on certain attributes.

# Define the size of the datasets
num_records_dataset1 = 1000
num_records_dataset2 = 800  # Second dataset will have fewer records

# Generate two datasets
def create_matching_datasets(num_records1, num_records2):
    # First dataset
    data1 = {
        'id': [i for i in range(num_records1)],
        'name': [fake.first_name() for _ in range(num_records1)],
        'surname': [fake.last_name() for _ in range(num_records1)],
        'birthdate': [fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%d/%m/%Y') for _ in range(num_records1)],
        'email': [fake.email() for _ in range(num_records1)]
    }
    df1 = pd.DataFrame(data1)

    # Second dataset with some overlapping and some different records
    overlap_size = int(0.5 * num_records2)  # Let's have 50% overlap
    data2 = {
        'unique_id': [i for i in range(num_records2)],
        'first_name': [df1.iloc[i]['name'] if i < overlap_size else fake.first_name() for i in range(num_records2)],
        'last_name': [df1.iloc[i]['surname'] if i < overlap_size else fake.last_name() for i in range(num_records2)],
        'dob': [df1.iloc[i]['birthdate'] if i < overlap_size else fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%d/%m/%Y') for i in range(num_records2)],
        'contact_email': [df1.iloc[i]['email'] if i < overlap_size else fake.email() for i in range(num_records2)]
    }
    df2 = pd.DataFrame(data2)

    return df1, df2

# Create the datasets
dataset1, dataset2 = create_matching_datasets(num_records_dataset1, num_records_dataset2)

# Save the DataFrames to CSV files
csv_file_path_dataset1 = '/mnt/data/48_1.csv'
csv_file_path_dataset2 = '/mnt/data/48_2.csv'
dataset1.to_csv(csv_file_path_dataset1, index=False)
dataset2.to_csv(csv_file_path_dataset2, index=False)

csv_file_path_dataset1, csv_file_path_dataset2
