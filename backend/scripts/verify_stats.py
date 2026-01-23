
import os
import sys

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db.supabase import supabase

def verify_stats():
    print("Verifying Dashboard Stats for All Cities...")
    print("-" * 50)
    print(f"{'City':<15} | {'Reports Count'}")
    print("-" * 50)
    
    # Fetch all jurisdictions
    jurs = supabase.table("government_jurisdictions").select("id, city_name").execute().data
    
    total_tracked = 0
    
    for jur in jurs:
        city = jur['city_name']
        jid = jur['id']
        
        # Count reports
        res = supabase.table("reports").select("id", count="exact").eq("government_id", jid).execute()
        count = res.count
        
        print(f"{city:<15} | {count}")
        total_tracked += count

    print("-" * 50)
    
    # Check for unassigned
    orphans = supabase.table("reports").select("id", count="exact").is_("government_id", "null").execute()
    orphan_count = orphans.count
    print(f"{'Unassigned':<15} | {orphan_count}")
    
    print("-" * 50)
    print(f"Total Assigned: {total_tracked}")
    print(f"Total Reports:  {total_tracked + orphan_count}")

if __name__ == "__main__":
    verify_stats()
