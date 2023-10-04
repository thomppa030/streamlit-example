from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate movement speed
def calculate_movement_speed(scale_factor, dexterity_multiplier, dexterity, base_speed):
    return scale_factor * np.log(dexterity_multiplier * dexterity + 1) + base_speed

# Streamlit app
st.title('Movement Speed Calculator')

# Sidebar for input parameters
st.sidebar.header('Input Parameters')
scale_factor = st.sidebar.slider('Scale Factor', 0.0, 10.0, 1.0, 0.1)
dexterity_multiplier = st.sidebar.slider('Dexterity Multiplier', 0.0, 10.0, 1.0, 0.1)
dexterity = st.sidebar.slider('Dexterity', 1, 100, 10)
base_speed = st.sidebar.slider('Base Speed', 0, 100, 10)

# Calculate movement speed
movement_speed = calculate_movement_speed(scale_factor, dexterity_multiplier, dexterity, base_speed)

# Display movement speed
st.write(f'Movement Speed: {movement_speed:.2f}')

# Plot graph
dexterities = np.arange(1, 101, 1)
movement_speeds = calculate_movement_speed(scale_factor, dexterity_multiplier, dexterities, base_speed)

plt.figure(figsize=(10, 6))
plt.plot(dexterities, movement_speeds, label='Movement Speed')

plt.xlabel('Dexterity')
plt.ylabel('Movement Speed')
plt.title('Movement Speed Based on Dexterity')
plt.legend()
plt.grid(True)

st.pyplot(plt.gcf())

### Updated Streamlit App with Multiple Pages:
```python
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate movement speed
def calculate_movement_speed(scale_factor, dexterity_multiplier, dexterity, base_speed):
    return scale_factor * np.log(dexterity_multiplier * dexterity + 1) + base_speed

# Page 1: Movement Speed Calculator
def movement_speed_calculator():
    st.title('Movement Speed Calculator')

    # Sidebar for input parameters
    st.sidebar.header('Input Parameters')
    scale_factor = st.sidebar.slider('Scale Factor', 0.0, 10.0, 1.0, 0.1)
    dexterity_multiplier = st.sidebar.slider('Dexterity Multiplier', 0.0, 10.0, 1.0, 0.1)
    dexterity = st.sidebar.slider('Dexterity', 1, 100, 10)
    base_speed = st.sidebar.slider('Base Speed', 0, 100, 10)

    # Calculate movement speed
    movement_speed = calculate_movement_speed(scale_factor, dexterity_multiplier, dexterity, base_speed)

    # Display movement speed
    st.write(f'Movement Speed: {movement_speed:.2f}')

    # Plot graph
    dexterities = np.arange(1, 101, 1)
    movement_speeds = calculate_movement_speed(scale_factor, dexterity_multiplier, dexterities, base_speed)

    plt.figure(figsize=(10, 6))
    plt.plot(dexterities, movement_speeds, label='Movement Speed')
    plt.xlabel('Dexterity')
    plt.ylabel('Movement Speed')
    plt.title('Movement Speed Based on Dexterity')
    plt.legend()
    plt.grid(True)

    st.pyplot(plt.gcf())

# Function to calculate max health based on the provided formula
def calculate_max_health(starting_health, growth_rate, character_level, attribute_influence, primary_attribute):
    return starting_health * (1 + growth_rate) * (character_level + attribute_influence * primary_attribute)

# Page 2: Another Feature or Information
def another_page():
    st.write('This is another page where you can add more features or information.')
    # Streamlit app
    st.title('Max Health Calculator')

    # Sidebar for input parameters
    st.sidebar.header('Input Parameters')
    starting_health = st.sidebar.slider('Starting Health', 50, 200, 100)
    growth_rate = st.sidebar.slider('Growth Rate', 0.0, 1.0, 0.1, 0.01)
    character_level = st.sidebar.slider('Character Level', 1, 50, 1)
    attribute_influence = st.sidebar.slider('Attribute Influence', 0.0, 2.0, 0.5, 0.1)
    primary_attribute = st.sidebar.slider('Primary Attribute', 1, 100, 10)

    # Calculate max health
    max_health = calculate_max_health(starting_health, growth_rate, character_level, attribute_influence, primary_attribute)

    # Display max health
    st.write(f'Max Health: {max_health:.2f}')

    # Plot graph
    levels = np.arange(1, 51, 1)
    attributes = np.arange(1, 101, 10)
    X, Y = np.meshgrid(levels, attributes)
    Z = calculate_max_health(starting_health, growth_rate, X, attribute_influence, Y)

    plt.figure(figsize=(10, 6))
    for attribute in attributes:
        max_healths = calculate_max_health(starting_health, growth_rate, levels, attribute_influence, attribute)
        plt.plot(levels, max_healths, label=f'Attribute {attribute}')

    plt.xlabel('Character Level')
    plt.ylabel('Max Health')
    plt.title('Max Health Growth Over Levels')
    plt.legend(title='Attributes', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)

    st.pyplot(plt.gcf())

# Main function to select pages
def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio('Go to', ['Movement Speed Calculator', 'Another Page'])

    if selection == 'Movement Speed Calculator':
        movement_speed_calculator()
    elif selection == 'Another Page':
        another_page()

# Run the main function
if __name__ == '__main__':
    main()

