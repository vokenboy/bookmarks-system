<script setup lang="ts">
import { defineProps, defineEmits, ref, watch } from "vue";
import { getTags } from "@/api/tag/tagAPI";
import { getWorkspaces } from "@/api/workspace/workspaceAPI";
import type { Tag } from "@/assets/types/tag";
import type { Workspace } from "@/assets/types/workspace";
import type { Bookmark } from "@/assets/types/bookmark";

const props = defineProps<{ visible: boolean; bookmark: Bookmark }>();

const emits = defineEmits<{
    (e: "update:visible", value: boolean): void;
    (e: "updated", bookmark: Bookmark): void;
}>();

const name = ref("");
const link = ref("");
const description = ref("");
const availTags = ref<Tag[]>([]);
const selectedTags = ref<number[]>([]);
const availWorkspaces = ref<Workspace[]>([]);
const selectedWorkspaces = ref<number[]>([]);

watch(
    () => props.visible,
    async (visible) => {
        if (visible) {
            name.value = props.bookmark.name;
            link.value = props.bookmark.link;
            description.value = props.bookmark.description;

            const userIdStr = localStorage.getItem("userId");
            if (!userIdStr) return;
            const userId = Number(userIdStr);

            availTags.value = await getTags(userId);
            availWorkspaces.value = await getWorkspaces(userId);

            selectedTags.value = props.bookmark.tags.map((t) => t.id);
            selectedWorkspaces.value = props.bookmark.workspaces
                ? props.bookmark.workspaces.map((w) => w.id)
                : [];
        } else {
            name.value = "";
            link.value = "";
            description.value = "";
            selectedTags.value = [];
            selectedWorkspaces.value = [];
        }
    },
    { immediate: true }
);

function close() {
    emits("update:visible", false);
}

async function handleUpdate() {
    const nameVal = name.value.trim();
    const linkVal = link.value.trim();
    const descVal = description.value.trim();
    if (!nameVal || !linkVal) return;

    try {
        const payload = {
            name: nameVal,
            link: linkVal,
            description: descVal,
            tag_ids: selectedTags.value,
            ws_ids: selectedWorkspaces.value,
        };
        const idNum = Number(props.bookmark.id);
    } catch (err) {
        console.error("Failed to update bookmark:", err);
    } finally {
        close();
    }
}
</script>

<template>
    <div v-if="props.visible" class="modal modal-open">
        <div class="modal-box w-11/12 max-w-2xl">
            <h3 class="font-bold text-lg">Edit Bookmark</h3>
            <input
                v-model="link"
                type="url"
                placeholder="Link"
                class="input input-bordered w-full mt-4"
            />
            <input
                v-model="name"
                type="text"
                placeholder="Name"
                class="input input-bordered w-full mt-4"
            />
            <textarea
                v-model="description"
                placeholder="Description"
                class="textarea textarea-bordered w-full mt-4"
                rows="3"
            ></textarea>

            <label class="mt-4 font-semibold block">Tags</label>
            <div class="flex flex-wrap gap-2 mt-2">
                <label
                    v-for="tag in availTags"
                    :key="tag.id"
                    class="inline-flex items-center"
                >
                    <input
                        type="checkbox"
                        class="checkbox mr-2"
                        v-model="selectedTags"
                        :value="tag.id"
                    />
                    {{ tag.name }}
                </label>
                <span
                    v-if="availTags.length === 0"
                    class="text-sm text-gray-500"
                    >No tags available</span
                >
            </div>
            <label class="mt-4 font-semibold block">Workspaces</label>
            <div class="flex flex-wrap gap-2 mt-2">
                <label
                    v-for="ws in availWorkspaces"
                    :key="ws.id"
                    class="inline-flex items-center"
                >
                    <input
                        type="checkbox"
                        class="checkbox mr-2"
                        v-model="selectedWorkspaces"
                        :value="ws.id"
                    />
                    {{ ws.name }}
                </label>
                <span
                    v-if="availWorkspaces.length === 0"
                    class="text-sm text-gray-500"
                    >No workspaces available</span
                >
            </div>

            <div class="modal-action">
                <button class="btn" @click="close">Cancel</button>
                <button
                    class="btn btn-primary"
                    :disabled="!name.trim() || !link.trim()"
                    @click="handleUpdate"
                >
                    Update
                </button>
            </div>
        </div>
    </div>
</template>

<style scoped></style>
