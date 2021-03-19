#!/bin/bash

echo "este es un conteo del 1 al 5"

function fin {
	echo "Finalizado"
}

i=0

while [ $i -lt 5 ]
do
  ((i++))
  if [[ "$i" == '2' ]]; then
    continue
  fi
  echo "$i"
done



fin
