
import os
import sys
import pathlib
from dotenv import load_dotenv
from supabase import create_client, Client

# Add backend directory to sys.path
sys.path.append(str(pathlib.Path(__file__).parent.parent))

# Load environment variables
env_path = pathlib.Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

url: str = os.environ.get("SUPABASE_URL", "")
key: str = os.environ.get("SUPABASE_SECRET_KEY", "")

if not url or not key:
    print("❌ Error: SUPABASE_URL or SUPABASE_SECRET_KEY not found in .env")
    sys.exit(1)

supabase: Client = create_client(url, key)

def reset_passwords():
    print("🔄 Resetting City Manager Passwords...")
    
    users_to_reset = [
        {"email": "vdr.manager@gmail.com", "city": "Vadodara"},
        {"email": "surat.aqua@gmail.com", "city": "Surat"},
        {"email": "rajkot.monitoring@gmail.com", "city": "Rajkot"},
        {"email": "bharuch.supervisor@gmail.com", "city": "Bharuch"}
    ]
    
    new_password = "City@123"
    
    for user in users_to_reset:
        email = user['email']
        print(f"Processing {user['city']} ({email})...")
        
        try:
            # 1. Try to find user by email first (Admin API)
            # We can't easily 'find' by email with admin api in python client sometimes, so we just attempt update
            # If update fails, it means user likely doesn't exist in Auth (even if they are in public.users)
            
            attributes = {"password": new_password, "email_confirm": True}
            
            # Using updateUserById requires ID. Let's try to get ID from our public table 'users' first
            # Assuming public table is synced.
            
            res = supabase.table("users").select("id").eq("email", email).execute()
            
            if res.data:
                user_id = res.data[0]['id']
                print(f"   Found User ID: {user_id}")
                
                # Update Password via Admin API
                update_res = supabase.auth.admin.update_user_by_id(user_id, attributes)
                print(f"   ✅ Password Reset to: {new_password}")
                
            else:
                print(f"   ⚠️ User not found in public DB. Checking Auth directly not implemented in this script.")
                # We could try creating them if missing?
                # Let's assume they exist because we saw them in the previous step.
        
        except Exception as e:
            print(f"   ❌ Error updating: {e}")
            # Fallback: Try creating if "User not found" error logic was present (but here generally exception)

if __name__ == "__main__":
    reset_passwords()
