# Use an official Jupyter Notebook image as the base image
FROM jupyter/base-notebook:latest

# Switch to root user to install PostgreSQL and other dependencies
USER root

# Install PostgreSQL client and other dependencies
RUN apt-get update && apt-get install -y postgresql postgresql-contrib libpq-dev && \
    pip install pandas psycopg2-binary

# Set environment variables for PostgreSQL
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

# Copy the initialization script to the Docker container
COPY init-db.sh /docker-entrypoint-initdb.d/

# Install Jupyter Notebook extensions for PostgreSQL
RUN pip install ipython-sql sqlalchemy

# Expose the Jupyter Notebook port and PostgreSQL port
EXPOSE 8888 5432

# Copy the start script and make it executable
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Switch back to the default user
#USER $NB_UID

# Set the entrypoint to start both PostgreSQL and Jupyter Notebook
ENTRYPOINT ["/start.sh"]
