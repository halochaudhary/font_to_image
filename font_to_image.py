import os
import sys
import fontforge

def export_glyphs_to_png(font_path, output_dir="output_images"):
    # Check if the font file exists
    if not os.path.isfile(font_path):
        print(f"Error: Font file '{font_path}' not found.")
        sys.exit(1)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the font
    font = fontforge.open(font_path)

    # Export each glyph to PNG
    for glyph_name in font:
        current_glyph = font[glyph_name]
        if current_glyph.isWorthOutputting():
            output_path = os.path.join(output_dir, f"{glyph_name}.png")

            # Check if the file already exists before exporting
            if os.path.exists(output_path):
                print(f"Warning: File '{output_path}' already exists. Skipping.")
            else:
                current_glyph.export(output_path)

    print("Export completed successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <font_file>")
        sys.exit(1)

    font_file = sys.argv[1]
    export_glyphs_to_png(font_file)
