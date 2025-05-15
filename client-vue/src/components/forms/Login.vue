<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import { login as loginAPI } from "@/api/auth/authAPI";

const username = ref("");
const password = ref("");
const router = useRouter();

async function login() {
    try {
        await loginAPI({ username: username.value, password: password.value });
        router.push("/");
    } catch (err: any) {
        console.error("Login error:", err);
        alert(err.response?.data?.detail || "Login failed – please try again.");
    }
}
</script>
<template>
    <div class="flex justify-center h-screen">
        <div class="p-6 m-auto rounded-md shadow-xl">
            <h1 class="text-3xl font-bold text-center mb-4">Login</h1>
            <form @submit.prevent="login" class="space-y-4">
                <div>
                    <label class="label">
                        <span class="text-base label-text">Username</span>
                    </label>
                    <input
                        v-model="username"
                        type="text"
                        placeholder="Username"
                        class="w-full input"
                        required
                    />
                </div>
                <div>
                    <label class="label">
                        <span class="text-base label-text">Password</span>
                    </label>
                    <input
                        v-model="password"
                        type="password"
                        placeholder="Enter Password"
                        class="w-full input"
                        required
                    />
                </div>
                <div>
                    <button type="submit" class="btn btn-primary w-full">
                        Login
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>
