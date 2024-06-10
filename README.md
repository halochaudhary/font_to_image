# Font to Image
## Export Glyphs to PNG

This repository contains two Python scripts that use FontForge to export glyphs from a font file into PNG images. One script exports all glyphs, while the other exports only a selected range of glyphs. This can be useful for various purposes such as creating font previews, generating assets for graphic design, or simply inspecting individual glyphs in detail.

### Script 1: Export All Glyphs to PNG | font_to_image.py

This script exports all glyphs from a specified font file.

#### Features

- **Check Font File Existence:** Ensures the specified font file exists before processing.
- **Automatic Output Directory Creation:** Creates an output directory if it doesn't already exist.
- **Glyph Export:** Exports each glyph in the font to a separate PNG file.
- **File Existence Check:** Skips exporting if the PNG file for a glyph already exists to prevent overwriting.

#### Usage

To use this script, follow these steps:

1. **Install Dependencies:**
   Make sure you have FontForge installed on your system. You can install it using the following command:
   ```sh
   sudo apt install python3-fontforge
   ```

2. **Run the Script:**
   Execute the script with the font file as an argument:
   ```sh
   python export_all_glyphs.py <font_file>
   ```

   Replace `<font_file>` with the path to your font file.

### Example

```sh
python export_all_glyphs.py /path/to/font.ttf
```

### Script 2: Export Selected Glyphs to PNG | font_to_image_selected_glyphs.py

This script exports only the selected glyphs (digits 0-9 and uppercase letters A-Z) from a specified font file.

#### Features

- **Check Font File Existence:** Ensures the specified font file exists before processing.
- **Automatic Output Directory Creation:** Creates an output directory if it doesn't already exist.
- **Selected Glyph Export:** Exports glyphs for digits (0-9) and uppercase letters (A-Z) to separate PNG files.
- **File Existence Check:** Skips exporting if the PNG file for a glyph already exists to prevent overwriting.
- **Glyph Validity Check:** Ensures only glyphs that are worth outputting are exported.

#### Usage

To use this script, follow these steps:

1. **Install Dependencies:**
   Make sure you have FontForge installed on your system. You can install it using the following command:
   ```sh
   sudo apt install python3-fontforge
   ```

2. **Run the Script:**
   Execute the script with the font file as an argument:
   ```sh
   python font_to_image.py <font_file>
   ```

   Replace `<font_file>` with the path to your font file.

### Example

```sh
python font_to_image_selected_glyphs.py /path/to/font.ttf
```

### Notes

- Both scripts skip exporting a glyph if the corresponding PNG file already exists in the output directory.
- Ensure the font file path provided is correct and the file is accessible.
- By default, the exported images are of size 101. You can uncomment and adjust the size parameter in the `export` method if a different image height is desired.

### Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
