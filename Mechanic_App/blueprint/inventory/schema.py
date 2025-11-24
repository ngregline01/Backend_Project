from Mechanic_App.blueprint.models import Inventory
from Mechanic_App.blueprint.extensions import ma

class InventorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inventory
inventoryschema = InventorySchema()
inventorys_schema = InventorySchema(many = True)