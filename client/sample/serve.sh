#!/bin/bash

set -e

# \e や \x1b または $'\e' は使用しない
# Do nit use \e, \x1b and $'\e'
ESC=$(printf '\033')

port_number="$1"

# Check the argument if it is a number or not
# 引数が数字であるかどうかチェックする
if expr "$port_number" : "[0-9]*$" >&/dev/null; then
  :
else
  printf "${ESC}[33m%s${ESC}[m\n" "[! ERROR !]" >&2
  printf "${ESC}[33m%s${ESC}[m\n" "Expected port number as an argument, but got '${port_number}'." >&2

  exit 1
fi

# このファイル自身が置かれているパスの更に下の /pages に移動
my_path=$(cd $(dirname ${0}) && pwd)

cd "${my_path}/pages"

# Python でサーバー起動
printf "${ESC}[34m%s${ESC}[m\n" "Serving the server at http://localhost:${port_number} ..." >&2
python -m http.server $port_number
