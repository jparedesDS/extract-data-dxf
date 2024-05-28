# Data Extraction from DXF Files
This project provides a Python script to extract data from DXF files for entity identification in technical drawings.

Description
The script extracts data from various types of entities present in DXF files, such as lines, circles, arcs, polylines, text, dimensions, etc. It then uses this data to create a new DXF file with the same entities, formatted according to a specific format.

Features
Data extraction: The script can extract data from a wide variety of entities present in DXF files.
Custom format: Allows you to define a specific format for the entities in the new DXF file.
Support for multiple entity types: The script can handle different types of entities present in DXF files, including 2D and 3D entities.
Easy to use: Simply provide the path to the input DXF file and the script will automatically generate the output DXF file with the extracted data.

Requirements
Python 3.x
ezdxf library

python extract_dxf_data.py path/from/file.dxf
The script will generate a new DXF file with the extracted data formatted according to the specified format.
It also generates the vector output of the .dxf file.

Translated with DeepL.com (free version)
