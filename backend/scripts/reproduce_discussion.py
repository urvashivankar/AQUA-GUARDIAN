
import sys
import os
from pathlib import Path
import httpx
import asyncio

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(backend_dir))

from db.supabase import supabase

def get_latest_report_id():
    res = supabase.table("reports").select("id").limit(1).order("created_at", desc=True).execute()
    if res.data:
        return res.data[0]['id']
    return None

def reproduce_error():
    report_id = get_latest_report_id()
    if not report_id:
        print("No reports found to test with.")
        return

    print(f"Testing with Report ID: {report_id}")
    
    # Needs a real login to get a token, because the endpoint depends on get_current_user
    # We can use our debug_login logic
    email = "ahm.manager@gmail.com"
    password = "Govt@123"
    
    session = supabase.auth.sign_in_with_password({"email": email, "password": password})
    if not session.user:
        print("Login failed, cannot test.")
        return
        
    token = session.session.access_token
    
    # Now interact with FASTAPI endpoint locally
    # We assume the server is running or we can simulate the request logic directly? 
    # Calling the function directly is hard because of Depends(get_current_user) and UploadFile
    # So we use requests/httpx against the running server if possible.
    # OR we just invoke the logic manually?
    
    # Let's try to hit the local server if it's running (User said "Everything is running" implicitly or we can assume)
    # Actually, let's just use the Supabase client to insert directly? 
    # NO, the logic is in the API (file upload, checks).
    
    # Since we can't easily hit the running server from here without knowing port reliably (usually 8000), 
    # we'll interpret the failure from code.
    # BUT wait, the user provided a screenshot of the Frontend.
    
    # Let's try to simulate the check logic from api/discussions.py
    print("\n--- Simulating Backend Logic ---")
    message_type = "CLOSURE_NOTE"
    has_file = True
    
    VALID_TYPES = {
        "government": ["INFO_REQUEST", "STATUS_UPDATE", "PROOF_UPLOAD", "CLOSURE_NOTE"]
    }
    user_role = "government"
    
    print(f"Role: {user_role}")
    print(f"Message Type: {message_type}")
    print(f"Has File: {has_file}")
    
    # Check 1: Role
    allowed = VALID_TYPES.get(user_role, [])
    if message_type not in allowed:
        print(f"❌ Role Check Failed: {message_type} not in {allowed}")
    else:
        print(f"✅ Role Check Passed")
        
    # Check 2: File Attachment (THE BUG)
    if has_file:
        if message_type not in ["PROOF_UPLOAD", "CLARIFICATION", "FIELD_UPDATE"]:
             print(f"❌ File Check Failed: Attachments only allowed for PROOF_UPLOAD, CLARIFICATION, or FIELD_UPDATE. Got {message_type}")
        else:
             print(f"✅ File Check Passed")

if __name__ == "__main__":
    reproduce_error()
