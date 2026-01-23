import os
import sys
from dotenv import load_dotenv

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

from db.supabase import supabase

def remove_dummy_reports():
    print("🧹 Starting cleanup of dummy reports...")

    # Patterns identified from seed scripts
    dummy_description_patterns = [
        "Looks severe.", # From seed_demo_data_robust.py
        "Severity level", # From seed_demo_data.py
    ]

    try:
        # Fetch all reports first to filter safely in python or use 'ilike' query
        print("🔍 Scanning for dummy reports...")
        
        # We'll use multiple queries to be safe and cover both seed patterns
        
        # Pattern 1: "Looks severe."
        res1 = supabase.table("reports").select("id, description").ilike("description", "%Looks severe.").execute()
        reports_to_delete = res1.data if res1.data else []
        
        # Pattern 2: "Severity level <number>."
        res2 = supabase.table("reports").select("id, description").ilike("description", "%Severity level %").execute()
        if res2.data:
            reports_to_delete.extend(res2.data)

        # Deduplicate
        unique_ids = list(set([r['id'] for r in reports_to_delete]))
        
        if not unique_ids:
            print("✅ No dummy reports found matching known patterns.")
            return

        print(f"⚠️ Found {len(unique_ids)} dummy reports to delete.")
        
        # Confirm deletion (auto-confirm for this script as per task)
        # Delete in batches if necessary, but Supabase handles list well usually
        
        print(f"🗑️ Deleting {len(unique_ids)} reports...")
        
        # Delete related photos first if cascade isn't set up (safeguard)
        try:
            supabase.table("photos").delete().in_("report_id", unique_ids).execute()
            print("   - Deleted associated photos.")
        except Exception as e:
            print(f"   - (Warning) Error deleting photos (might trigger cascade later): {e}")

        # Delete reports
        delete_res = supabase.table("reports").delete().in_("id", unique_ids).execute()
        
        if delete_res.data:
            print(f"✅ Successfully deleted {len(delete_res.data)} reports.")
        else:
            print("❓ Warning: Delete command ran but returned no data (check if rows were actually deleted).")

    except Exception as e:
        print(f"❌ Error during cleanup: {e}")

if __name__ == "__main__":
    remove_dummy_reports()
