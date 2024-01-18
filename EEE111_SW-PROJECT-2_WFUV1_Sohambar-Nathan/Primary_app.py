from ItemTable import ModifiedDataInventoryDB
from ItemGui import ModifiedDataInventoryGUI

if __name__ == "__main__":
    db = ModifiedDataInventoryDB()  # Update the class name
    app = ModifiedDataInventoryGUI(db)  # Update the class name
    app.mainloop()

