import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Login.vue";
import Signup from "../views/Signup.vue";
import Home from "../views/Home.vue";
import WorkspaceList from "@/views/WorkspaceList.vue";
import Workspace from "@/views/Workspace.vue";
import BookmarkList from "@/views/BookmarkList.vue";
import TagList from "@/views/TagList.vue";

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
        path: "/signup",
        name: "Signup",
        component: Signup,
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
        path: "/bookmarks",
        name: "Bookmarks",
        component: BookmarkList,
    },
    {
        path: "/tags",
        name: "Tags",
        component: TagList,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
