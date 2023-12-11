<script>
	import AdminNav from '@/lib/components/admin/AdminNav.svelte';
	import Navbar from '@/lib/components/admin/Navbar.svelte';
</script>

<svelte:head>
	<title>Admin</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<div class="container mx-auto min-h-full">
	<div class="border-b">
		<div class="flex h-16 items-center px-4">
			<Navbar class="mx-6" />
			<div class="ml-auto flex items-center space-x-4">
				<AdminNav />
			</div>
		</div>
	</div>
	<slot />
</div>
