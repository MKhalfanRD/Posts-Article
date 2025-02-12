<template>
  <div class="container mt-4">
    <h2>{{ post.title }}</h2>
    <p><strong>Category:</strong> {{ post.category }}</p>
    <p>{{ post.content }}</p>

    <!-- Tombol Kembali -->
    <button class="btn btn-primary mt-3" @click="$router.go(-1)">Kembali</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return { post: {} };
  },
  async mounted() {
    try {
      const res = await axios.get(`http://127.0.0.1:5000/api/article/${this.$route.params.id}`);
      this.post = res.data;
    } catch (error) {
      console.error("Gagal mengambil data artikel:", error);
    }
  }
};
</script>
