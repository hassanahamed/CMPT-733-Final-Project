import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go
from streamlit_searchbox import st_searchbox
from recipe_recommend import get_recipes

st.set_page_config(initial_sidebar_state='expanded')
# import the data set
cusine_products=pd.read_csv('product_cusine_df.csv')
pr_infer_json=pd.read_json('pr_infer_df.json')
pr_infer_json=pr_infer_json.reset_index()
prods_rec_map=pd.read_json('prods_rec_map.json')
prod_list = [i.lower() for i in list(prods_rec_map["name"])]
product_cusine_df=pd.read_csv('product_cusine_df.csv')
# Define a function for each page
def speed_chart(data):
    col = list(st.columns(len(data)))
    for i in range(len(data)):
        fig1 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = int(data[i][1]),
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': data[i][0]}))
        fig1.update_layout(width=250, height=250)
        col[i].plotly_chart(fig1)

def home():
    st.title("Grocery data analysis and user recommendation")
    # Speed Charts
    # DataSet
    dataset = st.selectbox('Select a dataset', ['Instacart Dataset', 'BBC Good Food Recipes','Cusines'])
    # Display the selected dataset
    if dataset =='Instacart Dataset':
        data=[('users',206209),('orders',3421083),('products',49688)]
        speed_chart(data)
    elif dataset == 'BBC Good Food Recipes':
        data=[('recipes',10028),('ingredients',8701)]
        speed_chart(data)
    else:
        data=[('Cusines',13)]
        speed_chart(data)

    #graphs
    st.title("Visualizations")
    path = "image_folder/"
    image_files = []
    # Iterate through all the files in the folder
    for filename in os.listdir(path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_files.append(os.path.join(path, filename))

    text=["Majority of the products purchased are from produce department followed by diary & eggs.","Most users have placed less the 10 orders, while some of users have ordered more than 100 times.","From this Word cloud we see the top products interms of sales. Interestly, the most sold item is Banana","Most of orders were placed on Sundays around 2 PM, followed by Mondays 10 AM","Produce orders are nearly 10 times higher than meat and egg orders combined.","From the above graph we can see that people are prefering to buy organic products, mainly in produce section.","Users of this application are consuming more fruits/vegetables than snack products.","Most of the orders were placed in one month in intervals, followed by weekly orders","From user history we can say that most users’ orders are equally divided between first time ordering products and reordered products.","Most of the users are buyinh American and Italian products. But there there many customers who are trying international products from cuisines like Indian, Mexican etc."]
    for i,img in enumerate(image_files):
        st.image(img,use_column_width=True)
        st.write(text[i])
    st.text("")
    container = st.container()
    # Divide the container into two columns
    _, col2 = container.columns([3, 1])
    # Add content to the right column
    col2.write("Presented by:")
    col2.write("Dilip Reddy Basireddy")
    col2.write("Hassan Ahamed Shaik")
    col2.write("Nagendra Reddy Vippala")

def prod_rec_page():
    st.title("Product Recommendation")
    user_input = st.text_input(
        "Select an User Id between 1 to 500"
    )
    submitted = st.button("Submit")
    if submitted:
        user_input=int(user_input)
        st.header("Purchase History")
        my_list=pr_infer_json['purchase_history'][user_input].split(",")
        df=pd.DataFrame(my_list,columns=['Products'])
        st.dataframe(df)
        st.header("Current Ordered Products")
        box_set=list(set(pr_infer_json['current_prod_list'][user_input]).intersection(set(pr_infer_json['recommeded_products'][user_input])))
        for item in pr_infer_json['current_prod_list'][user_input]:
            if item in box_set:
                st.write(f'<mark style="background-color: white;">{item}</mark>', unsafe_allow_html=True)
            else:
                st.write(item)
        st.header("Recommeded Products")
        for item in pr_infer_json['recommeded_products'][user_input]:
            if item in box_set:
                st.write(f'<mark style="background-color: white;">{item}</mark>', unsafe_allow_html=True)
            else:
                st.write(item)

def recipe_rec_page():

    def search(key):
        filtered_list = [elem for elem in prod_list if key in elem]
        
        def count_intersection(elem):
            intersection_count = len(set(elem) & set(key))
            return (intersection_count, -len(elem))
        
        sorted_list = sorted(filtered_list, key=count_intersection, reverse=True)
        
        return sorted_list
    
    items = []
    st.title("Recipe Recommendation")
    # Create a list to store items
    if 'items' not in st.session_state:
        st.session_state['items'] = []
    
    item = st_searchbox(search, key="prod_input_box")

    col1, col2, col3 = st.columns(3)

    with col1:
        add_button = st.button("Add item")

    with col2:
        submit_button = st.button("Submit items")

    with col3:
        clear_button = st.button("Clear items")
  
    if add_button:
        if item:
            st.session_state['items'].append(item)
        else:
            st.warning("Add an item to list!")
        

    
    if clear_button:
        st.session_state['items'] = []
    
    if not submit_button:
        st.write("Your Items List:")
        for i, item in enumerate(st.session_state['items']):
            st.write(f"{i+1}. {item}")
    else:
        if len(st.session_state['items'])>0:
            st.header('Recipes:')
            recipe_df = get_recipes(st.session_state['items'])
            for i, row in recipe_df.iterrows():
                st.markdown(f"<a href='{row['link']}' target='_blank' style='text-decoration:none'>{row['title']}</a>", unsafe_allow_html=True)
        else:
            st.warning("Add an item to list!")


def cuisine_class_page():

    def search_cus(key):
        filtered_list = [elem for elem in list(product_cusine_df["product_name"]) if key in elem]
        
        def count_intersection(elem):
            intersection_count = len(set(elem) & set(key))
            return (intersection_count, -len(elem))
        
        sorted_list = sorted(filtered_list, key=count_intersection, reverse=True)
        
        return sorted_list
    
    st.title("cuisine classication")
    
    product = st_searchbox(search_cus, key="cus_input_box")

    submit_button = st.button("Classify")

    if submit_button:
        if product:
            st.subheader(list(product_cusine_df[product_cusine_df["product_name"]==product]["cuisine"])[0])
        else:
            st.warning("Add an item to list!")

    st.write("Try with below products:")
    for i in product_cusine_df.head(10)["product_name"]:
        st.write(i)


    
       

if __name__ == '__main__':
    pages = {
        "Visualizations": home,
        "Product Recommendation": prod_rec_page,
        "Recipe Recommendation": recipe_rec_page,
        "Cuisine Classification": cuisine_class_page
    }

    # Add a sidebar to your app for navigation
    st.sidebar.title("Navigation Bar")
    selection = st.sidebar.radio("", list(pages.keys()))

    # Call the selected page function
    page = pages[selection]
    page()


