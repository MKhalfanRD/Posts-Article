<template>
    <div class="container mt-4">
      <h2>All Posts</h2>
      <div class="button d-flex gap-2">
          <button class="btn btn-primary my-3" @click="$router.push('/add')">Add New</button>
          <button class="btn btn-info my-3" @click="$router.push('/preview')">Preview</button>
      </div>
      <ul class="nav nav-tabs">
        <li class="nav-item">
          <button class="nav-link" :class="{ active: activeTab === 'Publish' }" @click="activeTab = 'Publish'">Published</button>
        </li>
        <li class="nav-item">
          <button class="nav-link" :class="{ active: activeTab === 'Draft' }" @click="activeTab = 'Draft'">Drafts</button>
        </li>
        <li class="nav-item">
          <button class="nav-link" :class="{ active: activeTab === 'Trash' }" @click="activeTab = 'Trash'">Trashed</button>
        </li>
      </ul>
      <PostList :posts="filteredPosts" @refresh="fetchPosts" />
    </div>
  </template>
  
  <script>
  import PostList from "../components/PostList.vue";
  import axios from "axios";
  
  export default {
    components: { PostList },
    data() {
      return {
        activeTab: "Publish", 
        posts: []
      };
    },
    computed: {
      filteredPosts() {
        return this.posts.filter(post => post.status === this.activeTab);
      }
    },
    methods: {
      async fetchPosts() {
        try {
          const res = await axios.get("http://127.0.0.1:5000/api/article");
          this.posts = res.data; 
        } catch (error) {
          console.error("Gagal mengambil data:", error);
        }
      }
    },
    mounted() {
      this.fetchPosts();
    }
  };
  </script>
  