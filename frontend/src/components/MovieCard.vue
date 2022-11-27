<script setup>
defineProps({
  movie: {
    required: false
  }
})
</script>

<template>
    <tr>
        <th>Id : <a :href="'/movie/'+movie.id">{{movie.id}}</a></th>
        <th>Titre : <a :href="'/movie/'+movie.id">{{movie.title}}</a> </th>
        <th>Note IMDB : {{movie.rating}}     </th>
        <th>Date : {{movie.year}}     </th>
        <th>Casting : {{movie.star_cast}}</th>
    </tr>
</template>

<style scoped>
tr {
  width: 100%;
  padding-top: 20px;
}
th {
  text-align:left;
  padding-left: 20px;
  }
  
</style>
