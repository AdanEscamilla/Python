#! /bin/bash

mkdir -p Taller_clase_2/Archivos/Textos_Planos
mkdir -p Taller_clase_2/Mover_Imagen1_aqui

cd ./Taller_clase_2/Archivos
mkdir Pdf
cd Textos_planos
touch Texto_plano1.txt Texto_plano2.txt
echo "EL PROFE RIFA Y LO QUIERO MUCHO 💕" > Texto_plano1.txt
cp Texto_plano1.txt ./Texto_plano2.txt
cd ..
cd Pdf
pdf=http://www.economia.unam.mx/deschimex/cechimex/chmxExtras/repositorio/archivos/Hola.pdf
curl -o Explicacion.pdf $pdf
cd ..
cd ..
Imagen1=https://e.rpp-noticias.io/xlarge/2020/01/31/234923_894633.png
curl -o Imagen1.png $Imagen1
mv Imagen1.png Mover_Imagen1_aqui
tree ./ > estructura.txt
echo "EL PROFE RIFA Y LO QUIERO MUCHO 💕" >> estructura.txt
