import streamlit
import pandas

streamlit.title("My Parents New Health Dinner")

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# read file from S3 bucket
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# user interactive widget called a Multi-select that will allow users to pick the fruits they want in their smoothies
streamlit.multiselect("Pick Some Fruits: ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

# streamlit display dataframe
streamlit.dataframe(my_fruit_list)
