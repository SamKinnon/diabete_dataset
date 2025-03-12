import gdown

url = "https://drive.google.com/uc?id=1SAHIFphYPNgRYxe72AEL6q1yYQvFArZA"
output = "downloaded_file.pdf"
gdown.download(url, output, quiet=False)
print("File downloaded from Google Drive")

