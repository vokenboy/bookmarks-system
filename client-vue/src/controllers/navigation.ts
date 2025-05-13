import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Home from "../views/Home.vue";
import WorkspaceList from "@/views/WorkspaceList.vue";
import Workspace from "@/views/Workspace.vue";
import UrlList from "@/views/UrlList.vue";

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/login",
        name: "Login",
        component: Login,
    },
    {
        path: "/register",
        name: "Register",
        component: Register,
    },
    {
        path: "/workspaces",
        name: "Workspaces",
        component: WorkspaceList,
    },
    {
        path: "/workspaces/:workspaceId",
        name: "Workspace",
        component: Workspace,
    },
    {
        path: "/urls",
        name: "Url",
        component: UrlList,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
