# Font to Image
## Export Glyphs to PNG

This repository contains a Python script that uses FontForge to export individual glyphs from a font file into PNG images. This can be useful for various purposes such as creating font previews, generating assets for graphic design, or simply inspecting individual glyphs in detail.

### Features

- **Check Font File Existence:** Ensures the specified font file exists before processing.
- **Automatic Output Directory Creation:** Creates an output directory if it doesn't already exist.
- **Glyph Export:** Exports each glyph in the font to a separate PNG file.
- **File Existence Check:** Skips exporting if the PNG file for a glyph already exists to prevent overwriting.

### Usage

To use this script, follow these steps:

1. **Install Dependencies:**
   Make sure you have FontForge installed on your system. You can install it using the following command:
   ```sh
   sudo apt install python3-fontforge
   ```

2. **Run the Script:**
   Execute the script with the font file as an argument:
   ```sh
   python script.py <font_file>
   ```

   Replace `<font_file>` with the path to your font file.

### Example

```sh
python script.py /path/to/font.ttf
```

This will create an `output_images` directory (if it doesn't exist) and export each glyph from `font.ttf` as a PNG image in that directory.

### Notes

- The script skips exporting a glyph if the corresponding PNG file already exists in the output directory.
- Ensure the font file path provided is correct and the file is accessible.

### Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
