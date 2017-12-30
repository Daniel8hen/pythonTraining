# importing relevant libraries
import folium
import pandas
# a function that checks for the elevation value and produces a color accordingly
def colorProducer(el):
    if el < 1000:
        return 'green'
    elif 1000 <= el < 3000:
        return 'orange'
    else:
        return 'red'
# instantiating a map object with 3 different values using folium.Map
map = folium.Map(location=[38.58, -99.09], zoom_start=4, tiles="Mapbox Bright")
df = pandas.read_csv("Volcanoes.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])
# instantiating featureGroup object which will be added to the map as a coordinate.
fg = folium.FeatureGroup(name="My map")


# for loop for iterating over two lists - lat, lon, which were derived by a .csv file
# zip function for running on both indexes in the same iteration
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + " m", icon=folium.Icon(color=colorProducer(el))))
# adding each of the coordinates to the map
map.add_child(fg)
# saving the map
map.save("Map1.html")
