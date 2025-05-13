<script setup lang="ts">
import { defineProps, defineEmits, ref, watch } from "vue";

const props = defineProps<{
    visible: boolean;
}>();

const emits = defineEmits<{
    (e: "update:visible", value: boolean): void;
    (e: "create", name: string, description: string): void;
}>();

const workspaceName = ref("");
const workspaceDescription = ref("");

watch(
    () => props.visible,
    (visible) => {
        if (!visible) {
            workspaceName.value = "";
            workspaceDescription.value = "";
        }
    }
);

function close() {
    emits("update:visible", false);
}

function handleCreate() {
    const name = workspaceName.value.trim();
    const description = workspaceDescription.value.trim();
    if (!name || !description) return;
    emits("create", name, description);
    close();
}
</script>

<template>
    <div v-if="props.visible" class="modal modal-open">
        <div class="modal-box">
            <h3 class="font-bold text-lg">Create New Workspace</h3>
            <input
                v-model="workspaceName"
                type="text"
                placeholder="Workspace name"
                class="input input-bordered w-full mt-4"
            />
            <textarea
                v-model="workspaceDescription"
                placeholder="Workspace description"
                class="textarea textarea-bordered w-full mt-4"
                rows="3"
            ></textarea>
            <div class="modal-action">
                <button class="btn" @click="close">Cancel</button>
                <button
                    class="btn btn-primary"
                    :disabled="
                        !workspaceName.trim() || !workspaceDescription.trim()
                    "
                    @click="handleCreate"
                >
                    Create
                </button>
            </div>
        </div>
    </div>
</template>

<style scoped></style>
