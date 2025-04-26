import plotly.express as px
   data = {"Country" :["United States", "Canada" , "Brazil", "Russia", "India"], "Values": [100, 50, 80, 90, 70]}
   fig = px.choropleth( data, locations='Country' locationmode='country names', color='Values', color_continuous_scale = "Blues",title='Choropleth Map of Values by Country') 
fig.show()
