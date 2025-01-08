
## Folder Size Tool

Easily measure the sizes of files and folders within a specified directory. This tool provides a structured overview of your directory structure and their respective sizes.


## Features

- Measures the size of directories and subdirectories up to a specified depth.
- Supports size outputs in MB, GB, or other units.
- Provides a clear, tree-structured output for easy navigation.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/folder-size-tool.git
   ```

2. Navigate to the project folder:
   ```bash
   cd folder-size-tool
   ```

3. Ensure Python is installed (Python 3.6 or higher recommended).


## Usage

Run the script with the following command:

```bash
python get_size.py --path <directory_path> --level <depth> --size_type <unit>
```

### Parameters:
- `--path`: The target directory to analyze (e.g., `/home/user/code`).
- `--level`: Depth of the folder hierarchy to scan (e.g., `3`).
- `--size_type`: Unit of size measurement (e.g., `MB`, `GB`).

### Example:

```bash
python get_size.py --path /home/kurnianto/code --level 3 --size_type MB
```


## Output Example

```plaintext
|- code/ (116.83 GB)
   |- folder-size-tool/ (0.00 GB)
      |- .git/ (0.00 GB)
   |- pia-video-classification/ (18.69 GB)
      |- not_used/ (0.02 GB)
      |- finetuned_model/ (2.34 GB)
      |- datas/ (14.05 GB)
      |- preprocess/ (0.00 GB)
      |- Side4Video/ (1.95 GB)
      |- .git/ (0.04 GB)
      |- newmodel_research/ (0.28 GB)
   |- old_code/ (44.66 GB)
      |- MUSE/ (5.38 GB)
      |- v2vgan/ (24.69 GB)
      |- CGDETR_FULL/ (4.46 GB)
      |- CM2_DVC/ (8.69 GB)
   |- videos/ (0.26 GB)
   |- CLIP4Clip/ (23.18 GB)
   |- dataset/ (26.02 GB)
```

## Contributing

Contributions are welcome! If you have ideas for improvements, feel free to fork the repository and submit a pull request.

