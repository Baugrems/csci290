import java.util.ArrayList;
import java.util.List;

public class Inventory {

	List<Item> items;

	public Inventory() {
		items = new ArrayList<>();
	}

	public void add(Item item) {
		items.add(item);
	}

	private void setDiscounts() {
		for(Item item : items) {
			if(item.name.equals("Gift Card")) { // Gift Cards are never discounted, just keep them the same with a continue in the loop
				continue;
			}
			if(item.timeInStore == 3 || item.timeInStore == 10) { // With gift card handled above, we don't need nearly as many if statements nested together
				item.price *= 0.9; // 10% discount on Tuesdays. 3 days and 10 days after Saturday
			} else if (item.timeInStore > 13) {
				item.price *= 0.75;   // These needed to be swapped, so > 13 would be seen separate from the 6. Don't need bread type shield... all else is removed by 14
			} else if (item.timeInStore > 6) {
				if (item.name == "Dairy") {
					item.price *= 0.75;
				}
			} else if (item.timeInStore > 4) {
				if(item.name == "Fruit") {
					item.price *= 0.75;
				}
			}
		}
	}

	private ArrayList<Item> findExpiredItems() { // We iterate over the items to remove here and return the arraylist of items over their time limit
		ArrayList<Item> itemsToRemove = new ArrayList<>();
		for(Item item: items) {
			if(item.name.equals("Gift Card")) { // Gift Cards do not expire.
				continue;
			}
			if(item.name == "Bread" && item.timeInStore > 14) { // combined the if statements so this isn't a giant mess of nested conditionals
				itemsToRemove.add(item);
				continue; // No need to check further, move to next item in loop
			} 
			if (item.name == "Dairy" && item.timeInStore > 7) {
				itemsToRemove.add(item); 
				continue; // No need to check further, move to next item in loop
			}
			if(item.name == "Fruit" && item.timeInStore > 5) {
				itemsToRemove.add(item);
				continue; // No need to check further, move to next item in loop (This one is not needed, but if we expand to more items it is useful and nice for symmetry
			}
		}
		return itemsToRemove;
	}

	private void incrementDay() { // Resets things while moving day forward
		for(Item item: items) {
			if(item.name.equals("Gift Card")) { // Gift Cards are never discounted, just keep them the same with a continue in the loop
				continue;
			}
			item.price = item.basePrice; // Reset the price each day to the original price
			item.timeInStore++; // This no longer needs to be shielded for certain types. Got rid of gift cards ever increasing
		}
	}

	public void updateInventory() {
		incrementDay(); // Reset prices and go up a day
		ArrayList<Item> itemsToRemove = findExpiredItems();
		for(Item item: itemsToRemove) { // Purge the items array of anything that we returned from expired function
			items.remove(item);
		}
		setDiscounts(); // Finally, set discounts for the day now that the list is trimmed, day is set correctly, and prices reset
	}
}
