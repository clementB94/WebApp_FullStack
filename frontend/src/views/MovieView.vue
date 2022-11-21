<script setup>
// import TheWelcome from '../components/TheWelcome.vue'
import MovieCard from '../components/MovieCard.vue';
import axios from 'axios'
import {ref, watchEffect} from 'vue'
const props = defineProps(['id'])
const movie = ref(null)
console.log(props)

watchEffect(async () => {
    movie.value = await axios.get("/movies/"+props.id).then(v => v.data)
})
</script>

<template>
  <main>
    <p>Information sur un film : {{props.id}}</p>
    <MovieCard :movie=movie></MovieCard>
  
  </main>
</template>
