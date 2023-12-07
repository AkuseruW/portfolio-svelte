<script>
	import '../app.css';
	import Separator from '$lib/svg/Separator.svelte';
	import { browser } from '$app/environment';
	import { QueryClient, QueryClientProvider } from '@tanstack/svelte-query';

	const queryClient = new QueryClient({
		defaultOptions: {
			queries: {
				enabled: browser
			}
		}
	});
</script>

<div class="app min-h-full">
	<Separator />

	<main class="container mx-auto h-full">
		<QueryClientProvider client={queryClient}>
			<slot />
		</QueryClientProvider>
	</main>

	<footer></footer>
</div>
