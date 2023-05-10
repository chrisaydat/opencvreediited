import geopandas as gpd

# Load the shapefile
gdf = gpd.read_file('Ghana_New_260_District.dbf')

# Print the column names
print(gdf.columns)
