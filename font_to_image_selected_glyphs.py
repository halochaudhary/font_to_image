import os
import sys
import fontforge

def export_selected_glyphs_to_png(font_path, output_dir="output_images"):
    # Check if the font file exists
    if not os.path.isfile(font_path):
        print(f"Error: Font file '{font_path}' not found.")
        sys.exit(1)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the font
    font = fontforge.open(font_path)

    # Define the range of glyphs to export (0-9, A-Z)
    selected_glyphs = [str(i) for i in range(10)] + [chr(i) for i in range(ord('A'), ord('Z')+1)]

    # Export selected glyphs to PNG
    for glyph_name in selected_glyphs:
        if glyph_name.isdigit():
            current_glyph = font.createMappedChar(glyph_name)
        else:
            current_glyph = font[glyph_name]

        if current_glyph.isWorthOutputting():
            output_path = os.path.join(output_dir, f"{glyph_name}.png")

            # Check if the file already exists before exporting
            if os.path.exists(output_path):
                print(f"Warning: File '{output_path}' already exists. Skipping.")
            else:
                #current_glyph.export(output_path, 800) # 800 for height of image
                current_glyph.export(output_path) # Default size 101 of exported image
        else:
            print(f"Warning: Glyph '{glyph_name}' is not worth outputting. Skipping.")

    print("Export completed successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <font_file>")
        sys.exit(1)

    font_file = sys.argv[1]
    export_selected_glyphs_to_png(font_file)
