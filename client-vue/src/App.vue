<script setup lang="ts">
import Navbar from "./components/Navbar.vue";
</script>

<template>
    <Navbar />
    <div class="navbar-spacer"></div>
    <RouterView />
</template>

<style scoped>
.navbar-spacer {
    height: 64px;
}
</style>
