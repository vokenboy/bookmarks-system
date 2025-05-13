import "./assets/main.css";

import { createApp } from "vue";
import router from "./controllers/navigation";
import App from "./App.vue";
import Home from "./views/Home.vue";
import Login from "./views/Login.vue";
import Register from "./views/Register.vue";

const routes = [
    { path: "/", component: Home },
    { path: "/login", component: Login },
    { path: "/register", component: Register },
];

createApp(App).use(router).mount("#app");
