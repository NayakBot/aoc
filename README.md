# aoc
Advent of Code solutions

### Alias for creation of folders:

This alias and template:
- create a folder for year/day basis 
- downloads the input for day mentioned
- creates a template with input loading and submit function

<br/>

First time setup:
- Create alias: ```sudo nano ~/.bashrc```
```
aocm() {
    YEAR=$2
    DAY=$1
    AOC_DIR="$HOME/aoc"  # Change this to your desired base directory for Advent of Code
    DAY_DIR="$AOC_DIR/$YEAR/day$DAY"
    TEMPLATE_FILE="$AOC_DIR/template.py"  # Replace with the path to your template file

    # Create year and day directories if they don't exist
    mkdir -p "$DAY_DIR"

    # Download input using aocd and save it
    aocd $DAY $YEAR > "$DAY_DIR/input.txt"

    # Copy the template file and replace placeholders with the day and year
    sed "s/{{DAY}}/$DAY/g; s/{{YEAR}}/$YEAR/g" "$TEMPLATE_FILE" > "$DAY_DIR/solution.py"

    # Change directory and open in VS Code
    cd "$DAY_DIR"
    code .
}

```
- Run ```source ~/.bashrc```
- Create a virtualenv and install:
```pip install aocd browser-cookies3```
---
- Running the command:
```aocm <day> <year>```

- Running the script:
```python solution.py <part>```
