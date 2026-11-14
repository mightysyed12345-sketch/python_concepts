public class Main {
    static class Car {
    String color;
    int speed;
    Car(Car s) {//copy constructor
        this.color=s.color;
        this.speed=s.speed;//reference copied 
    }
    void setcolor(String cc)  {
        color=cc;
    }
    public String getColor()  {
        return color;
    }
    void start() {
        System.out.println("Car Started");
    }
    Car()  {
        System.out.println("constructor is called ....");
    }
}
    public static void main(String[] args) {
        //object oriented programming system:Object-Oriented Programming (OOP) is a programming paradigm where programs are built using objects—self-contained units that hold data (attributes) and functions (methods).
        //why it is used:
        //Better code organization
        //Reusability through classes and inheritance
        //Easier debugging and maintenance
        //Supports large-scale software development
        //classes and objects:
        Car c1 = new Car();//created the car object called c1
        c1.color = "Red";
        c1.speed = 120;
        c1.start();
        //Car = Class (blueprint)
        //c1 = Object (actual car)
        //color, speed = Attributes/Data
        //start() = Method/Behavior
        Car c2=new Car(c1);
        c2.color="blue";
        c2.speed=230;
        System.out.println(c1.speed);
    }
}
//access and modifiers:who can use or modify a piece of code. They are central to encapsulation, one of the core principles of OOP, ensuring that internal object details are protected from unintended external access.by getters and setters
//Encapsulation:wrapping up the data & methods under a single unit it also implements data hiding
// constructors is the special method iinvoked automatically at the time of object creation  1)constructors have the same name as the classes or structure 2)constructors dont have the return type 3)memory allocation happens when constructor is called

