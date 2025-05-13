<script setup lang="ts">
import { ref } from "vue";
import { OhVueIcon, addIcons } from "oh-vue-icons";
import { CoPlus } from "oh-vue-icons/icons";
import CreateUrlModal from "@/components/modals/CreateUrl.vue";
import Dropdown from "@/components/Dropdown.vue";

addIcons(CoPlus);

const showCreateUrl = ref(false);
const openCreateUrlModal = () => {
    showCreateUrl.value = true;
};
const onAddUrl = (payload: {
    name: string;
    link: string;
    description: string;
    tags: string[];
}) => {
    console.log("New URL added:", payload);
};

const navItems = [
    { to: "/", label: "Home" },
    { to: "/workspaces", label: "Workspaces" },
    { to: "/urls", label: "URLS" },
];
</script>

<template>
    <div>
        <div class="navbar shadow-sm fixed top-0 z-10 w-full">
            <div class="navbar-start">
                <Dropdown :items="navItems" />
            </div>
            <div class="navbar-center hidden lg:flex">
                <ul class="menu menu-horizontal px-1">
                    <li v-for="item in navItems" :key="item.to">
                        <router-link
                            :to="item.to"
                            class="btn btn-ghost text-xl"
                            >{{ item.label }}</router-link
                        >
                    </li>
                </ul>
            </div>
            <div class="navbar-end space-x-2">
                <button
                    class="btn btn-sm btn-outline"
                    @click="openCreateUrlModal"
                    aria-label="Add URL"
                >
                    <oh-vue-icon name="co-plus" class="h-5 w-5" />
                </button>
                <router-link to="/login" class="btn btn-sm btn-outline"
                    >Login</router-link
                >
                <router-link to="/register" class="btn btn-sm btn-primary"
                    >Register</router-link
                >
            </div>
        </div>
        <CreateUrlModal
            :visible="showCreateUrl"
            @update:visible="showCreateUrl = $event"
            @add="onAddUrl"
        />
    </div>
</template>

<style scoped></style>
