# It seems there was an error due to the 'postalcode' attribute not being available in the Faker 'it_IT' locale.
# We will use a generic attribute for postal codes that should work across locales.

# Correcting the dataset creation function and re-running the creation and validation of the dataset
def create_dataset_for_business_rules(num_records):
    # Faker instance for Italian locale might not have 'zipcode' or 'postalcode' attribute
    # We will use a placeholder function to generate postal codes
    def generate_postal_code():
        return str(random.randint(10000, 99999))

    data = {
        'id': [i for i in range(num_records)],
        'age': [random.randint(1, 100) for _ in range(num_records)],  # All valid ages
        'marital_status': [random.choice(['single', 'married', 'divorced', 'widowed']) for _ in range(num_records)],
        'city': [fake.city() for _ in range(num_records)],
        'postal_code': [generate_postal_code() for _ in range(num_records)],
    }

    # Introduce some errors
    for _ in range(int(num_records * 0.05)):  # 5% of records will have an invalid age
        idx = random.randrange(num_records)
        data['age'][idx] = random.randint(-20, 0)  # Invalid negative age

    for _ in range(int(num_records * 0.05)):  # Another 5% will have improbable marital status
        idx = random.randrange(num_records)
        data['age'][idx] = random.choice([10, 11])  # Age less than 12
        data['marital_status'][idx] = 'married'  # Married status at an age less than 12

    # Create the DataFrame
    df = pd.DataFrame(data)
    return df

# Generate the dataset
business_rules_df = create_dataset_for_business_rules(1000)

# Save the DataFrame to a CSV file
csv_file_path_business_rules = '/mnt/data/business_rules_dataset.csv'
business_rules_df.to_csv(csv_file_path_business_rules, index=False)

# Define Python code to check business rules on the dataset
def check_business_rules(df):
    # Business rule 1: Age should be positive.
    rule_age_positive = df['age'] > 0

    # Business rule 2: It's improbable for someone under the age of 12 to be married in Italy.
    rule_marital_status = ~((df['age'] < 12) & (df['marital_status'] == 'married'))

    # Return all records that violate the business rules
    violations = df[~(rule_age_positive & rule_marital_status)]
    return violations

# Check the business rules
violations_df = check_business_rules(business_rules_df)

csv_file_path_business_rules, violations_df.head()
