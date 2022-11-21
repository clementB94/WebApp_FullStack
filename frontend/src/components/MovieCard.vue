<script setup>
defineProps({
  movie: {
    required: false
  }
})
</script>

<template>
    <div>
        Rank : {{movie.rank}}    
        Title : {{movie.movie_title}}    
        Grade : {{movie.rating}}     
        Date : {{movie.year}}     
        Casting : {{movie.star_cast}}
    </div>
</template>

<style scoped>
</style>
