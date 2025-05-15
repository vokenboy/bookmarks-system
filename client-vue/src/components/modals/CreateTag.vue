<script setup lang="ts">
import { ref } from "vue";

const props = defineProps<{
    isOpen: boolean;
}>();

const emit = defineEmits<{
    (e: "open", next: boolean): void;
    (e: "add", name: string): void;
}>();

const name = ref("");

const close = () => {
    emit("open", false);
};

const submit = () => {
    if (!name.value.trim()) return;
    emit("add", name.value);
    name.value = "";
    close();
};
</script>

<template>
    <div v-if="props.isOpen" class="modal modal-open">
        <div class="modal-box w-11/12 max-w-md">
            <h3 class="font-bold text-lg">Create New Tag</h3>
            <input
                v-model="name"
                type="text"
                placeholder="Tag name"
                class="input input-bordered w-full mt-4"
            />
            <div class="modal-action">
                <button class="btn" @click="close">Cancel</button>
                <button
                    class="btn btn-primary"
                    :disabled="!name.trim()"
                    @click="submit"
                >
                    Create Tag
                </button>
            </div>
        </div>
    </div>
</template>
