<script setup>
defineProps({
  comment: {
    required: false
  },
  with_author: {
    required: false
  },
  with_movie: {
    required: false
  }
})
</script>

<template>
    <div>
        Id : {{comment.id}}    
        <!-- Auteur : <a :href="'/profil/'+comment.username">{{comment.username}}</a> -->
        <p v-if="with_author">Auteur : <a :href="'/users/'+comment.username">{{comment.username}}</a></p>
        <p v-if="with_movie">Film : <a :href="'/movie/'+comment.movie_id">{{comment.movie_id}}</a></p>
        Commentaire : {{comment.comment}}    
    </div>
</template>

<style scoped>
</style>
