import os
import sys
import subprocess
import shutil

def extract_webp_frames(webp_path: str):
    """
    Extracts all frames from an animated WebP file into a directory
    named after the file.
    
    Args:
        webp_path (str): The full path to the animated WebP file.
    """
    # 1. Check if the anim_dump command is available
    if not shutil.which("anim_dump"):
        print("Error: 'anim_dump' command not found.")
        print("Please install the 'webp' or 'libwebp-tools' package.")
        print("  - On Debian/Ubuntu: sudo apt-get install webp")
        print("  - On macOS (Homebrew): brew install webp")
        print("  - On Fedora/CentOS: sudo dnf install libwebp-tools")
        sys.exit(1)

    # 2. Validate input file path
    if not os.path.isfile(webp_path):
        print(f"Error: File not found at '{webp_path}'")
        sys.exit(1)

    # 3. Create the output directory
    dir_path = os.path.dirname(os.path.abspath(webp_path))
    filename = os.path.basename(webp_path)
    output_dir_name = os.path.splitext(filename)[0]
    full_output_path = os.path.join(dir_path, output_dir_name)

    print(f"Creating output directory at: {full_output_path}")
    os.makedirs(full_output_path, exist_ok=True)

    # 4. Construct and run the command
    command = ["anim_dump", "-folder", full_output_path, webp_path]
    
    print(f"Extracting frames from '{filename}'...")
    try:
        process = subprocess.run(
            command, 
            check=True, 
            capture_output=True, 
            text=True
        )
        if process.stdout:
            print(process.stdout)
        if process.stderr:
            print("Errors:", process.stderr)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred during extraction for {filename}:")
        print(e.stderr)
        sys.exit(1)
    except FileNotFoundError:
         print(f"Error: Could not find the '{command[0]}' executable.")
         sys.exit(1)


    print("✅ Extraction complete!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_webp_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    extract_webp_frames(input_file)
