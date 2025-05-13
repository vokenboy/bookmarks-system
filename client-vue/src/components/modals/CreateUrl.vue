<script setup lang="ts">
import { defineProps, defineEmits, ref, watch } from "vue";

const props = defineProps<{ visible: boolean }>();

const emits = defineEmits<{
    (e: "update:visible", value: boolean): void;
    (
        e: "add",
        payload: {
            name: string;
            link: string;
            description: string;
            tags: string[];
        }
    ): void;
}>();

const name = ref("");
const link = ref("");
const description = ref("");
const tagsInput = ref("");

watch(
    () => props.visible,
    (visible) => {
        if (!visible) {
            name.value = "";
            link.value = "";
            description.value = "";
            tagsInput.value = "";
        }
    }
);

function close() {
    emits("update:visible", false);
}

function handleAdd() {
    const nameVal = name.value.trim();
    const linkVal = link.value.trim();
    const descVal = description.value.trim();
    const tags = tagsInput.value
        .split(",")
        .map((t) => t.trim())
        .filter((t) => t);
    if (!nameVal || !linkVal) return;
    emits("add", { name: nameVal, link: linkVal, description: descVal, tags });
    close();
}
</script>

<template>
    <div v-if="props.visible" class="modal modal-open">
        <div class="modal-box w-11/12 max-w-2xl">
            <h3 class="font-bold text-lg">Add New URL</h3>
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
            <input
                v-model="tagsInput"
                type="text"
                placeholder="Tags (comma separated)"
                class="input input-bordered w-full mt-4"
            />
            <div class="modal-action">
                <button class="btn" @click="close">Cancel</button>
                <button
                    class="btn btn-primary"
                    :disabled="!name.trim() || !link.trim()"
                    @click="handleAdd"
                >
                    Add
                </button>
            </div>
        </div>
    </div>
</template>

<style scoped></style>
