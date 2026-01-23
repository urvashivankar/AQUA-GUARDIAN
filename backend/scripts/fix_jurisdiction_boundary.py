
import os
import sys
import json

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db.supabase import supabase


def fix_boundary():
    print("Fixing Jurisdiction Boundaries...")
    
    # Map of ID to Correct Data
    # IDs taken from debug_dashboard.py output
    updates = [
        {
            "id": "7fed3ea7-e22c-4e16-93c7-c21a900a3a95", # Ahmedabad (Already done, but keeping for safety)
            "city": "Ahmedabad",
            "lat": 23.0225, "lng": 72.5714
        },
        {
            "id": "59246491-25d5-4c11-bf3e-7ca732d73061", # Vadodara
            "city": "Vadodara",
            "lat": 22.3072, "lng": 73.1812
        },
        {
            "id": "63892cd8-8a5b-496e-b9b0-2112557dcb36", # Surat
            "city": "Surat",
            "lat": 21.1702, "lng": 72.8311
        },
        {
            "id": "9e51a481-e454-4edb-9253-767aab69f058", # Rajkot
            "city": "Rajkot",
            "lat": 22.3039, "lng": 70.8022
        },
        {
            "id": "9e365bf3-382e-4387-b560-f245299dbff8", # Bharuch
            "city": "Bharuch",
            "lat": 21.7051, "lng": 72.9959
        }
    ]
    
    for item in updates:
        print(f"Updating {item['city']}...")
        new_boundary = {
            "type": "city",
            "coordinates": {
                "lat": item['lat'],
                "lng": item['lng'],
                "radius_km": 50 
            }
        }
        
        try:
            response = supabase.table("government_jurisdictions").update({
                "boundary_data": new_boundary,
                "city_name": item['city']
            }).eq("id", item['id']).execute()
            
            print(f"✅ Success: {item['city']}")
            
        except Exception as e:
            print(f"❌ Error updating {item['city']}: {e}")


if __name__ == "__main__":
    fix_boundary()
