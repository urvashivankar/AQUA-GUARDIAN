
import sys
import os
from pathlib import Path

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(backend_dir))

from db.supabase import supabase

def create_ngo_user():
    email = "green.earth@ngo.org"
    password = "Ngo@123"
    
    print(f"Creating NGO user: {email}")
    
    try:
        # Use Admin API to create user
        user_attributes = {
            "email": email,
            "password": password,
            "email_confirm": True,
            "user_metadata": {
                "full_name": "Green Earth Alliance",
                "role": "ngo"
            }
        }
        
        user = supabase.auth.admin.create_user(user_attributes)
        print(f"✅ User created successfully: {user.user.id}")
        
    except Exception as e:
        print(f"Error creating user: {e}")

if __name__ == "__main__":
    create_ngo_user()
