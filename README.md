# EncodeAnythingToImage

EncodeAnythingToImage is a Python project that allows you to encode any file by converting its binary data into RGB values and storing it in an image. This repository contains two scripts: `encoder.py` and `decoder.py`. The `encoder.py` script encodes a file into an image, and the `decoder.py` script decodes the image back into the original file.

## Features

- Encode any file into an image.
- Decode the image back into the original file.
- Simple and easy-to-use command-line interface.

## How It Works

### Encoding

The `encoder.py` script reads the binary data of the input file, converts this data into RGB values, and writes these values to an image file. 

### Decoding

The `decoder.py` script reads the RGB values from the encoded image and converts these values back into binary data to reconstruct the original file.

## Usage

### Encoding a File

To encode a file into an image, run the following command:

```bash
python3 src/encoder.py /path/to/sourceFile /path/to/encodedImage.png
```

### Decoding a File

To encode a encoded image into the original file, run the following command:

```bash
python3 src/decoder.py /path/to/encoded_song.png /path/to/decoded_song.mp3
```

## Example

Here is an example of how to use the scripts. We will encode this gif:

![spiderman-pizza-time](https://github.com/user-attachments/assets/9750585e-58e7-47ff-858c-f3c9b527c3fd)

1) Encode an GIF file into an image:

```bash
python3 src/decoder.py spiderman-pizza-time.gif EncodedImage.png
```

The Resulted Image:

![EncodedImage](https://github.com/user-attachments/assets/f43f3552-27a2-464c-88c2-f7699b917eca)

2) Decode the image into the actual file:
   
```bash
python3 src/decoder.py EncodedImage.png MysteriousFile
```

The Resulted File:

![MysteriousFile](https://github.com/user-attachments/assets/49206741-89ae-4754-886a-e1c9f72a55e4)

## License
This project is licensed under the MIT License . See the [LICENSE](LICENSE) file for details.

##

Ali Berk Karaarslan
##

2024
