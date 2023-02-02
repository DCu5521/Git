benjaminadams@Benjamins-MBP ~ % mkdir ships
benjaminadams@Benjamins-MBP ~ % cd ships
benjaminadams@Benjamins-MBP ships % git clone https://gitlab.com/NimboSurfer22/ships.git
Cloning into 'ships'...
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (12/12), done.
remote: Total 16 (delta 0), reused 16 (delta 0), pack-reused 0
Unpacking objects: 100% (16/16), done.
benjaminadams@Benjamins-MBP ships % git init
Initialized empty Git repository in /Users/benjaminadams/ships/.git/
benjaminadams@Benjamins-MBP ships % git remote add origin https://gitlab.com/NimboSurfer22/ships.git
benjaminadams@Benjamins-MBP ships % ls
ships
benjaminadams@Benjamins-MBP ships % touch README.md
benjaminadams@Benjamins-MBP ships % nano README.md
benjaminadams@Benjamins-MBP ships % git add README.md
benjaminadams@Benjamins-MBP ships % git commit -m "Python codes commits"
[master (root-commit) 5bc22c2] Python codes commits
 1 file changed, 60 insertions(+)
 create mode 100644 README.md
benjaminadams@Benjamins-MBP ships % git branch -a 
* master















#Code written in Python. - Addition Branch


class Shipment:
    def __init__(self, resource_id, order, shipment_location, shipment_date, expired_date, delivery_text, delivery_date, tracking_number, charge_amount):
        self.resource_id = resource_id
        self.order = order
        self.shipment_location = shipment_location
        self.shipment_date = shipment_date
        self.expired_date = expired_date
        self.delivery_text = delivery_text
        self.delivery_date = delivery_date
        self.tracking_number = tracking_number
        self.charge_amount = charge_amount

class ShipmentService:
    def __init__(self):
        self.shipments = []
    def add_shipment(self, shipment):
        self.shipments.append(shipment)





#Code written in Python. - Delete Branch

class ShipmentService:
    def __init__(self):
        self.shipments = []
    def delete_shipment(self, shipment):
        self.shipments.remove(shipment)




#Code written in Python. - GetShipment Branch

class ShipmentService:
    def __init__(self):
        self.shipments = []
    def get_shipment(self, resource_id):
        for shipment in self.shipments:
            if shipment.resource_id == resource_id:
                return shipment




#Code written in Python. - Memory Branch


class ShipmentService:
    def __init__(self):
        self.shipments = []
    def filter_shipments(self, filter_func):
        return filter(filter_func, self.shipments)
    def sort_shipments(self, sort_func):
        return sorted(self.shipments, key=sort_func)

