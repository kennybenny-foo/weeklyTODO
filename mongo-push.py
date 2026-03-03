from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://kennymejia10_db_user:G6to5sPxHPp8gBhW@weeklytodo.amcsggs.mongodb.net/?appName=weeklyTODO"
client = MongoClient(MONGODB_URI)

db = client["Week"]  # Access the "weeklyTODO" database
collection = db["TODOs"]

#Write 
# collection.insert_one({
#     "day": "Monday",
#     "title": "Vacuum living room",
#     "category": "Indoor",
#     "estimated_time_minutes": 25,
#     "priority": "Medium",
#     "notes": "Focus under couch and corners"
# })

# collection.insert_one({
#     "day": "Monday",
#     "title": "Take out trash & recycling",
#     "category": "Outdoor",
#     "estimated_time_minutes": 10,
#     "priority": "High",
#     "notes": "Trash pickup is Tuesday morning"
# })

# collection.insert_one({
#     "day": "Tuesday",
#     "title": "Clean bathroom surfaces",
#     "category": "Indoor",
#     "estimated_time_minutes": 30,
#     "priority": "High",
#     "notes": "Disinfect sink, toilet, and mirror"
# })

# collection.insert_one({
#     "day": "Tuesday",
#     "title": "Water plants",
#     "category": "Outdoor",
#     "estimated_time_minutes": 15,
#     "priority": "Low",
#     "notes": "Front yard and patio plants"
# })

# collection.insert_one({
#     "day": "Wednesday",
#     "title": "Laundry (wash & fold)",
#     "category": "Indoor",
#     "estimated_time_minutes": 90,
#     "priority": "Medium",
#     "notes": "Separate lights and darks"
# })

# collection.insert_one({
#     "day": "Wednesday",
#     "title": "Mow lawn",
#     "category": "Outdoor",
#     "estimated_time_minutes": 45,
#     "priority": "Medium",
#     "notes": "Check gas level before starting"
# })

# collection.insert_one({
#     "day": "Thursday",
#     "title": "Dust furniture",
#     "category": "Indoor",
#     "estimated_time_minutes": 20,
#     "priority": "Low",
#     "notes": "Shelves, TV stand, and desk"
# })

# collection.insert_one({
#     "day": "Thursday",
#     "title": "Sweep driveway",
#     "category": "Outdoor",
#     "estimated_time_minutes": 20,
#     "priority": "Low",
#     "notes": "Clear leaves and debris"
# })

# collection.insert_one({
#     "day": "Friday",
#     "title": "Clean kitchen appliances",
#     "category": "Indoor",
#     "estimated_time_minutes": 40,
#     "priority": "High",
#     "notes": "Microwave, stovetop, and fridge handles"
# })

# collection.insert_one({
#     "day": "Friday",
#     "title": "Wash car",
#     "category": "Outdoor",
#     "estimated_time_minutes": 60,
#     "priority": "Medium",
#     "notes": "Vacuum interior if time permits"
# })

# collection.insert_one({
#     "day": "Saturday",
#     "title": "Organize closet",
#     "category": "Indoor",
#     "estimated_time_minutes": 60,
#     "priority": "Medium",
#     "notes": "Donate unused clothes"
# })

# collection.insert_one({
#     "day": "Saturday",
#     "title": "Trim hedges",
#     "category": "Outdoor",
#     "estimated_time_minutes": 35,
#     "priority": "Medium",
#     "notes": "Wear gloves"
# })

# collection.insert_one({
#     "day": "Sunday",
#     "title": "Meal prep for the week",
#     "category": "Indoor",
#     "estimated_time_minutes": 120,
#     "priority": "High",
#     "notes": "Prepare lunches and dinners"
# })

# collection.insert_one({
#     "day": "Sunday",
#     "title": "Clean patio furniture",
#     "category": "Outdoor",
#     "estimated_time_minutes": 30,
#     "priority": "Low",
#     "notes": "Wipe down tables and chairs"
# })

for f in collection.find():
    print(f)