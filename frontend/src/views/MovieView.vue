<script setup>
// import TheWelcome from '../components/TheWelcome.vue'
import MovieCard from '../components/MovieCard.vue'
import Comment from '../components/Comment.vue';
import axios from 'axios'
import {ref, watchEffect} from 'vue'
const props = defineProps(['id'])
const movie = ref(null)
const new_rating = ref(null)
const rating = ref(null)

const comments = ref(null)
const new_comment = ref(null)
console.log(props)
const user = "admin" // TEMPORAIRE

// Get movie info
watchEffect(async () => {
    movie.value = await axios.get("/movies/"+props.id).then(v => v.data)
    console.log(movie.value)
    // movie.value = await get_movie(props.id)
})



// Get movie rating
watchEffect(async () => {
    rating.value = await axios.get("/ratings/rating/", {
      params: {
        username: user,
        movie_id: props.id
      }
    }).then(v => v.data)
    console.log("rating:")
    console.log(rating)
})

// Get movie comments
watchEffect(async () => {
    comments.value = await axios.get("/comments/movie/", {
      params: {
        movie_id: props.id
      }
    }).then(v => v.data)
})

async function add_rating() {
  rating.value = await axios.post("/ratings/", {
    movie_id:movie.value.id,
    username:user,
    rating:parseInt(new_rating.value)
  }).then(v => v.data)
}

async function add_comment() {
  console.log(comments.value)
  comments.value.push(await axios.post("/comments/", {
    movie_id:movie.value.id,
    username:user,
    comment:new_comment.value
  }).then(v => v.data))
}


</script>

<template>
  <main>
    <h2>Information sur un film : {{props.id}}</h2>
    <MovieCard v-if="movie" :movie=movie></MovieCard>
    <p v-else>...</p>
    <!-- Rating -->
    <div>
      <p v-if="rating">Votre note : {{ rating.rating }}</p>
      <p v-else>Votre note : Pas d'évaluation</p>
      <input v-model="new_rating" placeholder="Entrez une note pour ce film" type="numeric">
      <button @click="add_rating">Ajouter rating</button>
      <!-- Movie ratings -->
    </div>
    <!-- Comment -->
    <div>
      <textarea v-model="new_comment" placeholder="Entrez un commentaire"></textarea>
      <button @click="add_comment">Ajouter commentaire</button>
      <!-- Comments -->
      <div v-if="comments">
          <Comment v-for="comment in comments" :comment=comment :with_author=true></Comment>
      </div>
    </div>
  
  </main>
</template>
