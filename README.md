# Data Extraction from DXF Files  

This project provides a Python script to extract data from DXF files for entity identification in technical drawings.  

---

## Table of Contents  
- [Description](#description)  
- [Features](#features)  
- [Requirements](#requirements)  
- [Usage](#usage)  
- [Output](#output)  
- [License](#license)  

---

## Description  

This script extracts data from various types of entities present in DXF files, such as:  
- Lines  
- Circles  
- Arcs  
- Polylines  
- Text  
- Dimensions  

Once the data is extracted, the script generates a new DXF file with the same entities, formatted according to a specific user-defined format.  

---

## Features  

- **Data Extraction**: Extracts data from a wide variety of entities in DXF files.  
- **Custom Formatting**: Allows defining a specific format for the entities in the output DXF file.  
- **Multi-Entity Support**: Handles both 2D and 3D entities, supporting a broad range of DXF structures.  
- **User-Friendly**: Provide the input DXF file path, and the script will automatically generate the formatted output.  

---

## Requirements  

- **Python 3.x**  
- **`ezdxf` library** (Install it with `pip install ezdxf`)  

---

## Usage  

To extract data from a DXF file and generate a new formatted DXF file:  

1. Clone the repository:  
```
   git clone https://github.com/jparedesDS/dxf-data-extraction.git  
   cd dxf-data-extraction
```
2. Run the script:
```
python extract_dxf_data.py path/to/input_file.dxf
```

## Output
Formatted DXF File: A new DXF file is generated with entities formatted according to the specified format.

Vector Representation: The script also generates a vector representation of the DXF file for additional use cases.

- Example
```
Input:
A DXF file containing a technical drawing with lines, circles, and text.

Output:
1. A new DXF file with the same entities in a custom format.
2. A vectorized representation of the file for visualization or further processing.
```
## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the project.
