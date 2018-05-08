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
      :items="products"
      :search="search"
    >
      <template slot="items" slot-scope="props">
        <td>{{ props.item.name }}</td>
        <td class="text-xs-right">$ {{ props.item.price }}</td>
      </template>
      <v-alert slot="no-results" :value="true" color="error" icon="warning">
        La búsqueda "{{ search }}" no arrojó resultados.
      </v-alert>
    </v-data-table>
  </v-card>
</template>

<script>
export default {
  data () {
    return {
      search: '',
      headers: [
        {
          text: 'Producto',
          align: 'left',
          sortable: true,
          value: 'name'
        },
        {
          text: 'Precio (AR$)',
          align: 'left',
          sortable: true,
          value: 'price'
        }
      ],
      products: [
        {
          value: false,
          name: 'Frozen Yogurt',
          price: 159
        },
        {
          value: false,
          name: 'Ice cream sandwich',
          price: 237
        },
        {
          value: false,
          name: 'Eclair',
          price: 262
        },
        {
          value: false,
          name: 'Cupcake',
          price: 305
        },
        {
          value: false,
          name: 'Gingerbread',
          price: 356
        },
        {
          value: false,
          name: 'Jelly bean',
          price: 375
        },
        {
          value: false,
          name: 'Lollipop',
          price: 392
        },
        {
          value: false,
          name: 'Honeycomb',
          price: 408
        },
        {
          value: false,
          name: 'Donut',
          price: 452
        },
        {
          value: false,
          name: 'KitKat',
          price: 518
        }
      ]
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
