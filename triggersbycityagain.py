import pandas as pd
import geopandas as gpd
import folium
from folium.plugins import HeatMap
import fiona

# Set SHAPE_RESTORE_SHX config option to YES
with fiona.Env(SHAPE_RESTORE_SHX='YES'):
    # Load a shapefile of Ghana
    ghana = gpd.read_file('Ghana_New_260_District.shp')

# Load the data from CSV file
data = pd.read_csv('DDS-test.csv')

# Convert region names to lower case to ensure proper matching
data['Region'] = data['Region'].str.lower()

# Check what column in the 'ghana' dataframe corresponds to the region names and convert it to lower case
ghana['REGION'] = ghana['REGION'].str.lower()

# Extract centroid coordinates for each region
ghana['longitude'] = ghana['geometry'].centroid.x
ghana['latitude'] = ghana['geometry'].centroid.y

# Merge your data with the Ghana shapefile
merged = ghana.set_index('REGION').join(data.set_index('Region'))

# Drop rows containing NaN values in latitude, longitude, or 'Alarm triggered (times)'
merged = merged.dropna(subset=['latitude', 'longitude', 'Alarm triggered (times)'])

# Create a map centered around Ghana
m = folium.Map(location=[7.9465, -1.0232], zoom_start=7) # these coordinates roughly represent the center of Ghana

# Add a heatmap to the map
HeatMap(data=merged[['latitude', 'longitude', 'Alarm triggered (times)']].groupby(['latitude', 'longitude']).mean().reset_index().values.tolist(), radius=8, max_zoom=13).add_to(m)

# Save the map to heatmap.html
m.save('heatmap.html')
