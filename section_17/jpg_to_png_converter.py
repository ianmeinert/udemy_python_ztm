import sys
import os
from PIL import Image

# grab first and second argument
file_path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(file_path):
    clean_name = os.path.splitext(filename)[0]

    input = os.path.join(file_path, filename)
    output = os.path.join(directory, clean_name)

    img = Image.open(input)
    img.save(f'{output}.png', 'png')

print('all done!')
