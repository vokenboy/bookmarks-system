<script setup lang="ts">
import { ref, onMounted } from "vue";
import BookmarkCard from "@/components/BookmarkCard.vue";
import { type Bookmark } from "@/assets/types/bookmark";
import { getBookmarks, deleteBookmark } from "@/api/bookmark/bookmarkAPI";

const bookmarks = ref<Bookmark[]>([]);

const fetchBookmarks = async () => {
    try {
        const userId = Number(localStorage.getItem("userId"));
        bookmarks.value = await getBookmarks(userId);
    } catch (error) {
        console.error("Error fetching bookmarks:", error);
        bookmarks.value = [];
    }
};

const handleDelete = async (id: number) => {
    const confirmed = window.confirm(
        `Are you sure you want to delete the bookmark?`
    );
    if (!confirmed) return;

    try {
        await deleteBookmark(id);
        bookmarks.value = bookmarks.value.filter(
            (bookmark) => bookmark.id !== id
        );
    } catch (error) {
        alert("Failed to delete bookmark. Please try again.");
    }
};

onMounted(fetchBookmarks);
</script>
<template>
    <div class="container mx-auto p-4">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            <BookmarkCard
                v-for="bookmark in bookmarks"
                :key="bookmark.id"
                :bookmark="bookmark"
            />
        </div>
    </div>
</template>

<style scoped></style>
