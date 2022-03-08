public class Animal {
    public String name;
    public int hungerLevel;
    public String foodType;

    public static void sleep(){
        System.out.println("The animal is sleeping.")
    }

    public void eat(){
        System.out.println("It is feeding time.")
    }

    public void makeNoise(){
        System.out.println("The animal is screaming")
    }
}

class Cat extends Animal {
    public void makeNoise(){
        System.out.println("Meoww says the cat")
    }
}

class Dog extends Animal {
    public void play(){
        System.out.println("Fenza, the dog kicks footballs around")
    }
}

class animalSounds {
    public void getAnimalSounds(Animal a){
        a.makeNoise();
    }
}

// Objects of both Cat and Dog can be passed to a call to the getAnimalSounds method
    // For the Cat object: Meow says the cat will be displayed
    // Dog object: The animal is screaming will be displayed as it does not override this method in its class