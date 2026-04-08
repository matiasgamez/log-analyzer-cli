# Log Analysis CLI Tool

## Overview

This project provides a command line tool for parsing and analyzing the content of log files. It processes structured log entries and extracts key metrics such as IP frequency, traffic volume, and request distribution over time.

The tool is designed to be simple, modular and robust, following the assignment requirements.

Basic DevSecOps practices are followed through containerization (Docker) and reproducible environments.

---

## Assumptions

- Log lines are expected to contain at least 10 fields
- Malformed lines are skipped during parsing
- Input files follow a consistent structure

---
## Features

- Parse structured log files into Python dictionaries.
- Compute the most frequent IP address.
- Compute the least frequent IP address.
- Calculate total byte transfer.
- Compute events per second.
- Export results to a JSON file.

---

## Structure

```
src/
├── main.py        # CLI entry point
├── parser.py      # Log parsing logic
└── functions.py   # Data processing functions
```

---

## Requirements

- Python 3.11+

---

## Usage

Run the project from the project root directory

```bash
python src/main.py --input <input.log> --output <output.json> [OPTIONS]
```

---

## Arguments

### Required:
- `--input`: Path to the input log file.
- `--output`: Path to the output file (JSON format).

### Optional
- `--mfip`: Most frequent IP address.
- `--lfip`: Least frequent IP address.
- `--bytes`: Total bytes exchanged.
- `--eps`: Events per second.

---

## Examples

### Most frequent IP
`python src/main.py --input access.log --output result.json --mfip`

### Multiple metrics
`python src/main.py --input access.log --output results.json --mfip --bytes --eps`

---

## Output

Results are saved in plain JSON format. 

---

## Notes

- The log file used for testing is not included due to its size
- The tool is designed to be extensible and fault-tolerant

---
## Author

*Matías Gámez Marín*



