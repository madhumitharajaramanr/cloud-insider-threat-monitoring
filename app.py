import streamlit as st
import csv
import os

# CSV file to store logs
LOG_FILE = "activity_logs.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["User", "Login_Hour", "File_Accessed", "Status"])

# Predefined rules
ALLOWED_START = 9
ALLOWED_END = 18
AUTHORIZED_FILES = ["file1.txt", "file2.txt"]

def check_activity(login_hour, file_accessed):
    if login_hour < ALLOWED_START or login_hour > ALLOWED_END:
        return "⚠ Suspicious Login Time"
    if file_accessed not in AUTHORIZED_FILES:
        return "⚠ Unauthorized File Access"
    return "✅ Normal Activity"

# ---------------- Streamlit UI ----------------
st.title("☁️ Cloud Activity Monitoring Prototype (CSV Version)")

user = st.text_input("User Name")
login_hour = st.number_input("Login Hour (0-23)", min_value=0, max_value=23)
file_accessed = st.text_input("File Accessed")

if st.button("Submit Activity"):
    status = check_activity(login_hour, file_accessed)
    
    # Save activity to CSV
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user, login_hour, file_accessed, status])
    
    st.subheader("Activity Status")
    st.write(status)

# Display all logs
st.subheader("📊 Activity Logs")
with open(LOG_FILE, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        st.write(row)
