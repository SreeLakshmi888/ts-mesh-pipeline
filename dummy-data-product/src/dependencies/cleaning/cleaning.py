#converting the data into a pandas csv file 
df.to_csv (r'gen.csv', index = False, header=True)

#dropping of unwanted columns from the csv file
df = df.drop('bbox', 1)
df = df.drop('type', 1)

#The csv file now exist as a single column. 
#Here we are separating the data in this one column to multiple columns
x=pd.DataFrame(df['features'].values.tolist(), index=df.index)
x = x.drop('type',1)
x = x.drop('bbox', 1)
x = x.drop('geometry',1)
y=pd.DataFrame(x['properties'].values.tolist(), index=df.index)

#Similar to we separated the properties column
#Here we are trying to properly extract the coordinate values from the data
loc=pd.DataFrame(df['features'].values.tolist(), index=df.index)
loc = loc.drop('type',1)
loc = loc.drop('bbox',1)
geo=pd.DataFrame(loc['geometry'].values.tolist(), index=df.index)
geo = geo.drop('type',1)
geo=pd.DataFrame(geo['coordinates'].values.tolist(), index=df.index)
geo.columns = ['longitude', 'latitude']

#Now we merge the two dataframes into a single dataframe
y=pd.merge(y, geo, left_index=True, right_index=True)

#dropping of unwanted columns from the csv file
y = y.drop('icon',1)
y = y.drop('iconoverall',1)
y = y.drop('url',1)
y = y.drop('severitydata',1)
y = y.drop('polygonlabel',1)
y = y.drop('Class',1)
y = y.drop('description',1)
y = y.drop('htmldescription',1)
y = y.drop('eventname',1)
y = y.drop('glide',1)

#Now from the extracted data we are fetching only the data required 
#That is, data related to India
India = y.loc[y['country'] == 'India'] 
