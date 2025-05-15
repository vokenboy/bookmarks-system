<script setup lang="ts">
import { ref, onMounted } from "vue";
import TagCard from "@/components/TagCard.vue";
import CreateTag from "@/components/modals/CreateTag.vue";
import { getTags, createTag } from "@/api/tag/tagAPI";
import type { Tag } from "@/assets/types/tag";

const tags = ref<Tag[]>([]);
const isOpen = ref(false);

const fetchTags = async () => {
    try {
        const userId = Number(localStorage.getItem("userId"));
        tags.value = await getTags(userId);
    } catch {
        tags.value = [];
    }
};

const handleAdd = async (tagName: string) => {
    const name = tagName.trim();
    if (!name || tags.value.some((t) => t.name === name)) return;

    try {
        const userId = Number(localStorage.getItem("userId"));
        const newTag = await createTag({ name, user: userId });
        tags.value.push(newTag);
    } finally {
        isOpen.value = false;
    }
};

onMounted(fetchTags);
</script>

<template>
    <div class="container mx-auto p-4">
        <div class="flex justify-between items-center mb-6">
            <h1 class="text-3xl font-bold">Tags</h1>
            <button class="btn btn-primary" @click="isOpen = true">
                Create Tag
            </button>
        </div>
        <div class="flex flex-wrap gap-2">
            <TagCard v-for="tag in tags" :key="tag.id" :tag="tag" />
        </div>
        <CreateTag :is-open="isOpen" @open="isOpen = $event" @add="handleAdd" />
    </div>
</template>
