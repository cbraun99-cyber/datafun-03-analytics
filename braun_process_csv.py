#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
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

def count_synthetic_fields(file_path: pathlib.Path) -> dict:
    """Count how many synthetic football fields there are in the dataset."""
    try:
        synthetic_count = 0
        field_list = []  # Store details of synthetic fields
        
        with file_path.open('r', encoding='utf-8') as file:
            dict_reader = csv.DictReader(file)  
            
            # Check if required columns exist
            if 'Surface' not in dict_reader.fieldnames or 'NAME' not in dict_reader.fieldnames:
                logger.error("CSV file missing required columns 'Surface' or 'NAME'")
                return {"synthetic_count": 0, "total_fields_processed": 0, "synthetic_fields": []}
            
            for row in dict_reader:
                try:
                    surface = row.get("Surface", "").strip().lower()
                    name = row.get("NAME", "Unknown").strip()
                    
                    # Check for synthetic surface types
                    if any(keyword in surface for keyword in ["synthetic", "turf", "artificial"]):
                        synthetic_count += 1
                        field_list.append({
                            "name": name,
                            "surface": surface
                        })
                        
                except Exception as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")
        
        results = {
            "synthetic_count": synthetic_count,
            "total_fields_processed": dict_reader.line_num - 1,  # Subtract header row
            "synthetic_fields": field_list
        }
        return results
        
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {"synthetic_count": 0, "total_fields_processed": 0, "synthetic_fields": []}

def process_csv_file():
    """Read the football fields CSV and count synthetic fields."""
    
    # Path to your CSV data file
    input_file = pathlib.Path(FETCHED_DATA_DIR, "Football_Fields_8792193028106921212.csv")
    
    # Path to your output CSV file
    output_file = pathlib.Path(PROCESSED_DIR, "synthetic_football_fields_in_seattle.csv")
    
    # Call the function to count synthetic fields
    results = count_synthetic_fields(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results as CSV
    with output_file.open('w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        
        # Write summary header
        writer.writerow(["Synthetic Football Fields in Seattle - Analysis Summary"])
        writer.writerow([])
        
        # Write summary statistics
        writer.writerow(["Total football fields processed", results['total_fields_processed']])
        writer.writerow(["Number of synthetic fields", results['synthetic_count']])
        writer.writerow(["Percentage synthetic", f"{(results['synthetic_count']/results['total_fields_processed']*100):.1f}%"])
        writer.writerow([])
        
        # Write detailed list header
        writer.writerow(["Detailed List of Synthetic Football Fields"])
        writer.writerow([])
        writer.writerow(["Number", "Field Name (from NAME column)", "Surface Type"])
        writer.writerow([])
        
        # Write each synthetic field as a row
        if results['synthetic_fields']:
            for i, field in enumerate(results['synthetic_fields'], 1):
                writer.writerow([i, field['name'], field['surface']])
        else:
            writer.writerow(["No synthetic football fields found"])
    
    # Log the processing of the CSV file
    logger.info(f"Processed CSV file: {input_file}")
    logger.info(f"Found {results['synthetic_count']} synthetic football fields out of {results['total_fields_processed']} total")
    logger.info(f"Results saved to CSV: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")