
import sys
import os
from pathlib import Path
from datetime import datetime

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(backend_dir))

from db.supabase import supabase

def check_assignment():
    print("Checking Report Assignments (Last 20)...")
    
    # Get recent reports
    res = supabase.table("reports").select("id, description, status, government_id, created_at, location").order("created_at", desc=True).limit(20).execute()
    reports = res.data
    
    unassigned_count = 0
    for r in reports:
        assigned = "✅ Assigned" if r['government_id'] else "❌ ORPHANED"
        if not r['government_id']:
            unassigned_count += 1
        
        # Truncate description
        desc = (r['description'][:40] + '..') if len(r['description']) > 40 else r['description']
        print(f"[{r['created_at']}] {desc} | {r['status']} | {assigned} ({r['government_id']})")
        
    print(f"\nSummary: {unassigned_count} orphaned reports in last 20.")
    
    if unassigned_count > 0:
        print("\nPossible Causes:")
        print("1. Reports created before jurisdiction logic was fixed/added.")
        print("2. 'find_government_jurisdiction' logic returning None for the location.")
        print("3. Location coordinates not matching any known jurisdiction polygon.")

if __name__ == "__main__":
    check_assignment()
