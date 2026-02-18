# PLAKTUKAS

A simple Python-based poster and placard generator.

## Description

PLAKTUKAS (Lithuanian for "poster" or "placard") is a lightweight Python library for creating formatted text-based posters and placards. Perfect for creating eye-catching terminal output, notifications, or simple text-based announcements.

## Features

- Create customizable text posters with titles and content
- Automatic text wrapping for long content
- Adjustable width (20-100 characters)
- Clean, bordered output format
- Simple and intuitive API

## Usage

### Basic Example

```python
from plaktukas import Plaktukas

# Create a simple poster
poster = Plaktukas(
    title="Welcome",
    content="This is a sample poster!",
    width=50
)

print(poster)
```

### Running the Demo

```bash
python3 plaktukas.py
```

## Installation

Simply copy `plaktukas.py` to your project directory or add this repository to your Python path.

## Testing

Run the test suite:

```bash
python3 -m unittest test_plaktukas.py -v
```

## API Reference

### Plaktukas Class

**Constructor:**
```python
Plaktukas(title="", content="", width=60)
```

**Parameters:**
- `title` (str): The title of the poster (optional)
- `content` (str): The main content/message (optional)
- `width` (int): Width of the poster in characters (default: 60, range: 20-100)

**Methods:**
- `generate()`: Returns the formatted poster as a string
- `__str__()`: Returns the same output as `generate()`

## Example Output

```
============================================================
                         PLAKTUKAS                          
------------------------------------------------------------
  Welcome to PLAKTUKAS - A simple poster and placard        
  generator!                                                
============================================================
```

## License

MIT
