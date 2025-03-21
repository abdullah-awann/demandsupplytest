import streamlit as st
import altair as alt
import pandas as pd

# Title
st.title("Demand and Supply Matrix")
st.write("This app visualizes the demand and supply matrix with four quadrants based on input metrics.")

# User inputs for demand and supply metrics
total_games = st.number_input("Total games in the family", min_value=0, value=10)
total_downloads = st.number_input("Total family downloads", min_value=0, value=100000)
per_day_installs = st.number_input("Total per day installs of the family", min_value=0, value=5000)
last_30_days_downloads = st.number_input("Last 30 days downloads of the family", min_value=0, value=150000)
games_above_50k_installs = st.number_input("Number of games in the family getting more than 50K per day installs", min_value=0, value=2)

# Calculate demand and supply based on inputs
def calculate_demand(total_downloads, last_30_days_downloads, games_above_50k_installs):
    return (total_downloads * 0.4 + last_30_days_downloads * 0.4 + games_above_50k_installs * 0.2) / 1000000 * 100

def calculate_supply(total_games, per_day_installs):
    return (total_games * 0.5 + per_day_installs * 0.5) / 10000 * 100

demand = min(100, calculate_demand(total_downloads, last_30_days_downloads, games_above_50k_installs))
supply = min(100, calculate_supply(total_games, per_day_installs))

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
points = pd.DataFrame({
    'Demand': [demand],
    'Supply': [supply],
    'Quadrant': [quadrant]
})

# Background quadrants data
quadrant_data = pd.DataFrame({
    'x': [25, 75, 25, 75],
    'y': [25, 25, 75, 75],
    'label': [
        'Low Demand\nLow Supply',
        'Low Demand\nHigh Supply',
        'High Demand\nLow Supply',
        'High Demand\nHigh Supply'
    ],
    'color': ['#D3D3D3', '#FFD700', '#87CEFA', '#90EE90']
})

# Create background quadrants
background = alt.Chart(quadrant_data).mark_rect(opacity=0.3).encode(
    x=alt.X('x:Q', bin=alt.Bin(extent=[0, 100], step=50), title='Supply'),
    y=alt.Y('y:Q', bin=alt.Bin(extent=[0, 100], step=50), title='Demand'),
    color=alt.Color('color:N', scale=None, legend=None)
)

# Add quadrant labels
labels = alt.Chart(quadrant_data).mark_text(size=16, fontWeight='bold').encode(
    x='x:Q',
    y='y:Q',
    text='label:N'
)

# Point for user input
demand_supply_point = alt.Chart(points).mark_circle(size=300, color='red').encode(
    x='Supply:Q',
    y='Demand:Q',
    tooltip=['Demand', 'Supply', 'Quadrant']
)

# Combine charts
final_chart = (background + labels + demand_supply_point).properties(
    width=700,
    height=700,
    title="Demand and Supply Matrix"
)

# Display chart
st.altair_chart(final_chart)

# Display quadrant details
st.write("### Quadrant Definitions")
st.write("1. **Low Demand and Low Supply (Bottom Left)**: Both demand and supply are below the midpoint.")
st.write("2. **Low Demand and High Supply (Bottom Right)**: Demand is below the midpoint, but supply is above.")
st.write("3. **High Demand and Low Supply (Top Left)**: Demand is above the midpoint, but supply is below.")
st.write("4. **High Demand and High Supply (Top Right)**: Both demand and supply are above the midpoint.")
