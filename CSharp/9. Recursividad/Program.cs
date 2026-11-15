using System.Runtime.InteropServices;

Console.WriteLine("Funciones Recursivas");
/*
static TipoRetorno FuncionRecursiva(TipoParametro Parametro) {
    if (condiicondeParada) {
        return valorConocido;
    }
    else {
        return Operacion(Parametro, FuncionRecursiva(parametrorReducido));
    }
}
*/
// Funcion de Cuenta Regresiva
static void CuentraRegresiva(int n)
{
    // Caso base
    if (n < 0)
    {
        Console.WriteLine("¡Despegue!");
        return;
    }
    Console.WriteLine(n);
    CuentraRegresiva(n - 1); //Caso recursivo
}

CuentraRegresiva(7);

// Errores Comunes
/*
Sin caso base
static void f(int n) {
    return f(n-1)
}
Caso base inalcanzable
...
    if (n==0){
        ...
    }
    n==5;
    n-2;


No reducr el problema 
    return n+f(n) --> infnito

Desbordamiento
    f(1000000)  --> StacOverflowError
*/

Console.WriteLine("Funciones Recursivas Simpleas");
Console.WriteLine("-----------------------------");
Console.WriteLine("Factorial");
Console.WriteLine("---------");
/*
    Error --> n < 0
    n! = 1 --> n=0
    n! = nx (n-1)! --> n > 0
*/

static long Factorial(int n)
{

    if (n < 0)
        throw new ArgumentException("Numero no válido");
    if (n == 0) // Caso base
        return 1;
    else
        return n * Factorial(n - 1); // Caso Recursivo
}
Console.WriteLine($"Factorial de 5! = {Factorial(5)}");
Console.WriteLine($"Factorial de 0! = {Factorial(0)}");

Console.WriteLine("Potencia");
Console.WriteLine("---------");
/*
base^exp=1  --> exp=0
base^exp= base x base^(exp-1)   --> exp > 0
*/
static long Potencia(int baseNum, int exp)
{
    if (exp < 0)
        throw new ArgumentException("Exponente no válido");
    if (exp == 0)
        return 1;
    else
        return baseNum * Potencia(baseNum, exp - 1);
}

Console.WriteLine($"La potencia de 2^10 = {Potencia(2, 10)}");
Console.WriteLine("Sumatoria");
Console.WriteLine("---------");
// Suma 1 a n
static int SumaHasta(int n)
{
    if (n < 0)
        throw new ArgumentException("Numero no válido");
    if (n == 0)
        return 0;
    else
        return n + SumaHasta(n - 1);
}

Console.WriteLine($"La sumatoria de 10 primeros numeros es: {SumaHasta(10)}");
// Suma elementos lista
static int SumaLista(int[] lista, int i = 0)
{
    if (i >= lista.Length)
        return 0;
    else
        return lista[i] + SumaLista(lista, i + 1);
}

Console.WriteLine($"La suma de los elementos de la lista es: {SumaLista(new int[] { 1, 3, 5, 7, 9 })}");

// suma digitos de un numero
static int SumaDitigos(int n)
{
    if (n == 0)
        return 0;
    else
        return (n % 10) + SumaDitigos(n / 10);
}

Console.WriteLine($"La suma de los digitos del numero 123456 es: {SumaDitigos(123456)}");

Console.WriteLine("Conteo");
Console.WriteLine("---------");
//Conteo hacia arriba
static void ContarArriba(int n, int actual = 1)
{
    if (actual > n)
        return;
    Console.WriteLine(actual);
    ContarArriba(n, actual + 1);
}

ContarArriba(5);

//Contar digitos de un numero
static int ContarDigitos(int n)
{
    if (n == 0)
        return 0;
    else
        return 1 + ContarDigitos(n / 10);
}

Console.WriteLine($"El numero 987654 tiene {ContarDigitos(987654)} digitos");

//Contar cuantas veces aparece un elemento en una lista
static int ContarOcurrencias(int[] lista, int objetivo, int i = 0)
{
    if (i >= lista.Length)
        return 0;
    int coincide = (lista[i] == objetivo) ? 1 : 0;
    return coincide + ContarOcurrencias(lista, objetivo, i + 1);
}

Console.WriteLine($"El numero 1 se repite {ContarOcurrencias(new int[] { 1, 2, 1, 4, 6, 7, 1, 4, 1 }, 1)}");