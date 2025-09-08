"""
Main processing script that runs all data processing files in sequence.
"""

#####################################
# Import Modules
#####################################

import time
import subprocess
import sys
import pathlib

#####################################
# Declare Global Variables
#####################################

# List of scripts to run in order
SCRIPTS_TO_RUN = [
    "braun_get_csv.py",
    "braun_get_excel.py", 
    "braun_get_json.py",
    "braun_get_text.py",
    "braun_process_csv.py",
    "braun_process_excel.py",
    "braun_process_json.py",
    "braun_process_text.py"
]

# Delay between scripts in seconds
DELAY_BETWEEN_SCRIPTS = 5

#####################################
# Define Functions
#####################################

def run_script(script_name):
    """Run a Python script and print status messages."""
    print(f"⏳ Processing: {script_name}")
    
    try:
        # Run the script using the same Python interpreter
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, 
                              text=True,
                              timeout=300)  # 5 minute timeout per script
        
        if result.returncode == 0:
            print(f"✅ Successfully processed: {script_name}")
            # Print any output from the script
            if result.stdout.strip():
                print(f"   Output: {result.stdout.strip()}")
        else:
            print(f"❌ Failed to process: {script_name}")
            print(f"   Error: {result.stderr.strip()}")
            
    except subprocess.TimeoutExpired:
        print(f"⏰ Timeout processing: {script_name} (took too long)")
    except FileNotFoundError:
        print(f"❌ Script not found: {script_name}")
    except Exception as e:
        print(f"❌ Unexpected error processing {script_name}: {e}")

def main():
    """Main function to run all processing scripts."""
    print("=" * 60)
    print("STARTING DATA PROCESSING PIPELINE")
    print("=" * 60)
    print()
    
    # Get the current directory
    current_dir = pathlib.Path(__file__).parent
    
    for script in SCRIPTS_TO_RUN:
        script_path = current_dir / script
        
        if script_path.exists():
            run_script(script)
        else:
            print(f"❌ Script not found: {script}")
        
        # Add delay between scripts (except after the last one)
        if script != SCRIPTS_TO_RUN[-1]:
            print(f"⏸️  Waiting {DELAY_BETWEEN_SCRIPTS} seconds before next script...")
            time.sleep(DELAY_BETWEEN_SCRIPTS)
            print()
    
    print()
    print("=" * 60)
    print("DATA PROCESSING PIPELINE COMPLETE")
    print("=" * 60)

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    main()