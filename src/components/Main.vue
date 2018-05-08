<template>
  <v-card>
    <v-card-title>
      Productos Consol ლ(╹◡╹ლ)
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
        <td class="text-xs-right">{{ props.item.precio }}</td>
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
          return elem.producto
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
          align: 'left',
          sortable: true,
          value: 'producto'
        },
        {
          text: 'Precio (AR$)',
          align: 'left',
          sortable: true,
          value: 'precio'
        },
        {
          text: 'Agregar al carrito',
          align: 'left',
          sortable: false,
          value: 'carrito'
        }
      ],
      products: []
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
