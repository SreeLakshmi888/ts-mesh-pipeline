mapit = folium.Map( location=[0, 0], zoom_start=1 )
 
for lat , lon in zip(India.latitude , India.longitude):
    #There may occur some values where latitude and longitude are simply zero.
    # In such cases we can't locate them. 
    # So since the country is India, on situations were a null value occurs we give a default 
    # value for it.    
    if(lat != 0 and lon != 0):
      folium.Marker( location=[ lat,lon ] ).add_to( mapit )
    else:  
      folium.Marker( location=[ 20.5937, 78.9629] ).add_to( mapit )
     
mapit
