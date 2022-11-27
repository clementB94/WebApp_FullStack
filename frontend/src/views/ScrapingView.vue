<script setup>
    import axios from 'axios'
    import {ref, watchEffect} from 'vue'
    import MovieCard from '../components/MovieCard.vue'
    // import MovieView from './views/M.vue'

    const link_imdb = ref(null)
    const scraped_movie = ref(null)

    async function scrap_movie() {
        scraped_movie.value = await axios.post("/movies/scrape/?url_imdb="+link_imdb.value).then(v => v.data)
    }
</script>

<template>
    <main>
        <h2>Scraper un film à partir d'un lien IMDb</h2>
        <input v-model="link_imdb">
        <button @click="scrap_movie">Scraper</button>
        <MovieCard v-if="scraped_movie" :movie="scraped_movie"></MovieCard>
        
        
    </main>
</template>