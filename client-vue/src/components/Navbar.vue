<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch } from "vue";
import { useRouter, useRoute } from "vue-router";
import { logout as apiLogout } from "@/api/auth/authAPI";
import { OhVueIcon, addIcons } from "oh-vue-icons";
import { CoPlus, CoHamburgerMenu } from "oh-vue-icons/icons";
import { createBookmark } from "@/api/bookmark/bookmarkAPI";
import CreateBookmarkModal from "@/components/modals/CreateBookmark.vue";
import Dropdown from "@/components/Dropdown.vue";

addIcons(CoPlus, CoHamburgerMenu);

const router = useRouter();
const route = useRoute();

const loggedIn = ref(!!localStorage.getItem("token"));

function handleStorage(e: StorageEvent) {
    if (e.key === "token") loggedIn.value = !!e.newValue;
}
onMounted(() => window.addEventListener("storage", handleStorage));
onUnmounted(() => window.removeEventListener("storage", handleStorage));

watch(
    () => route.fullPath,
    () => {
        loggedIn.value = !!localStorage.getItem("token");
    }
);

const goLogin = () => {
    router.push("/login");
};
const goSignup = () => {
    router.push("/signup");
};
const logout = () => {
    apiLogout();
    loggedIn.value = false;
    router.push("/");
};

const showCreateBookmark = ref(false);
function openCreateBookmarkModal() {
    showCreateBookmark.value = true;
}

async function onAddBookmark(payload: {
    name: string;
    link: string;
    description: string;
    tag_ids: number[];
    ws_ids: number[];
}) {
    try {
        const userId = Number(localStorage.getItem("userId"));
        if (!userId) throw new Error("No userId in localStorage");

        const newBookmark = await createBookmark({
            name: payload.name,
            link: payload.link,
            description: payload.description,
            user: userId,
            tag_ids: payload.tag_ids,
            ws_ids: payload.ws_ids,
        });

        console.log("Created bookmark:", newBookmark);
    } catch (err) {
        console.error("Failed to create bookmark:", err);
    } finally {
        showCreateBookmark.value = false;
    }
}

const navItems = [
    { to: "/", label: "Home" },
    { to: "/workspaces", label: "Workspaces" },
    { to: "/bookmarks", label: "Bookmarks" },
    { to: "/tags", label: "Tags" },
];
</script>

<template>
    <div class="navbar shadow-sm fixed top-0 z-10 w-full">
        <div class="navbar-start">
            <Dropdown :items="navItems" />
        </div>
        <div class="navbar-center hidden lg:flex">
            <ul class="menu menu-horizontal px-1">
                <li v-for="item in navItems" :key="item.to">
                    <router-link :to="item.to" class="btn btn-ghost text-xl">
                        {{ item.label }}
                    </router-link>
                </li>
            </ul>
        </div>
        <div class="navbar-end space-x-2">
            <button
                class="btn btn-sm btn-outline"
                @click="openCreateBookmarkModal"
                aria-label="Add Bookmark"
            >
                <oh-vue-icon name="co-plus" class="h-5 w-5" />
            </button>

            <button
                v-if="!loggedIn"
                @click="goLogin"
                class="btn btn-sm btn-outline"
            >
                Login
            </button>
            <button
                v-if="!loggedIn"
                @click="goSignup"
                class="btn btn-sm btn-primary"
            >
                Signup
            </button>
            <button
                v-if="loggedIn"
                @click="logout"
                class="btn btn-sm btn-outline"
            >
                Logout
            </button>
        </div>

        <CreateBookmarkModal
            :visible="showCreateBookmark"
            @update:visible="(val) => (showCreateBookmark = val)"
            @add="onAddBookmark"
        />
    </div>
</template>

<style scoped></style>
