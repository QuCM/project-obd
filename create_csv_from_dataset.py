import pandas as pd

df = pd.read_json('data/reseau-cyclable-et-vert.json')

df = pd.concat([df.drop(['fields'], axis=1), df['fields'].apply(pd.Series)], axis=1)

## geo_point_2d
df['geo_point_2d'] = df['geo_point_2d'].apply(lambda x: str(x).replace('[', '('))
df['geo_point_2d'] = df['geo_point_2d'].apply(lambda x: str(x).replace(']', ')'))

## geometry
df = pd.concat([df.drop(['geometry'], axis=1), df['geometry'].apply(pd.Series).rename(columns={"type": "geometry_type", "coordinates": "geometry_coordinates"}) ], axis=1)
df['geometry_coordinates'] = df['geometry_coordinates'].apply(lambda x: str(x).replace('[', '('))
df['geometry_coordinates'] = df['geometry_coordinates'].apply(lambda x: str(x).replace(']', ')'))

## geo_shape
# Flatten the geo_shape dictionnary
df = pd.concat([df.drop(['geo_shape'], axis=1), df["geo_shape"].apply(pd.Series).rename(columns={"type": "geo_shape_type", "coordinates": "geo_shape_coordinates_1"}) ], axis=1)
# Transform the [] into () and delete 2 () and add 1 []
df['geo_shape_coordinates_1'] = df['geo_shape_coordinates_1'].apply(lambda x: str(x).replace('[', '('))
df['geo_shape_coordinates_1'] = df['geo_shape_coordinates_1'].apply(lambda x: str(x).replace(']', ')'))
df['geo_shape_coordinates_1'] = df['geo_shape_coordinates_1'].apply(lambda x: '{' + x[2:-2] + '}')

df['geo_shape_coordinates_1'] = df['geo_shape_coordinates_1'].apply(lambda x: str(x).replace('(', '"('))
df['geo_shape_coordinates_1'] = df['geo_shape_coordinates_1'].apply(lambda x: str(x).replace(')', ')"'))
# Sometimes too many parenthesis, how to fix ?
# Function ? split on double parenthesis and puts just one ?
# Does it change the data format ?
# Lack of flexibility
# split on ')),', but problem of how to store ? Another table for that ?
# -> create another column when that happens

df[['geo_shape_coordinates_1', 'geo_shape_coordinates_2']] = df['geo_shape_coordinates_1'].str.split('\)"\)", "\("\(', 1, expand=True)
df['geo_shape_coordinates_1'] = df['geo_shape_coordinates_1'].apply(lambda x: str(x) + ')"}' if x is not None and str(x)[-1] != '}' else x)
df['geo_shape_coordinates_2'] = df['geo_shape_coordinates_2'].apply(lambda x: '{"(' + str(x) if x else x)

df[['geo_shape_coordinates_2', 'geo_shape_coordinates_3']] = df['geo_shape_coordinates_2'].str.split('\)"\)", "\("\(', 1, expand=True)
df['geo_shape_coordinates_2'] = df['geo_shape_coordinates_2'].apply(lambda x: str(x) + ')"}' if x is not None and str(x)[-1] != '}' else x) #pb here
df['geo_shape_coordinates_3'] = df['geo_shape_coordinates_3'].apply(lambda x: '{"(' + str(x) if x else x)

# Modify date format to have a format understandable by PostGreSQL as a TIMESTAMP
df['record_timestamp'] = df['record_timestamp'].apply(lambda x: str(x).split('T')[0] + ' ' + str(x).split('T')[1])

df.to_csv('data/reseau-cyclable-et-vert.csv', index=False)