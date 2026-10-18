using System.Numerics;
using System.Xml.Serialization;
using System.Text.RegularExpressions;

Console.WriteLine("Ordenamiento y Busqueda en Cadenas");
Console.WriteLine("Ordenamiento Alfabetico");

List<string> nombres = new List<string> {"Susana", "Diana", "Ana", "Zendaya","Maria"};
//Ordenar usando metodo sort
nombres.Sort();
//Mostrar la lista ordenada
foreach (string nombre in nombres) {
    Console.WriteLine(nombre);
}

Console.WriteLine("Ordenamiento por Longitud");
string[] paises = {"Uruguay", "Peru", "Chile", "Argentina", "USA", "Mexico", "Colombia"};
//Usando OrderBy
string[] ordenados = paises.OrderBy(p=>p.Length).ToArray();
//Mostrarlo
Console.WriteLine(string.Join(", ",ordenados));

Console.WriteLine("Ordenamiento personzalizado");
//usando OrderBy
string[] ordenados_per=paises.OrderBy(p=>p[p.Length -1]).ToArray();
//mostrarlo
Console.WriteLine(string.Join(", ", ordenados_per));

Console.WriteLine("Ordenamiento Metodo de la Burbuja");
string[] nombres2 =  {"Susana", "Diana", "Ana", "Zendaya","Maria"};
for (int i = 0; i < nombres2.Length; i++) {
    for (int j=0; j< nombres2.Length -1; j++) {
        if (string.Compare(nombres2[j], nombres2[j + 1]) > 0) {
            string temporal = nombres2[j];
            nombres2[j] = nombres2[j+1];
            nombres2[j+1] = temporal;
        }
    }
}
// mostrar ordenamiento
Console.WriteLine(string.Join(", ", nombres2));

Console.WriteLine("Ordenamiento Metodo de Seleccion");
string[] nombres3 =  {"Susana", "Diana", "Ana", "Zendaya","Yesenia"};
for (int i=0; i<nombres3.Length; i++){
    int menor = i;
    for (int j=i+1;j<nombres3.Length;j++){
        if (string.Compare(nombres3[j], nombres3[menor]) < 0) {
            menor = j;
        }
    }
    string temporal = nombres3[i];
    nombres3[i]=nombres3[menor];
    nombres3[menor]=temporal;
}
//mostrar ordenamiento
Console.WriteLine(string.Join(", ", nombres3));

Console.WriteLine("Ordenamiento Metodo de Insercion");
string[] nombres4 =  {"Luis", "Diana", "Ana", "Zendaya","Yesenia"};
for (int i=0; i<nombres4.Length; i++) {
    string actual = nombres4[i];
    int j=i-1;
    while (j>=0 && string.Compare(nombres4[j], actual) > 0) {
        nombres4[j+1] =nombres4[j];
        j--;
    }
    nombres4[j+1] = actual;
}
//mostrar ordenamiento
Console.WriteLine(string.Join(", ", nombres4));

Console.WriteLine("Busqueda en Cadenas");
Console.WriteLine("Busqueda Textual - Contains");
string mensaje = "Aprendiendo Fundamentos de Programación";
//verificar si la subcadena esta dentro del texto
bool existe = mensaje.Contains("Fundamentos");
Console.WriteLine(mensaje);
Console.WriteLine($"La palaba 'Fundamentos' esta dentro del texto: {existe}");

Console.WriteLine("Busqueda Exacta - Equals");
string clave = "N000127";
string codigo = "N000127";
bool coincide = clave.Equals(codigo);
Console.WriteLine($"La clave {clave} es igual a {codigo}: {coincide}");

Console.WriteLine("Busqueda Sensible a Mayusculas y Minusculas");
string curso = "PROGRAMACIÓN";
string buscar ="programación";
bool coinciden = curso.Equals(buscar, StringComparison.OrdinalIgnoreCase);
Console.WriteLine($"{curso} es igual a {buscar}: {coinciden}");

Console.WriteLine("Busqueda Subcadenas");
string fragmento = "Aprendiendo";
bool existe_texto = mensaje.Contains(fragmento);
Console.WriteLine(mensaje);
Console.WriteLine($"La palabra {fragmento} esta dentro del texto: {existe_texto}");

Console.WriteLine("Busqueda Expresion Regular");
string placa = "ABC-123";
//Usar Regex. IsMacth
bool existe_digitos = Regex.IsMatch(placa, @"\d{3}");
Console.WriteLine($"Existe 3 digitos en la placa {placa}: {existe_digitos}");

Console.WriteLine("Busqueda Primera posicion - Indexof");
int posicion = curso.IndexOf("O");
Console.WriteLine(curso);
Console.WriteLine(posicion);

Console.WriteLine("Busqueda Ultima posicion - Indexof");
int Ultima_posicion = curso.LastIndexOf("A");
Console.WriteLine(curso);
Console.WriteLine(Ultima_posicion);

Console.WriteLine("Busqueda empieza texto especifico - startswith");
bool inicia = placa.StartsWith("ABC");
Console.WriteLine(inicia);

Console.WriteLine("Busqueda termina texto especifico - endswith");
bool termina = placa.EndsWith("123");
Console.WriteLine(termina);