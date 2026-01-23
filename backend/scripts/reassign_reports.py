
import os
import sys

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db.supabase import supabase
from utils.jurisdiction_utils import find_government_jurisdiction

def reassign_all():
    print("Run Full Reassignment Check...")
    
    # 1. Fetch All Reports
    res = supabase.table("reports").select("id, latitude, longitude, government_id").execute()
    reports = res.data
    
    print(f"Checking {len(reports)} reports for correct jurisdiction assignment...")
    
    updates = 0
    errors = 0
    
    for report in reports:
        r_id = report.get('id')
        lat = report.get('latitude')
        lng = report.get('longitude')
        current_gov_id = report.get('government_id')
        
        if lat and lng:
            correct_gov_id = find_government_jurisdiction(lat, lng)
            
            # If we found a jurisdiction and it's different from current
            # Note: If correct_gov_id is None (outside all cities), we might want to set it to None?
            # For now, let's only update if we find a POSITIVE match that differs.
            
            if correct_gov_id: 
                if correct_gov_id != current_gov_id:
                    print(f"📝 Reassigning Report {r_id} (Lat: {lat}, Lng: {lng})")
                    print(f"   FROM: {current_gov_id}")
                    print(f"   TO:   {correct_gov_id}")
                    
                    try:
                        supabase.table("reports").update({"government_id": correct_gov_id}).eq("id", r_id).execute()
                        updates += 1
                    except Exception as e:
                        print(f"   ❌ Failed to update: {e}")
                        errors += 1
            else:
                # If report is outside all known jurisdictions
                if current_gov_id is not None:
                     print(f"⚠️ Report {r_id} at ({lat}, {lng}) is outside all cities but has gov_id={current_gov_id}. Leaving potential mismatch.")
        else:
             print(f"⚠️ Report {r_id} has no location data.")

    print(f"Summary: {updates} reports reassigned. {errors} errors.")

if __name__ == "__main__":
    reassign_all()
