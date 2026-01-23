
import os
import sys

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db.supabase import supabase

def delete_dummy_reports():
    print("Deleting dummy reports...")
    
    try:
        # Fetch reports with NULL location to confirm count before deletion
        response = supabase.table('reports').select("*").is_('location', 'null').execute()
        reports = response.data
        
        count = len(reports)
        print(f"Found {count} reports with NULL location.")

        if count > 0:
            print("Proceeding to delete...")
            # Perform deletion
            delete_response = supabase.table('reports').delete().is_('location', 'null').execute()
            print(f"Successfully deleted dummy reports.")
            
            # Verify deletion
            verify_response = supabase.table('reports').select("*").is_('location', 'null').execute()
            remaining = len(verify_response.data)
            print(f"Remaining reports with NULL location: {remaining}")
        else:
            print("No dummy reports found to delete.")

    except Exception as e:
        print(f"Error during deletion: {e}")

if __name__ == "__main__":
    delete_dummy_reports()
