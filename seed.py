from __future__ import annotations
import os
from models import Product, get_session, Base, ENGINE

SAMPLE = [
    {"name": "AA Batteries (24-pack)", "sku": "BAT-AA-24", "quantity": 18, "reorder_level": 10, "unit_cost": 0.22},
    {"name": "HDMI Cable 2m", "sku": "HDMI-2M", "quantity": 6, "reorder_level": 8, "unit_cost": 2.50},
    {"name": "USB-C Hub 7-in-1", "sku": "USBC-HUB7", "quantity": 3, "reorder_level": 5, "unit_cost": 14.90},
    {"name": "Ethernet Cat6 10m", "sku": "CAT6-10M", "quantity": 25, "reorder_level": 10, "unit_cost": 4.30},
    {"name": "Notebook A5 Grid", "sku": "NOTE-A5-G", "quantity": 12, "reorder_level": 12, "unit_cost": 1.10},
    {"name": "Gel Pen 0.5mm Black", "sku": "PEN-05-BLK", "quantity": 60, "reorder_level": 20, "unit_cost": 0.35},
    {"name": "Packing Tape (3)", "sku": "TAPE-PACK-3", "quantity": 2, "reorder_level": 6, "unit_cost": 1.75},
    {"name": "Label Roll 500ct", "sku": "LABEL-500", "quantity": 8, "reorder_level": 10, "unit_cost": 0.08},
]

def main():
    # Ensure tables exist
    Base.metadata.create_all(ENGINE)
    with get_session() as s:
        # Clear existing
        s.query(Product).delete()
        # Add sample
        for row in SAMPLE:
            s.add(Product(**row))
        s.commit()
        print("Seeded database with sample products.")

if __name__ == "__main__":
    os.makedirs("instance", exist_ok=True)
    main()
