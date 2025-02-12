<template>
    <table class="table">
      <thead>
        <tr>
          <th>Title</th>
          <th>Category</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="post in posts" :key="post.id">
          <td>{{ post.title }}</td>
          <td>{{ post.category }}</td>
          <td class="d-flex gap-2">
            <button class="btn btn-primary btn-sm" @click="$router.push(`/edit/${post.id}`)">✏️</button>
            <button class="btn btn-danger btn-sm" @click="moveToTrash(post.id)">🗑️</button>
          </td>
        </tr>
      </tbody>
    </table>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    props: ["posts"],
    methods: {
      async moveToTrash(id) {
        try {
          await axios.put(`http://127.0.0.1:5000/api/article/${id}`, { status: "Trash" });
          this.$emit("refresh"); 
        } catch (error) {
          console.error("Gagal memindahkan ke trash:", error);
        }
      }
    }
  };
  </script>
  