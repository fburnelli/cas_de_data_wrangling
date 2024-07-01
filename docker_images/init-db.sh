#!/bin/bash
set -e
echo "Running PostgreSQL initialization script"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE test_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    );
    INSERT INTO test_table (name) VALUES ('example1'), ('example2');
EOSQL

