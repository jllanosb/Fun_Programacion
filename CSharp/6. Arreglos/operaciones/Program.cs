Console.WriteLine("Operacions con Arreglos");
Console.WriteLine("Operacions INSERCION");
// Insercion en posicion especifica de la lista
List<string> productos = new List<string> {"Teclado", "Mouse", "Laptop"};
productos.Insert(1, "Parlantes");
Console.WriteLine(string.Join(", ", productos));

// Insercion al Final de la lista
productos.Add("Refrigeradora");
Console.WriteLine(string.Join(", ", productos));

// Insercion Multiple
productos.AddRange(new List<string> {"Hp", "Dell", "Asus", "Lenovo", "Hp"});
Console.WriteLine(string.Join(", ", productos));

Console.WriteLine("Operacions BUSQUEDA");
// Busqueda
if (productos.Contains("Hp")) {
    int posicion = productos.IndexOf("Hp");
    Console.WriteLine($"Encontrado en la Posicion: {posicion}");
}
else {
    Console.WriteLine("Producto No encontrado");
}

// Equivalen in
Console.WriteLine($"Contiene producto HP: {productos.Contains("Hp")}");
// Primera posicion
Console.WriteLine($"HP se encuentra en la Posicion: {productos.IndexOf("Hp")}");
// cantidad de repeticiones
Console.WriteLine($"Producto HP se repite: {productos.Count(x => x == "Hp")} veces");

Console.WriteLine("Operacions MODIFICACION");
// Modificacion en posicion
productos[5] = "Nvidia";
Console.WriteLine(string.Join(", ", productos));

// modificacion masiva
List<double> notas = new List<double> {12.9, 14.3, 19.1, 11.49};
for (int i=0; i<notas.Count; i++) {
    notas[i] = notas[i] + 0.9;
}
Console.WriteLine(string.Join(", ", notas));

// Modificacion por segmento
for (int j=0; j<=3; j++) {
    productos[j]=productos[j].ToUpper();
}
Console.WriteLine(string.Join(", ", productos));

// Modificacion TransformacionMasiva
List<double> salarios = new List<double> {2000, 1560, 2700, 4000};
salarios = salarios.Select(salario => salario > 1900 ? salario * 1.1: salario).ToList();
Console.WriteLine(string.Join(", ", salarios));

Console.WriteLine("Operacions ELIMINACION");
// Eliminacion de un valor
productos.Remove("Refrigeradora");
Console.WriteLine(string.Join(", ", productos));

// Eliminacion por indice
productos.RemoveAt(1);
Console.WriteLine(string.Join(", ", productos));

// Eliminacion por RANGO
productos.RemoveRange(1,2);
Console.WriteLine(string.Join(", ", productos));

// Eliminacion por criterio
List<int> datos = new List<int> {11,11,20,18,11,20,17,16};
datos.RemoveAll(x=>x == 11);
Console.WriteLine(string.Join(", ", datos));

// Vaciar la lista
salarios.Clear();
Console.WriteLine(string.Join(", ", salarios));