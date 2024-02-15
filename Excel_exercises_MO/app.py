import streamlit as st
from app_functions import merge_excel_sheets, create_blocked_pivot_table, create_GFS_and_company_pivot_table, get_unique_values_from_excel
import pandas as pd

# Define global constants
EXCEL_FILE = "Report_Feb14_2024.xlsx"
SHEET1_NAME = "Data 1"
SHEET2_NAME = "Data 2"
SHEET3_NAME = "Report Data"
CATEGORY = "Category"

def main():
    st.title("Excel Data Analysis")

    # Sidebar for file selection and sheet names
    st.sidebar.header("Displaying data")

    # Button to show all data
    if st.sidebar.button("Show All Data"):
        # Merge sheets
        st.subheader("Report Data")
        merged_data = merge_excel_sheets(EXCEL_FILE, SHEET1_NAME, SHEET2_NAME)
        if merged_data is not None:
            st.write(merged_data)
        else:
            st.write("Error occurred during merging. Please check the file and sheet names.")

    # Sidebar for file selection and sheet names
    st.sidebar.header("Displaying pivot tables")
    
    # Button to show indicator of blocked customers
    if st.sidebar.button("Indicator of blocked customers"):
        # Create pivot table for blocked customers
        st.header("Pivot Analysis")
        st.subheader("Indicator of Blocked Customers")
        blocked_pivot_table = create_blocked_pivot_table(EXCEL_FILE, SHEET3_NAME)
        st.write(blocked_pivot_table)

    # Button to show customer per GFS Entity and Company Code
    if st.sidebar.button("Customer per GFS Entity and Company Code"):
        # Create pivot table for GFS entity and company code
        st.header("Pivot Analysis")
        st.subheader("Customer per GFS Entity and Company Code")
        GFS_company_pivot_table = create_GFS_and_company_pivot_table(EXCEL_FILE, SHEET3_NAME)
        st.dataframe(GFS_company_pivot_table, width=800)  # Adjust the width of the table here

    # Sidebar for file selection and sheet names
    st.sidebar.header("Displaying Categories")

    # Button to show unique categories
    if st.sidebar.button("Unique categories"):
        # Create pivot table for blocked customers
        st.header("Unique categories")
        unique_values = get_unique_values_from_excel(EXCEL_FILE, SHEET2_NAME, CATEGORY)
        st.write(unique_values)


    # Sidebar for other options
    st.sidebar.header("Options")


    if st.sidebar.button("Download in Excel"):
        excel_data = {
            "Merged Data": merge_excel_sheets(EXCEL_FILE, SHEET1_NAME, SHEET2_NAME),
            "Blocked Customers Pivot Table": create_blocked_pivot_table(EXCEL_FILE, SHEET3_NAME),
            "GFS Entity and Company Code Pivot Table": create_GFS_and_company_pivot_table(EXCEL_FILE, SHEET3_NAME),
            "Unique Categories": get_unique_values_from_excel(EXCEL_FILE, SHEET2_NAME, CATEGORY)
        }

        with pd.ExcelWriter("excel_data_analysis.xlsx") as writer:
            for sheet_name, data in excel_data.items():
                data.to_excel(writer, sheet_name=sheet_name, index=False)
    
        # Download using buffer (adjust encoding if needed)
        buffer = BytesIO()
        writer.save(buffer)
        st.download_button("Download Excel file", buffer.getvalue(), file_name="excel_data_analysis.xlsx")
    

    # Button to refresh data
    if st.sidebar.button("Refresh Data"):
        # Clear cache
        st.experimental_rerun()



if __name__ == "__main__":
    main()
