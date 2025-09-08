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

def count_total_meteorites(file_path: pathlib.Path) -> int:
    """Count the total number of meteorite hits in the dataset."""
    try:
        # Open the JSON file using the file_path passed in as an argument
        with file_path.open('r', encoding='utf-8') as file:
            # Load the JSON data
            meteorite_data = json.load(file)  

            # NASA data structure: the actual meteorite records are in the "data" key
            if isinstance(meteorite_data, dict) and "data" in meteorite_data:
                meteorite_list = meteorite_data["data"]
                if isinstance(meteorite_list, list):
                    return len(meteorite_list)
                else:
                    logger.warning("Meteorite data is not in expected list format")
                    return 0
            else:
                logger.warning("JSON data does not contain expected 'data' key")
                return 0
            
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return 0

def process_json_file():
    """Read a JSON file and count total meteorite hits."""

    # Path to your JSON data file
    input_file: pathlib.Path = pathlib.Path(FETCHED_DATA_DIR, "Meteorite_Landings.json")

    # Path to your output text file
    output_file: pathlib.Path = pathlib.Path(PROCESSED_DIR, "total_meteorite_hits.txt")
    
    # Count the total meteorite hits
    total_hits = count_total_meteorites(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w', encoding='utf-8') as file:
        file.write("Total Meteorite Hits Analysis\n")
        file.write("=" * 30 + "\n\n")
        file.write(f"Data source: NASA Meteorite Landings\n")
        file.write(f"Total number of meteorite hits: {total_hits:,}\n")
    
    # Log the processing of the JSON file
    logger.info(f"Processed JSON file: {input_file}")
    logger.info(f"Found {total_hits:,} total meteorite hits")
    logger.info(f"Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")