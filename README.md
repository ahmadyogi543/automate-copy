# Automate Copy - Python

## Pendahuluan

**Automate Copy** adalah sebuah program sederhana yang digunakan untuk menyalin beberapa folder yang sudah didaftarkan pada file `config.txt` dari folder sumber (folder yang berisikan nama-nama folder pada list) ke folder tujuan!

## Cara Penggunaan

Untuk menggunakan program ini, tinggal mengetikkan _path_ folder sumber `src_path`, _path_ folder tujuan `dst_path` dan nama-nama folder yang berada dalam folder sumber yang ingin disalin, dipisah dengan tanda koma ",".

## Format config.txt

Format _config.txt_ **jangan pernah diubah**, hanya ubah yang memang perlu diubah saja!

```python
[setup]
src_path=PATH_ABSOLUTE_FOLDER_SUMBER
dst_path=PATH_ABSOLUTE_FOLDER_TUJUAN
folder_list=folder1,folder2,folder3....
```
