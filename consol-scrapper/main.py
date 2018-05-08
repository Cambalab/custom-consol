import urllib2, datetime, sys, csv
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

categorias = ['almacen', 'bebidas', 'cooperativos', 'fiambreria', 'frescos', 'limpieza', 'organicos', 'sin-tacc', 'todos']
productos = {}
for categoria in categorias:
    for i in xrange(1, sys.maxint):
        try:
            req = urllib2.Request('http://www.tiendaconsol.coop/product-category/' + categoria + '/page/' + str(i))
            print 'Leyendo categoria: '+ categoria + ' pagina '+ str(i)
            response = urllib2.urlopen(req)
            the_page = response.read()
            soup = BeautifulSoup(the_page, "html.parser")
            for item_elem in soup.find_all('div','item-product'):
                productos[item_elem.find('h3').text] = [item_elem.find('span', 'price').text, 'http://www.tiendaconsol.coop'+item_elem.find('a', 'button add_to_cart_button product_type_simple')['href']]
        except urllib2.HTTPError, e:
            print 'Pagina no encontrada, pasando a siguiente categoria'
            break

with open('static/precios.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(('producto', 'precio', 'carrito'))
    for key, value in productos.items():
        wr.writerow([key, value[0], value[1]])
