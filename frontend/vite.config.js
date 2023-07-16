import { sveltekit } from "@sveltejs/kit/vite";
import { defineConfig } from "vitest/config";

export default defineConfig(({ command, mode }) => {
    return {
        plugins: [sveltekit()],
        test: {
            include: ["src/**/*.{test,spec}.{js,ts}"]
        },
        define: {
            __APP_BUILD__: JSON.stringify(String(new Date()))
        }
    };
});
