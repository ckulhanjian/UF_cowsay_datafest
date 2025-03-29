# "year","quarter","monthsigned","market","building_name","building_id","address",
#  "region","city","state","zip","internal_submarket","internal_class","leasedSF","company_name",
#  "internal_industry","transaction_type","internal_market_cluster","costarID","space_type",
#  "CBD_suburban","RBA","available_space","availability_proportion","internal_class_rent",
#  "overall_rent","direct_available_space","direct_availability_proportion",
#  "direct_internal_class_rent","direct_overall_rent","sublet_available_space",
#  "sublet_availability_proportion","sublet_internal_class_rent","sublet_overall_rent","leasing"

# geographic - market, address, region, city, state, zip, CBD_suburban

# california, texas - most suceptible
# chicago or manhattan - compare

import mysql.connector as mariadb

config = {
    "user":"carakul",
    "password":"password",
    "host":"localhost",
    "database":"datafest",
}

conn = mariadb.connect(user=config["user"], password=config["password"], host=config["host"], collation='utf8mb4_unicode_ci')
cur = conn.cursor()

cur.execute(f"USE {config['database']};")

cur.execute("""
    CREATE TABLE California (
    market VARCHAR(30),
    address VARCHAR(50),
    region VARCHAR(40),
    city VARCHAR(30),
    state VARCHAR(20),
    zip VARCHAR(10),
    CBD_suburban VARCHAR(20),
    )
    """"")

cur.execute("""
    CREATE TABLE Texas (
    market VARCHAR(30),
    address VARCHAR(50),
    region VARCHAR(40),
    city VARCHAR(30),
    state VARCHAR(20),
    zip VARCHAR(10),
    CBD_suburban VARCHAR(20),
    )
    """)

cur.execute("""
    CREATE TABLE Illinois (
    market VARCHAR(30),
    address VARCHAR(50),
    region VARCHAR(40),
    city VARCHAR(30),
    state VARCHAR(20),
    zip VARCHAR(10),
    CBD_suburban VARCHAR(20),
    )
    """)

cur.execute("""
    CREATE TABLE NewYork (
    market VARCHAR(30),
    address VARCHAR(50),
    region VARCHAR(40),
    city VARCHAR(30),
    state VARCHAR(20),
    zip VARCHAR(10),
    CBD_suburban VARCHAR(20),
    )
    """)

cur.execute("SHOW TABLES;")

# cursor = conn.cursor()

# Run a Query (Example: Show Tables)
# cursor.execute("SHOW TABLES;")

# Fetch and print results
# for table in cursor.fetchall():
#     print(table)

# Close Connection
# conn.close()
