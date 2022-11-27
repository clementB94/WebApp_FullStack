<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <h1>Web App movies reviews</h1>

    <div class="wrapper">

      <nav>
        <RouterLink to="/">Accueil</RouterLink>
        <RouterLink to="/list">250 films les mieux notés</RouterLink>
        <RouterLink to="/scraping">Scraper un film</RouterLink>
      
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  width: 100%;
}

nav a {
  display: inline-block;
  padding: 0 10px;
  border-left: 1px solid var(--color-border);
}

.wrapper {
  padding-bottom: 30px;
}
</style>
