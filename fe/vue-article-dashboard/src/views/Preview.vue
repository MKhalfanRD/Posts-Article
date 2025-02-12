<template>
  <div class="container mt-4">
    <h2>Preview</h2>

    <div v-for="post in paginatedPosts" :key="post.id" class="card my-3">
      <div class="card-body">
        <h3 @click="$router.push(`/article/${post.id}`)" style="cursor: pointer; color: blue;">
          {{ post.title }}
        </h3>
        <p><strong>Category:</strong> {{ post.category }}</p>
        <p>{{ post.content.substring(0, 100) }}...</p>
      </div>
    </div>

    <div class="pagination">
      <button @click="prevPage" :disabled="currentPage === 1">Prev</button>
      <span>Page {{ currentPage }} of {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage >= totalPages">Next</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      posts: [],
      currentPage: 1,
      itemsPerPage: 5, 
    };
  },
  computed: {
    paginatedPosts() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      return this.posts.slice(start, start + this.itemsPerPage);
    },
    totalPages() {
      return Math.ceil(this.posts.length / this.itemsPerPage);
    }
  },
  async mounted() {
    const res = await axios.get("http://127.0.0.1:5000/api/article");
    this.posts = res.data.filter(post => post.status === "Publish");
  },
  methods: {
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    }
  }
};
</script>

<style>
.pagination {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
.pagination button {
  margin: 0 10px;
  padding: 5px 10px;
  border: none;
  background-color: blue;
  color: white;
  cursor: pointer;
}
.pagination button:disabled {
  background-color: gray;
  cursor: not-allowed;
}
</style>
