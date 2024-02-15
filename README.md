# Medtronic project
Processing data in Python, SQL and creating a report

## Python project
#### 1. Python project - description

    1.	Write a script 'append_tables.py' that
    	1.1 reads data from all the CSV files
    	1.2 appends all data into single table
    	1.3 first column will be 'Date' (taken from the file name)
    	1.4 prints number of files, number of files with data in it, total number of rows
    	1.5 stores the final table into csv as 'user_actions_{today}.csv' e.g. 'user_actions_2023-10-17.csv'
    	
    2. 	Write a function 'clean_cols' in 'helpers.py' that cleanses the column names e.g. 'Unique Visitor ID [v78] (evar78)' -> 'Unique Visitor ID'
    	2.1 this function should be imported and used in the main script 'append_tables.py'


#### 1. Python project - solution
The output consists of 2 Python files (append_table.py and helpers.py) that are able to read all CSV files, append all data into one table, modify the first column as required, print all results and store the final table into the required format.

**IMPORTANT**: The append_table.py is defined as a Python class. To run the script you just need to specify the location of the data. You can run in your terminal via the following command:
```python
python append_tables.py "data_folder_path"
```

#### 1. Python project - output files
- **append_tables.py**: Python class that reads, appends, modifies as required and stores all data, plus print necessary results
- **helpers.py**: Python function that cleanses the column names (imported in the append_tables.py)
- **user_actions_2024-02-14.csv**: Final csv file 
- **Command_line_example.png**: Screenshot with results and showing what the command to run the script could look like

## SQL project
#### 2. SQL project - description

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

#### 2. SQL project - solution
The output consists of 2 SQL queries that should cover the requirements mentioned above.

**QUERY 2**: The query returns 17 rows.

#### 2. SQL project - output files
- **1st_query.sql**: Selecting unique visitor ID, first name, last name, and counting occurrences
- **2nd_query.sql**: Selecting period, category, first name, last name, and counting rows

## Excel project
#### 3. Excel project - description

1. Report: This tab contains a table information. 
The table must contain all avaible columns from tab Data 1 and columns that will be merged with  the information from Data 2.

2. Pivot: It displays 3 pivot tables
3. User running this report needs to be able to refresh previously created queries/tables in a single click as well as share the report with others. For a specific purpose another user receiving this report expects to have list of unique categories in the 'dropdown' sheet. 


#### 3. Excel project - solution
The solution has been prepared in 2 versions - In Excel (I do not have paid version of Excel, so I worked on this task in Google Sheets which could be an alternative to Excel) and via Web application in Python. 

#### Start the Application

#### Directly (using streamlit library)
First, make sure you have Streamlit and Pandas installed (e.g. pip install streamlit). 
To run the app, navigate to the directory containing the script in your terminal and run:
```python
streamlit run app.py
```

#### Using a Dockerfile
You can also use a Dockerfile to build the image for the scraper script. Open a terminal and navigate to the directory containing your Dockerfile and Streamlit app files.
Build the image using the following command:
```bash
docker build -t my_streamlit_app .
```
You can replace "my_streamlit_app" with the desired name for your Docker image.

Run the Docker container: Once the image is built, you can run it as a container:
```bash
docker run -p 8501:8501 my_streamlit_app
```

This command maps port 8501 of your local machine to port 8501 inside the container, where Streamlit is running.

Access your Streamlit app: Open a web browser and go to http://localhost:8501 to access your Streamlit app running inside the Docker container.


#### 3. Excel project - possible improvements (if there is more time)
- Python files could be refactored and optimized
- The layout could be adapted to the user requeirements
- Results could be direcly send to the email recipient
- One pivot table is missing (due to lack of time)
- Storing to Excel could be fixed as well

#### 3. Excel project - files
- **app_functions.py**: Functions to calculate information for the report
- **app.py**: Web application written in Python
- **Dockerfile**: This file contains instructions for building your Docker image.
- **requirements.txt**: This file contains all the Python libraries your Streamlit app depends on.
- **Report_Feb14_2024.xlsx**: This file contains merged data from Data 1 and Data 2 (in the column "Report data"), then 3 pivot tables and a sheet called "dropdown" using function UNIQUE to get 'Data 2' column 'O' (Category) in column 'A' in this sheet called 'dropdown'
