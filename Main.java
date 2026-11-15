public class Main {
    public static void main(String[] args) {
        Calculator c1=new Calculator();
        System.out.println(c1.add(10,78,66));
        Cat cc=new Cat();
        cc.makeSound();
        Animal aan=new Animal();
        aan.makeSound();
        Payment payment;
        payment = new UpiPayment();
        payment.pay();
        payment = new CreditCardPayment();
        payment.pay();
        //static keyword explaination here 
        Student s1 = new Student();
        Student s2 = new Student();
        s1.name = "Syed";
        s2.name = "Ali";
        System.out.println(Student.college);//yaha Student kyu ho rahi bolto static keyword class mai hoti hai Student.college hona kyu ki college defined static String college sai horahi hai
        //static method 
        int result = MathUtil.add(10, 20);
        System.out.println(result);
        //super keyword from new 
        Doog d = new Doog();
        d.display();//black locally applied hai to agar color print karai to black aata hai agar super.color karain toh white aata hai
        Dogi de=new Dogi();
        de.display();
    }
}
//polymorphism: means MANY FORMS hence it can be defined as two types: 1)compile time polymorphism(static) which is method overloading It happens when multiple methods have the same name but different parameters. The compiler decides which method to call during compilation. and 2) run time polymorphism which is method overriding(dynamic) It happens when a child class provides its own implementation of a method already present in the parent class.The JVM decides at runtime which method to call.

class Calculator {//compile  time polymorphism compiler know which method to put at the compile time of it 
    int add(int a, int b) {
        return a + b;
    }
    double add(double a, double b) {
        return a + b;
    }
    int add(int a, int b, int c) {
        return a + b + c;
    }
}
class Animal {
    void makeSound() {
        System.out.println("Animal makes a sound");
    }
}
class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Dog barks");
    }
}
class Cat extends Animal {
    @Override
    void makeSound() {
        System.out.println("Cat meows");
    }
}
//Bhai interview mein agar pooche "Which polymorphism is more important in real projects?", answer: Runtime Polymorphism (Method Overriding) because it enables flexibility, abstraction, interfaces, dependency injection, and is used extensively in Spring Boot applications.

//PACKAGES IN JAVA:A package is a group of related classes, interfaces, enums, and sub-packages.Just like folders in Windows organize files, packages organize Java code.

//Why use Packages?
//✅ Avoid class name conflicts
 //✅ Better code organization
 //✅ Easier maintenance
 //✅ Access control (package-private access)
 //✅ Reusability
 //packages are defined in two types:1) built in packages 2)user defined packages 

 //ABSTRACTION:Abstraction means implementation details ko hide karna aur sirf essential features dikhana.java mai abstraction achieve karne kai 2 tarikai hai 1)abstract class 2)interface
abstract class Animallls {
    abstract void makeSound();
    void sleep() {//abstract class can make the normal methods tooo..
        System.out.println("Sleeping...");
    }//child class ko sleep already miljayega 
    //interface abstraction ka pure form hai 
}
interface Payment {
    void pay();//payment kaisi honi chaiyai jaisi kai upi payment aur credit card payment etc 
}
class UpiPayment implements Payment {
    @Override
    public void pay() {
        System.out.println("UPI Payment");
    }
}
class CreditCardPayment implements Payment {
    @Override
    public void pay() {
        System.out.println("Credit Card Payment");
    }
}
//what is the difference btw the abstraction and encapsulation : Abstraction is the process of hiding implementation details and showing only the essential functionality to the user. It is achieved using abstract classes and interfaces in Java.
//Encapsulation = Data Hiding  and Abstraction = Implementation Hiding

//KEYWORDS:
//static keyword:The static keyword in Java is used to create members that belong to the class rather than to individual objects of the class.
class Student {
    String name;
    static String college = "IIT Hyderabad";
}
//static method 
class MathUtil {
    static int add(int a, int b) {
        return a + b;
    }
}
//SUPER KEYWORD :The super keyword in Java refers to the immediate parent class object and is used to access parent class variables, methods, and constructors.super = parent class ko refer karne ke liye use hota hai.
class Animalii {
    String color = "White";
}
class Doog extends Animalii {
    String color = "Black";
    void display() {
        System.out.println(color);
        System.out.println(super.color);
    }
}
class Animalaa {
    void sound() {
        System.out.println("Animal Sound");
    }
}
class Dogi extends Animalaa {
    void sound() {
        System.out.println("Dog Barking");
    }
    void display() {
        sound();
        super.sound();
    }
}
//static → Belongs to Class
//this → Current Object
//super → Parent Object