
import sys
import os
from pathlib import Path
import random

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(backend_dir))

from db.supabase import supabase

def reproduce_campaign_error():
    print("🚀 Reproducing Campaign Error...")
    
    # 1. Create/Ensure NGO User (we can trust force_create concept or just check)
    email = "green.earth@ngo.org"
    password = "Ngo@123"
    
    # 2. Login as NGO
    print(f"Logging in as {email}...")
    try:
        res = supabase.auth.sign_in_with_password({"email": email, "password": password})
        if not res.user:
             print("❌ Login Failed. User might not exist. Please create user first.")
             return
        
        user_id = res.user.id
        token = res.session.access_token
        print(f"✅ Logged in. User ID: {user_id}")
    except Exception as e:
        print(f"❌ Login Error: {e}")
        return

    # 3. Create a High Severity Report
    print("Creating High Severity Report...")
    report_data = {
        "severity": 9,
        "description": "Critical Chemical Spill - TEST",
        "status": "Verified",
        "user_id": user_id, # Self-reported for ease
        "ai_class": "Chemical Hazard",
        "latitude": 22.3072, 
        "longitude": 73.1812
    }
    
    rep_res = supabase.table("reports").insert(report_data).execute()
    if not rep_res.data:
        print("❌ Failed to create test report.")
        return
        
    report_id = rep_res.data[0]['id']
    print(f"✅ Report Created: {report_id} (Severity: 9)")
    
    # 4. Simulate Backend Logic (since we can't easily curl local API without relying on port)
    # Logic from cleanup.py:
    # Check Severity -> Block if >= 8 and not government
    
    print("\n--- Simulating Backend Logic ---")
    user_role = "ngo" # We know this from context
    severity = 9
    
    print(f"User Role: {user_role}")
    print(f"Report Severity: {severity}")
    
    if severity >= 8 and user_role != "government":
        print(f"❌ BLOCKED: SAFETY PROTOCOL: High-severity incidents require HAZMAT clearance. Restricted to Government agencies only.")
    else:
        print(f"✅ ALLOWED: Cleanup started.")

if __name__ == "__main__":
    reproduce_campaign_error()
