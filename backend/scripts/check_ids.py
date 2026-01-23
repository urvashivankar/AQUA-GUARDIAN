
import sys
import os
from pathlib import Path

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(backend_dir))

from db.supabase import supabase

def check_ids():
    email = "ahm.manager@gmail.com"
    password = "Govt@123"
    
    print(f"Checking IDs for: {email}")
    
    # 1. Get Auth ID via Login
    try:
        res = supabase.auth.sign_in_with_password({"email": email, "password": password})
        if not res.user:
             print("❌ Login Failed.")
             return
        auth_id = res.user.id
        print(f"🔑 Auth User ID (from Token): {auth_id}")
        
        # Check Metadata
        print(f"Metadata: {res.user.user_metadata}")
        role = res.user.user_metadata.get('role')
        print(f"Role in Metadata: {role}")
    except Exception as e:
        print(f"❌ Login Error: {e}")
        return

    # 2. Get Public ID via Table Query
    try:
        user_res = supabase.table("users").select("id").eq("email", email).execute()
        if user_res.data:
            public_id = user_res.data[0]['id']
            print(f"📋 Public User ID (from 'users' table): {public_id}")
        else:
            print("❌ Public User not found in 'users' table.")
            return
            
        # 3. Compare
        if auth_id == public_id:
            print("✅ IDs MATCH.")
        else:
            print("❌ IDs MISMATCH! Logic using 'users' table is getting wrong ID.")
            
        # 4. Check Jurisdiction Link
        jur_res = supabase.table("government_jurisdictions").select("id, government_user_id").eq("government_user_id", auth_id).execute()
        if jur_res.data:
            print(f"✅ Jurisdiction linked to Auth ID: {jur_res.data[0]['id']}")
        else:
            print(f"❌ No Jurisdiction linked to Auth ID ({auth_id})")
            
        jur_res_pub = supabase.table("government_jurisdictions").select("id, government_user_id").eq("government_user_id", public_id).execute()
        if jur_res_pub.data:
            print(f"Example: Jurisdiction linked to Public ID: {jur_res_pub.data[0]['id']}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_ids()
