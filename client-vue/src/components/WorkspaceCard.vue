<script setup lang="ts">
import { defineProps } from "vue";
import { useRouter } from "vue-router";
import type { Workspace } from "@/assets/types/workspace";

const props = defineProps<{ workspace: Workspace }>();

const router = useRouter();

const handleClick = () => {
    router.push(`/workspaces/${props.workspace.id}`);
};
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
