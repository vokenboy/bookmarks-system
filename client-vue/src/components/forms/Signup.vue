<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
import { signup as signupAPI } from "@/api/auth/authAPI";

const username = ref("");
const password = ref("");
const router = useRouter();

async function signup() {
    try {
        await signupAPI({ username: username.value, password: password.value });
        router.push("/");
    } catch (err: any) {
        console.error("Signup error:", err);
        alert(
            err.response?.data?.detail ||
                "Could not sign up – please try again."
        );
    }
}
</script>
<template>
    <div class="flex justify-center h-screen">
        <div class="p-6 m-auto rounded-md shadow-xl">
            <h1 class="text-3xl font-bold text-center mb-4">Signup</h1>
            <form @submit.prevent="signup" class="space-y-4">
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
                        Signup
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>
