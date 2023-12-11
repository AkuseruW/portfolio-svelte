import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vitest/config';

export default defineConfig({
	plugins: [sveltekit()],
	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	},
	server: {
		fs: {
			strict: false,
			allow: ["/api"],
		},
		proxy: {
			"/api": {
				target: "/api",
				changeOrigin: true,
			},
			"/docs": {
				target: process.env.NODE_ENV === "development"
					? "http://127.0.0.1:8000/docs"
					: "/docs",
				changeOrigin: true,
				rewrite: (path) => path.replace(/^\/docs/, '')
			},
			"/openapi.json": {
				target: process.env.NODE_ENV === "development"
					? "http://127.0.0.1:8000/openapi.json"
					: "/openapi.json",
				changeOrigin: true,
				rewrite: (path) => path.replace(/^\/openapi.json/, '')
			}
		}
	}
});
