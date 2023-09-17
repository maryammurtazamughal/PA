
# Sensor Data Task with Streamlit

This is a simple Streamlit web application for visualizing and analyzing sensor data from a CSV file. 
It provides various data preprocessing and visualization options. 
The application is built using Python and leverages libraries such as Pandas for data manipulation and Plotly
 for data visualization.

Libraries

  Streamlit 
  Pandas 
  Plotly 

Workflow:

 Data Upload:
   Users upload a CSV file containing sensor data using the "Upload a CSV file" widget provided by Streamlit.

 Data Preprocessing (preprocess_data function):
      The uploaded data is preprocessed using Pandas.
      Missing values are removed (dropna).
      Duplicate rows are removed (drop_duplicates).
      A new categorical column "Timecategory" is created based on the hour of the timestamp.

 Summary Statistics Calculation (calculate_summary_statistics function):

       Median values and summary statistics (count, mean, std, min, max, etc.) are calculated for the processed data using Pandas.
       Data Visualization (create_scatter_chart, create_heatmap, create_bar_chart functions):
       Users can choose from various visualization options using a sidebar radio button.

 Available visualizations:
       Scatter Charts: These display humidity and temperature data over time categories.
       Heatmap: A density heatmap showing the relationship between humidity and temperature.
       Bar Chart: A stacked bar chart displaying humidity and temperature data by time category.

 Displaying Data and Visualizations:
         The selected visualization is displayed using the Plotly library in the Streamlit app.

 Run the App:
         To run the application, users must execute streamlit run app.py 
in their terminal after installing the required Python packages.
