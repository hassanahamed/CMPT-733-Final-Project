# GROCERY DATA ANALYSIS AND USER RECOMMENDATION

Online grocery delivery application like “Instacart” have become very popular in past few years. As more and more people like the convenience of having their groceries delivered right to their doorstep, we have started this project to get a better understanding of this market and provide some ways to improve customer experience such as product recommendations and recipe recommendations.

There are mainly four components in our project:
1) Market analysis
2) Product recommendation
3) Recipe recommendation
4) cuisine classification

You can test our project through our frontend. To get a better understanging of how use our front, please see our project presentation video or follow below steps:
1) You can access our application through the following link: http://34.135.55.143:5000/
   Link for presentation video: https://youtu.be/RweDaDUQIUw

2) Visualization page contains basics information regarding all the datasets we have used in our project. Following this, you see some of the visualizations which we have created during our project as part of market analysis.
 
3) In product recommendation page you can use our product recommendation engine. To use this page, you just have to enter a number between “1” to “500” in the search, this number represents user ID and click on submit button. In output the first component you see the previous purchase history of the user next you can see the products actually purchased by the user in the current order lastly, you can see the top 10 product recommendation from our model. The products which are highlighted in white background are common products between actual purchase and recommended products.
                    
3) The next page is a recipe recommendation page. To use this page, you need to add products for which you want recipes using the search box and the "add items" button. We have added an autofill functionality to the search box so that users can have an idea of what products are available. Once you have added the items, click on the "submit" button to see the recipes or click on the "clear" button to reset your previous item list.

4) The last page in our front-end cuisine classification page, there is a similar search bar with autofill functionality in this page, once you enter name product from suggested list of items or any other available product though search bar and click on “submit” button you can get the cuisine classification output from our model.

If our credits in GCP are used, above mentioned link might not work in that case follow below steps:
1) Clone the repository.
2) Install libraries present from "requirements.txt" file in "front end" folder of this repo.
3) Move command prompt to "front end" folder and run "streamlit run app.py" command in your command prompt to run accss our data product.
4) This should open our data product in "http://localhost:8501/" page.
5) Follow previously mentioned steps or watch our presentation video to test or project.


Note: Due to space restriction of github we could not add our models and data.
