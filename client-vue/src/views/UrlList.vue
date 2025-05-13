<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
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

const urls = ref<Url[]>([]);
const router = useRouter();

async function fetchUrls() {
    urls.value = [
        {
            id: 1,
            name: "Vue.js",
            link: "https://vuejs.org",
            description: "The Progressive JavaScript Framework",
            tags: ["javascript", "framework"],
            status: "alive",
            workspace: { id: 1, name: "Personal" },
        },
        {
            id: 2,
            name: "Django",
            link: "https://www.djangoproject.com",
            description: "The web framework for perfectionists with deadlines.",
            tags: ["python", "backend"],
            status: "alive",
            workspace: { id: 2, name: "Team Projects" },
        },
        {
            id: 3,
            name: "Old Link",
            link: "https://example.com/old",
            description: "This one redirects",
            tags: ["test"],
            status: "redirected",
            workspace: { id: 3, name: "Research" },
        },
    ];
}

onMounted(fetchUrls);

function goToUrlDetail(id: number) {
    router.push(`/urls/${id}`);
}
</script>

<template>
    <div class="container mx-auto p-4">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            <UrlCard
                v-for="url in urls"
                :key="url.id"
                :url="url"
                @select="goToUrlDetail"
            />
        </div>
    </div>
</template>

<style scoped></style>
