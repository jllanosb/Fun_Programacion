Console.WriteLine("-- Tipos de Variables --");
Console.WriteLine("Variable Local");
static void saludar()
{
    string nombre = "Jaime";
    Console.WriteLine($"Hola {nombre}, Bienvenido");
}

saludar();
//Console.WriteLine(nombre);

Console.WriteLine("Variable Global - Compartida");
int incrementar = 0;

static void incrementa(int a)
{
    //incrementar++;
    a++;
    Console.WriteLine($"El valor de incrementar es: {a}");
}

incrementa(incrementar);
incrementa(incrementar);

Console.WriteLine("Variable No Local");
static void calcularmonto()
{
    double subtotal = 100;
    double calcular_igv(double a)
    {
        return a * 0.18;
    }

    double resultado = calcular_igv(subtotal);
    Console.WriteLine($"El total a pagar es: {resultado + subtotal}");
}
calcularmonto();