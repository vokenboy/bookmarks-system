<script setup lang="ts">
import { defineProps } from "vue";

interface NavItem {
    to: string;
    label: string;
}

const props = defineProps<{ items: NavItem[] }>();
</script>

<template>
    <div class="dropdown lg:hidden">
        <label tabindex="0" class="btn btn-ghost">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
            >
                <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M4 6h16M4 12h16M4 18h16"
                />
            </svg>
        </label>
        <ul
            tabindex="0"
            class="menu menu-sm dropdown-content bg-base-100 rounded-box mt-3 w-40 p-2 shadow"
        >
            <li v-for="item in props.items" :key="item.to">
                <router-link :to="item.to">{{ item.label }}</router-link>
            </li>
        </ul>
    </div>
</template>

<style scoped></style>
