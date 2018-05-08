<template>
  <v-card>
    <v-card-title>
      <div class="header">
        <img src="static/camba-logo.png">
        Productos Consol <span class="carita"><span class="manitos">ლ</span>(╹◡╹<span class="manitos">ლ</span>)</span>
      </div>
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        append-icon="search"
        label="Buscar productos por palabra"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      v-bind:items="products"
      :search="search"
      :rows-per-page-items="[20]"
    >
      <template slot="items" slot-scope="props">
        <td>{{ props.item.producto }}</td>
        <td class="text-xs-right">{{ props.item.precioHumanReadable }}</td>
        <td class="text-xs-right">
          <a :href='props.item.carrito' target="_blank"><v-icon color="orange darken-2">shopping_cart</v-icon></a>
        </td>
      </template>
      <v-alert slot="no-results" :value="true" color="error" icon="warning">
        La búsqueda "{{ search }}" no arrojó resultados.
      </v-alert>
    </v-data-table>
  </v-card>
</template>

<script>
import * as Papa from 'papaparse'

export default {
  created () {
    Papa.parse('static/precios.csv', {
      download: true,
      header: true,
      complete: (results) => {
        this.products = results.data.filter((elem) => {
          return elem.precio
        })
        this.products = this.products.map((elem) => {
          elem.precioHumanReadable = elem.precio
          elem.precio = parseFloat(elem.precio.substr(1).replace(',', '.'))
          return elem
        })
      }
    })
  },
  data () {
    return {
      search: '',
      headers: [
        {
          text: 'Producto',
          align: 'center',
          sortable: true,
          value: 'producto',
          width: '70%'
        },
        {
          text: 'Precio (AR$)',
          align: 'right',
          sortable: true,
          value: 'precio',
          width: '15%'
        },
        {
          text: 'Agregar al carrito',
          align: 'right',
          sortable: false,
          value: 'carrito',
          width: '15%'
        }
      ],
      products: []
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

                              /* v.._                       _..v
                               )\ '-.                 .-' /(
                               : \   :               :   / :
                                '.\   '.    ._.    .''  /.'
                                  :\    i.-'   '-.i    /:
                                   '\ .-'         '-. /'
_..eeaa.._                          :                :                          _..eeaa.._
i"T$P^T888aaa.._                   /   .-'\. ./'-.   \                    _..eee8887^T$P"i
'.     "T888888aa.               /   /  ()/ \()  \   \                .ee8888887"     .'
  '      '"T8888.88a            :    '._.' . '._.'    :             e88.88887"'      '
  i           "T8888a.          | .i'     / \     'i. |          .e8888P"           i
  :             "T8888a.        |  '.     '-'     .'  |        .e88867"             :
   i               T8888a.      :    i__..-=-..__i    :      .e8888P               i
  :                "T8888a.     '.   \/       \/   .'     .e8888P"                :
  :                  "88888a.     i-.           .-i     .e88888"                  :
  i                  "T88888a._./   '-..___..-'   \._.e88888P"                  i
  :                     "T88888P                   Y88888P"                     :
  :                       'T88"                     "88P'                       :
  i                    .__.:                         :.__.                    i
  :               _.--'   :                           :   '--._               :
  :         _.--'        |          C A M B A         |        '--._         :
  i___...--'             :            2018           :             '--...___i
                          :                         :
                          '.                       .'
                           '.                     .'
                             ''                 .' .
                              Y'-..         ..-'Y
                             :     '-.___.-'     :
                             |      .'87"'.      |
                             :     :  ^.   :     :
                              :   :   "^.   :   :        ._.
                              |   |    "^.  |   |        )&(
                              :   :      "'e:   :    .aP" ^
                               : :           : : "TP"
                               | |           | |
                               : :           : :
                              /   )         (   \          fsc
                           _.'   /           \   '._
                         .' _ . /             \     '.
                        (_i-i/_i               i_\i-i_)                                */

.header img {
  display: block;
  margin-bottom: 5px;
}
.header {
  position: relative;
  display: block;
}
.carita {
  font-weight: bolder;
}
.manitos {
  animation: MoveUpDown 1s linear infinite;
  position: relative;
  left: 0;
  bottom: 0;
}

@keyframes MoveUpDown {
  0%, 100% {
    bottom: 0;
  }
  50% {
    bottom: 5px;
  }
}

h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

</style>
