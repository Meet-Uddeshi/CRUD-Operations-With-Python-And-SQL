# Step 1 => Import required libraries
import mysql.connector 
import streamlit as st

# Step 2 => Create main function for CRUD operations
def main():
    
# Step 3 => Details of database and connection
    database_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Madhav@123",
        database="crud"
    )
    database_cursor = database_connection.cursor()
    print("Connection established")

# Step 4 => CRUD operation functions 
    st.title("CRUD Operations with Python & SQL")
    operation = st.sidebar.selectbox("Select an Operation", ("CREATE", "READ", "UPDATE", "DELETE"))

# Step 5 => CRUD operation = "CREATE"
    if operation == "CREATE":
        st.subheader("Create Record")
        name_input = st.text_input("Enter Your Name")
        email_input = st.text_input("Enter Your Email")
        if st.button("CREATE"):
            sql_query = "insert into users (name, email) values (%s, %s)"
            values = (name_input, email_input)
            database_cursor.execute(sql_query, values)
            database_connection.commit()
            st.success("RECORD CREATED SUCCESSFULLY")

# Step 6 => CRUD operation = "READ"
    elif operation == "READ":
        st.subheader("Read Record")
        database_cursor.execute("select * from users")
        records = database_cursor.fetchall()
        for record in records:
            st.write(record)
            st.divider()
            
# Step 7 => CRUD operation = "UPDATE"
    elif operation == "UPDATE":
        st.subheader("Update Record")
        user_id = st.number_input("Enter ID")
        new_name = st.text_input("Enter New Name")
        new_email = st.text_input("Enter New Email")
        if st.button("UPDATE"):
            sql_update = "update users set name=%s, email=%s where id=%s"
            updated_values = (new_name, new_email, user_id)
            database_cursor.execute(sql_update, updated_values)
            database_connection.commit()
            st.success("RECORD UPDATED SUCCESSFULLY")

# Step 8 => CRUD operation = "DELETE"
    elif operation == "DELETE":
        st.subheader("Delete Record")
        user_id = st.number_input("Enter ID")
        if st.button("DELETE"):
            sql_delete = "delete from users where id=%s"
            delete_value = (user_id,)
            database_cursor.execute(sql_delete, delete_value)
            database_connection.commit()
            st.success("RECORD DELETED SUCCESSFULLY")

if __name__ == "__main__":
    main()
