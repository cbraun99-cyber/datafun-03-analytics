"""
Process a text file to count the total number of words and save the result.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
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

def count_total_words(file_path: pathlib.Path) -> int:
    """Count the total number of words in a text file."""
    try:
        with file_path.open('r', encoding='utf-8') as file:
            content: str = file.read()
            # Split the content by whitespace to get words and count them
            words = content.split()
            return len(words)
    except Exception as e:
        logger.error(f"Error reading text file: {e}")
        return 0

def process_text_file():
    """Read a text file, count total words, and save the result."""
 
    # Path to your text data file
    input_file = pathlib.Path(FETCHED_DATA_DIR, "readme_3.txt")

    # Path to your output text file
    output_file = pathlib.Path(PROCESSED_DIR, "total_word_count.txt")

    # Count total words in the file
    total_words: int = count_total_words(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Write the results to the output file
    with output_file.open('w', encoding='utf-8') as file:
        file.write("Total Word Count Analysis\n")
        file.write("=" * 25 + "\n\n")
        file.write(f"Text file processed: {input_file.name}\n")
        file.write(f"Total number of words: {total_words:,}\n")  # Format with commas for readability
    
    # Log the processing of the TEXT file
    logger.info(f"Processed text file: {input_file}")
    logger.info(f"Found {total_words:,} total words")
    logger.info(f"Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting text processing...")
    process_text_file()
    logger.info("Text processing complete.")