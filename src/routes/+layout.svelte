<script lang="ts">
	import '../app.css';
	import type { Config } from '@sveltejs/adapter-vercel';

	export const config: Config = {
		runtime: 'nodejs18.x'
	};
</script>

<div class="app min-h-full">
	<main>
		<slot />
	</main>
</div>
