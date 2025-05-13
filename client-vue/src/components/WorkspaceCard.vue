<script setup lang="ts">
import { defineProps, defineEmits } from "vue";

interface Workspace {
    id: number;
    name: string;
}

const props = defineProps<{
    workspace: Workspace;
}>();

const emit = defineEmits<{
    (e: "select", id: number): void;
}>();

function handleClick() {
    emit("select", props.workspace.id);
}
</script>

<template>
    <div
        class="card shadow hover:shadow-lg cursor-pointer transition"
        @click="handleClick"
    >
        <div class="card-body">
            <h2 class="card-title">{{ workspace.name }}</h2>
            <p class="text-sm text-gray-500">{{ workspace.description }}</p>
        </div>
    </div>
</template>

<style scoped></style>
