import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class InventoryTest {

    @Test
    public void testGiftCardUpdates() {
        Item item = new Item("Gift Card", 20);
        Inventory inventory = new Inventory();
        inventory.add(item);

        inventory.updateInventory();

        Assertions.assertEquals(0, item.timeInStore);
        Assertions.assertEquals(20, item.price);
    }

    @Test
    public void testDairyUpdates() {
        Item item = new Item("Dairy", 50);
        Inventory inventory = new Inventory();
        inventory.add(item);

        inventory.updateInventory();
        Assertions.assertEquals(1, item.timeInStore);
        Assertions.assertEquals(50, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(2, item.timeInStore);
        Assertions.assertEquals(50, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(3, item.timeInStore);
        Assertions.assertEquals(45, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(4, item.timeInStore);
        Assertions.assertEquals(50, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(5, item.timeInStore);
        Assertions.assertEquals(50, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(6, item.timeInStore);
        Assertions.assertEquals(50, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(7, item.timeInStore);
        Assertions.assertEquals(37, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(0, inventory.items.size());
    }

    @Test
    public void testFruitUpdates() {
        Item item = new Item("Fruit", 30);
        Inventory inventory = new Inventory();
        inventory.add(item);

        inventory.updateInventory();
        Assertions.assertEquals(1, item.timeInStore);
        Assertions.assertEquals(30, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(2, item.timeInStore);
        Assertions.assertEquals(30, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(3, item.timeInStore);
        Assertions.assertEquals(27, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(4, item.timeInStore);
        Assertions.assertEquals(30, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(5, item.timeInStore);
        Assertions.assertEquals(22, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(0, inventory.items.size());
    }

    @Test
    public void testBreadUpdates() {
        Item item = new Item("Bread", 100);
        Inventory inventory = new Inventory();
        inventory.add(item);

        inventory.updateInventory();
        Assertions.assertEquals(1, item.timeInStore);
        Assertions.assertEquals(100, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(2, item.timeInStore);
        Assertions.assertEquals(100, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(3, item.timeInStore);
        Assertions.assertEquals(90, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(4, item.timeInStore);
        Assertions.assertEquals(100, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(5, item.timeInStore);
        Assertions.assertEquals(100, item.price);
        inventory.updateInventory();
        inventory.updateInventory();
        inventory.updateInventory();
        inventory.updateInventory();
        inventory.updateInventory();
        inventory.updateInventory();
        inventory.updateInventory();
        inventory.updateInventory();
        inventory.updateInventory(); // Day 14
        Assertions.assertEquals(14, item.timeInStore);
        Assertions.assertEquals(75, item.price);
        inventory.updateInventory();
        Assertions.assertEquals(0, inventory.items.size());
    }
    
    @Test
    public void testWeekdays() {
    	Item item1 = new Item("Bread", 100);
    	Item item2 = new Item("Bread", 100);
    	Item item3 = new Item("Bread", 100);
    	Inventory inventory = new Inventory();
    	inventory.add(item1);
    	
    	inventory.updateInventory();
    	inventory.updateInventory();
    	Assertions.assertEquals(2, item1.timeInStore);
        Assertions.assertEquals(100, item1.price);
        inventory.updateInventory(); // Tuesday, check for discounts
        Assertions.assertEquals(3, item1.timeInStore);
        Assertions.assertEquals(90, item1.price);
        inventory.updateInventory();
        Assertions.assertEquals(4, item1.timeInStore);
        Assertions.assertEquals(100, item1.price);
        inventory.add(item2); // Wednesday is here, add a new item from shipment
        Assertions.assertEquals(0, item2.timeInStore);
        Assertions.assertEquals(100, item2.price);
        inventory.updateInventory(); // Thursday
    	inventory.updateInventory(); // Friday
    	inventory.updateInventory(); // Saturday
    	inventory.add(item3); // new shipment of bread
    	inventory.updateInventory(); // Sunday
    	inventory.updateInventory(); // Monday
    	inventory.updateInventory(); // Tuesday discount time again
    	Assertions.assertEquals(10, item1.timeInStore);
        Assertions.assertEquals(90, item1.price);
        Assertions.assertEquals(6, item2.timeInStore);
        Assertions.assertEquals(90, item2.price);
        Assertions.assertEquals(3, item3.timeInStore);
        Assertions.assertEquals(90, item3.price); // Discounts should work for all items still in inventory
    }

}
