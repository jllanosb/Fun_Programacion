Console.WriteLine("Modularidad");

// modulos --> funcion especifica

// Calcular Productos

static string leer_producto()
{
    Console.Write("Ingrese nombre de un producto: ");
    return Console.ReadLine();
}
static double leer_precio()
{
    Console.Write("Ingrese precio de un producto: ");
    return double.Parse(Console.ReadLine());
}
static double calcular_igv(double precio)
{
    return precio * 0.18;
}
static void mostrar_resultados(string nombre, double precio, double igv)
{
    double total = precio + igv;
    Console.WriteLine($"Producto: {nombre}");
    Console.WriteLine($"Precio: {precio}");
    Console.WriteLine($"IGV: {igv}");
    Console.WriteLine($"Total a pagar: {total}");
}
string nombre = leer_producto();
double precio = leer_precio();
double igv = calcular_igv(precio);
mostrar_resultados(nombre, precio, igv);
