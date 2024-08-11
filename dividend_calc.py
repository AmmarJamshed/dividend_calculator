#!/usr/bin/env python
# coding: utf-8

# In[1]:
import streamlit as st

# Inject custom CSS to style the app
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f8ff;
        color: #00008b;
    }
    h1 {
        color: #008080;
    }
    h2 {
        color: #800080;
    }
    .stAlert {
        background-color: #e0ffff;
    }
    .stButton>button {
        color: white;
        background-color: #ff4b4b;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and header with custom colors
st.title("🎨 Colorful Dividend Calculator")
st.header("📈 Stock Information")

# Sidebar input for text area
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

# Process input text
if input_text:
    # Parse the information
    dividend_info = parse_dividend_info(input_text)

    # Display information with colors
    st.markdown(f"## Company Name: <span style='color:green'>{dividend_info['company_name']}</span>", unsafe_allow_html=True)
    st.markdown(f"### Symbol: <span style='color:orange'>{dividend_info['symbol']}</span>", unsafe_allow_html=True)
    st.markdown(f"#### Announcement Date: <span style='color:blue'>{dividend_info['announcement_date']}</span>", unsafe_allow_html=True)
    st.markdown(f"#### Dividend Percentage: <span style='color:purple'>{dividend_info['dividend_percent']}%</span>", unsafe_allow_html=True)
    st.markdown(f"#### Net Quantity: <span style='color:red'>{dividend_info['net_quantity']}</span>", unsafe_allow_html=True)
    st.markdown(f"#### Share Price: <span style='color:brown'>{dividend_info['share_price']}</span>", unsafe_allow_html=True)

    # Calculate dividend
    dividend = calculate_dividend(dividend_info['net_quantity'], dividend_info['dividend_percent'])
    
    # Display dividend result with success message
    st.success(f"**Total Dividend Amount:** PKR {dividend}")
else:
    st.warning("Please enter the dividend announcement text to proceed.")

# Using color picker widget to choose a color (just for fun)
color = st.color_picker("Pick A Color for Your Mood", "#00f900")
st.write("The selected color is", color)

# Example of using a button with custom styles
if st.button("🎉 Calculate Dividend Again"):
    st.write("Calculation done!")




