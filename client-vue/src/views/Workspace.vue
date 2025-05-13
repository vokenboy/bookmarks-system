<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import UrlCard from "@/components/UrlCard.vue";

interface Url {
    id: number;
    name: string;
    link: string;
    description: string;
    tags: string[];
    status: "alive" | "redirected" | "dead";
    workspace: { id: number; name: string };
}

interface Workspace {
    id: number;
    name: string;
    description?: string;
}

const route = useRoute();
const router = useRouter();
const workspaceId = Number(route.params.id);

const workspace = ref<Workspace | null>(null);
const urls = ref<Url[]>([]);

async function fetchWorkspace() {
    workspace.value = {
        id: workspaceId,
        name: `Workspace #${workspaceId}`,
        description: "A description for this workspace.",
    };
}

async function fetchUrls() {
    urls.value = [
        {
            id: 1,
            name: "Vue.js",
            link: "https://vuejs.org",
            description: "The Progressive JS Framework",
            tags: ["javascript", "framework"],
            status: "alive",
            workspace: { id: workspaceId, name: workspace.value?.name! },
        },
        {
            id: 2,
            name: "Django",
            link: "https://www.djangoproject.com",
            description: "The web framework for perfectionists with deadlines.",
            tags: ["python", "backend"],
            status: "alive",
            workspace: { id: workspaceId, name: workspace.value?.name! },
        },
    ];
}

onMounted(async () => {
    await fetchWorkspace();
    await fetchUrls();
});

function goToUrlDetail(id: number) {
    router.push(`/urls/${id}`);
}
</script>

<template>
    <div class="container mx-auto p-4">
        <div v-if="workspace" class="mb-8">
            <h1 class="text-3xl font-bold">{{ workspace.name }}</h1>
            <p class="text-gray-600 mt-2">{{ workspace.description }}</p>
        </div>
        <div
            v-if="urls.length"
            class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"
        >
            <UrlCard
                v-for="url in urls"
                :key="url.id"
                :url="url"
                @select="goToUrlDetail"
            />
        </div>
        <p v-else class="text-gray-500">No URLs in this workspace yet.</p>
    </div>
</template>

<style scoped></style>
