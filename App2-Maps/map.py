# importing the relevant library (folium)
import folium
# instantiating a map object with 3 different values using folium.Map
map = folium.Map(location=[32.091612, 34.780355], zoom_start=7, tiles="Mapbox Bright")
# instantiating featureGroup object which will be added to the map as a coordinate.
fg = folium.FeatureGroup(name="My map")
# for loop for iterating over a set of coordinates using .csv file
for coordinates in [[32.45, 34.78],[32.45, 36.78]]:
    fg.add_child(folium.Marker(location=coordinates, popup="This is a marker", icon=folium.Icon(color='green')))
# adding each of the coordinates to the map
map.add_child(fg)
# saving the map
map.save("Map1.html")
