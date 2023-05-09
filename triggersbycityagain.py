import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import HeatMap
import fiona
with fiona.Env(SHAPE_RESTORE_SHX='YES'):
    ghana = gpd.read_file('ghana.shp')


# Load the data from CSV file
data = pd.read_csv('DDS-test.csv')

# Convert city names to lower case to ensure proper matching
data['City'] = data['City'].str.lower()

# Load a shapefile of Ghana
ghana = gpd.read_file('ghana.shp') # You need a shapefile of Ghana

# Convert city names to lower case to ensure proper matching
ghana['city'] = ghana['city'].str.lower()

# Merge your data with the Ghana shapefile
merged = ghana.set_index('city').join(data.set_index('City'))

# Create a map centered around Ghana
m = folium.Map(location=[7.9465, -1.0232], zoom_start=7) # these coordinates roughly represent the center of Ghana

# Add a heatmap to the map
HeatMap(data=merged[['latitude', 'longitude', 'Alarm triggered (times)']].groupby(['latitude', 'longitude']).mean().reset_index().values.tolist(), radius=8, max_zoom=13).add_to(m)

# Display the map
m
