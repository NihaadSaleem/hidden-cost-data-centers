import json
from datetime import date
import random

# simulate changing data (replace later with real API calls)
new_value = 415 + random.randint(-5, 5)

data = {
    "electricity_twh": new_value,
    "last_updated": str(date.today()),
    "note": "Estimated global data center electricity consumption"
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

print("Data updated!")
