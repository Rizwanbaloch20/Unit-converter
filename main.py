import streamlit as st

# App Title and Description
st.title("🌍 Welcome to  Unit Converter!")
st.markdown("Convert between **Length**, **Weight**, and **Time** in just a few clicks! 🚀")
st.write("Choose a category below, enter your value, and see the magic happen. ✨")

# Choose Category
category = st.selectbox("🔎 What would you like to convert today?", ["Length", "Weight", "Time"])

# Choose Conversion Type Based on Category
if category == "Length":
    unit = st.selectbox("📏 Select a conversion type:", [
        "Kilometers ➡️ Miles", 
        "Miles ➡️ Kilometers"
    ])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select a conversion type:", [
        "Kilograms ➡️ Pounds", 
        "Pounds ➡️ Kilograms"
    ])
elif category == "Time":
    unit = st.selectbox("⏰ Select a conversion type:", [
        "Seconds ➡️ Minutes", 
        "Minutes ➡️ Seconds", 
        "Minutes ➡️ Hours", 
        "Hours ➡️ Minutes", 
        "Hours ➡️ Seconds", 
        "Seconds ➡️ Hours"
    ])

# Input Value
value = st.number_input("✍️ Enter the value you want to convert:", min_value=0.0)

# Conversion Function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers ➡️ Miles":
            return value * 0.621371
        elif unit == "Miles ➡️ Kilometers":
            return value / 0.621371
    elif category == "Weight":
        if unit == "Kilograms ➡️ Pounds":
            return value * 2.20462
        elif unit == "Pounds ➡️ Kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds ➡️ Minutes":
            return value / 60
        elif unit == "Minutes ➡️ Seconds":
            return value * 60
        elif unit == "Minutes ➡️ Hours":
            return value / 60
        elif unit == "Hours ➡️ Minutes":
            return value * 60
        elif unit == "Hours ➡️ Seconds":
            return value * 3600
        elif unit == "Seconds ➡️ Hours":
            return value / 3600
    return None

# Convert Button
if st.button("🔄 Convert Now!"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"✅ Result: **{result:.2f}**")
    else:
        st.error("Oops! Something went wrong. Please check your inputs.")

# Footer
st.markdown("---")
st.caption("Made By  ❤️ Rizwan Ahmed")
