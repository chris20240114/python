public class AddFractions 
{
    public static int fractions(int a, int b, int c, int d){
    int x = a*d+b*c;
    int y = b*d;
    int z = x/y;
    
    System.out.printf("The numerator of the first fraction is %d", a);
    System.out.println("");
    System.out.printf("The denominator of the first fraction is %d", b);
    System.out.println("");
    System.out.printf("The numerator of the second fraction is %d", c);
    System.out.println("");
    System.out.printf("The denominator of the second fraction is %d", d);
    System.out.println("");
    System.out.printf("The sum of %d/%d + %d/%d = %d/%d", a, b, c, d, x, y);
    System.out.println("");
    return z;
}
    public static void main(String[] args)
    {
        //Your code goes here!
            fractions(1, 2, 2, 5);
            int firstNum = 1;

    int firstDen = 2;
    int secondNum = 2;
    int secondDen = 5;
    int newNum;
    int newDen;
    System.out.print("The numerator of the first fraction is ");
    System.out.println(firstNum);
    System.out.print("The denominator of the first fraction is ");
    System.out.println(firstDen);
    System.out.print("The numerator of the second fraction is ");
    System.out.println(secondNum);
    System.out.print("The denominator of the second fraction is ");
    System.out.println(secondDen);
    newNum = (firstNum * secondDen + secondNum * firstDen);
    newDen = firstDen * secondDen;
    System.out.print("The sum of ");
    System.out.print(firstNum);
    System.out.print("/");
    System.out.print(firstDen);
    System.out.print(" + ");
    System.out.print(secondNum);
    System.out.print("/");
    System.out.print(secondDen);
    System.out.print(" = ");
    System.out.print(newNum);
    System.out.print("/");
    System.out.println(newDen);
    boolean x = true;
    int a = 2;
    int b = 3;
    int c = 4;
    System.out.println(a * b + b / a + (a * c / 4.0) * c);
    }
}