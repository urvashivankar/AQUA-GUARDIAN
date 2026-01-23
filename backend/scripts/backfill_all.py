
import os
import sys

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db.supabase import supabase
from utils.jurisdiction_utils import find_government_jurisdiction

def backfill_all():
    print("Run Smart Backfill for ALL Orphaned Reports...")
    
    # 1. Find Orphans
    res = supabase.table("reports").select("id, latitude, longitude").is_("government_id", "null").execute()
    orphans = res.data
    
    count = len(orphans)
    print(f"Found {count} orphaned reports.")
    
    if count == 0:
        return

    # 2. Assign each orphan
    assigned_count = 0
    for report in orphans:
        lat = report.get('latitude')
        lng = report.get('longitude')
        r_id = report.get('id')
        
        if lat and lng:
            gov_id = find_government_jurisdiction(lat, lng)
            
            if gov_id:
                print(f"Assigning Report {r_id} -> Jurisdiction {gov_id}")
                try:
                    supabase.table("reports").update({"government_id": gov_id}).eq("id", r_id).execute()
                    assigned_count += 1
                except Exception as e:
                    print(f"Failed to update {r_id}: {e}")
            else:
                print(f"No jurisdiction found for Report {r_id} at ({lat}, {lng})")
        else:
            print(f"Report {r_id} has invalid coordinates.")

    print(f"✅ Successfully assigned {assigned_count}/{count} orphans.")

if __name__ == "__main__":
    backfill_all()
