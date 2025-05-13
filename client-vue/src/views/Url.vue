<script setup lang="ts">
import { defineProps } from "vue";

interface URLDetailsProps {
    name: string;
    link: string;
    description?: string;
    tags?: string[];
    status?: string;
}

const props = defineProps<URLDetailsProps>();
</script>

<template>
    <div class="container mx-auto p-4">
        <div class="card bg-base-100 shadow-lg">
            <div class="card-body">
                <h2 class="card-title text-2xl">{{ props.name }}</h2>
                <a
                    :href="props.link"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="link link-primary break-all"
                >
                    {{ props.link }}
                </a>
                <p v-if="props.description" class="mt-2 text-base">
                    {{ props.description }}
                </p>
                <div v-if="props.tags && props.tags.length" class="mt-4">
                    <span
                        v-for="tag in props.tags"
                        :key="tag"
                        class="badge badge-outline mr-2"
                    >
                        {{ tag }}
                    </span>
                </div>
                <div v-if="props.status" class="mt-4">
                    <span
                        class="badge"
                        :class="{
                            'badge-success': props.status === 'alive',
                            'badge-warning': props.status === 'redirect',
                            'badge-error': props.status === 'dead',
                        }"
                    >
                        {{ props.status }}
                    </span>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped></style>
