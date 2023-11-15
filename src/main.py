import os

# Mendapatkan path dari direktori saat ini
current_directory = os.getcwd()
# Path dari direktori parent untuk file atau direktori tertentu
file_path = os.path.join(current_directory,'src', 'example.html')

with open(file_path, 'r') as file:
    # Membaca seluruh konten file
    html_content = file.read()

# Sekarang, variabel html_content berisi seluruh string dari file HTML
splittedcontent = html_content.split()
result_string = "".join(splittedcontent)

print(result_string)