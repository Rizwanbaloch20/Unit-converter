import streamlit as st

st.title("🌍Unit Converter")
st.markdown("### convert Length, Weight, and Temperature")
st.write("This is a simple unit converter app built with Streamlit.")

category = st.selectbox("select a category " , ["Length, weight, Temperature"])
def convert_units(category,value ,unit):
    if category == "Length":
        if unit == "kilo Meters to miles":
            return value * 0.621371
        elif unit == "miles to kilo Meters":
            return value / 0.621371
        elif category == "weight":
            if unit == "kilo grams to pounds":
                return value * 2.20462
            elif unit == "pounds to kilo grams":
                return value / 2.20462
            elif category == "Time":
                if unit == "seconds to minutes":
                    return value / 60
                elif unit == "minutes to seconds":
                    return value * 60
                elif unit == "minutes to hours":
                    return value / 60
                elif unit == "hours to minutes":
                    return value * 60
                elif unit == "hours to seconds":
                    return value * 3600
                elif unit == "seconds to hours":
                    return value / 3600
                return 0
        
if category == "Length":
    unit = st.selectbox("select a unit", ["kilo Meters to miles", "miles to kilo Meters"])
elif category == "weight":
    unit = st.selectbox("⚖select a unit", ["kilo grams to pounds", "pounds to kilo grams"]) 
elif category == "Time":
    unit = st.selectbox("⏰select a unit", ["seconds to minutes", "minutes to seconds", "minutes to hours", "hours to minutes", "hours to seconds", "seconds to hours"])
    value = st.number_input("Enter the value to convert") 

    if st.button("Convert"):
        result = convert_units(category, value, unit)
        st.success(f"The converted value is: {result:.2f}")