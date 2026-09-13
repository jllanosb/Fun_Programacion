Console.WriteLine("-- Funciones --");
static void Saludar()
{
    Console.WriteLine("Hola, Bienvenido a Fundamentos");
}
Saludar();    

Console.WriteLine("-- Funciones sin retorno --");
Console.WriteLine("----------------------------");
Menu();
static void Menu()
{
    Console.WriteLine("1. Registrar");
    Console.WriteLine("2. Buscar");
    Console.WriteLine("3. Salir");
}

Console.WriteLine("-- Funciones con retorno --");
Console.WriteLine("----------------------------");
int resultado= Producto(8,7);
Console.WriteLine($"{resultado}, Resultado*2={resultado*2}");
static int Producto(int a, int b)
{
    return a * b;    
}

Console.WriteLine("-- Funciones con varios parametros --");
Console.WriteLine("----------------------------");

static double Promedio(double t1, double t2, double t3, double ep, double ef)
{
    return t1*0.10 + t2*0.10 + t3*0.10 + ep* 0.20 + ef*0.50;
}

double prom = Promedio(20,20,20,14,12);
Console.WriteLine($"Promedio obtenido es: {prom}");

Console.WriteLine("-- Funciones con parametros predeterminados --");
Console.WriteLine("----------------------------");

static void saludar_estudiante(string nombre, string curso="Fundamentos de Programación")
{
    Console.WriteLine($"Hola {nombre}, Bienvenido a {curso}");
}

saludar_estudiante("Jaime");
saludar_estudiante("Jaime", "Base de Datos");

Console.WriteLine("-- Funciones Anidadas --");
Console.WriteLine("----------------------------");

static double Proceso_Compra(double monto)
{
    double aplicar_igv(double valor)
    {
        return valor*0.18;
    }
    double igv = aplicar_igv(monto);
    double total = monto + igv;
    return total;
}

double venta = Proceso_Compra(550);
Console.WriteLine($"Total a pagar s/.  {venta}");