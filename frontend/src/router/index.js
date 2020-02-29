import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Example from "../views/Example.vue";
import Tweetty from "../views/Tweetty.vue";
import TwettyEditor from "../views/TweettyEditor";
Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
     {
    path: "/example",
    name: "example",
    component: Example
  },
        {
    path: "/tweety/:slug",
    name: "tweety",
    component: Tweetty,
    props:true
  },
    {
    path: "/ask:slug?",
    name: "tweety-editor",
    component: TwettyEditor,
    props: true
    },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  ///base: process.env.BASE_URL,
  routes
});

export default router;
