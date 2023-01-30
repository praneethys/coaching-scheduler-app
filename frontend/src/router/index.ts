import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CoachView from "../views/CoachView.vue";
import StudentView from "../views/StudentView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/coach/:coachId",
    name: "coach",
    component: CoachView,
    props: true,
  },
  {
    path: "/student/:studentId",
    name: "student",
    component: StudentView,
    props: true,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

router.beforeEach((routeTo, routeFrom) => {
  console.log(`Navigating "${routeFrom.path}" -> "${routeTo.path}"`);
});

export default router;
