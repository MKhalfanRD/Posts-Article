<template>
    <div class="container mt-4">
      <h2>Edit Post</h2>
      <PostForm :postId="$route.params.id" />
    </div>
  </template>
  
  <script>
  import PostForm from "../components/PostForm.vue";
  
  export default {
    components: { PostForm }
  };
  </script>
  