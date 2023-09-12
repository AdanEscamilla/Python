#! /bin/bash

read -p "Introduce tu edad: " age
: ' echo "Tu edad es de: $age"
'
: '
    -eq: igual
    -le: lower or equal
    -ge: Greather or equal
    -lt: Lower than
    -gt: Grather than
'

if (( $age >= 31 ))
then 
    echo "Tienes más de 31"
elif (( $age -eq 30  ||  $age -eq 29 ))
then
    echo "Eres chavoruco"
else 
    echo "No tienes 20 años"
fi

: 'if [ $age -ge 31 ]
then 
    echo "Tienes más de 31"
elif [[ $age -eq 30 ] || [ $age -eq 29 ]]
then
    echo "Eres chavoruco"
else 
    echo "No tienes 20 años"
fi
'