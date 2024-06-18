import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')
from io import BytesIO
# 🚧 what for - from faker import Faker

st.title('Tips analysis')
uploaded_file = st.sidebar.file_uploader('Please upload the file called tips.csv', type='csv')

@st.cache_data
def load_data(file):
    data = pd.read_csv(file)
    data['tip_ratio'] = data['tip'] / data['total_bill']
    return data

def save_fig_as_bytesio(fig):
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    return buf

if uploaded_file is not None:
    data = load_data(uploaded_file)

    # Plotting functions
    def plot_tip_ratio_histogram():
        fig, ax = plt.subplots()
        sns.histplot(data=data, x='tip_ratio', bins=20, ax=ax)
        st.pyplot(fig)
        return fig

    def plot_tip_ratio_and_tip_histogram():
        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        sns.histplot(data=data, x='tip_ratio', hue='sex', multiple="dodge", bins=10, ax=axes[0])
        sns.histplot(data=data, x='tip', hue='sex', multiple="dodge", bins=10, ax=axes[1])
        st.pyplot(fig)
        return fig
    # 🚧 dogde?

    def plot_size_tip_ratio_scatterplot():
        fig, ax = plt.subplots()
        sns.scatterplot(data=data, x='time', y='smoker', size='tip_ratio', sizes=(20, 200), ax=ax)
        st.pyplot(fig)
        return fig

    def plot_size_tip_ratio_scatterplot_day():
        fig, ax = plt.subplots()
        sns.scatterplot(data=data, x='day', y='smoker', size='tip_ratio', sizes=(20, 200), ax=ax)
        st.pyplot(fig)
        return fig

    def plot_violin_total_bill_sex():
        fig, ax = plt.subplots()
        sns.violinplot(data=data, x='sex', y='total_bill', ax=ax, inner='quartile', palette=["lightblue", "lightpink"])
        st.pyplot(fig)
        return fig

    # Display charts
    st.write("## Histogram of Tip Ratio")
    fig1 = plot_tip_ratio_histogram()
    buf1 = save_fig_as_bytesio(fig1)
    st.download_button(label="Download Histogram of Tip Ratio", data=buf1, file_name='histogram_tip_ratio.png', mime='image/png')

    st.write("## Histograms of Tip Ratio and Tip by Sex")
    fig2 = plot_tip_ratio_and_tip_histogram()
    buf2 = save_fig_as_bytesio(fig2)
    st.download_button(label="Download Histograms of Tip Ratio and Tip by Sex", data=buf2, file_name='histograms_tip_ratio_and_tip_by_sex.png', mime='image/png')

    st.write("## Scatter Plot: Tip Ratio vs SmokerTime")
    fig3 = plot_size_tip_ratio_scatterplot()
    buf3 = save_fig_as_bytesio(fig3)
    st.download_button(label="Download Scatter Plot (Tip Ratio vs SmokerTime)", data=buf3, file_name='scatter_plot_tip_ratio_vs_smoker.png', mime='image/png')

    st.write("## Scatter Plot: Tip Ratio vs Smokerf Week")
    fig4 = plot_size_tip_ratio_scatterplot_day()
    buf4 = save_fig_as_bytesio(fig4)
    st.download_button(label="Download Scatter Plot (Tip Ratio vs Smokerf Week)", data=buf4, file_name='scatter_plot_tip_ratio_vs_smokerek.png', mime='image/png')

    st.write("## Violin Plot of Sex and Total Bill")
    fig5 = plot_violin_total_bill_sex()
    buf5 = save_fig_as_bytesio(fig5)
    st.download_button(label="Download Violin Plot of Sex and Total Bill", data=buf5, file_name='violin_plot_sex_total_bill.png', mime='image/png')

else:
    st.write("Please upload a CSV file to proceed.")
    st.stop()
    

# CHART OPTIONS

# Histogram but make it for tip / total bill! ❗️🚧
# plt.figure(figsize=(10, 6))
# sns.histplot(tips['total_bill'], kde=True)
# plt.show()

# Scatterplots - create various 3D stuff where size = tip / bill! ❗️🚧
# sns.scatterplot(x='total_bill', y='tip', size= tip / total_bill , data=tips)

# plt.figure(figsize=(10, 6))
# sns.lineplot(x='time_order', y='tip', data=tips)
# plt.show()

# Chart 2*2 bars 
# tips['tip_pct'] = 100 * tips['tip'] / tips['total_bill']
# grid = sns.FacetGrid(tips, row="sex", col="time", hue='smokertitles=True)
# grid.map(plt.hist, "tip_pct", bins=np.linspace(0, 40, 15), alpha=0.5, density=True);

#boxplot
# with sns.axes_style(style='ticks'):
#     g = sns.catplot("dayl_bill", "sex", data=tips, kind="box")
#     g.set_axis_labels("Day", "Total Bill");

# sns.violinplot(
#     "sex", "total_bill", data=tips,
#     inner='quartile',
#     palette=["lightblue", "lightpink"],);

# TIME for LINE PLOT
# time add 🚧
    # np.random.seed(42)  # For reproducibility
    # start_date = datetime(2023, 1, 1)
    # end_date = datetime(2023, 1, 31)
    # tips['time_order'] = [start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days)) for _ in range(len(tips))]




# WIDGET OPTIONS
# # Sidebar widgets
#     st.sidebar.header("Filter Options")

#     # Dropdown Selector for dayweek
#     day_of_week = st.sidebar.selectbox('Select Day of the Week', data['day'].unique())

#     # Slider for filtering total bill amount
#     total_bill_range = st.sidebar.slider('Select Total Bill Range', float(data['total_bill'].min()), float(data['total_bill'].max()), (float(data['total_bill'].min()), float(data['total_bill'].max())))

#     # Multiselect for meal time
#     meal_time = st.sidebar.multiselect('Select Meal Time', data['meal time'].unique(), default=data['meal time'].unique())

#     # Filter data based on selections
#     data = data[
#         (data['day'] == day_of_week) &
#         (data['total_bill'] >= total_bill_range[0]) &
#         (data['total_bill'] <= total_bill_range[1]) &
#         (data['meal time'].isin(meal_time))
#     ]

#     # Display the dataframe
#     st.write("## Filtered Dataset")
#     st.write(data)