<script setup>
defineProps({
  comment: {
    required: false
  }
})
</script>

<template>
    <div>
        Id : {{comment.id}}    
        Auteur : {{comment.user_id}}    
        Commentaire : {{comment.comment}}    
    </div>
</template>

<style scoped>
</style>
