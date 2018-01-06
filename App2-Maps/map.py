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
fgv = folium.FeatureGroup(name="Volcanoes")


# for loop for iterating over two lists - lat, lon, which were derived by a .csv file
# zip function for running on both indexes in the same iteration
for lt, ln, el in zip(lat, lon, elev):
    #this is for coordinate point.
    # fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + " m", icon=folium.Icon(color=colorProducer(el))))
    #this is for circle point
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, fill_color=colorProducer(el), fill='true', color='grey', fill_opacity=0.7,  popup=str(el) + " m"))
# adding each of the coordinates to the map
#create a GeoJson object in order to add a polygon layer
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x ['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
# saving the map
map.save("Map1.html")
