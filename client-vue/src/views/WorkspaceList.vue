<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import WorkspaceCard from "@/components/WorkspaceCard.vue";
import CreateWorkspaceModal from "@/components/modals/CreateWorkspace.vue";

interface Workspace {
    id: number;
    name: string;
    description?: string;
}

const workspaces = ref<Workspace[]>([]);
const router = useRouter();
const showModal = ref(false);

async function fetchWorkspaces() {
    workspaces.value = [
        { id: 1, name: "Personal", description: "My personal workspace" },
        {
            id: 2,
            name: "Team Projects",
            description: "Workspace for team projects",
        },
        {
            id: 3,
            name: "Research",
            description: "Workspace for research projects",
        },
    ];
}

onMounted(fetchWorkspaces);

function goToWorkspace(id: number) {
    router.push(`/workspaces/${id}`);
}

function openCreateModal() {
    showModal.value = true;
}

function onCreateWorkspace(name: string) {
    const newId = Math.max(...workspaces.value.map((w) => w.id)) + 1;
    workspaces.value.push({ id: newId, name });
    showModal.value = false;
    router.push(`/workspaces/${newId}`);
}
</script>

<template>
    <div class="container mx-auto p-4">
        <div class="flex justify-between items-center mb-6">
            <h1 class="text-3xl font-bold">Workspaces</h1>
            <button class="btn btn-primary" @click="openCreateModal">
                New Workspace
            </button>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            <WorkspaceCard
                v-for="ws in workspaces"
                :key="ws.id"
                :workspace="ws"
                @select="goToWorkspace"
            />
        </div>

        <CreateWorkspaceModal
            :visible="showModal"
            @update:visible="showModal = $event"
            @create="onCreateWorkspace"
        />
    </div>
</template>

<style scoped></style>
