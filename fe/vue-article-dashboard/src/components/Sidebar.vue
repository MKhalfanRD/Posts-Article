<template>
    <div class="sidebar">
      <router-link to="/">📋 All Posts</router-link>
      <router-link to="/add">📝 Add New</router-link>
      <router-link to="/preview">👀 Preview</router-link>
    </div>
  </template>
  
  <style scoped>
  .sidebar {
    width: 200px;
    height: 100vh;
    position: fixed;
    left: 0;
    top: 0;
    background: #2c3e50;
    padding: 20px;
    color: white;
    display: flex;
    flex-direction: column;
  }
  .sidebar a {
    color: white;
    text-decoration: none;
    margin: 10px 0;
  }
  .sidebar a:hover {
    text-decoration: underline;
  }
  </style>
  