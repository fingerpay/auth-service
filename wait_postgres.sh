#!/bin/bash

set -e

user="$1" && shift
password="$1" && shift
host="$1" && shift
port="$1" && shift
db="$1" && shift
cmd=$@

# \e や \x1b または $'\e' は使用しない
ESC=$(printf '\033')

until psql "user=$user password=$password host=$host port=$port dbname=$db" -c "\q"; do
  echo "DB is unavailable - waiting" >&2
  echo "" >&2
  sleep 5
done

if [ ! -e ./.venv ]; then
  printf "${ESC}[33m%s${ESC}[m\n" "[! WARNING !]" >&2
  printf "${ESC}[33m%s${ESC}[m\n" "Directory ./.venv not found." >&2
  printf "${ESC}[33m%s${ESC}[m\n" "Creating new virtual environment..." >&2
  echo "" >&2

  if [ -f pyproject.toml ]; then
    poetry install
  fi
fi

echo "DB is ready - executing command" >&2
echo "" >&2

set +e
eval $cmd
cmd_result=$?
set -e

if [ "$FP_AUTH_IS_DEBUG" = 1 ] && [ $cmd_result != 0 ]; then
  printf "${ESC}[33m%s${ESC}[m\n" "[! NOTICE !]" >&2
  printf "${ESC}[33m%s${ESC}[m\n" "The previous command did not exit with code 0." >&2
  printf "${ESC}[33m%s${ESC}[m\n" "Entering debug mode..." >&2
  printf "${ESC}[33m%s${ESC}[m\n" "To terminate this process, simply just kill me or shutdown." >&2
  echo "" >&2

  sleep 3600
fi
