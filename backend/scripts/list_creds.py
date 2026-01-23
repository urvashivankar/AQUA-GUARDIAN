
import os
import sys

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db.supabase import supabase

def list_govt_users():
    print("Fetching Government Users...")
    
    # We need to find users with role 'government'. 
    # Since auth.users is not directly accessible usually via client if not admin, 
    # we might check 'public.users' or 'government_jurisdictions'.
    
    try:
        # Join jurisdictions with user email if possible, or just list jurisdictions
        jurs = supabase.table("government_jurisdictions").select("*").execute().data
        
        print(f"{'City':<15} | {'Code':<10} | {'User ID'}")
        print("-" * 60)
        
        for jur in jurs:
            print(f"{jur['city_name']:<15} | {jur['government_code']:<10} | {jur['government_user_id']}")
            
        print("\nNote: For exact emails, please check the 'users' table or auth dashboard.")
        
        # Try fetching from public users table if it exists and has email
        try:
             users = supabase.table("users").select("*").execute().data
             print("\nPublic Users Table (Role Check):")
             for u in users:
                 role = u.get('role', 'N/A')
                 if role == 'government':
                     print(f"Email: {u.get('email')} | Role: {role} | ID: {u.get('id')}")
        except Exception as e:
            print(f"Could not fetch public users: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_govt_users()
