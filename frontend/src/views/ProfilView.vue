<script setup>
// import TheWelcome from '../components/TheWelcome.vue'
import MovieCard from '../components/MovieCard.vue'
import Comment from '../components/Comment.vue';
import axios from 'axios'
import {ref, watchEffect} from 'vue'
const props = defineProps(['id'])
const user = ref(null)
const ratings = ref(null)

const comments = ref(null)
console.log(props)

// Get user info
watchEffect(async () => {
    user.value = await axios.get("/users/"+props.id).then(v => v.data)
    console.log(user.value)
    // movie.value = await get_movie(props.id)
})

// Get user rating
watchEffect(async () => {
    ratings.value = await axios.get("/ratings/user/", {
      params: {
        username: props.id,
      }
    }).then(v => v.data)
})

// Get user comments
watchEffect(async () => { 
    comments.value = await axios.get("/comments/user/", {
      params: {
        username: props.id
      }
    }).then(v => v.data)
})


</script>

<template>
  <main>
    <h2>Profil de l'utilisateur : {{props.id}}</h2>
    <div v-if="user">
        <p> User : {{user.username}} </p>
        <div class="category">
            <h3>Evaluations :</h3>
            <tr>
                <div v-for="rating in ratings">
                    Film : <a :href="'/movie/'+rating.movie_id">{{rating.movie_id}}</a> Note : {{rating.rating}}
                </div>
            </tr>
        </div>
        <div class="category">
            <h3>Commentaires :</h3>
            <tr>
                <Comment v-for="comment in comments" :comment=comment :with_movie=true></Comment>
            </tr>
        </div>
        
        
    </div>
    <div v-else>...</div>

  
  </main>
</template>

<style scoped>
.category {
    padding-top: 20px;
}
</style>
