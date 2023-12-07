<script>
	import Header from './Header.svelte';
	import '../app.css';
</script>

<div class="app">
	<Header />

	<main class="container h-full bg-slate-600">
		<slot />
	</main>

	<footer>
	</footer>
</div>