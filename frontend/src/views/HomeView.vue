<script setup>
// import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
  <section>
    <p>Bienvenue sur le site de notation/avis sur des films.</p>
  
    <p>Réalisé dans le cadre du projet full stack data</p>
    <div v-if="isLoggedIn" id="logout">
      <!-- <p id="logout">Click <a href="/dashboard">here</a> to view all notes.</p> -->
      <p>Logged in</p>
    </div>
    <p v-else>
      <span><a href="/register">Register</a></span>
      <span> or </span>
      <span><a href="/login">Log In</a></span>
    </p>
  </section>
</template>
<script>
// export default {
//   name: 'Home',
//   computed : {
//     isLoggedIn: function() {
//       return this.$store.getters.isAuthenticated;
//     }
//   },
// }
</script>
