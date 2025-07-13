from app.models.db import get_collection
from app.services.pinecone_service import upsert_product_vector, generate_embedding  # Ensure this is imported

def insert_mock_data():
    # --- MongoDB Collections ---
    users_collection = get_collection("users")
    consents_collection = get_collection("consents")

    # Optional: Clean existing data
    users_collection.delete_many({})
    consents_collection.delete_many({})

    # --- Insert Mock Users ---
    mock_users = [
        {"_id": f"u{i+1}", "name": name, "email": f"{name.lower().replace(' ', '_')}@example.com", "ceramic_stream_id": f"stream_{1000+i}"}
        for i, name in enumerate([
            "Aadra Sharma", "Riya Mehta", "Shyam Verma", "Karan Joshi", "Tanya Kapoor",
            "Arjun Sen", "Megha Rao", "Kabir Malhotra", "Isha Jain", "Rohan Das",
            "Neha Bansal", "Yash Arora", "Ananya Ghosh", "Rajeev Pillai", "Shruti Khanna",
            "Kunal Agarwal", "Nikita Roy", "Manav Gupta", "Pooja Sinha", "Varun Yadav",
            "Divya Nair", "Ritika Paul", "Aman Saxena", "Priya Kaul", "Rahul Bedi",
            "Simran Kaur", "Siddharth Iyer", "Avni Mishra", "Nikhil Rathi", "Pavitra Shetty",
            "Rajat Goel", "Sneha Menon", "Aditya Bhatt", "Kritika Sharma", "Mohit Rana",
            "Tina D'Souza", "Parth Tripathi", "Ira Mallick", "Devansh Pandey", "Vani Kohli",
            "Zoya Rehman", "Vikram Chauhan", "Jasmine Dey", "Harshit Bansal", "Anmol Singh",
            "Lavanya Nanda", "Deepak Negi", "Swati Jha", "Keshav Meena", "Anjali Dubey"
        ])
    ]
    users_collection.insert_many(mock_users)

    # --- Insert Mock Consents ---
    mock_consents = [
        {"user_id": f"u{i+1}", "given": (i % 2 == 0)}  # True for even indices (u1, u3...), False otherwise
        for i in range(50)
    ]
    consents_collection.insert_many(mock_consents)

    print("✅ Users and consents inserted")

    # --- Insert Mock Products into Pinecone ---
    mock_products = [
        {"id": "p1", "name": "Red Running Shoes", "description": "Lightweight shoes for daily workouts", "price": 59.99},
        {"id": "p2", "name": "Bluetooth Earbuds", "description": "True wireless stereo with long battery life", "price": 39.99},
        {"id": "p3", "name": "Smart LED Bulb", "description": "WiFi-enabled bulb with voice assistant support", "price": 12.99},
        {"id": "p4", "name": "Fitness Tracker", "description": "Tracks steps, calories, and heart rate", "price": 44.99},
        {"id": "p5", "name": "Laptop Stand", "description": "Adjustable height for better ergonomics", "price": 29.99},
        {"id": "p6", "name": "Electric Kettle", "description": "1.7L stainless steel with auto shut-off", "price": 24.49},
        {"id": "p7", "name": "Memory Foam Pillow", "description": "Orthopedic support for neck and spine", "price": 19.99},
        {"id": "p8", "name": "Reusable Water Bottle", "description": "Insulated stainless steel bottle", "price": 17.99},
        {"id": "p9", "name": "Face Moisturizer", "description": "Hydrating and oil-free for daily use", "price": 14.50},
        {"id": "p10", "name": "Backpack", "description": "Water-resistant laptop backpack for travel", "price": 34.99},
        {"id": "p11", "name": "Portable Blender", "description": "USB rechargeable personal smoothie maker", "price": 27.89},
        {"id": "p12", "name": "Yoga Mat", "description": "Eco-friendly non-slip mat for all practices", "price": 21.99},
        {"id": "p13", "name": "Desk Organizer", "description": "Multi-compartment organizer for home or office", "price": 15.99},
        {"id": "p14", "name": "Noise Cancelling Headphones", "description": "Over-ear design with ANC and Bluetooth", "price": 79.99},
        {"id": "p15", "name": "Ceramic Mug", "description": "Microwave and dishwasher-safe", "price": 9.99},
        {"id": "p16", "name": "Phone Tripod", "description": "Flexible mini tripod for smartphone photography", "price": 11.99},
        {"id": "p17", "name": "LED Desk Lamp", "description": "Dimmable with USB charging port", "price": 18.99},
        {"id": "p18", "name": "Wireless Mouse", "description": "Ergonomic design with adjustable DPI", "price": 13.49},
        {"id": "p19", "name": "Electric Toothbrush", "description": "Rechargeable with multiple cleaning modes", "price": 36.99},
        {"id": "p20", "name": "Cordless Vacuum Cleaner", "description": "Powerful suction for home and car", "price": 99.99},
        {"id": "p21", "name": "Gaming Keyboard", "description": "RGB backlit mechanical keyboard", "price": 59.49},
        {"id": "p22", "name": "Portable Charger", "description": "10,000mAh fast-charging power bank", "price": 22.99},
        {"id": "p23", "name": "Wireless Charger", "description": "Qi-certified with fast charge support", "price": 19.99},
        {"id": "p24", "name": "Laptop Sleeve", "description": "Padded waterproof protection", "price": 14.99},
        {"id": "p25", "name": "Scented Candles", "description": "Relaxing aroma for stress relief", "price": 16.99},
        {"id": "p26", "name": "Hair Dryer", "description": "Compact ionic dryer with foldable handle", "price": 32.99},
        {"id": "p27", "name": "Eyeglass Cleaner Kit", "description": "Streak-free lens wipes and microfiber cloths", "price": 7.99},
        {"id": "p28", "name": "Wall Clock", "description": "Silent non-ticking with modern design", "price": 23.49},
        {"id": "p29", "name": "Air Purifier", "description": "HEPA filter for allergens and dust", "price": 89.99},
        {"id": "p30", "name": "Kitchen Scale", "description": "Digital scale with LCD and tare function", "price": 10.49},
        {"id": "p31", "name": "Bluetooth Speaker", "description": "Portable and waterproof with deep bass", "price": 34.99},
        {"id": "p32", "name": "Electric Shaver", "description": "Rechargeable with precision trimming", "price": 44.89},
        {"id": "p33", "name": "Mini Projector", "description": "HD display for home theater experience", "price": 129.99},
        {"id": "p34", "name": "Tablet Stand", "description": "Adjustable and foldable for convenience", "price": 12.99},
        {"id": "p35", "name": "Makeup Brush Set", "description": "Professional soft bristle brushes", "price": 25.00},
        {"id": "p36", "name": "Laundry Basket", "description": "Collapsible and breathable mesh", "price": 14.59},
        {"id": "p37", "name": "Cooking Utensil Set", "description": "Heat-resistant silicone tools", "price": 29.99},
        {"id": "p38", "name": "Smart Thermostat", "description": "Energy-saving programmable device", "price": 149.99},
        {"id": "p39", "name": "Indoor Plant Pot", "description": "Self-watering ceramic pot", "price": 20.49},
        {"id": "p40", "name": "Resistance Bands", "description": "Full body workout bands with handles", "price": 19.99},
        {"id": "p41", "name": "Digital Alarm Clock", "description": "Large LED display with USB port", "price": 16.49},
        {"id": "p42", "name": "Bike Phone Mount", "description": "Secure adjustable holder for bikes", "price": 13.99},
        {"id": "p43", "name": "Car Air Freshener", "description": "Long-lasting scent with clip-on design", "price": 5.99},
        {"id": "p44", "name": "Desk Chair Cushion", "description": "Memory foam comfort support", "price": 28.49},
        {"id": "p45", "name": "Spice Rack Organizer", "description": "Rotating design for kitchen storage", "price": 22.49},
        {"id": "p46", "name": "Digital Drawing Tablet", "description": "Pen display for designers and artists", "price": 99.00},
        {"id": "p47", "name": "Sleep Mask", "description": "3D contoured for complete blackout", "price": 9.49},
        {"id": "p48", "name": "Pet Grooming Glove", "description": "Gentle de-shedding brush glove", "price": 8.99},
        {"id": "p49", "name": "WiFi Range Extender", "description": "Boosts signal for better coverage", "price": 34.99},
        {"id": "p50", "name": "Door Draft Stopper", "description": "Noise-blocking and energy saving", "price": 12.50},
    ]


    for product in mock_products:
        # Create embedding from name + description
        text = f"{product['name']} {product['description']}"
        vector = generate_embedding(text)

        # Push to Pinecone
        upsert_product_vector(
            product_id=product["id"],
            vector=vector,
            metadata=product
        )

    print("✅ Mock product vectors inserted into Pinecone")

if __name__ == "__main__":
    insert_mock_data()
