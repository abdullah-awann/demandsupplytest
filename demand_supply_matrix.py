import streamlit as st
import altair as alt
import pandas as pd

# Title
st.title("Demand and Supply Matrix")
st.write("This app visualizes the demand and supply matrix with four quadrants.")

# User inputs for demand and supply
demand = st.slider("Select Demand", 0, 100, 50)
supply = st.slider("Select Supply", 0, 100, 50)

# Function to determine quadrant
def get_quadrant(demand, supply):
    if demand <= 50 and supply <= 50:
        return "Low Demand and Low Supply"
    elif demand <= 50 and supply > 50:
        return "Low Demand and High Supply"
    elif demand > 50 and supply <= 50:
        return "High Demand and Low Supply"
    else:
        return "High Demand and High Supply"

quadrant = get_quadrant(demand, supply)
st.write(f"### Current Quadrant: {quadrant}")

# Create a DataFrame for plotting
data = pd.DataFrame({
    'Demand': [demand],
    'Supply': [supply],
    'Quadrant': [quadrant]
})

# Altair chart for visualization
chart = alt.Chart(data).mark_circle(size=200, color='red').encode(
    x=alt.X('Supply:Q', scale=alt.Scale(domain=[0, 100]), title='Supply'),
    y=alt.Y('Demand:Q', scale=alt.Scale(domain=[0, 100]), title='Demand'),
    tooltip=['Demand', 'Supply', 'Quadrant']
).properties(
    width=600,
    height=600,
    title="Demand and Supply Matrix"
)

# Add quadrant background
background = alt.Chart(pd.DataFrame({
    'x': [50, 50, 0, 100],
    'y': [0, 100, 50, 50],
    'label': ['Low Demand\nLow Supply', 'Low Demand\nHigh Supply', 'High Demand\nLow Supply', 'High Demand\nHigh Supply']
})).mark_text(size=14, opacity=0.5).encode(
    x='x:Q',
    y='y:Q',
    text='label:N'
)

# Display chart with background
st.altair_chart(background + chart)

# Display quadrant details
st.write("### Quadrant Definitions")
st.write("1. **Low Demand and Low Supply**: Both demand and supply are below the midpoint.")
st.write("2. **Low Demand and High Supply**: Demand is below the midpoint, but supply is above.")
st.write("3. **High Demand and Low Supply**: Demand is above the midpoint, but supply is below.")
st.write("4. **High Demand and High Supply**: Both demand and supply are above the midpoint.")
