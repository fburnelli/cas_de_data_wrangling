#!/bin/bash
# Start PostgreSQL service
service postgresql start

# Start Jupyter Notebook
jupyter notebook --ip=0.0.0.0 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''

