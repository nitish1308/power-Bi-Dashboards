# PowerBI-Spotify-Dashboard
Welcome to my PowerBI Showcase GitHub repository! Here, you'll find an interacive dashboard, insightful report, and data visualizations demonstrating my expertise in PowerBI, a powerful business intelligence tool.

## [Dashboard Link](https://app.powerbi.com/view?r=eyJrIjoiZjZiN2QzNTgtYjYzYS00NzRkLTlkNWMtYWMxYmI3MWVlNGY3IiwidCI6ImE4ZWVjMjgxLWFhYTMtNGRhZS1hYzliLTlhMzk4YjkyMTVlNyIsImMiOjN9)

## Table of Contents

- [Introduction](#introduction)
- [Dataset Source](#dataset-source)
- [Advanced Visualization and Tools](#advanced-visualization-and-tools)
- [Features](#features)
- [Dashboard Insights](#dashboard-insights)
- [Key Performance Indicators (KPIs)](#key-performance-indicators-kpis)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Usage](#usage)
- [PowerBI Dashboard](#powerbi-dashboard)
- [Python Scripts](#python-scripts)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction
This project presents a dynamic and interactive dashboard developed in PowerBI, showcasing an analysis of the top Spotify songs from 2018 to 2023. Utilizing a comprehensive dataset from kaggle, the dashboard provides insights into trends in music preferences, artist popularity, and song characteristics over the years. The aim is to offer users a detailed overview of the evolving music landscape, highlighting key metrics such as energy levels, average stream counts per year, and top artists. This tool is designed for music enthusiasts, industry analysts, and anyone interested in understanding the dynamics of popular music through data visualization.
![Dashboard Screenshot](./Dashboard%20Image/Dashboard.png)

## Dataset Source
The analysis is based on the dataset available at [Kaggle: Top Spotify Songs 2023](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023/data). This dataset encompasses a wide range of information, including:
- Track Information
- Music Statistics

## Advanced Visualization and Tools

### DENEB Visuals

The dashboard incorporates DENEB visuals, a powerful tool for creating custom visualizations within PowerBI. Here's how DENEB has been used to enhance the dashboard's analytical capabilities:

Github Link: 

[DENEB](https://github.com/PBI-David/Deneb-Showcase/tree/main)

[DENEB-TEMPLATES](https://github.com/PowerBI-tips/Deneb-Templates/tree/main/templates)

- **Energy Gauge**: Custom-built to display the energy level of songs, providing an intuitive visual representation of song intensity.
- **Heatmap with Bars**: Combines the heatmap and bar chart to offer a detailed comparison of various metrics across different categories, such as artist popularity or song features over time.
- **Customizing with Vega/Vega-Lite**: Access the Deneb visual's properties and insert your Vega or Vega-Lite JSON specification into the editor. You can design your gauge or heatmap based on the dataset fields available in your PowerBI model.
- **Interactivity**: Leverage Vega's signal and event handlers to add interactivity to your visuals, such as tooltips, zooming, or filtering based on user interaction.

These visuals were crafted using the Vega-Lite visualization grammar, allowing for a high degree of customization and interactivity not available with standard PowerBI visuals.

### HTML Content

To further enrich the dashboard, HTML content has been embedded to display dynamic images and links, offering a more engaging user experience. This approach allows for the integration of album covers and artist images directly within the dashboard, making the data exploration process both informative and visually appealing.

### External Tools: BRAVO

The use of BRAVO, an external tool for PowerBI, showcases an advanced level of data analysis and dashboard development. Key features and benefits include:

- Enhanced data connectivity and transformation capabilities, enabling more complex data manipulations and enrichments.
- Advanced custom visualizations and analytics features that go beyond the default PowerBI functionalities, allowing for a more tailored analysis experience.

The incorporation of these advanced tools and techniques signifies a deep understanding of PowerBI's ecosystem and a commitment to leveraging the full spectrum of its capabilities to deliver insightful and compelling data stories.


## Features
The dashboard highlights several key features:
- **Yearly Trends**: Visualize how music preferences have changed from 2018 to 2023, with a focus on streaming counts and popularity.
- **Energy Levels**: Explore the energy levels of top tracks to understand the mood and dynamics of popular music.
- **Average Streams per Year (Avg stream /Year)**: A metric that showcases the average popularity of songs, providing insight into listening trends.
- **Top Artist of All Time and Each Year**: Identify which artists dominate the Spotify charts over time and in specific years.

## Dashboard Insights
The dashboard utilizes these KPIs to uncover insights such as the evolution of music tastes over the years, the impact of streaming on music popularity, and the characteristics that define top-charting songs. By analyzing data through these lenses, users can gain a deeper understanding of the streaming music landscape.


## Key Performance Indicators (KPIs)
The dashboard features several KPIs to aid in the analysis:
1. **Average Stream per Year**
   - Calculates the average number of streams per song per year, offering insights into annual streaming trends.
2. **Max Stream**
   - Identifies the song with the maximum streams, highlighting the most popular track in the dataset.
3. **Percent Val (Energy %)**
   - Shows the average energy percentage of songs, indicating the intensity and activity level prevalent in popular music.
4. **Top Song vs AVG**
   - Compares the streams of the top song against the average streams per year, visually represented with upward (above average) or downward (below average) arrows.
5. **Top Song vs Avg Val**
   - Calculates the percentage difference between the streams of the top song and the average streams per year, quantifying its popularity relative to the average.
6. **Top Song Streams**
   - Summarizes the total streams for the top song, showcasing the peak of popularity within the dataset.
7. **Track Count**
   - Counts the total number of unique tracks in the dataset, providing a sense of the dataset's diversity.
8. **Image HTML**
   - Generates an HTML snippet for displaying the image of the most streamed song, enriching the dashboard with visual content.

## Getting Started

These instructions will guide you through setting up and running the Spotify Data Analysis Dashboard on your local machine. This project is ideal for those interested in music trends, data analysis, and visualization with PowerBI and Python.

### Prerequisites

Before you begin, ensure you have the following installed on your computer:

- **PowerBI Desktop**: The dashboard is built and runs on PowerBI Desktop. You can download it for free from the [official Microsoft PowerBI website](https://powerbi.microsoft.com/en-us/desktop/).

- **Python**: Some scripts for data preprocessing or fetching additional data from the Spotify Web API are written in Python. Ensure you have Python 3.6 or later installed, which you can download from [python.org](https://www.python.org/downloads/).

- **pip**: Python's package installer, used to install the dependencies required by the Python scripts. pip usually comes installed with Python.

- **A Spotify Developer Account**: For scripts that fetch data from the Spotify Web API, you'll need a Spotify Developer account to create an app and get your `CLIENT_ID` and `CLIENT_SECRET`. Sign up or log in at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

## Usage
This section provides detailed instructions on how to use the Spotify Data Analysis Dashboard and accompanying Python scripts to fetch and preprocess data for enhanced insights into Spotify's top songs from 2018 to 2023.

### PowerBI Dashboard
1. **Opening the Dashboard**: After completing the installation and setup, open the PowerBI Desktop application and load the `.pbix` file provided in the repository. This file contains the pre-built dashboard.

2. **Navigating the Dashboard**: The dashboard is segmented into various pages, each focusing on different aspects of the dataset, such as yearly trends, artist popularity, and song characteristics. Use the tabs at the bottom to switch between these views.

3. **Interacting with Visuals**: Click on any visual or graph to drill down into more detailed data views. Many visuals are interactive and allow for filtering the dataset based on criteria such as year, artist, or song characteristics.

4. **Using Filters**: Apply filters to customize the data display according to specific interests or queries. Filters can be used to display information for a particular year, artist, or track.

5. **Exporting Data**: If you need to analyze data outside of PowerBI, you can export data from visuals by clicking on the "..." menu in the upper-right corner of each visual and selecting "Export data".


### Python Scripts
1. **Setting Up Environment**: Ensure your Python environment is set up as described in the [Prerequisites](#prerequisites) sections.

2. **Running Scripts**: Navigate to the directory containing the Python scripts. Use a command line interface to run a script with `python script_name.py`, replacing `script_name.py` with the actual name of the script you wish to run.

3. **Fetching Data**: The main purpose of the Python scripts is to fetch additional data from the Spotify Web API, such as updated stream counts or additional song metadata. These scripts may require you to input your Spotify API credentials.

4. **Preprocessing Data**: Some scripts are designed to preprocess the data for better compatibility with PowerBI, such as formatting dates or aggregating data points.

5. **Updating the Dashboard**: After running the Python scripts, you may need to refresh the data source in PowerBI to reflect any new or updated data. This can typically be done through the "Data" tab in PowerBI Desktop.

Remember, the specifics of how to use the dashboard and scripts will depend on their actual functionalities and the structure of your project. Adjust the instructions based on the actual features of your dashboard and scripts.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for more details.

## Acknowledgments

This project would not have been possible without the contributions and support from various individuals and organizations:

- Kaggle, for providing the comprehensive Spotify dataset.
- The Spotify Web API, for allowing us to enrich our dataset with additional data.
- The PowerBI Community, for the invaluable resources and support.

Your encouragement, feedback, and contributions have been indispensable to this project's success.
