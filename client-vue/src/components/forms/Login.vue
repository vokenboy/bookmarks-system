<template>
    <div class="relative flex flex-col justify-center h-screen overflow-hidden">
        <div class="w-full p-6 m-auto rounded-md shadow-xl lg:max-w-lg">
            <h1 class="text-3xl font-semibold text-center">Login</h1>
            <form class="space-y-4">
                <div>
                    <label class="label">
                        <span class="text-base label-text">Username</span>
                    </label>
                    <input
                        type="text"
                        placeholder="Username"
                        class="w-full input"
                    />
                </div>
                <div>
                    <label class="label">
                        <span class="text-base label-text">Password</span>
                    </label>
                    <input
                        type="password"
                        placeholder="Enter Password"
                        class="w-full input"
                    />
                </div>
                <div>
                    <button class="btn btn-primary">Login</button>
                </div>
            </form>
        </div>
    </div>
</template>
