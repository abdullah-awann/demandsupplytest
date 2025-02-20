
import streamlit as st
import matplotlib.pyplot as plt

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

# Plotting the matrix
fig, ax = plt.subplots(figsize=(10, 8))

# Draw grid lines
ax.axhline(50, color='black', linewidth=1)
ax.axvline(50, color='black', linewidth=1)

# Scatter plot for the current point
ax.scatter(supply, demand, color='red', s=100, label='Current Point')

# Labels and limits
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_xlabel("Supply")
ax.set_ylabel("Demand")
ax.set_title("Demand and Supply Matrix")

# Quadrant labels
ax.text(25, 75, "Low Demand\nLow Supply", ha='center', fontsize=12)
ax.text(75, 75, "Low Demand\nHigh Supply", ha='center', fontsize=12)
ax.text(25, 25, "High Demand\nLow Supply", ha='center', fontsize=12)
ax.text(75, 25, "High Demand\nHigh Supply", ha='center', fontsize=12)

ax.legend()
st.pyplot(fig)
