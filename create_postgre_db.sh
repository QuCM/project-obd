#!/bin/bash

dropdb db-reseau-vert || echo
createdb db-reseau-vert
psql -p 5432 -d db-reseau-vert -f import_data.sql