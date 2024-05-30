import streamlit as st

# Title and description
st.title("Cholesterol-Lowering Food Suggestions")
st.write("""
### Welcome to the Cholesterol-Lowering Food Suggestions App
This application helps you choose foods that can help lower your cholesterol levels. 
Enter your dietary preferences, total daily calorie intake, and current cholesterol level to get personalized recommendations.
""")

# User inputs
dietary_preferences = st.multiselect(
    "Dietary Preferences (select all that apply)",
    ["Vegetarian", "Vegan", "Pescatarian", "Gluten-Free", "Dairy-Free", "Low-Carb", "None"]
)
total_calories = st.number_input("Total Daily Calorie Intake", min_value=1000, max_value=4000, value=2000)
current_cholesterol = st.number_input("Current Cholesterol Level (mg/dL)", min_value=100, max_value=500, value=200)

# Food suggestions based on dietary preferences and cholesterol-lowering benefits
def get_food_suggestions(dietary_preferences, total_calories, current_cholesterol):
    suggestions = []
    
    if "Vegetarian" in dietary_preferences or "None" in dietary_preferences:
        suggestions.extend(["Oats", "Barley", "Beans", "Eggplant", "Nuts", "Vegetable oils", "Fruits (especially apples, grapes, strawberries, citrus fruits)"])
    
    if "Vegan" in dietary_preferences:
        suggestions.extend(["Oats", "Barley", "Beans", "Nuts", "Vegetable oils", "Fruits (especially apples, grapes, strawberries, citrus fruits)", "Soy-based foods", "Leafy greens"])
    
    if "Pescatarian" in dietary_preferences:
        suggestions.extend(["Oats", "Barley", "Beans", "Nuts", "Vegetable oils", "Fruits (especially apples, grapes, strawberries, citrus fruits)", "Fish (especially fatty fish like salmon, mackerel, and sardines)"])
    
    if "Gluten-Free" in dietary_preferences:
        suggestions.extend(["Gluten-free oats", "Beans", "Nuts", "Vegetable oils", "Fruits", "Quinoa", "Buckwheat"])
    
    if "Dairy-Free" in dietary_preferences:
        suggestions.extend(["Oats", "Barley", "Beans", "Nuts", "Vegetable oils", "Fruits", "Leafy greens"])
    
    if "Low-Carb" in dietary_preferences:
        suggestions.extend(["Nuts", "Vegetable oils", "Avocados", "Fish", "Leafy greens", "Non-starchy vegetables"])
    
    # Default healthy options if no specific preference
    if not dietary_preferences or "None" in dietary_preferences:
        suggestions.extend(["Oats", "Barley", "Beans", "Nuts", "Vegetable oils", "Fruits", "Fish", "Leafy greens"])
    
    return suggestions

# Get and display food suggestions
food_suggestions = get_food_suggestions(dietary_preferences, total_calories, current_cholesterol)
st.subheader("Recommended Foods to Lower Cholesterol:")
for food in set(food_suggestions):
    st.write(f"- {food}")
