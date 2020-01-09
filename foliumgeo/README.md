# Map implementation in Django with Folium


# Django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

#Folium

Folium is a powerful Python library that helps you create several types of Leaflet maps

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash

pip install Django
pip install Folium

```

## Usage

```python

import folium

```

# How to load Map with folium

    map = folium.Map(tiles='Stamen Terrain',
                     width=1000,height=500,location=[19.869777,75.339153],
                     zoom_start=14)
        
   where, map ->   keyword ,
   		  tiles->  Map type(e.g tiles='Stamen Terrain',tiles='Stamen Toner',tiles='Mapbox Bright') ,
   		  width -> Width of map ,
   		  height ->Height of Map ,
   		  location -> consist of two values i.e [latitude,longitude] ,
   		  zoom_start -> from which zoom position the map should load
   		  
   		  
# Add marker to map

 folium.Marker(location=[19.873038,75.328386],popup="<strong>Kranti Chowk</strong>",tooltip="click here for more info").add_to(map)
 
 where,
 		folium.Marker() -> used to display marker ,
 		location -> consist of two values i.e [latitude,longitude] ,
 		popup -> Actual value of popup(will show after click) ,
 		tooltip -> tooltip (str or folium. Tooltip, default None) Display a text when hovering over the object ,
 		add_to(map) -> add the values to map 
 		

# Plot lines in folium map

Like ‘markers’, lines are added to folium map objects with the add_to() method

folium.PolyLine(points, color="blue", weight=3.5, opacity=1).add_to(map)

where, 
		points=[[[19.872914,75.328454],[19.871240,75.327725]......] ,
		i.e multiple [latitude,longitude] in list ,
		color -> color to the lines ,
		weight -> thickness of line  ,
		opacity -> visibility of path
		
		
		
# Ref links	

https://docs.djangoproject.com/en/3.0/

https://python-visualization.github.io/folium/

https://deparkes.co.uk/2016/06/10/folium-map-tiles/

https://deparkes.co.uk/2016/06/03/plot-lines-in-folium/