#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
import pathlib
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

FETCHED_DATA_DIR: str = "braun_data"
PROCESSED_DIR: str = "braun_processed"

#####################################
# Define Functions
#####################################

def count_meteorite_hits(file_path: pathlib.Path, target_location: str) -> int:
    """Count the number of meteorite hits on a specific location."""
    try:
        # Open the JSON file using the file_path passed in as an argument
        with file_path.open('r', encoding='utf-8') as file:
            # Load the JSON data
            meteorite_data = json.load(file)  

            # Initialize counter
            hit_count = 0

            # Check if the data is a list of meteorites
            if isinstance(meteorite_data, list):
                for meteorite in meteorite_data:
                    try:
                        # Get the location from the meteorite data
                        location = meteorite.get("location", "").strip()
                        
                        # Check for Elephant Mountain hits (case-insensitive)
                        if target_location.lower() in location.lower():
                            hit_count += 1
                            
                    except Exception as e:
                        logger.warning(f"Skipping invalid meteorite entry: {meteorite} ({e})")
            
            return hit_count
            
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return 0

def process_json_file():
    """Read a JSON file and count meteorite hits on Elephant Mountain."""

    # Path to your JSON data file
    input_file: pathlib.Path = pathlib.Path(FETCHED_DATA_DIR, "Meteorite_Landings.json")

    # Path to your output text file
    output_file: pathlib.Path = pathlib.Path(PROCESSED_DIR, "metorite_hits_on_elephant_mountain.txt")
    
    # Target location to search for
    target_location = "Elephant Mountain"
    
    # Count the meteorite hits
    hit_count = count_meteorite_hits(input_file, target_location)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w', encoding='utf-8') as file:
        file.write("Meteorite Hit Count Analysis\n")
        file.write("=" * 30 + "\n\n")
        file.write(f"Target location: {target_location}\n")
        file.write(f"Number of meteorite hits: {hit_count}\n")
    
    # Log the processing of the JSON file
    logger.info(f"Processed JSON file: {input_file}")
    logger.info(f"Found {hit_count} meteorite hits on {target_location}")
    logger.info(f"Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")