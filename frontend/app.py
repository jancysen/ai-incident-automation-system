import streamlit as st
import requests

st.title("🚀 AI Incident Automation Dashboard")

st.header("Create New Incident Ticket")

title = st.text_input("Title")
description = st.text_area("Description")
system = st.text_input("System (Auth/DB/UI)")

if st.button("Create Ticket"):

    data = {
        "title": title,
        "description": description,
        "system": system
    }

    response = requests.post(
        "http://127.0.0.1:8000/create-ticket",
        json=data
    )

    if response.status_code == 200:
        result = response.json()

        st.success("Ticket Created Successfully!")

        st.subheader("📊 Incident Analysis")

        st.write("**Ticket ID:**", result["ticket_id"])
        st.write("**Assigned Team:**", result["assigned_team"])
        st.write("**Severity:**", result["severity"])
        st.write("**Log:**", result["log"])
        st.write("**Root Cause:**", result["root_cause"])

        st.subheader("🤖 AI Suggestion")
        st.write(result["ai_suggestion"])

    else:
        st.error("Error creating ticket")
