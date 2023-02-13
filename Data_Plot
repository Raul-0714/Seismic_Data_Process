# Plot the data downloaded from IRIS in .mseed format

st = read("iris_data.mseed") # The filename

# Get the first trace (stream) from the read file
tr = st[0]

# Plot the seismic data
plt.plot(tr.times(), tr.data, 'k')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Seismic Data')
plt.show()
