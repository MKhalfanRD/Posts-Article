<template>
  <div class="app">
    <Sidebar />
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Sidebar from "./components/Sidebar.vue";
export default { components: { Sidebar } };
</script>

<style>
.app {
  display: flex;
}
.content {
  margin-left: 220px;
  padding: 20px;
  width: 100%;
}
</style>
