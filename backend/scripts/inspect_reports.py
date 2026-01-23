
import os
import sys

# Add the backend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from db.supabase import supabase

def inspect_reports():
    print("Fetching reports...")
    # Fetch all reports, selecting relevant fields
    try:
        response = supabase.table('reports').select("*").execute()
        reports = response.data
        
        print(f"Total reports found: {len(reports)}")
        
        print("\nPossible Dummy Reports (Location = 'Unknown' or 'Ahmedabad'):")
        print("-" * 100)
        print(f"{'ID':<10} | {'Location':<20} | {'City':<15} | {'Created At':<25} | {'Description'}")
        print("-" * 100)
        
        dummy_count = 0
        for report in reports:
            # Check for potential dummy indicators
            location = report.get('location', 'N/A')
            city = report.get('city', 'N/A')
            
            # Use 'Unknown' or empty location as a primary indicator based on the user's screenshot
            if location == 'Unknown' or location is None or city == 'Ahmedabad': 
                 print(f"{str(report.get('id', ''))[:8]:<10} | {str(location)[:20]:<20} | {str(city)[:15]:<15} | {report.get('created_at', ''):<25} | {str(report.get('description', ''))[:50]}")
                 dummy_count += 1
        
        print("-" * 100)
        print(f"Total potential dummy reports linked to Ahmedabad/Unknown: {dummy_count}")

    except Exception as e:
        print(f"Error fetching reports: {e}")

if __name__ == "__main__":
    inspect_reports()
