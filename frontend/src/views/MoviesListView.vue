<script setup>
import MovieCard from '../components/MovieCard.vue'
import axios from 'axios'
import {ref, watchEffect} from 'vue'

const movies = ref(null)
const text = ref("")

watchEffect(async () => {
    movies.value = await axios.get("/movies/", {
      params: {
        skip: 0,
        limit:50
      }
    }).then(v => v.data)
  })

console.log(movies)

</script>

<template>
  <main>
    <h2>Tous les films</h2>
    <p>Recherchez l'id d'un film : </p>
    <input v-model="text">
    <!-- <button @click="click">TEST</button> -->
    <a :href="'/movie/'+text" tag="button">Recherche</a>
    
    <tr>
        <MovieCard v-for="movie in movies" :movie=movie></MovieCard>
    </tr>
    
  </main>
</template>
