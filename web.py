import re
import csv

with open('kemik.html', 'r', encoding='utf-8') as file:
    html_content = file.read()


product_name_pattern = re.compile(r'alt="([^"]+)"')  
image_url_pattern = re.compile(r'<img[^>]+src="([^"]+)"')


product_names = product_name_pattern.findall(html_content)
image_urls = image_url_pattern.findall(html_content)


processed_image_urls = [url.split('Compra en línea fácil_files/')[-1] for url in image_urls]


if len(product_names) != len(processed_image_urls):
    print("La cantidad de nombres de productos y URLs de imágenes no coincide.")


with open('productos_limpios.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['URL de la Imagen', 'Nombre del Producto'])
    for name, url in zip(product_names, processed_image_urls):
        writer.writerow([url, name])

print("Datos exportados a 'productos_limpios.csv'.")
