import matplotlib.pyplot as plt
import cartopy.crs as c
import cartopy.feature as cf
import streamlit as st
import ssl
from io import BytesIO

ssl._create_default_https_context = ssl._create_unverified_context

st.title('flight path between two cities')
st.subheader("enter the country names to visualise the flight path")
cities = {
    'New York': (-74.0060, 40.7128),
    'Bengaluru': (77.5946, 12.9716),
    'Berlin': (13.4050, 52.5200),
    'Rio de Janeiro': (-43.1729, -22.9068),
    'Moscow': (37.6173, 55.7558),
    'Denver': (-104.9903, 39.7392),
    'Tokyo': (139.6917, 35.6895),
    'London': (-0.1276, 51.5074),
    'Madrid': (-3.7038, 40.4168),
    'Paris': (2.3522, 48.8566),
}

city_names=cities.keys()
city_list=list(city_names)

city1=st.selectbox('choose city 1:',city_list)
city2=st.selectbox('choose city 2:',city_list)

if st.button("click me"):
    st.write("flight path")
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(1, 1, 1, projection=c.PlateCarree())
    ax.set_extent([-180, 180, -90, 90], crs=c.PlateCarree())
    ax.add_feature(cf.LAND, facecolor='lightgreen', alpha=0.5, linewidth=0.3)
    ax.add_feature(cf.OCEAN, facecolor='skyblue', alpha=0.5, linewidth=0.3)
    ax.add_feature(cf.COASTLINE, linestyle='-.')
    for key, (lon, lat) in cities.items():
            ax.plot(lon, lat, marker='o', color='red', mec='k', ms=6, transform=c.PlateCarree())
            ax.text(lon + 3, lat - 3, key, fontsize=12, transform=c.PlateCarree())

    if city1 in cities.keys() and city2 in cities.keys() and city1!=city2:
            lon_ny, lat_ny = cities[city1]
            lon_b, lat_b = cities[city2]

            ax.plot([lon_ny, lon_b], [lat_ny, lat_b], color="blue", linestyle='dotted', transform=c.Geodetic())
            ax.set_title("World map")
            st.pyplot(fig)
            buf=BytesIO()
            fig.savefig(buf,format='png',bbox_inches='tight')
            buf.seek(0)
            st.download_button(
                label='Download as image',
                data=buf,
                file_name=f'Flight_path_{city1}_to_{city2}.png',
                mime='image/png'
            )
    elif city1==city2:
        st.warning("please enter 2 different countries")

    else:
            st.warning('Please enter a valid city name.....')
