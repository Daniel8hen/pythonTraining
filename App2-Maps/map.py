import folium
map = folium.Map(location=[32.091612, 34.780355], zoom_start=7, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My map")
for coordinates in [[32.22, 34.78],[39.22, 36.78]]:
    fg.add_child(folium.Marker(location=coordinates, popup="This is a marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
