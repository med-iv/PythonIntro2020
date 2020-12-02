import sys, zipfile, io

stdinput = bytes.fromhex(sys.stdin.read())
zf = zipfile.ZipFile(io.BytesIO(stdinput), "r")

size_ar = 0
count = 0
for elem in zf.infolist():
    if not elem.is_dir():
        count += 1
        size_ar += elem.file_size
print(count, size_ar)