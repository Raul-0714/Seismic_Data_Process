from obspy import UTCDateTime
from obspy.clients.fdsn import Client

# Define start and end times
starttime = UTCDateTime("2023-02-06T00:00:00")
endtime = UTCDateTime("2023-02-08T00:00:00")

# Define networks, stations and component
networks = ["II"]
station = "KIV"
component = "LHZ"

# Define client
client = Client("IRIS")

# Loop over networks and download data
st = None
for network in networks:
    st_temp = client.get_waveforms(network, station, "*", component, starttime, endtime)
    if st is None:
        st = st_temp
    else:
        st += st_temp

# Save data to file
st.write("iris_data.mseed", format="MSEED")





