import os
import json
os.system("cls")

file = "data/raw_data.json"

intends_arr = []
querys_arr = []
responses_arr = []
related_arr = []

# ✅ Fix: Use UTF-8 encoding to handle special characters
with open(file, "r", encoding="utf-8") as file:
    all_data = json.load(file)
    for data in all_data:
        intend = data["tag"]
        questions = data["questions"]
        responses = data["response"]
        related = data["related"]

        if intend not in intends_arr:
            intends_arr.append(intend)
        
        querys_arr.append({
            "intent": intend,
            "questions": questions,
        })
        
        responses_arr.append({
            "intent": intend,
            "responses": responses,
        })
        
        if len(related) > 0:
            related_arr.append({
                "intent": intend,
                "related": related,
            })

# ✅ Save outputs in UTF-8 encoding
with open("data/intends.json", "w", encoding="utf-8") as f:
    json.dump(intends_arr, f, indent=1)
    
with open("data/querys.json", "w", encoding="utf-8") as f:
    json.dump(querys_arr, f, indent=1)

with open("data/responses.json", "w", encoding="utf-8") as f:
    json.dump(responses_arr, f, indent=1)

with open("data/related.json", "w", encoding="utf-8") as f:
    json.dump(related_arr, f, indent=1)

print("✅ Data processing completed successfully!")
