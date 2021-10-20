import os
import time

n_test = 1000
command = 'psql -d db-reseau-vert -f query_toulouse.sql > /dev/null 2>&1'

start_time = time.time()

for i in range(n_test):
    os.system(command)

stop_time = time.time()

print('Execution time of ' + str(n_test) + ' in ' + str((stop_time - start_time)/n_test) + 's on average')

# For query_toulouse.sql, ~0.04s on average for 1000 tries on Quentin's computer