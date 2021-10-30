import os
import time
import sys

def main():
    args = sys.argv[1:]
    if not args:
        raise Exception('You should specify a filename')
    FILE_NAME = args[0]

    n_test = 1000
    command = 'psql -d db-reseau-vert -f' + FILE_NAME + '> /dev/null 2>&1'

    start_time = time.time()
    for i in range(n_test):
        os.system(command)
    stop_time = time.time()

    print('Execution time of ' + str(n_test) + ' in ' + str((stop_time - start_time)/n_test) + 's on average')

    # For query_cycle_paths_toulouse.sql, ~0.03s on average for 1000 tries on Quentin's computer
    # For query_around_supaero.sql, ~0.07s on average for 1000 tries on Quentin's computer

if __name__ == "__main__":
    main()