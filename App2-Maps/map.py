import folium
map = folium.Map(location=[32.091612, 34.780355], zoom_start=7, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My map")
fg.add_child(folium.Marker(location=[32.091612, 34.780355], popup="This is the marker", icon=folium.Icon(color='green')))

map.add_child(fg)
map.save("Map1.html")
