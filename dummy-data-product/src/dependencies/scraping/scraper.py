# In the given site the required data is given inside a dynamic table.
# So if we use beautifulsoup to extract this data it will return null value.
# So we are fetching the geojson link that contains the json data
url ="https://gdacs.org/xml/gdacs_archive.geojson"
response = urlopen(url)
data = json.loads(response.read())

#storing the fetched data as a pandas dataframe
df = pd.DataFrame(data)
df = pd.DataFrame.from_dict(data)
