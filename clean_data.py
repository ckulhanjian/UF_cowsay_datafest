import pandas as pd
# import mysql.connector
import mysql.connector as mariadb
# Step 1: Read the CSV file and select only the columns you need
csv_file_path = '/Users/carakool/Applications/Python/cowsay_datafest/Leases.csv'
columns_to_select = [
    "year","market", "address", "region", "city", "state", "zip","CBD_suburban"
]

# Read the CSV into a DataFrame and select only the necessary columns
df = pd.read_csv(csv_file_path, usecols=columns_to_select)

# Replace NaN values with None (to be interpreted as NULL in the database)
# df = df.where(pd.notna(df), None)
df = df.replace('NA', None)
# df = df.replace('nan', None)
df = df.where(pd.notna(df), None)


# Display the first few rows to verify
print(df.head())

config = {
    "user":"carakul",
    "password":"password",
    "host":"localhost",
    "database":"datafest",
}
conn = mariadb.connect(user=config["user"], password=config["password"], host=config["host"], collation='utf8mb4_unicode_ci')
cursor = conn.cursor()

print("connected!")

# cursor = conn.cursor()

cursor.execute(f"USE {config['database']};")
cursor.execute("SHOW TABLES;")
#
# print(f"using {config['database']}")
#
# # Step 3: Insert Data into MariaDB Table
# # Step 3: Insert Data into MariaDB Table
for index, row in df.iterrows():
    # Create your insert query with "INSERT IGNORE" to handle duplicates
    query = """
    INSERT IGNORE INTO temp (year, market, address, region, city, state, zip, CBD_suburban)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    data = (
        row['year'], row['market'], row['address'], row['region'], row['city'], row['state'],
        row['zip'], row['CBD_suburban']
    )

    try:
        print(f"Inserting data: {data}")  # Debugging the data
        cursor.execute(query, data)
    except Exception as e:
        print(f"Error inserting row {index}: {e}")
        continue  # Skip to the next row if error occurs



# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
