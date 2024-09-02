# Honduras Municipality Extractor

A script to extract municipality names from Wikipedia.

## Setup

1. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```

3. Install required packages:
   ```
   pip install requests beautifulsoup4
   ```

## Usage

1. Ensure your virtual environment is activated:
   ```
   source venv/bin/activate
   ```

2. Run the script:
   ```
   python scripts/honduras_municipality_extractor.py
   ```

3. When finished, you can deactivate the virtual environment:
   ```
   deactivate
   ```

## Notes

- Remember to activate the virtual environment each time you work on this project.
- Add `venv/` to your `.gitignore` file to avoid committing it to version control.