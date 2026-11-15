public class oopspart2 {
    public static void main(String[] args)  {
        Smartphone s = new Smartphone();
        s.clickPhoto();
        s.playMusic();

    }
}
class Animal {
    void eat() {
        System.out.println("Animal is eating");
    }
}
class Dog extends Animal {//single inheritance 
    void bark() {
        System.out.println("Dog is barking");
    }
}//Animal --> Dog ---> Puppy
class Puppy extends Dog {//phir yai dog ko extend kar raha hai dog animal ko extend kiya tha yai hai multi inheritance 
    void weep() {
        System.out.println("Weeping");
    }
}
class Cat extends Animal {
    //yaha phir yai animal extend kar raha hai jab kai dog bhi animal ko extend kiya tha  Animal ----> Dog and Cat also extending it 
    void meow() {
        System.out.println("Meow");
    }
}
// Java classes ke through multiple inheritance allow nahi karta.jabkai java interfaces sai multiple inheritance achieve karta hai yaha 

//MULTIPLE INHERITANCE:through classes it will not allow such that through the interfaces it will do the multiple inheritance 
interface Camera {
    void clickPhoto();
}
interface MusicPlayer {
    void playMusic();
}
class Smartphone implements Camera, MusicPlayer {
    public void clickPhoto() {
        System.out.println("Photo Clicked");
    }
    public void playMusic() {
        System.out.println("Music Playing");
    }
}
//hybrid inheritance:Multiple + Hierarchical ka combination.Java classes ke through directly support nahi karta, lekin interfaces se kar sakte hain.
interface A {
    void show();
}
interface B extends A {
}
interface C extends A {
}
class D implements B, C {
    public void show() {
        System.out.println("Hybrid Inheritance");
    }
}
