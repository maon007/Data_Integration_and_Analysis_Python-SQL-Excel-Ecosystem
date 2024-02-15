# Medtronic project
Processing data in Python, SQL and creating a report

### 1. Python project - description

    1.	Write a script 'append_tables.py' that
    	1.1 reads data from all the CSV files
    	1.2 appends all data into single table
    	1.3 first column will be 'Date' (taken from the file name)
    	1.4 prints number of files, number of files with data in it, total number of rows
    	1.5 stores the final table into csv as 'user_actions_{today}.csv' e.g. 'user_actions_2023-10-17.csv'
    	
    2. 	Write a function 'clean_cols' in 'helpers.py' that cleanses the column names e.g. 'Unique Visitor ID [v78] (evar78)' -> 'Unique Visitor ID'
    	2.1 this function should be imported and used in the main script 'append_tables.py'


### 1. Python project - solution
The output consists of 2 Python files (append_table.py and helpers.py) that are able to read all CSV files, append all data into one table, modify the first column as required, print all results and store the final table into the required format.

**IMPORTANT**: The append_table.py is defined as a Python class. To run the script you just need to specify the location of the data. You can run in your terminal via the following command:
```python
python append_tables.py "data_folder_path"
```

### 1. Python project - output files
- **append_tables.py**: Python class that reads, appends, modifies as required and stores all data, plus print necessary results
- **helpers.py**: Python function that cleanses the column names (imported in the append_tables.py)
- **user_actions_2024-02-14.csv**: Final csv file 
- **Command_line_example.png**: Screenshot with results and showing what the command to run the script could look like

### 2. SQL project - description

INSTRUCTIONS TO COMPLETE THE SQL TESTING:

	1.	Download any free database tool (example: https://dbeaver.io/download/)
	2. 	Your dataset is "data.sqlite"
	3. 	Compose 2 SQL queries
	4.	Query 1 - select the top 10 users from the available tables. 
	              Return fields - Unique Visitor ID, First Name, Last Name, COUNT (user occurence in USER_ACTION table), sort results by COUNT
	5.  Query 2 - from the available tables select PERIOD, GenClick Cleansed as CATEGORY, FIRST NAME, LAST NAME, COUNT (rows)

			Query conditions:
		
			5.1.	LAST NAME is either Edwards, or Harris
			5.2.	PERIOD contains string 'JUN'
	
			QUESTION:	How many rows does the query return?
	6.	After you are finished, please send us both SQL queries.  

### 2. SQL project - solution
The output consists of 2 SQL queries that should cover the requirements mentioned above.

**QUERY 2**: The query returns 17 rows.

### 2. SQL project - output files
- **1st_query.sql**: Selecting unique visitor ID, first name, last name, and counting occurrences
- **2nd_query.sql**: Selecting period, category, first name, last name, and counting rows





