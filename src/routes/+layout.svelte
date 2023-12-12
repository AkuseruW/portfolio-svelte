<script lang="ts">
	import '../app.css';
	import type { Config } from '@sveltejs/adapter-vercel';
	import { injectSpeedInsights } from '@vercel/speed-insights/sveltekit';
	import { dev } from '$app/environment';
	import { inject } from '@vercel/analytics';

	inject({ mode: dev ? 'development' : 'production' });
	injectSpeedInsights();

	export const config: Config = {
		runtime: 'nodejs18.x'
	};
</script>

<div class="app min-h-full">
	<main class="min-h-full">
		<slot />
	</main>
</div>
