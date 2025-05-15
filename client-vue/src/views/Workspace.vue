<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import BookmarkCard from "@/components/BookmarkCard.vue";
import { getBookmarks } from "@/api/bookmark/bookmarkAPI";
import type { Bookmark } from "@/assets/types/bookmark";
import type { Workspace } from "@/assets/types/workspace";
import { getWorkspace } from "@/api/workspace/workspaceAPI";

const route = useRoute();
const workspaceId = Number(route.params.workspaceId);

const workspace = ref<Workspace | null>(null);
const allBookmarks = ref<Bookmark[]>([]);
const bookmarks = ref<Bookmark[]>([]);

const fetchWorkspace = async () => {
    try {
        workspace.value = await getWorkspace(workspaceId);
    } catch (err) {
        console.error("Failed to load workspace:", err);
    }
};

const fetchBookmarks = async () => {
    try {
        const userId = Number(localStorage.getItem("userId"));
        allBookmarks.value = await getBookmarks(userId);

        bookmarks.value = allBookmarks.value.filter((b) =>
            b.workspaces.some((ws) => ws.id === workspaceId)
        );
    } catch (err) {
        bookmarks.value = [];
    }
};

onMounted(() => {
    fetchWorkspace();
    fetchBookmarks();
});
</script>

<template>
    <div class="container mx-auto p-4">
        <div v-if="workspace" class="mb-8">
            <h1 class="text-3xl font-bold">{{ workspace.name }}</h1>
            <p class="text-gray-600 mt-2">{{ workspace.description }}</p>
        </div>

        <div
            v-if="bookmarks.length"
            class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"
        >
            <BookmarkCard
                v-for="bookmark in bookmarks"
                :key="bookmark.id"
                :bookmark="bookmark"
            />
        </div>
    </div>
</template>

<style scoped></style>
