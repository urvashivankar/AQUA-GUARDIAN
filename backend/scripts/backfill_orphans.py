
import sys
import os
from pathlib import Path

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(backend_dir))

from db.supabase import supabase

def backfill_orphans():
    print("Run Backfill for Orphaned Reports...")
    
    # 1. Get Target Jurisdiction (Ahmedabad for demo)
    # Using the ID we found earlier for ahm.manager@gmail.com
    target_jurisdiction = "7fed3ea7-e22c-4e16-93c7-c21a900a3a95" # Ahmedabad
    
    # 2. Find Orphans
    res = supabase.table("reports").select("id").is_("government_id", "null").execute()
    orphans = res.data
    
    count = len(orphans)
    print(f"Found {count} orphaned reports.")
    
    if count == 0:
        print("No orphans to backfill.")
        return

    # 3. Update
    print(f"Assigning {count} reports to Jurisdiction {target_jurisdiction}...")
    
    # Supabase bulk update is tricky with .update(), we iterate or use 'in' filter
    # Ideally: supabase.table("reports").update({"government_id": target_jurisdiction}).is_("government_id", "null").execute()
    
    try:
        update_res = supabase.table("reports").update({"government_id": target_jurisdiction}).is_("government_id", "null").execute()
        print(f"✅ Successfully updated orphans.")
    except Exception as e:
        print(f"❌ Error updating: {e}")

if __name__ == "__main__":
    backfill_orphans()
