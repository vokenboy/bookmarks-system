<script setup lang="ts">
import { defineProps, defineEmits } from "vue";

interface Url {
    id: number;
    name: string;
    link: string;
    description: string;
    tags: string[];
    status: "alive" | "redirected" | "dead";
    workspace: { id: number; name: string };
}

const props = defineProps<{ url: Url }>();
const emit = defineEmits<{ (e: "select", id: number): void }>();

function onClickCard() {
    emit("select", props.url.id);
}
</script>

<template>
    <div
        class="card shadow hover:shadow-lg cursor-pointer transition"
        @click="onClickCard"
    >
        <div class="card-body">
            <div class="flex justify-between items-start">
                <h2 class="card-title">{{ url.name }}</h2>
                <span class="badge badge-outline">{{
                    url.workspace.name
                }}</span>
            </div>

            <a
                :href="url.link"
                target="_blank"
                rel="noopener"
                class="link link-primary break-all mt-1"
                @click.stop
            >
                {{ url.link }}
            </a>

            <p class="mt-2 text-sm">{{ url.description }}</p>

            <div class="flex flex-wrap gap-2 mt-3">
                <span
                    v-for="tag in url.tags"
                    :key="tag"
                    class="badge badge-outline"
                >
                    {{ tag }}
                </span>
            </div>

            <div class="mt-3">
                <span
                    :class="{
                        'badge badge-success': url.status === 'alive',
                        'badge badge-warning': url.status === 'redirected',
                        'badge badge-error': url.status === 'dead',
                    }"
                >
                    {{ url.status }}
                </span>
            </div>
        </div>
    </div>
</template>

<style scoped></style>
