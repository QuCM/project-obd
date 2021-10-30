CREATE TABLE reseau
(
  datasetid VARCHAR(100),
  recordid VARCHAR(40),
  record_timestamp TIMESTAMP WITH TIME ZONE,
  commune VARCHAR(100),
  obs_gestion VARCHAR(100),
  section VARCHAR(100),
  geo_point_2d POINT,
  nom_voie VARCHAR(100),
  mot_directeur VARCHAR(100),
  pole VARCHAR(10),
  tm VARCHAR(3),
  observations VARCHAR(100),
  code_insee INTEGER,
  carte_velo  VARCHAR(100),
  longueur_m INTEGER,
  type  VARCHAR(2),
  obs_type VARCHAR(100),
  revetement VARCHAR(100),
  eclairage VARCHAR(100),
  geometry_type VARCHAR(100),
  geometry_coordinates POINT,
  geo_shape_type VARCHAR(100),
  geo_shape_coordinates_1 POINT[],
  geo_shape_coordinates_2 POINT[],
  geo_shape_coordinates_3 POINT[]
);

\COPY reseau(datasetid, recordid, record_timestamp, commune, obs_gestion, section, geo_point_2d, nom_voie, mot_directeur, pole, tm, observations, code_insee, carte_velo, longueur_m, type, obs_type, revetement, eclairage, geometry_type, geometry_coordinates, geo_shape_type, geo_shape_coordinates_1, geo_shape_coordinates_2, geo_shape_coordinates_3) FROM './data/reseau-cyclable-et-vert.csv' DELIMITER ',' CSV HEADER