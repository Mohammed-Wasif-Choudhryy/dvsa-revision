import json

# Let's import the base questions from build_data
from build_data import questions as base_q

extra = [
    {
        "id": 73,
        "category": "Obscure Signs",
        "q": "What does a triangular warning sign depicting a tram within a red triangle mean?",
        "options": ["Trams crossing or sharing the road ahead", "Tram maintenance depot entrance only", "Trams have to give way to you", "Electric vehicle charging point"],
        "correct": 0,
        "explanation": "Trams operate quietly and cannot steer out of their tracks. The triangular sign warns you are approaching a tram crossing or tram route."
    },
    {
        "id": 74,
        "category": "Obscure Signs",
        "q": "What do DOUBLE RED lines along the edge of the carriageway (Red Route) signify in London and major cities?",
        "options": ["Strictly NO STOPPING at any time, even to set down passengers or unload", "No parking between 8am and 6pm", "Emergency service parking only", "Free loading zone for goods vehicles"],
        "correct": 0,
        "explanation": "Double red lines indicate a strict Red Route: NO STOPPING AT ANY TIME for any reason (including dropping off passengers or picking up goods)."
    },
    {
        "id": 75,
        "category": "Obscure Signs",
        "q": "What does a circular sign with a red ring showing '14′-6″' and '4.4m' with inward-pointing black arrows at the top and bottom indicate?",
        "options": ["Maximum vehicle height limit (prohibition)", "Recommended bridge clearance (advisory)", "Width restriction between bollards", "Distance to the next overhead gantry"],
        "correct": 0,
        "explanation": "Circular signs with a red ring give orders: inward-pointing vertical arrows indicate a mandatory MAXIMUM VEHICLE HEIGHT limit."
    },
    {
        "id": 76,
        "category": "Speed Limits",
        "q": "What is the maximum motorway speed limit for a bus or coach not exceeding 12 metres in overall length?",
        "options": ["70 mph (unless fitted with a 62 mph speed limiter)", "60 mph", "50 mph", "80 mph"],
        "correct": 0,
        "explanation": "Buses and coaches up to 12m length have a maximum motorway speed limit of 70 mph (though speed limiters may restrict them to 62 mph/100 km/h)."
    },
    {
        "id": 77,
        "category": "Speed Limits",
        "q": "What is the speed limit within a designated 20 mph zone (indicated by a 20 roundel sign surrounded by traffic calming features)?",
        "options": ["20 mph", "Advisory 20 mph, legal limit is 30 mph", "25 mph", "15 mph"],
        "correct": 0,
        "explanation": "A 20 mph zone sign indicates a mandatory 20 mph speed limit, typically accompanied by speed bumps, chicanes, and pedestrian priority."
    },
    {
        "id": 78,
        "category": "Crossings & Lights",
        "q": "When approaching a School Crossing Patrol displaying a round 'STOP - CHILDREN' sign, what MUST you do?",
        "options": ["You MUST stop before the sign and wait until the warden has returned completely to the pavement", "Slow down to 10 mph and navigate around them", "Sound your horn to alert children", "Stop only if children are actively on the road"],
        "correct": 0,
        "explanation": "You MUST stop when signalled to do so by a school crossing patrol. It is an offence to proceed before the patrol has stepped entirely off the carriageway."
    },
    {
        "id": 79,
        "category": "Crossings & Lights",
        "q": "When passing horses and riders on a public road, what are the two vital Highway Code rules?",
        "options": ["Pass at NO MORE THAN 10 mph and allow at least 2.0 metres of clearance", "Pass at 20 mph and tap your horn lightly", "Accelerate past quickly to minimise disturbance", "Leave 0.5 metres and rev engine so they know you are there"],
        "correct": 0,
        "explanation": "Highway Code Rule 215: Pass horses wide and slow. Keep speed to a MAXIMUM of 10 mph and maintain at least 2 metres clearance without sudden revs or horn sounds."
    },
    {
        "id": 80,
        "category": "Towing & Mechanics",
        "q": "What is 'noseweight' in relation to towing a caravan or trailer?",
        "options": ["The downward vertical force that the trailer's hitch puts onto the vehicle's towball", "The weight of the car's front engine and gearbox", "The drag created by the caravan's front wind deflector", "The weight of the car's front axle when loaded"],
        "correct": 0,
        "explanation": "Noseweight is the downward load exerted by the trailer hitch onto the towball. Proper noseweight (typically 50-100 kg) is critical to prevent dangerous snaking."
    },
    {
        "id": 81,
        "category": "Towing & Mechanics",
        "q": "When carrying a full load of passengers and heavy luggage in the boot, how should you adjust your tyre pressures?",
        "options": ["Increase tyre pressures to the manufacturer's recommended 'heavy load' settings", "Decrease tyre pressures to improve tyre footprint and grip", "Leave pressures unchanged", "Only increase the front tyre pressures"],
        "correct": 0,
        "explanation": "A heavily loaded car requires increased tyre pressures (specified in the vehicle handbook) to maintain tyre stability, prevent overheating, and ensure correct handling."
    },
    {
        "id": 82,
        "category": "Numbers & Limits",
        "q": "What is the minimum distance from which you must be able to read a standard UK vehicle registration number plate in good daylight (with glasses or contacts if worn)?",
        "options": ["20 metres (66 feet) for new style plates (20.5m for old style)", "15 metres (50 feet)", "30 metres (100 feet)", "10 metres (33 feet)"],
        "correct": 0,
        "explanation": "You must be able to read a standard post-2001 number plate from a distance of 20 metres (approx. 5 car lengths) in clear daylight."
    },
    {
        "id": 83,
        "category": "Numbers & Limits",
        "q": "Under what circumstance are you legally exempt from wearing a seatbelt while driving a passenger car?",
        "options": ["While carrying out a manoeuvre that includes reversing", "When driving on a quiet residential road at under 20 mph", "When driving a car older than 10 years", "When carrying a sleeping child"],
        "correct": 0,
        "explanation": "The law provides an exemption from wearing a seatbelt when you are reversing or supervising a learner driver who is reversing, or if you hold a valid medical exemption certificate."
    },
    {
        "id": 84,
        "category": "Numbers & Limits",
        "q": "What is the legal requirement for windscreen and front side window tinting on vehicles first used after 1 April 1985?",
        "options": ["Windscreen must let in at least 75% of light; front side windows at least 70%", "Windscreen 50%; front side windows 50%", "Any tint is legal as long as headlights are bright", "Windscreen 90%; side windows 90%"],
        "correct": 0,
        "explanation": "The windscreen MUST allow at least 75% of light through, and the front side windows MUST allow at least 70% of light through."
    },
    {
        "id": 85,
        "category": "Numbers & Limits",
        "q": "What should you do before selling a vehicle to ensure you are no longer legally responsible for it?",
        "options": ["Notify the DVLA immediately online or by sending the V5C/2 slip", "Give the entire V5C logbook to the buyer and do nothing else", "Notify your local police station", "Post the registration plates to the DVLA"],
        "correct": 0,
        "explanation": "You MUST notify the DVLA immediately online or send the relevant section of the V5C registration document to the DVLA, otherwise you remain liable for fines and tax."
    }
]

all_q = base_q + extra
print(f"Total compiled questions: {len(all_q)}")
with open('all_questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_q, f, indent=2)
print("Saved all_questions.json")
