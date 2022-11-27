<script setup>
defineProps({
  movie: {
    required: false
  }
})
</script>

<template>
    <div>
        Id : {{movie.id}}    
        Titre : <a :href="'/movie/'+movie.id">{{movie.title}}</a>
        Note IMDB : {{movie.rating}}     
        Date : {{movie.year}}     
        Casting : {{movie.star_cast}}
    </div>
</template>

<style scoped>
</style>
