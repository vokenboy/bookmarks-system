<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import WorkspaceCard from "@/components/WorkspaceCard.vue";
import CreateWorkspaceModal from "@/components/modals/CreateWorkspace.vue";
import { getWorkspaces, createWorkspace } from "@/api/workspace/workspaceAPI";
import { type Workspace } from "@/assets/types/workspace";

const router = useRouter();
const workspaces = ref<Workspace[]>([]);
const showModal = ref(false);

const fetchWorkspaces = async () => {
    try {
        const userId = Number(localStorage.getItem("userId"));
        workspaces.value = await getWorkspaces(userId);
    } catch (err) {
        workspaces.value = [];
    }
};

const onCreateWorkspace = async (name: string, description: string) => {
    try {
        const userId = Number(localStorage.getItem("userId"));
        const newWs: Workspace = await createWorkspace({
            name,
            description,
            user: userId,
        });
        workspaces.value.push(newWs);
        showModal.value = false;
    } catch (err) {
        showModal.value = false;
    }
};

const openCreateModal = () => {
    showModal.value = true;
};

const goToWorkspace = (id: number) => {
    router.push(`/workspaces/${id}`);
};

onMounted(fetchWorkspaces);
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
                v-for="workspace in workspaces"
                :key="workspace.id"
                :workspace="workspace"
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
