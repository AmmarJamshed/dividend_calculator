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

# Function to parse the text input and extract relevant information
def parse_dividend_info(text):
    info = {}
    
    # Search for company name
    company_match = re.search(r'Company Name:\s*(.*)', text)
    if company_match:
        info['company_name'] = company_match.group(1).strip()
    else:
        st.error("Company Name not found in the input text.")
    
    # Search for symbol
    symbol_match = re.search(r'Symbol:\s*(.*)', text)
    if symbol_match:
        info['symbol'] = symbol_match.group(1).strip()
    else:
        st.error("Symbol not found in the input text.")
    
    # Search for announcement date
    announcement_date_match = re.search(r'Announcement Date:\s*(.*)', text)
    if announcement_date_match:
        info['announcement_date'] = announcement_date_match.group(1).strip()
    else:
        st.error("Announcement Date not found in the input text.")
    
    # Search for dividend percentage
    dividend_percent_match = re.search(r'Dividend \(%\):\s*(\d+)', text)
    if dividend_percent_match:
        info['dividend_percent'] = float(dividend_percent_match.group(1).strip())
    else:
        st.error("Dividend Percentage not found in the input text.")
    
    # Search for net quantity
    net_quantity_match = re.search(r'Net Quantity:\s*(\d+)', text)
    if net_quantity_match:
        info['net_quantity'] = int(net_quantity_match.group(1).strip())
    else:
        st.error("Net Quantity not found in the input text.")
    
    # Search for share price
    share_price_match = re.search(r'Share Price:\s*(\d+\.\d+)', text)
    if share_price_match:
        info['share_price'] = float(share_price_match.group(1).strip())
    else:
        st.error("Share Price not found in the input text.")
    
    return info

# Streamlit app layout
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

# Process input text
if input_text:
    # Parse the information
    dividend_info = parse_dividend_info(input_text)

    if dividend_info:
        # Display information with colors
        st.markdown(f"## Company Name: <span style='color:green'>{dividend_info.get('company_name', 'N/A')}</span>", unsafe_allow_html=True)
        st.markdown(f"### Symbol: <span style='color:orange'>{dividend_info.get('symbol', 'N/A')}</span>", unsafe_allow_html=True)
        st.markdown(f"#### Announcement Date: <span style='color:blue'>{dividend_info.get('announcement_date', 'N/A')}</span>", unsafe_allow_html=True)
        st.markdown(f"#### Dividend Percentage: <span style='color:purple'>{dividend_info.get('dividend_percent', 'N/A')}%</span>", unsafe_allow_html=True)
        st.markdown(f"#### Net Quantity: <span style='color:red'>{dividend_info.get('net_quantity', 'N/A')}</span>", unsafe_allow_html=True)
        st.markdown(f"#### Share Price: <span style='color:brown'>{dividend_info.get('share_price', 'N/A')}</span>", unsafe_allow_html=True)

        # Calculate dividend
        dividend = calculate_dividend(dividend_info['net_quantity'], dividend_info['dividend_percent'])
        
        # Display dividend result with success message
        st.success(f"**Total Dividend Amount:** PKR {dividend}")
    else:
        st.warning("The input text is missing some required information.")
else:
    st.warning("Please enter the dividend announcement text to proceed.")
