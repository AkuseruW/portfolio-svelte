<script>
	import '../app.css';
	import Separator from '$lib/svg/Separator.svelte';
</script>

<div class="app min-h-full">
	<Separator />

	<main class="container mx-auto h-full">
		<slot />
	</main>

	<footer>
	</footer>
</div>