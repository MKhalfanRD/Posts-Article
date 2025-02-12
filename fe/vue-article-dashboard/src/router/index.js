import { createRouter, createWebHistory } from "vue-router";

import AllPosts from "../views/AllPosts.vue";
import AddPost from "../views/AddPost.vue";
import EditPost from "../views/EditPost.vue";
import Preview from "../views/Preview.vue";
import ArticleDetail from "../views/ArticleDetail.vue";

const routes = [
  { path: "/", component: AllPosts },
  { path: "/add", component: AddPost },
  { path: "/edit/:id", component: EditPost },
  { path: "/preview", component: Preview },
  { path: "/preview/:id", component: Preview },
  { path: "/article/:id", component: ArticleDetail },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
