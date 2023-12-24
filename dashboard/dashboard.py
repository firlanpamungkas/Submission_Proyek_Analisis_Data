import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# Load data
#bike_day_df = pd.read_csv('day_data.csv')
#bike_hour_df = pd.read_csv('hour_data.csv')
#rfm_data = pd.read_csv('rfm_data.csv')

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the CSV file
csv_file_path = os.path.join(script_dir, 'day_data.csv')
csv_file_path = os.path.join(script_dir, 'hour_data.csv')
csv_file_path = os.path.join(script_dir, 'rfm_data.csv')
# Read the CSV file
bike_day_df = pd.read_csv(csv_file_path)
bike_hour_df = pd.read_csv(csv_file_path)
rfm_data = pd.read_csv(csv_file_path)

# Function to plot Recency vs Frequency
def plot_recency_frequency():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(rfm_data['Recency'], rfm_data['Frequency'], alpha=0.5)
    ax.set_title('Recency vs Frequency')
    ax.set_xlabel('Recency (days)')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

# Function to plot Frequency vs Monetary
def plot_frequency_monetary():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(rfm_data['Frequency'], rfm_data['Monetary'], alpha=0.5)
    ax.set_title('Frequency vs Monetary')
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Monetary')
    st.pyplot(fig)

# Function to plot Recency vs Monetary
def plot_recency_monetary():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(rfm_data['Recency'], rfm_data['Monetary'], alpha=0.5)
    ax.set_title('Recency vs Monetary')
    ax.set_xlabel('Recency (days)')
    ax.set_ylabel('Monetary')
    st.pyplot(fig)

# Function to plot 3D scatter plot for RFM Analysis
def plot_3d_scatter():
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(rfm_data['Recency'], rfm_data['Frequency'], rfm_data['Monetary'], alpha=0.5)
    ax.set_xlabel('Recency (days)')
    ax.set_ylabel('Frequency')
    ax.set_zlabel('Monetary')
    ax.set_title('3D Scatter Plot - RFM Analysis')
    st.pyplot(fig)

# Function to plot Bike Usage Over Time
def plot_bike_usage_over_time():
    fig, ax = plt.subplots(figsize=(10, 6))
    bike_day_df['dteday'] = pd.to_datetime(bike_day_df['dteday'])
    ax.plot(bike_day_df['dteday'], bike_day_df['cnt'], marker='o', linestyle='-')
    ax.set_title('Pola Penggunaan Sepeda Seiring Waktu')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Jumlah Peminjaman Sepeda')
    ax.grid(True)
    st.pyplot(fig)

# Function to plot Bike Distribution Based on Weather and Working Day
def plot_bike_distribution():
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.boxplot(x='weathersit', y='cnt', hue='workingday', data=bike_hour_df)
    ax.set_title('Distribusi Peminjaman Sepeda Berdasarkan Cuaca dan Hari Kerja')
    ax.set_xlabel('Cuaca')
    ax.set_ylabel('Jumlah Peminjaman Sepeda')
    ax.legend(title='Hari Kerja', loc='upper right')
    st.pyplot(fig)

# Streamlit App
def main():
    st.title('Bike Sharing Data Analysis Dashboard')

    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Sidebar with options
    analysis_option = st.sidebar.selectbox(
        'Choose Analysis',
        ('Recency vs Frequency', 'Frequency vs Monetary', 'Recency vs Monetary', '3D Scatter Plot - RFM Analysis',
         'Bike Usage Over Time', 'Bike Distribution Based on Weather and Working Day')
    )

    if analysis_option == 'Recency vs Frequency':
        st.header('Recency vs Frequency Analysis')
        plot_recency_frequency()

    elif analysis_option == 'Frequency vs Monetary':
        st.header('Frequency vs Monetary Analysis')
        plot_frequency_monetary()

    elif analysis_option == 'Recency vs Monetary':
        st.header('Recency vs Monetary Analysis')
        plot_recency_monetary()

    elif analysis_option == '3D Scatter Plot - RFM Analysis':
        st.header('3D Scatter Plot - RFM Analysis')
        plot_3d_scatter()

    elif analysis_option == 'Bike Usage Over Time':
        st.header('Bike Usage Over Time')
        plot_bike_usage_over_time()

    elif analysis_option == 'Bike Distribution Based on Weather and Working Day':
        st.header('Bike Distribution Based on Weather and Working Day')
        plot_bike_distribution()

if __name__ == '__main__':
    main()

st.caption('Copyright (c) firlan pamungkas 2023')