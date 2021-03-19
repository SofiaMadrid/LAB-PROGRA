$a = Read-Host -Prompt "Menu principal
Usa 1 para mostrar numeros del 1 al 5
Usa 2 para mostrar numeros del 1 al 10
Elige una opción: _"


function contar
{
$a = 5; while ($a -ge 1) { echo $a; $a--; } 

}

function contar_2
{
$a = 10; while ($a -ge 1) { echo $a; $a--; }  
}


if ($a -eq "1"){
	write-host "elegiste la opcion 1:"
    contar
}
if ($a -eq "2"){
	write-host "elegiste la opcion 2"
    contar_2
}
