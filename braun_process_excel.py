#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import sys

# Import from external packages
import openpyxl

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

def count_word_in_column(file_path: pathlib.Path, column_letter: str, word: str) -> int:
    """Count the occurrences of a specific word in a given column of an Excel file."""
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        count = 0
        for cell in sheet[column_letter]:
            if cell.value and isinstance(cell.value, str):
                # Count exact matches of the word (case-insensitive)
                if cell.value.strip().lower() == word.lower():
                    count += 1
        return count
    except Exception as e:
        logger.error(f"Error reading Excel file: {e}")
        return 0

def process_excel_file():
    """Read an Excel file, count occurrences of 'Free' in column E, and save the result."""
    
    # Path to your Excel data file
    input_file = pathlib.Path(FETCHED_DATA_DIR, "2023 HTS Revision 11 xlsx.xlsx")

    # Path to your output text file
    output_file = pathlib.Path(PROCESSED_DIR, "duty_free_count.txt")

    # Column to check for "Free" occurrences (Column E - General Rate of Duty)
    column_to_check = "E"

    # Word to count in the Excel file
    word_to_count = "Free"

    # Call the function to count occurrences of the word in the specified column
    free_count = count_word_in_column(input_file, column_to_check, word_to_count)
    
    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w', encoding='utf-8') as file:
        file.write("Duty Free Occurrence Analysis\n")
        file.write("=" * 30 + "\n\n")
        file.write(f"Excel file processed: {input_file.name}\n")
        file.write(f"Column analyzed: {column_to_check} (General Rate of Duty)\n")
        file.write(f"Search term: '{word_to_count}' (exact match)\n")
        file.write(f"Number of occurrences: {free_count}\n")
    
    # Log the processing of the Excel file    
    logger.info(f"Processed Excel file: {input_file}")
    logger.info(f"Found {free_count} occurrences of '{word_to_count}' in column {column_to_check}")
    logger.info(f"Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    process_excel_file()
    logger.info("Excel processing complete.")