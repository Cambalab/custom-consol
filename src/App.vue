<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
body {
  background-color: #8bc34a;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 60px 0;
}

.card {
  width: 90%;
  border-radius: 10px;
  background-color: #ffffffbf;
  margin: 0 auto;
}

.card__title {
  background-color: #0000000d;
}

input[type="text"]:focus {
  background-color: #8bc34a7d;
  padding: 0 10px;
}

.datatable__actions,
table.table thead {
  background-color: #0000000d;
}

table.table tbody tr:hover {
  background-color: #8bc34a7d;
}

.datatable thead th.column.sortable {
  outline: none;
}

.datatable thead tr th {
  font-weight: bolder;
}
</style>
