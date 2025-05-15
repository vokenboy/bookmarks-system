<script setup lang="ts">
import { defineProps, defineEmits } from "vue";
import { type Tag } from "@/assets/types/tag";

defineProps<{
    tag: Tag;
}>();
</script>

<template>
    <span class="badge badge-outline cursor-pointer">
        {{ tag.name }}
    </span>
</template>

<style scoped></style>
