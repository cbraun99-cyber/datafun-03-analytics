# datafun-03-analytics
Week 3 of Data Analytics Fundamentals \
\
Run py -m venv .venv \
then .venv\Scripts\activate \
run py -m pip install -r requirements.txt \

datafun-03-analytics
Automate the creation and management of standardized data folders for analytics projects.

Overview \
This project automates the setup of multiple folder structures for organizing data files in Python. It is a fork of the original https://github.com/cbraun99-cyber/datafun-03-analytics and expands on the that project initialization to support five folder variations for different data types and organizational needs.

Features \

braun_main_processor.py \
Runs all 8 processes in a controlled fashion
to run py .\braun_main_processor.py \

To run files individually: \

braun_get_csv.py \
Fetches Football_Fields_8792193028106921212.csv from https://data-seattlecitygis.opendata.arcgis.com/api/download/v1/items/8e333cf52e9d49808e6e4e0caab5af8d/csv?layers=0 \
to run py .\braun_get_csv.py \

braun_get_excel.py \
Fetches 2023 HTS Revision 11 xlsx.xlsx from https://www.usitc.gov/sites/default/files/tata/hts/hts_2023_revision_11_xlsx.xlsx \
to run py .\braun_get_excel.py \

braun_get_json.py \
Fetches Meteorite_Landings.json from https://data.nasa.gov/docs/legacy/meteorite_landings/Meteorite_Landings.json \
to run py .\braun_get_json.py \

braun_get_text.py \
Fetches readme_3.txt from https://ndownloader.figshare.com/files/44334662 \
to run py .\braun_get_text.py \

braun_process_csv.py \
Counts and lists the number of synthetic football fields in Seattle, WA \
to run py .\braun_process_csv.py \

braun_process_excel.py \
Counts the number of Duty Free products \
to run py .\braun_process_excel.py \

braun_process_json.py \
Counts the number of meteorite hits \
to run py .\braun_process_json.py \

braun_process_text.py \
Counts the number of total words in the text file \
to run py .\braun_process_text.py \

Requirements \
Python 3.8+ \
See requirements.txt for dependencies \

