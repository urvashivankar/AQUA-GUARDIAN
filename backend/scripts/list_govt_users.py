
import sys
import os
from pathlib import Path

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(backend_dir))

from db.supabase import supabase

def list_govt_users():
    print("Listing All Users:")
    
    # Get all users (limit 50)
    users_res = supabase.table("users").select("*").execute()
    users = users_res.data
    
    print(f"Total Users: {len(users)}")
    
    for u in users:
        role = u.get('role')
        email = u.get('email')
        name = u.get('full_name') or u.get('name')
        
        # Check jurisdiction
        jur_res = supabase.table("government_jurisdictions").select("id, city_name").eq("government_user_id", u['id']).execute()
        jur_info = f"Linked to: {jur_res.data[0]['city_name']}" if jur_res.data else "❌ Unlinked"
        
        # Filter for relevant users
        if role == 'government' or (name and ('Ahmedabad' in name or 'Manager' in name)):
             print(f"User: {name} ({email}) | Role: {role} | ID: {u['id']} | {jur_info}")

if __name__ == "__main__":
    list_govt_users()
