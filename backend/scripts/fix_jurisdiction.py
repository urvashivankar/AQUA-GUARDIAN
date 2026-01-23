
import sys
import os
from pathlib import Path

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(backend_dir))

from db.supabase import supabase

def fix_jurisdiction(email, city_name, gov_code):
    print(f"🚀 Fixing jurisdiction for {email} -> {city_name} ({gov_code})")
    
    try:
        # 0. Inspect Schema
        print("🔍 Inspecting table schema...")
        schema_res = supabase.table("government_jurisdictions").select("*").limit(1).execute()
        valid_keys = []
        if schema_res.data:
            print(f"Existing row sample: {schema_res.data[0].keys()}")
            valid_keys = list(schema_res.data[0].keys())
        else:
            print("⚠️ Table is empty, guessing minimal schema...")
            valid_keys = ["government_user_id", "city_name", "government_code", "latitude", "longitude"]

        # 1. Get User ID
        user_res = supabase.table("users").select("id").eq("email", email).execute()
        if not user_res.data:
            print(f"❌ User {email} not found.")
            return

        user_id = user_res.data[0]['id']
        print(f"User ID: {user_id}")
        
        # 2. Check for existing jurisdiction
        print("Checking for existing jurisdiction (by user)...")
        existing_by_user = supabase.table("government_jurisdictions").select("*").eq("government_user_id", user_id).execute()
        
        # 3. Check by code
        print(f"Checking for existing jurisdiction (by code: {gov_code})...")
        existing_by_code = supabase.table("government_jurisdictions").select("*").eq("government_code", gov_code).execute()

        payload = {
            "government_user_id": user_id,
            "city_name": city_name,
            "government_code": gov_code,
            "state": "Gujarat",
            "boundary_type": "city",
            "boundary_data": {
                "type": "Polygon",
                "coordinates": [[[72.5, 23.0], [72.6, 23.0], [72.6, 23.1], [72.5, 23.1], [72.5, 23.0]]]
            }
        }
        
        target_id = None
        
        if existing_by_user.data:
            print(f"Found existing record by USER. ID: {existing_by_user.data[0]['id']}")
            target_id = existing_by_user.data[0]['id']
        elif existing_by_code.data:
            print(f"Found existing record by CODE. ID: {existing_by_code.data[0]['id']}")
            print("Reassigning jurisdiction to new user...")
            target_id = existing_by_code.data[0]['id']
        
        if target_id:
            print(f"Updating record {target_id}...")
            res = supabase.table("government_jurisdictions").update(payload).eq("id", target_id).execute()
        else:
            print("Creating NEW jurisdiction record...")
            res = supabase.table("government_jurisdictions").insert(payload).execute()
        
        if not res.data:
             print("❌ Update/Insert failed to return data.")
             return

        print(f"✅ Jurisdiction Fixed! ID: {res.data[0]['id']}")
        
        # 4. Update reports
        jurisdiction_id = res.data[0]['id']
        print("🔄 Backfilling recent reports...")
        update_res = supabase.table("reports").update({"government_id": jurisdiction_id})\
            .is_("government_id", "null")\
            .execute()
        print(f"✅ Assigned {len(update_res.data)} reports.")

    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    fix_jurisdiction("ahm.manager@gmail.com", "Ahmedabad", "AMC")
