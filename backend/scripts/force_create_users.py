
import sys
import os
from pathlib import Path

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(backend_dir))

from db.supabase import supabase

def create_govt_users():
    users_to_create = [
        {
            "email": "ahm.manager@gmail.com",
            "password": "Govt@123",
            "data": {"name": "Ahmedabad City Manager", "role": "government"}
        },
        {
            "email": "admin@ahmedabad.gov.in",
            "password": "Ahmedabad@123",
            "data": {"name": "Ahmedabad Municipal Corporation", "role": "government"}
        }
    ]

    print("🚀 Starting User Creation (Bypassing Rate Limits)...")

    for user in users_to_create:
        print(f"\nProcessing {user['email']}...")
        try:
            # Check if user already exists
            # We can't search by email directly with admin client easily without listing all, 
            # so we'll just try to create and catch error, or list all again (expensive).
            # ACTUALLY: admin.create_user will throw error if exists, which is fine.
            
            attributes = {
                "email": user["email"],
                "password": user["password"],
                "email_confirm": True, # Auto-confirm email
                "user_metadata": user["data"]
            }
            
            # Create user via Admin API
            new_user = supabase.auth.admin.create_user(attributes)
            
            if new_user:
                print(f"✅ User created successfully: {new_user.user.id}")
                
                # Also ensure they are in the 'users' table (public profile)
                print("   Ensuring public profile exists...")
                profile_data = {
                    "id": new_user.user.id,
                    "email": user["email"],
                    "full_name": user["data"]["name"],
                    "role": user["data"]["role"]
                }
                res = supabase.table("users").upsert(profile_data).execute()
                print("   ✅ Public profile upserted.")
                
        except Exception as e:
            print(f"⚠️ Failed to create {user['email']}: {e}")

if __name__ == "__main__":
    create_govt_users()
