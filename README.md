# OCR+OpenAi Identity document Extractor

This is a Python project that uses EasyOCR and OpenAI to extract specific information from an image and format it into a specific structure. It follows best practices such as error handling, dataclasses, and small, well-documented functions.

## Installation

Before you begin, ensure that you have the latest version of Python installed. We recommend Python 3.7 or later. You can verify your Python installation by using the following command:

```bash
python --version
```

To install the necessary libraries for this project, use pip, which is a package manager for Python.

Use the following commands to install the required libraries:

```bash
pip install openai
pip install easyocr
pip install rich
```

## Usage

After you have installed the necessary libraries, you can run the Python script with the following command:

```bash
python main.py
```

Before running the script, make sure to replace the `openai_key` in `main` function with your actual OpenAI key and `file_path` with the path to the image file you want to process.

The script reads an image, applies OCR to extract text data, formats the text data into a structure as defined by the `OCRResult` dataclass, and then prints this structured information.

## License

This project is licensed under the terms of the MIT license.

For any issues or suggestions related to this project, please open an issue on this GitHub repository. Contributions are always welcome.

## Acknowledgments

This project uses OpenAI and EasyOCR libraries to process images and extract textual information. We express our gratitude to the developers of these libraries.
