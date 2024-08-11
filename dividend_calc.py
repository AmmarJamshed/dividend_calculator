#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import re

# Function to parse the text input and extract relevant information
def parse_dividend_info(text):
    info = {}
    info['company_name'] = re.search(r'Company Name:\s*(.*)', text).group(1).strip()
    info['symbol'] = re.search(r'Symbol:\s*(.*)', text).group(1).strip()
    info['announcement_date'] = re.search(r'Announcement Date:\s*(.*)', text).group(1).strip()
    info['dividend_percent'] = float(re.search(r'Dividend \(%\):\s*(\d+)', text).group(1).strip())
    info['net_quantity'] = int(re.search(r'Net Quantity:\s*(\d+)', text).group(1).strip())
    info['share_price'] = float(re.search(r'Share Price:\s*(\d+\.\d+)', text).group(1).strip())
    return info

# Assuming face value is known (commonly it's 10 PKR in Pakistan)
FACE_VALUE = 10

# Function to calculate dividend
def calculate_dividend(net_quantity, dividend_percent):
    dividend_per_share = FACE_VALUE * (dividend_percent / 100)
    total_dividend = net_quantity * dividend_per_share
    return total_dividend

# Streamlit app layout
st.title("Dividend Calculator")

# Input text
st.sidebar.header("Enter Dividend Announcement Text")
input_text = st.sidebar.text_area(
    "Paste the announcement text here. Ensure you include 'Share Price: <price>' in the text", 
    height=300,
    value="""This is to inform you that following Company has announced result for the period ended 30-JUN-24, (Interim).
As you are holding 19 shares in your trading Account maintained with BMA Capital Management Limited, you are entitled for the below mentioned announced benefits.

Company Name:                     NESTLE PAKISTAN LIMITED
Announcement Date:             25-Jul-24
Dividend (%):                           1110
Bonus (%):                               0
Rights (%):                               0
Book Closure Start Date:       07-AUG-24
Book Closure End Date:         09-AUG-24
BMA Trading A/C #:               19311
Account Title:                         Muhammad Ammar Jamshed
CDC Sub A/C #:                       180281
Symbol:                                   NESTLE
Net Quantity:                          19
Share Price:                           7200.00"""
)

# Process input text
if input_text:
    # Parse the information
    dividend_info = parse_dividend_info(input_text)

    st.write(f"**Company Name:** {dividend_info['company_name']}")
    st.write(f"**Symbol:** {dividend_info['symbol']}")
    st.write(f"**Announcement Date:** {dividend_info['announcement_date']}")
    st.write(f"**Dividend Percentage:** {dividend_info['dividend_percent']}%")
    st.write(f"**Net Quantity:** {dividend_info['net_quantity']}")
    st.write(f"**Share Price:** {dividend_info['share_price']}")

    # Calculate dividend
    dividend = calculate_dividend(dividend_info['net_quantity'], dividend_info['dividend_percent'])
    
    # Display dividend
    st.write(f"**Total Dividend Amount:** {dividend}")
else:
    st.write("Please enter the dividend announcement text to proceed.")



