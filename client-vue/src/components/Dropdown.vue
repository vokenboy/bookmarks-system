<script setup lang="ts">
import { defineProps } from "vue";
import { OhVueIcon } from "oh-vue-icons";

interface NavItem {
    to: string;
    label: string;
}

const props = defineProps<{
    items: NavItem[];
}>();
</script>

<template>
    <div class="dropdown lg:hidden">
        <label tabindex="0" class="btn btn-ghost">
            <OhVueIcon name="co-hamburger-menu" scale="1.8" />
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
