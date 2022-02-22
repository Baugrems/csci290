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

}
