def analyze_braw_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()

    # Check if the file starts with the 'braw' marker
    if data.startswith(b'\x62\x72\x61\x77'):
        # Extract picture length, columns, rows, width, height, slice height, and slice widths
        picture_length = int.from_bytes(data[4:8], byteorder='big')
        columns = int.from_bytes(data[12:14], byteorder='big')
        rows = int.from_bytes(data[14:16], byteorder='big')
        width = int.from_bytes(data[16:18], byteorder='big')
        height = int.from_bytes(data[18:20], byteorder='big')
        slice_height = int.from_bytes(data[22:24], byteorder='big')
        slice_widths = [int.from_bytes(data[i:i+2], byteorder='big') for i in range(28, 60, 2)]

        # Calculate the total number of slices and verify the offset of the 7th slice
        num_slices = columns * rows
        seventh_slice_offset = int.from_bytes(data[72:76], byteorder='big')

        # Print extracted information
        print(f"Picture length: {picture_length}")
        print(f"Columns: {columns}, Rows: {rows}")
        print(f"Picture width: {width}, Picture height: {height}")
        print(f"Slice height: {slice_height}")
        print(f"Slice widths: {slice_widths}")
        print(f"Total number of slices: {num_slices}")
        print(f"Offset of 7th slice: {seventh_slice_offset}")
    else:
        print("Invalid Blackmagic RAW file.")

def main():
    file_path = input("Enter the path to the Blackmagic RAW file: ")
    analyze_braw_file(file_path)

if __name__ == "__main__":
    main()
