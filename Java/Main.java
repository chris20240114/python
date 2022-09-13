public class Main {
  int x = 5;
}
class Rectangle {
  int width;
  int height;
  String rectangle_label;
  public Rectangle(String rectangle_label, int width, int height){
    this.width = width;
    this.height = height;
    this.rectangle_label = rectangle_label;
  }

  public String getname(){
    return rectangle_label;
  }
  public int getheight(){
    return height;
  }
  public int getwidth(){
    return width;
  }
  public int getperimeter(){
    return width*2+height*2;
  }
  public int getarea(){
    return width*height;
  }
  public String info(){
    return("Attributes of rectangle " + this.getname()+ ":\n The height is "+this.getheight() + ",\n the width is " + this.getwidth() + ",\n the perimeter is "+this.getperimeter() + ",\n the area is "+this.getarea());
  }
}
class Second {
  public static void main(String[] args) {
    Main myObj = new Main();
    Rectangle rect1 = new Rectangle("rect1", 17, 29);
    System.out.println(rect1.info());
    System.out.println(myObj.x);
  }
}