import streamlit as st
import mysql.connector
import pandas as pd
import json
import requests
from streamlit_lottie import st_lottie

# Set the page title and favicon


# Define a CSS style for better layout and spacing
st.markdown(
    """
    <style>
        .main {
            padding: 2rem;
        }
        .content {
            max-width: 800px;
            margin: auto;
        }
        .header {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Create sections with improved styling
with st.container():
    st.title("Welcome to StockMate: Your Inventory Management Solution")
    st.write("🚀 Where Efficiency Meets Inventory Control Excellence! 📦")
    st.markdown("---")
    
    st.header("🌟 Discover StockMate's Benefits:")
    st.write("• Effortless Management: Say goodbye to inventory hassles. Our user-friendly platform is designed to make managing your stock a breeze.")
    st.write("• Data-Driven Insights: Make decisions with confidence. Dive into our comprehensive analytics to gain valuable insights and optimize your inventory strategy.")
    st.write("• Security and Reliability: Your data's security is our utmost priority. We employ advanced security measures to ensure your information is always safe and accessible.")
    
    st.write("Join us today and embark on a journey towards streamlined inventory management, informed decision-making, and a brighter future for your business.")
    st.write("Your Success, Our Promise. 🚀📈")
    
    if st.button("Login Now!", key="login_button", type="primary"):
        st.session_state.page = "login"

# You can apply similar styling to other pages (About, Help, Credits) as needed.

# Define the rest of your app's logic and pages here...
import streamlit as st

# Set the page title and favicon
st.set_page_config(page_title="StockMate", page_icon="📦")

# Define a CSS style for better layout and spacing
st.markdown(
    """
    <style>
        .main {
            padding: 2rem;
        }
        .content {
            max-width: 800px;
            margin: auto;
        }
        .header {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .section {
            margin-bottom: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Define the function to display the homepage
def homepage():
    st.title("Welcome to StockMate: Your Inventory Management Solution")

    # Add a brief description of your app
    st.write("🚀 Where Efficiency Meets Inventory Control Excellence! 📦")
    
    # Add sections with improved styling
    with st.container():
        st.markdown("---")
        st.header("🌟 Discover StockMate's Benefits:")
        st.write("• Effortless Management: Say goodbye to inventory hassles. Our user-friendly platform is designed to make managing your stock a breeze.")
        st.write("• Data-Driven Insights: Make decisions with confidence. Dive into our comprehensive analytics to gain valuable insights and optimize your inventory strategy.")
        st.write("• Security and Reliability: Your data's security is our utmost priority. We employ advanced security measures to ensure your information is always safe and accessible.")
    
        st.write("Join us today and embark on a journey towards streamlined inventory management, informed decision-making, and a brighter future for your business.")
        st.write("Your Success, Our Promise. 🚀📈")

        # Add a button to navigate to the login page
        if st.button("Login Now!", key="login_button", type="primary"):
            st.session_state.page = "login"

# Display the homepage when the app starts
if st.session_state.page is None:
    homepage()
import streamlit as st

# Set the page title and favicon
st.set_page_config(page_title="StockMate", page_icon="📦")

# Define a CSS style for better layout and spacing
st.markdown(
    """
    <style>
        .main {
            padding: 2rem;
        }
        .content {
            max-width: 800px;
            margin: auto;
        }
        .header {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .section {
            margin-bottom: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Define the function for the login page
def login():
    st.title("Login")

    # Create input fields for username and password
    username = st.text_input("Enter Username")
    password = st.text_input("Enter Password", type="password")

    # Check if the "Login" button is clicked
    if st.button("Login", type="primary"):
        if username and password:
            # Add your authentication logic here
            # For demonstration purposes, let's assume username: "admin" and password: "password"
            if username == "admin" and password == "password":
                st.success("Login Successful!")
                # Redirect the user to the dashboard or desired page after successful login
                st.session_state.page = "dashboard"
            else:
                st.error("Login failed. Please try again.")

# Display the login page when the app starts
if st.session_state.page is None:
    login()
import streamlit as st

# Set the page title and favicon
st.set_page_config(page_title="StockMate", page_icon="📦")

# Define a CSS style for better layout and spacing
st.markdown(
    """
    <style>
        .main {
            padding: 2rem;
        }
        .content {
            max-width: 800px;
            margin: auto;
        }
        .header {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .section {
            margin-bottom: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Define a dictionary for navigation options
navigation_options = {
    "Dashboard": "dashboard",
    "Add Stock": "add_stock",
    "Show Stock": "show_stock",
    "Remove Stock": "remove_stock",
    "Issue Stock": "issue_stock",
    "Show Issued Stock": "show_issued_stock",
    "Add Department": "add_department",
}

# Define the function for the dashboard page
def dashboard():
    st.title("Dashboard")

    # Create a dropdown for navigation
    selected_option = st.selectbox("Select Action", list(navigation_options.keys()))

    # Check the selected option and navigate accordingly
    if selected_option == "Dashboard":
        # Display dashboard content here
        st.write("Welcome to the StockMate Dashboard. Here, you can manage your inventory.")
    elif selected_option == "Add Stock":
        # Redirect to the "Add Stock" page
        st.session_state.page = navigation_options[selected_option]
    elif selected_option == "Show Stock":
        # Redirect to the "Show Stock" page
        st.session_state.page = navigation_options[selected_option]
    elif selected_option == "Remove Stock":
        # Redirect to the "Remove Stock" page
        st.session_state.page = navigation_options[selected_option]
    elif selected_option == "Issue Stock":
        # Redirect to the "Issue Stock" page
        st.session_state.page = navigation_options[selected_option]
    elif selected_option == "Show Issued Stock":
        # Redirect to the "Show Issued Stock" page
        st.session_state.page = navigation_options[selected_option]
    elif selected_option == "Add Department":
        # Redirect to the "Add Department" page
        st.session_state.page = navigation_options[selected_option]

# Display the dashboard page when the app starts
if st.session_state.page is None:
    dashboard()
import streamlit as st

# Set the page title and favicon
st.set_page_config(page_title="StockMate", page_icon="📦")

# Define a CSS style for better layout and spacing
st.markdown(
    """
    <style>
        .main {
            padding: 2rem;
        }
        .content {
            max-width: 800px;
            margin: auto;
        }
        .header {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .section {
            margin-bottom: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Define the function for the "Add Stock" page
def add_stock():
    st.title("Add Stock")

    # Create input fields for stock details
    name = st.text_input("Name")
    id_no = st.text_input("ID No.")
    qty = st.number_input("Quantity", 1)
    date = st.date_input("Date")
    warranty_period = st.text_input("Warranty Period (in months)")
    condition = st.text_input("Condition (OK or Not OK)")
    specifications = st.text_area("Specifications")

    # Check if the "Insert" button is clicked
    if st.button("Insert"):
        if name and id_no and qty:
            # Add your database insert logic here
            # Insert the provided stock details into your database
            # For demonstration purposes, you can print the details
            st.write("Stock Details:")
            st.write(f"Name: {name}")
            st.write(f"ID No.: {id_no}")
            st.write(f"Quantity: {qty}")
            st.write(f"Date: {date}")
            st.write(f"Warranty Period: {warranty_period}")
            st.write(f"Condition: {condition}")
            st.write(f"Specifications: {specifications}")

            # After inserting into the database, you can redirect or display a success message
            st.success("Stock details added successfully!")

# Define the function for the "Show Stock" page
def show_stock():
    st.title("Show Stock")

    # Create input fields for filtering stock data
    id_filter = st.text_input("Enter ID No. (Optional)")
    date_filter = st.date_input("Enter Date (Optional)")

    # Check if the "Show" button is clicked
    if st.button("Show"):
        if id_filter or date_filter:
            # Add your database query logic here to fetch and display stock data
            # For demonstration purposes, let's assume you have fetched stock data as a list
            stock_data = [
                {"Name": "Product 1", "ID No.": 12345, "Quantity": 50, "Date": "2023-10-10", "Warranty Period": 12, "Condition": "OK", "Specifications": "Lorem ipsum"},
                {"Name": "Product 2", "ID No.": 67890, "Quantity": 30, "Date": "2023-10-15", "Warranty Period": 6, "Condition": "Not OK", "Specifications": "Lorem ipsum"},
            ]

            # Display the filtered stock data in a table
            st.write("Filtered Stock Data:")
            st.table(stock_data)
        else:
            st.warning("Please provide at least one filter (ID No. or Date) to show stock data.")

# Define the main app function
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select Page", ["Dashboard", "Add Stock", "Show Stock"])

    if page == "Dashboard":
        dashboard()
    elif page == "Add Stock":
        add_stock()
    elif page == "Show Stock":
        show_stock()

# Run the main app function
if __name__ == "__main__":
    main()
# ... (previous code)

# Define the function for the "Remove Stock" page
def remove_stock():
    st.title("Remove Stock")

    # Create an input field to enter the ID for the stock to be removed
    id_to_remove = st.text_input("Enter ID No. of Stock to Remove")

    # Check if the "Confirm" button is clicked
    if st.button("Confirm"):
        if id_to_remove:
            # Add your database delete logic here
            # Delete the stock with the provided ID from your database
            # For demonstration purposes, you can display a success message
            st.success(f"Stock with ID No. {id_to_remove} has been successfully removed.")
        else:
            st.warning("Please enter the ID No. of the stock to remove.")

# Define the function for the "Issue Stock" page
def issue_stock():
    st.title("Issue Stock")

    # Create input fields for issuing stock
    stock_id = st.text_input("Stock ID")
    quantity = st.number_input("Quantity to Issue", 1)
    department = st.text_input("Department")
    issue_date = st.date_input("Issue Date")

    # Check if the "Issue" button is clicked
    if st.button("Issue"):
        if stock_id and quantity and department and issue_date:
            # Add your logic here to issue stock and update the database
            # For demonstration purposes, you can print the issued details
            st.write("Issued Details:")
            st.write(f"Stock ID: {stock_id}")
            st.write(f"Quantity Issued: {quantity}")
            st.write(f"Department: {department}")
            st.write(f"Issue Date: {issue_date}")

            # After issuing stock, you can display a success message
            st.success("Stock has been successfully issued.")
        else:
            st.warning("Please fill in all the required fields.")

# Define the function for the "Show Issued Stock" page
def show_issued_stock():
    st.title("Show Issued Stock")

    # Create input fields for filtering issued stock data
    issue_id_filter = st.text_input("Enter Issue ID (Optional)")
    issue_date_filter = st.date_input("Enter Issue Date (Optional)")

    # Check if the "Show" button is clicked
    if st.button("Show"):
        if issue_id_filter or issue_date_filter:
            # Add your database query logic here to fetch and display issued stock data
            # For demonstration purposes, let's assume you have fetched issued stock data as a list
            issued_stock_data = [
                {"Issue ID": 1, "Stock ID": 12345, "Department": "Dept A", "Quantity Issued": 5, "Issue Date": "2023-10-10"},
                {"Issue ID": 2, "Stock ID": 67890, "Department": "Dept B", "Quantity Issued": 3, "Issue Date": "2023-10-15"},
            ]

            # Display the filtered issued stock data in a table
            st.write("Filtered Issued Stock Data:")
            st.table(issued_stock_data)
        else:
            st.warning("Please provide at least one filter (Issue ID or Issue Date) to show issued stock data.")

# ... (previous code)

# Update the main app function to include the new pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select Page", ["Dashboard", "Add Stock", "Show Stock", "Remove Stock", "Issue Stock", "Show Issued Stock"])

    if page == "Dashboard":
        dashboard()
    elif page == "Add Stock":
        add_stock()
    elif page == "Show Stock":
        show_stock()
    elif page == "Remove Stock":
        remove_stock()
    elif page == "Issue Stock":
        issue_stock()
    elif page == "Show Issued Stock":
        show_issued_stock()

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()
# ... (previous code)

# Define the function for the "Add Department" page
def add_department():
    st.title("Add Department")

    # Create input fields for adding a new department
    department_no = st.text_input("Department No.")
    department_name = st.text_input("Department Name")
    incharge_name = st.text_input("Incharge Name")

    # Check if the "Add" button is clicked
    if st.button("Add"):
        if department_no and department_name and incharge_name:
            # Add your logic here to insert the new department into the database
            # For demonstration purposes, you can display a success message
            st.success(f"Department No. {department_no} has been added successfully.")
        else:
            st.warning("Please fill in all the required fields.")

# Define the function for the "Credits" page
def credits_page():
    st.title("Development Team")

    # List the names of the development team members
    team_members = ["Ujjwal Barange", "Pushkar Verma", "Prathamesh Kale"]

    # Display the names of the team members
    for member in team_members:
        st.write(member)

# ... (previous code)

# Update the main app function to include the new pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select Page", ["Dashboard", "Add Stock", "Show Stock", "Remove Stock", "Issue Stock", "Show Issued Stock", "Add Department", "Credits"])

    if page == "Dashboard":
        dashboard()
    elif page == "Add Stock":
        add_stock()
    elif page == "Show Stock":
        show_stock()
    elif page == "Remove Stock":
        remove_stock()
    elif page == "Issue Stock":
        issue_stock()
    elif page == "Show Issued Stock":
        show_issued_stock()
    elif page == "Add Department":
        add_department()
    elif page == "Credits":
        credits_page()

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()
# ... (previous code)

# Define the function for the "Issue Stock" page
def issue_stock():
    st.title("Issue Stock")

    # Create input fields for issuing stock
    stock_id = st.text_input("Stock ID")
    department_no = st.text_input("Department No.")
    qty_issued = st.number_input("Quantity Issued", 1)
    issued_date = st.date_input("Date of Issue")

    # Check if the "Issue" button is clicked
    if st.button("Issue"):
        if stock_id and department_no and qty_issued and issued_date:
            # Add your logic here to issue stock and update the database
            # For demonstration purposes, you can display a success message
            st.success(f"{qty_issued} units of Stock ID {stock_id} have been issued to Department {department_no} on {issued_date}.")
        else:
            st.warning("Please fill in all the required fields.")

# Define the function for the "Show Issued Stock" page
def show_issued_stock():
    st.title("Show Issued Stock")

    # Create input fields for filtering issued stock
    issue_id = st.text_input("Issue ID")
    issue_date = st.date_input("Issue Date")
    department_filter = st.selectbox("Filter by Department", ["All Departments", "Department 1", "Department 2", "Department 3"])

    # Display the issued stock based on filters
    if st.button("Show Issued Stock"):
        # Add your logic here to fetch and display issued stock based on the selected filters
        # For demonstration purposes, you can display the results in a table

        # Example data (replace this with actual data from your database)
        issued_stock_data = [
            {"Issue ID": 1, "Stock ID": 101, "Department": "Department 1", "Quantity Issued": 5, "Issue Date": "2023-01-10"},
            {"Issue ID": 2, "Stock ID": 102, "Department": "Department 2", "Quantity Issued": 3, "Issue Date": "2023-01-15"},
        ]

        # Display the data in a table
        issued_stock_df = pd.DataFrame(issued_stock_data)
        st.table(issued_stock_df)

# ... (previous code)

# Update the main app function to include the new pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select Page", ["Dashboard", "Add Stock", "Show Stock", "Remove Stock", "Issue Stock", "Show Issued Stock", "Add Department", "Credits"])

    if page == "Dashboard":
        dashboard()
    elif page == "Add Stock":
        add_stock()
    elif page == "Show Stock":
        show_stock()
    elif page == "Remove Stock":
        remove_stock()
    elif page == "Issue Stock":
        issue_stock()
    elif page == "Show Issued Stock":
        show_issued_stock()
    elif page == "Add Department":
        add_department()
    elif page == "Credits":
        credits_page()

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()
# ... (previous code)

# Define the function for the "Add Department" page
def add_department():
    st.title("Add Department")

    # Create input fields for adding a department
    department_no = st.text_input("Department No.")
    department_name = st.text_input("Department Name")
    incharge_name = st.text_input("Incharge Name")

    # Check if the "Add" button is clicked
    if st.button("Add"):
        if department_no and department_name and incharge_name:
            # Add your logic here to add the department to the database
            # For demonstration purposes, you can display a success message
            st.success(f"Department {department_no} - {department_name} with Incharge {incharge_name} has been added.")
        else:
            st.warning("Please fill in all the required fields.")

# Define the function for the "Credits" page
def credits_page():
    st.title("Development Team")

    # List the names of the development team
    st.write("Ujjwal Barange")
    st.write("Pushkar Verma")
    st.write("Prathamesh Kale")

# ... (previous code)

# Update the main app function to include the new pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select Page", ["Dashboard", "Add Stock", "Show Stock", "Remove Stock", "Issue Stock", "Show Issued Stock", "Add Department", "Credits"])

    if page == "Dashboard":
        dashboard()
    elif page == "Add Stock":
        add_stock()
    elif page == "Show Stock":
        show_stock()
    elif page == "Remove Stock":
        remove_stock()
    elif page == "Issue Stock":
        issue_stock()
    elif page == "Show Issued Stock":
        show_issued_stock()
    elif page == "Add Department":
        add_department()
    elif page == "Credits":
        credits_page()

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()
# ... (previous code)

# Define the function for the "Issue Stock" page
def issue_stock():
    st.title("Issue Stock")
    stock_id = st.text_input("Stock ID")
    
    # Add logic here to fetch stock details and display them
    
    qty_to_issue = st.number_input("Quantity to Issue", min_value=1)
    department = st.selectbox("Department", ["Department 1", "Department 2", "Department 3"])  # You can fetch department names from the database
    
    issue_date = st.date_input("Issue Date")

    if st.button("Issue"):
        # Add logic here to update stock and record the issue in the database
        st.success(f"Issued {qty_to_issue} units of Stock ID {stock_id} to {department} on {issue_date}")

# Define the function for the "Show Issued Stock" page
def show_issued_stock():
    st.title("Show Issued Stock")
    st.write("Here you can view issued stock records.")

    # Add logic here to fetch and display issued stock records

# ... (previous code)

# Update the main app function to include the new pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select Page", ["Dashboard", "Add Stock", "Show Stock", "Remove Stock", "Issue Stock", "Show Issued Stock", "Add Department", "Credits"])

    if page == "Dashboard":
        dashboard()
    elif page == "Add Stock":
        add_stock()
    elif page == "Show Stock":
        show_stock()
    elif page == "Remove Stock":
        remove_stock()
    elif page == "Issue Stock":
        issue_stock()
    elif page == "Show Issued Stock":
        show_issued_stock()
    elif page == "Add Department":
        add_department()
    elif page == "Credits":
        credits_page()

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()
# ... (previous code)

# Define the function for the "Show Stock" page
def show_stock():
    st.title("Show Stock")
    st.write("Here you can view stock details based on different criteria.")

    # Add options to select how to display stock details
    display_option = st.selectbox("Display Stock By:", ["Show All", "Show by ID", "Show by Date"])

    if display_option == "Show All":
        # Add logic here to fetch and display all stock details
        st.write("Showing all stock details:")
        # Sample code to display stock details in a table
        stock_data = get_all_stock_data()  # Replace with your database query
        st.table(stock_data)

    elif display_option == "Show by ID":
        stock_id = st.text_input("Enter Stock ID:")
        if st.button("Show"):
            # Add logic here to fetch and display stock details by ID
            st.write(f"Showing stock details for Stock ID: {stock_id}")
            # Sample code to display stock details in a table
            stock_data = get_stock_data_by_id(stock_id)  # Replace with your database query
            st.table(stock_data)

    elif display_option == "Show by Date":
        selected_date = st.date_input("Select Date:")
        if st.button("Show"):
            # Add logic here to fetch and display stock details by date
            st.write(f"Showing stock details for Date: {selected_date}")
            # Sample code to display stock details in a table
            stock_data = get_stock_data_by_date(selected_date)  # Replace with your database query
            st.table(stock_data)

# ... (previous code)

# Update the main app function to include the new pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select Page", ["Dashboard", "Add Stock", "Show Stock", "Remove Stock", "Issue Stock", "Show Issued Stock", "Add Department", "Credits"])

    if page == "Dashboard":
        dashboard()
    elif page == "Add Stock":
        add_stock()
    elif page == "Show Stock":
        show_stock()
    elif page == "Remove Stock":
        remove_stock()
    elif page == "Issue Stock":
        issue_stock()
    elif page == "Show Issued Stock":
        show_issued_stock()
    elif page == "Add Department":
        add_department()
    elif page == "Credits":
        credits_page()

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()
# ... (previous code)

# Define the function for the "Remove Stock" page
def remove_stock():
    st.title("Remove Stock")
    st.write("Here you can remove stock from the inventory.")

    # Create input fields for stock removal
    stock_id = st.text_input("Enter Stock ID to Remove:")
    quantity_to_remove = st.number_input("Quantity to Remove:", 1)
    
    if st.button("Remove"):
        # Add logic here to remove stock from the inventory
        if remove_stock_from_inventory(stock_id, quantity_to_remove):  # Implement this function
            st.success(f"Successfully removed {quantity_to_remove} units of stock with ID {stock_id}.")
        else:
            st.error("Failed to remove stock. Please check the ID and quantity.")

# Define the function for the "Issue Stock" page
def issue_stock():
    st.title("Issue Stock")
    st.write("Here you can issue stock from the inventory to a department.")

    # Create input fields for issuing stock
    stock_id = st.text_input("Enter Stock ID to Issue:")
    department = st.selectbox("Select Department:", ["Department A", "Department B", "Department C"])  # Replace with your departments
    quantity_to_issue = st.number_input("Quantity to Issue:", 1)
    
    if st.button("Issue"):
        # Add logic here to issue stock to a department
        if issue_stock_to_department(stock_id, department, quantity_to_issue):  # Implement this function
            st.success(f"Successfully issued {quantity_to_issue} units of stock with ID {stock_id} to {department}.")
        else:
            st.error("Failed to issue stock. Please check the ID and quantity.")

# ... (previous code)

# Update the main app function to include the new pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select Page", ["Dashboard", "Add Stock", "Show Stock", "Remove Stock", "Issue Stock", "Show Issued Stock", "Add Department", "Credits"])

    if page == "Dashboard":
        dashboard()
    elif page == "Add Stock":
        add_stock()
    elif page == "Show Stock":
        show_stock()
    elif page == "Remove Stock":
        remove_stock()
    elif page == "Issue Stock":
        issue_stock()
    elif page == "Show Issued Stock":
        show_issued_stock()
    elif page == "Add Department":
        add_department()
    elif page == "Credits":
        credits_page()

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()
# ... (previous code)

# Define the function for the "Show Issued Stock" page
def show_issued_stock():
    st.title("Show Issued Stock")
    st.write("Here you can view issued stock records.")

    # Add options to filter issued stock records
    filter_option = st.selectbox("Filter By:", ["All Issued Stock", "By Department", "By Date"])
    
    if filter_option == "All Issued Stock":
        # Display all issued stock records
        issued_stock_records = get_all_issued_stock_records()  # Implement this function
        if issued_stock_records:
            st.table(pd.DataFrame(issued_stock_records, columns=["Issue ID", "Stock ID", "Department", "Quantity Issued", "Issue Date"]))
        else:
            st.warning("No issued stock records found.")
    elif filter_option == "By Department":
        # Display issued stock records filtered by department
        selected_department = st.selectbox("Select Department:", ["Department A", "Department B", "Department C"])  # Replace with your departments
        issued_stock_records = get_issued_stock_records_by_department(selected_department)  # Implement this function
        if issued_stock_records:
            st.table(pd.DataFrame(issued_stock_records, columns=["Issue ID", "Stock ID", "Department", "Quantity Issued", "Issue Date"]))
        else:
            st.warning(f"No issued stock records found for {selected_department}.")
    elif filter_option == "By Date":
        # Display issued stock records filtered by date
        selected_date = st.date_input("Select Date:")
        issued_stock_records = get_issued_stock_records_by_date(selected_date)  # Implement this function
        if issued_stock_records:
            st.table(pd.DataFrame(issued_stock_records, columns=["Issue ID", "Stock ID", "Department", "Quantity Issued", "Issue Date"]))
        else:
            st.warning(f"No issued stock records found for {selected_date}.")

# Define the function for the "Add Department" page
def add_department():
    st.title("Add Department")
    st.write("Here you can add a new department to the system.")

    # Create input fields for adding a department
    department_id = st.text_input("Enter Department ID:")
    department_name = st.text_input("Enter Department Name:")
    incharge_name = st.text_input("Enter Incharge Name:")
    
    if st.button("Add Department"):
        # Add logic here to add a new department
        if add_new_department(department_id, department_name, incharge_name):  # Implement this function
            st.success(f"Successfully added the {department_name} department.")
        else:
            st.error("Failed to add the department. Please check the information provided.")

# ... (previous code)

# Update the main app function to include the new pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select Page", ["Dashboard", "Add Stock", "Show Stock", "Remove Stock", "Issue Stock", "Show Issued Stock", "Add Department", "Credits"])

    if page == "Dashboard":
        dashboard()
    elif page == "Add Stock":
        add_stock()
    elif page == "Show Stock":
        show_stock()
    elif page == "Remove Stock":
        remove_stock()
    elif page == "Issue Stock":
        issue_stock()
    elif page == "Show Issued Stock":
        show_issued_stock()
    elif page == "Add Department":
        add_department()
    elif page == "Credits":
        credits_page()

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()
# ... (previous code)

# Define the function for the "Return Stock" page
def return_stock():
    st.title("Return Stock")
    st.write("Here you can process the return of stock items.")

    # Create input fields for processing return
    stock_id = st.text_input("Enter Stock ID:")
    department = st.selectbox("Select Department:", ["Department A", "Department B", "Department C"])  # Replace with your departments
    quantity_returned = st.number_input("Quantity Returned:", min_value=1)
    return_date = st.date_input("Return Date:")

    if st.button("Process Return"):
        # Add logic here to process the return of stock items
        if process_stock_return(stock_id, department, quantity_returned, return_date):  # Implement this function
            st.success(f"Successfully processed the return of {quantity_returned} items from Stock ID {stock_id}.")
        else:
            st.error("Failed to process the return. Please check the information provided.")

# Define the function for the "Show Return Stock" page
def show_return_stock():
    st.title("Show Return Stock")
    st.write("Here you can view returned stock records.")

    # Add options to filter returned stock records
    filter_option = st.selectbox("Filter By:", ["All Returned Stock", "By Department", "By Date"])
    
    if filter_option == "All Returned Stock":
        # Display all returned stock records
        returned_stock_records = get_all_returned_stock_records()  # Implement this function
        if returned_stock_records:
            st.table(pd.DataFrame(returned_stock_records, columns=["Return ID", "Stock ID", "Department", "Quantity Returned", "Return Date"]))
        else:
            st.warning("No returned stock records found.")
    elif filter_option == "By Department":
        # Display returned stock records filtered by department
        selected_department = st.selectbox("Select Department:", ["Department A", "Department B", "Department C"])  # Replace with your departments
        returned_stock_records = get_returned_stock_records_by_department(selected_department)  # Implement this function
        if returned_stock_records:
            st.table(pd.DataFrame(returned_stock_records, columns=["Return ID", "Stock ID", "Department", "Quantity Returned", "Return Date"]))
        else:
            st.warning(f"No returned stock records found for {selected_department}.")
    elif filter_option == "By Date":
        # Display returned stock records filtered by date
        selected_date = st.date_input("Select Date:")
        returned_stock_records = get_returned_stock_records_by_date(selected_date)  # Implement this function
        if returned_stock_records:
            st.table(pd.DataFrame(returned_stock_records, columns=["Return ID", "Stock ID", "Department", "Quantity Returned", "Return Date"]))
        else:
            st.warning(f"No returned stock records found for {selected_date}.")

# ... (previous code)

# Update the main app function to include the new pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select Page", ["Dashboard", "Add Stock", "Show Stock", "Remove Stock", "Issue Stock", "Return Stock", "Show Return Stock", "Add Department", "Credits"])

    if page == "Dashboard":
        dashboard()
    elif page == "Add Stock":
        add_stock()
    elif page == "Show Stock":
        show_stock()
    elif page == "Remove Stock":
        remove_stock()
    elif page == "Issue Stock":
        issue_stock()
    elif page == "Return Stock":
        return_stock()
    elif page == "Show Return Stock":
        show_return_stock()
    elif page == "Add Department":
        add_department()
    elif page == "Credits":
        credits_page()

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()
# ... (previous code)

# Define the function for the "Add Department" page
def add_department():
    st.title("Add Department")
    st.write("Here you can add a new department to your inventory management system.")

    # Create input fields for adding a new department
    department_number = st.text_input("Department Number:")
    department_name = st.text_input("Department Name:")
    incharge_name = st.text_input("Incharge Name:")

    if st.button("Add Department"):
        # Add logic here to add a new department to the database
        if add_new_department(department_number, department_name, incharge_name):  # Implement this function
            st.success(f"Successfully added a new department: {department_name} (Department {department_number}).")
        else:
            st.error("Failed to add the department. Please check the information provided.")

# ... (previous code)

# Update the main app function to include the new pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select Page", ["Dashboard", "Add Stock", "Show Stock", "Remove Stock", "Issue Stock", "Return Stock", "Show Return Stock", "Add Department", "Credits"])

    if page == "Dashboard":
        dashboard()
    elif page == "Add Stock":
        add_stock()
    elif page == "Show Stock":
        show_stock()
    elif page == "Remove Stock":
        remove_stock()
    elif page == "Issue Stock":
        issue_stock()
    elif page == "Return Stock":
        return_stock()
    elif page == "Show Return Stock":
        show_return_stock()
    elif page == "Add Department":
        add_department()
    elif page == "Credits":
        credits_page()

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()


# ... (previous code)

# Define a function to display an animation
def display_animation(animation_url):
    lottie_json = requests.get(animation_url)
    if lottie_json.status_code == 200:
        animation_data = lottie_json.json()
        st_lottie(animation_data, key="lottie", height=200, loop=True)
    else:
        st.warning("Failed to load animation.")

# Define the "Add Department" page with HTML and animations
def add_department():
    st.title("Add Department")
    st.write("Here you can add a new department to your inventory management system.")
    
    # Display an animation
    animation_url = "https://assets5.lottiefiles.com/packages/lf20_0w7i3rld.json"  # Replace with your animation URL
    display_animation(animation_url)

    # Create input fields for adding a new department
    department_number = st.text_input("Department Number:")
    department_name = st.text_input("Department Name:")
    incharge_name = st.text_input("Incharge Name:")

    if st.button("Add Department"):
        # Add logic here to add a new department to the database
        if add_new_department(department_number, department_name, incharge_name):  # Implement this function
            st.success(f"Successfully added a new department: {department_name} (Department {department_number}).")
        else:
            st.error("Failed to add the department. Please check the information provided.")

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()
# ... (previous code)

# Define a function to display an animation
def display_animation(animation_url):
    lottie_json = requests.get(animation_url)
    if lottie_json.status_code == 200:
        animation_data = lottie_json.json()
        st_lottie(animation_data, key="lottie", height=200, loop=True)
    else:
        st.warning("Failed to load animation.")

# Define the "Issue Stock" page with HTML and animations
def issue_stock():
    st.title("Issue Stock")
    st.write("Here you can issue stock from your inventory.")
    
    # Display an animation
    animation_url = "https://assets5.lottiefiles.com/packages/lf20_0w7i3rld.json"  # Replace with your animation URL
    display_animation(animation_url)

    # Create input fields for issuing stock
    stock_id = st.text_input("Stock ID:")
    department_number = st.text_input("Department Number:")
    quantity = st.number_input("Quantity:", min_value=1)
    issue_date = st.date_input("Issue Date:")

    if st.button("Issue Stock"):
        # Add logic here to issue stock
        if issue_stock_logic(stock_id, department_number, quantity, issue_date):  # Implement this function
            st.success(f"Stock successfully issued: {quantity} units from Stock ID {stock_id}.")
        else:
            st.error("Failed to issue stock. Please check the information provided.")

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()
# ... (previous code)

# Define the "Return Stock" page with HTML and animations
def return_stock():
    st.title("Return Stock")
    st.write("Here you can return stock to your inventory.")
    
    # Display an animation
    animation_url = "https://assets5.lottiefiles.com/packages/lf20_0w7i3rld.json"  # Replace with your animation URL
    display_animation(animation_url)

    # Create input fields for returning stock
    stock_id = st.text_input("Stock ID:")
    department_number = st.text_input("Department Number:")
    quantity = st.number_input("Quantity Returned:", min_value=1)
    return_date = st.date_input("Return Date:")

    if st.button("Return Stock"):
        # Add logic here to return stock
        if return_stock_logic(stock_id, department_number, quantity, return_date):  # Implement this function
            st.success(f"Stock successfully returned: {quantity} units to Stock ID {stock_id}.")
        else:
            st.error("Failed to return stock. Please check the information provided.")

# Define the "Show Returned Stock" page with HTML and animations
def show_returned_stock():
    st.title("Show Returned Stock")
    st.write("Here you can view the stock that has been returned.")

    # Display an animation
    animation_url = "https://assets5.lottiefiles.com/packages/lf20_0w7i3rld.json"  # Replace with your animation URL
    display_animation(animation_url)

    # Add logic here to retrieve and display returned stock data
    returned_stock_data = retrieve_returned_stock_data()  # Implement this function
    if returned_stock_data:
        st.table(returned_stock_data)
    else:
        st.warning("No returned stock data available.")

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()
# ... (previous code)

# Define the "Add Department" page with HTML and animations
def add_department():
    st.title("Add Department")
    st.write("Here you can add a new department to your inventory system.")
    
    # Display an animation
    animation_url = "https://assets5.lottiefiles.com/packages/lf20_0w7i3rld.json"  # Replace with your animation URL
    display_animation(animation_url)

    # Create input fields for adding a department
    department_number = st.text_input("Department Number:")
    department_name = st.text_input("Department Name:")
    incharge_name = st.text_input("Incharge Name:")

    if st.button("Add Department"):
        # Add logic here to add a new department
        if add_department_logic(department_number, department_name, incharge_name):  # Implement this function
            st.success(f"Department {department_number}: {department_name} added successfully.")
        else:
            st.error("Failed to add the department. Please check the information provided.")

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()
# ... (previous code)

# Define the "Show Department" page with HTML and animations
def show_department():
    st.title("Show Departments")
    st.write("Here you can view the list of departments in your inventory system.")
    
    # Display an animation
    animation_url = "https://assets5.lottiefiles.com/packages/lf20_0w7i3rld.json"  # Replace with your animation URL
    display_animation(animation_url)

    # Add logic here to retrieve and display department data
    department_data = retrieve_department_data()  # Implement this function
    if department_data:
        st.table(department_data)
    else:
        st.warning("No department data available.")

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()
# ... (previous code)

# Define the "Remove Department" page with HTML and animations
def remove_department():
    st.title("Remove Department")
    st.write("Here you can remove a department from your inventory system.")
    
    # Display an animation
    animation_url = "https://assets5.lottiefiles.com/packages/lf20_0w7i3rld.json"  # Replace with your animation URL
    display_animation(animation_url)

    # Create input field for department number to be removed
    department_number_to_remove = st.text_input("Enter Department Number to Remove:")

    if st.button("Remove Department"):
        # Add logic here to remove the department
        if remove_department_logic(department_number_to_remove):  # Implement this function
            st.success(f"Department {department_number_to_remove} removed successfully.")
        else:
            st.error("Failed to remove the department. Please check the department number.")

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()
# ... (previous code)

# Define the "Add Department" page with HTML and animations
def add_department():
    st.title("Add Department")
    st.write("Here you can add a new department to your inventory system.")
    
    # Display an animation
    animation_url = "https://assets5.lottiefiles.com/packages/lf20_0w7i3rld.json"  # Replace with your animation URL
    display_animation(animation_url)

    # Create input fields for department details
    department_number = st.text_input("Department Number:")
    department_name = st.text_input("Department Name:")
    incharge_name = st.text_input("Incharge Name:")

    if st.button("Add Department"):
        # Add logic here to add the department
        if add_department_logic(department_number, department_name, incharge_name):  # Implement this function
            st.success(f"Department {department_number} added successfully.")
        else:
            st.error("Failed to add the department. Please check the input data.")

# ... (previous code)

# Run the main app function
if __name__ == "__main__":
    main()






