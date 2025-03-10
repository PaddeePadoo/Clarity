#!/usr/bin/env bash
set -e

host="$1"
port="$2"
shift 2
cmd="$@"

until pg_isready -h db -p 5432 -U postgres; do
  echo "Postgres is unavailable - sleeping"
  sleep 2
done
echo "Postgres is up - executing command"