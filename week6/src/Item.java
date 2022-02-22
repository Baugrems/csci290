// Importing date is not used, removed it.
public class Item {

    int timeInStore;
    String name;
    int price;
    int basePrice;
    
    
// I would probably also change the tests so each item type was its own class. That way we can overload functions a bit better and use some interfaces smoothly.
    //Gift cards especially should really just be their own class so we don't even use same functions.
    public Item(String name, int price) {
        this.name = name;
        this.price = price;
        this.basePrice = price; // set another variable to hold base-price so we can easily return to it
        this.timeInStore = 0;
    }
}
