<template>
  <form @submit.prevent="savePost">
    <div class="mb-3">
      <label>Title</label>
      <input v-model="post.title" class="form-control" required />
    </div>
    <div class="mb-3">
      <label>Content</label>
      <textarea v-model="post.content" class="form-control" required></textarea>
    </div>
    <div class="mb-3">
      <label>Category</label>
      <input v-model="post.category" class="form-control" required />
    </div>
    <div class="button d-flex gap-2">
      <button class="btn btn-success" type="submit">Publish</button>
      <button class="btn btn-secondary" type="button" @click="saveAsDraft">Draft</button>
    </div>
  </form>
</template>

<script>
import axios from "axios";

export default {
  props: ["postId"], 
  data() {
    return { 
      post: { title: "", content: "", category: "", status: "Publish" }
    };
  },
  methods: {
    async fetchPost() {
      if (this.postId) {
        try {
          const res = await axios.get(`http://127.0.0.1:5000/api/article/${this.postId}`);
          this.post = res.data; 
        } catch (error) {
          console.error("Gagal mengambil data artikel:", error);
        }
      }
    },
    async savePost() {
      try {
        this.post.status = "Publish";
        if (this.postId) {
          await axios.put(`http://127.0.0.1:5000/api/article/${this.postId}`, this.post);
          alert("Article updated successfully!");
        } else {
          await axios.post("http://127.0.0.1:5000/api/article", this.post);
          alert("Article added successfully!");
        }
        this.$router.push("/"); 
      } catch (error) {
        console.error("Gagal menyimpan artikel:", error);
      }
    },
    async saveAsDraft() {
      try {
        this.post.status = "Draft"; 
        if (this.postId) {
          await axios.put(`http://127.0.0.1:5000/api/article/${this.postId}`, this.post);
          alert("Article saved as draft!");
        } else {
          await axios.post("http://127.0.0.1:5000/api/article", this.post);
          alert("Article added as draft!");
        }
        this.$router.push("/");
      } catch (error) {
        console.error("Gagal menyimpan sebagai draft:", error);
      }
    }
  },
  mounted() {
    this.fetchPost();
  }
};
</script>
