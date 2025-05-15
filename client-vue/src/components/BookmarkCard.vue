<script setup lang="ts">
import { defineProps, defineEmits, ref } from "vue";
import EditBookmarkModal from "@/components/modals/EditBookmark.vue";
import { deleteBookmark } from "@/api/bookmark/bookmarkAPI";
import type { Bookmark } from "@/assets/types/bookmark";

const props = defineProps<{ bookmark: Bookmark }>();

const emit = defineEmits<{
    (e: "select", id: number): void;
    (e: "deleted", id: number): void;
    (e: "update", updated: Bookmark): void;
}>();

const showEditModal = ref(false);
const isDeleting = ref(false);

function onClickCard() {
    emit("select", props.bookmark.id);
}

function openEdit(event: MouseEvent) {
    event.stopPropagation();
    showEditModal.value = true;
}

async function onDelete(event: MouseEvent) {
    event.stopPropagation();
    if (isDeleting.value) return;

    const confirmed = window.confirm(
        `Are you sure you want to delete the bookmark '${props.bookmark.name}'?`
    );
    if (!confirmed) return;

    isDeleting.value = true;
    try {
        await deleteBookmark(props.bookmark.id);
        emit("deleted", props.bookmark.id);
    } catch (error) {
        console.error("Failed to delete bookmark:", error);
        alert("Failed to delete bookmark. Please try again.");
    } finally {
        isDeleting.value = false;
    }
}

// function handleUpdate(payload: {
//     id: string;
//     name: string;
//     link: string;
//     description: string;
//     tags: string[];
// }) {
//     const updated: Bookmark = {
//         ...props.bookmark,
//         name: payload.name,
//         link: payload.link,
//         description: payload.description,
//         tags: props.bookmark.tags
//             .map((t) => (payload.tags.includes(t.name) ? t : undefined))
//             .filter((t): t is Bookmark["tags"][0] => !!t),
//     };
//     emit("update", updated);
//     showEditModal.value = false;
// }

const closeModal = () => {
    showEditModal.value = false;
};
</script>

<template>
    <div
        class="card shadow hover:shadow-lg cursor-pointer transition"
        @click="onClickCard"
    >
        <div class="card-body">
            <div class="flex justify-between items-start">
                <h2 class="card-title">{{ props.bookmark.name }}</h2>
            </div>
            <div class="mt-3">
                <h3 class="text-sm font-semibold mb-1">Workspaces</h3>
                <div class="flex flex-wrap gap-2">
                    <span
                        v-for="ws in props.bookmark.workspaces"
                        :key="ws.id"
                        class="badge badge-outline"
                    >
                        {{ ws.name }}
                    </span>
                    <span
                        v-if="props.bookmark.workspaces.length === 0"
                        class="text-gray-500 italic text-sm"
                    >
                        No workspaces
                    </span>
                </div>
            </div>
            <a
                :href="props.bookmark.link"
                target="_blank"
                rel="noopener"
                class="link link-primary break-all mt-4 block"
                @click.stop
            >
                {{ props.bookmark.link }}
            </a>
            <p class="mt-2 text-sm">{{ props.bookmark.description }}</p>
            <div class="mt-3">
                <h3 class="text-sm font-semibold mb-1">Tags</h3>
                <div class="flex flex-wrap gap-2">
                    <span
                        v-for="tag in props.bookmark.tags"
                        :key="tag.id"
                        class="badge badge-outline"
                    >
                        {{ tag.name }}
                    </span>
                    <span
                        v-if="props.bookmark.tags.length === 0"
                        class="text-gray-500 italic text-sm"
                    >
                        No tags
                    </span>
                </div>
            </div>
            <div class="mt-3">
                <span
                    :class="{
                        'badge badge-success':
                            props.bookmark.status === 'alive',
                        'badge badge-warning':
                            props.bookmark.status === 'redirected',
                        'badge badge-error': props.bookmark.status === 'dead',
                    }"
                >
                    {{ props.bookmark.status }}
                </span>
            </div>
            <div class="card-actions justify-end mt-4">
                <button class="btn btn-sm btn-outline" @click="openEdit">
                    Edit
                </button>
                <button
                    class="btn btn-sm btn-error"
                    :disabled="isDeleting"
                    @click="onDelete"
                >
                    Delete
                </button>
            </div>
        </div>
    </div>

    <!-- <EditBookmarkModal
        :visible="showEditModal"
        :bookmark="{
            id: props.bookmark.id.toString(),
            name: props.bookmark.name,
            link: props.bookmark.link,
            description: props.bookmark.description,
            tags: props.bookmark.tags.map((t) => t.name),
        }"
        @update:visible="closeModal"
        @update="handleUpdate"
    /> -->
</template>

<style scoped></style>
