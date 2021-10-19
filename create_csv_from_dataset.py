import pandas as pd

df = pd.read_json('data/reseau-cyclable-et-vert.json')
df = pd.concat([df.drop(['fields'], axis=1), df['fields'].apply(pd.Series)], axis=1)
df = pd.concat([df.drop(['geo_point_2d'], axis=1), df['geo_point_2d'].apply(pd.Series, index=['geo_point_2d_x', 'geo_point_2d_y'])], axis=1)
df = pd.concat([df.drop(['geometry'], axis=1), df['geometry'].apply(pd.Series).rename(columns={"type": "geometry_type", "coordinates": "geometry_coordinates"}) ], axis=1)
df = pd.concat([df.drop(['geometry_coordinates'], axis=1), df["geometry_coordinates"].apply(pd.Series, index=['geometry_coordinates_x', 'geometry_coordinates_y'])], axis=1)

df.to_csv('data/reseau-cyclable-et-vert.csv', index=False)