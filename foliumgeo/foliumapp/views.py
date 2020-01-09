from django.shortcuts import render
import folium 
import os
from foliumgeo.settings import BASE_DIR

#below code can use as different types in map
'''
tiles='Stamen Terrain'
tiles='Stamen Toner'
tiles='Mapbox Bright'
https://pypi.org/project/django-fresh/
'''
#default tiles will be “OpenStreetMap”

def show(request):
    map = folium.Map(#tiles='Stamen Terrain',
                     width=1000,height=500,location=[19.869777,75.339153],
                     zoom_start=14)

    

    folium.TileLayer('openstreetmap').add_to(map)
    #folium.TileLayer('StamenTerrain').add_to(map) 
    #not working properly , only work if mention in folium.Map()
    folium.TileLayer('stamentoner').add_to(map)
    folium.TileLayer('stamenwatercolor').add_to(map)
    folium.TileLayer('cartodbpositron').add_to(map)
    folium.TileLayer('cartodbdark_matter').add_to(map)
    
    folium.LayerControl(collapsed=False).add_to(map)
    #above line will add layers in map(i.e radio button to choose different tiles)
    
    folium.Marker(location=[19.873038,75.328386],popup="<strong>Kranti Chowk</strong>",tooltip="click here for more info").add_to(map)
    #above will display marker on given location
    
    locationbluecir=[19.852510,75.319102]
    bluecircleicon=folium.features.CustomIcon(os.path.join(BASE_DIR,'foliumapp\static\circle.png'),icon_size=(15,15))
    popupblucircle="<strong>GetStarted</strong>"
    folium.Marker(location=locationbluecir,tooltip='current location',popup=popupblucircle,icon=bluecircleicon).add_to(map)
    
    #above code display bluecircle png in given location as Marker
    
    
    locationgeca=[19.867789,75.323893]
    gecaicon=folium.features.CustomIcon(os.path.join(BASE_DIR,'foliumapp\static\geca.png'),icon_size=(55,25))
    popupgeca="<strong>Government College of Engineering Aurangabad</strong>"
    folium.Marker(location=locationgeca,tooltip='G.E.C.A',popup=popupgeca,icon=gecaicon).add_to(map)
     
    #above code will display image as marker in Map
    
    
    
    #path coordinates to display in map
    points=[[19.872914,75.328454],[19.871240,75.327725],[19.870392,75.327117],[19.867116,75.318938],[19.864513,75.317179],[19.862750,75.315335],[19.860746,75.311260],[19.861250,75.308000],[19.861210,75.307249],[19.860988,75.306799],[19.859474,75.305340],[19.856353,75.303506],[19.854859,75.302240],[19.852009,75.319458]]
    
    folium.PolyLine(points, color="blue", weight=3.5, opacity=1).add_to(map)
    #it will display highlighted path in blue color
    
    for each in points:
        folium.Marker(location=each,tooltip=each).add_to(map)
    #it will point Marker on the given points
    
    
    
    map.save("map.html")
    #save the map object
    
    context = {'my_map': map._repr_html_()} #{'my_map': map} change to {'my_map': map._repr_html_()}
    #display map on html page
    
    return render(request, 'map.html', context)
    