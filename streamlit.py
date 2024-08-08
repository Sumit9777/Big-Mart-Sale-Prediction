import pandas as pd
import streamlit as st
import plotly.express as px

# Load data from Excel file
def load_data():
    file_path = "C:\\Users\\Sumit\\Desktop\\streamlit\\Train.xlsx"  # Specify the path to your Excel file
    df = pd.read_excel(file_path)
    return df

# Main function to display data
def main():
    st.title('Sales Data Exploration')

    # Load data directly from file path
    df = load_data()

    # Display basic information about the dataset
    st.subheader('Dataset Info:')
    st.write(f"Number of Rows: {df.shape[0]}")
    st.write(f"Number of Columns: {df.shape[1]}")
    st.write(f"Columns: {', '.join(df.columns)}")

    # Display a sample of the data
    st.subheader('Sample Data:')
    st.write(df.head())

    # Display interactive visualizations
    st.subheader('Interactive Visualizations:')
    # You can add more visualizations here based on your requirements
    fig = px.scatter(df, x='Item_MRP', y='Item_Outlet_Sales', color='Item_Type', hover_data=['Item_Identifier'])
    st.plotly_chart(fig)

    # Interactive Visualizations
    st.subheader('Interactive Visualizations:')
    
    # Scatter plot
    fig = px.scatter(df, x='Item_Weight', y='Item_Fat_Content', color='Item_Fat_Content', hover_data=['Item_Weight'])
    st.plotly_chart(fig)
    
    # Pie chart
    st.subheader("Pie Chart of Item Fat Content")
    fat_content_counts = df['Item_Fat_Content'].value_counts()
    fig_pie = px.pie(names=fat_content_counts.index, values=fat_content_counts.values, title='Item Fat Content Distribution')
    st.plotly_chart(fig_pie)

    st.subheader('Interactive Visualizations:')
    
    # Scatter plot
    fig_scatter = px.scatter(df, x='Outlet_Location_Type', y='Outlet_Type', color='Outlet_Location_Type', size='Item_Outlet_Sales', hover_data=['Item_Outlet_Sales'])
    st.plotly_chart(fig_scatter)

    hist_fig = px.histogram(df, x='Item_Fat_Content', y='Item_MRP', title='Histogram of Item MRP by Fat Content')
    st.plotly_chart(hist_fig)

    hist_fig = px.histogram(df, x='Item_Type', y='Item_Outlet_Sales', title='Item Outlet Sales by Item Type')
    st.plotly_chart(hist_fig)

    line_fig = px.line(df, x='Outlet_Size', y='Outlet_Location_Type', title='Item Outlet Size by Outlet Location Type')
    st.plotly_chart(line_fig)

    line_fig = px.line(df, x='Outlet_Establishment_Year', y='Outlet_Type', title='Item Outlet Established Year by Outlet Type')
    st.plotly_chart(line_fig)

    box_fig = px.box(df[['Item_Weight', 'Item_MRP', 'Item_Outlet_Sales']], title='Box Plot of Item Features')
    st.plotly_chart(box_fig)


if __name__ == '__main__':
    main()