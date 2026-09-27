Console.WriteLine("Procesamiento Datos en Arrays");

Console.WriteLine("Ordenamiento Arrays");
Console.WriteLine("Metodo de la Burbuja");
int [] numeros = {20, 56, 4, 90, 77, 23, 100, 1, 20, 89};
Console.WriteLine(string.Join(", ", numeros));
for (int pasar= 0; pasar<numeros.Length; pasar++) {
    for (int i=0; i< numeros.Length - 1; i++) {
        if(numeros[i] > numeros[i + 1]) {
            int temp = numeros[i];
            numeros[i]=numeros[i+1];
            numeros[i+1]=temp;
        }
    }
}
Console.WriteLine("Arreglo Ordenado");
foreach (int n in numeros){
    Console.Write($"{n}, ");
}
Console.WriteLine();
Console.WriteLine("Metodo de Seleccion");
int [] numeros2 = {20, 56, 4, 90, 77, 23, 100, 1, 20, 89};
Console.WriteLine(string.Join(", ", numeros2));
for (int j=0; j < numeros2.Length-1; j++){
    int posMenor = j;
    for (int k=j+1; k<numeros2.Length; k++) {
        if (numeros2[k] < numeros2[posMenor]) {
            posMenor = k;
        }
    }
    int temp1 = numeros2[j];
    numeros2[j] = numeros2[posMenor];
    numeros2[posMenor] = temp1;
}

Console.WriteLine("Arreglo Ordenado");
foreach (int x in numeros2){
    Console.Write($"{x}, ");
}

Console.WriteLine("Metodo Sort");
int [] numeros3 = {20, 56, 4, 90, 77, 23, 100, 1, 20, 89};
numeros3.Sort();
Console.WriteLine(string.Join(", ", numeros3));
