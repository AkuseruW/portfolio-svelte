<script lang="ts">
	import * as DropdownMenu from '$lib/components/ui/dropdown-menu';
	import { Button } from '$lib/components/ui/button';
	import { MoreHorizontal } from 'lucide-svelte';
	import { PUBLIC_SERVEUR_URL } from '$env/static/public';
	export let id: string;
	let showModal = false;

	const confirmDelete = () => {
		showModal = true;
	};

	const handleDelete = async () => {
		const response = await fetch(`${PUBLIC_SERVEUR_URL}/api/projects/${id}`, {
			method: 'DELETE'
		});

		if (response.ok) {
			location.reload();
		}
	};

	const closeModal = () => {
		showModal = false;
	};
</script>

<DropdownMenu.Root>
	<DropdownMenu.Trigger asChild let:builder>
		<Button variant="ghost" builders={[builder]} size="icon" class="relative w-8 h-8 p-0">
			<span class="sr-only">Open menu</span>
			<MoreHorizontal class="w-4 h-4" />
		</Button>
	</DropdownMenu.Trigger>
	<DropdownMenu.Content class="bg-white">
		<DropdownMenu.Label class="underline">Actions</DropdownMenu.Label>
		<DropdownMenu.Item class="cursor-pointer">
			<a href="/admin/projects/{id}">edit</a></DropdownMenu.Item
		>
		<DropdownMenu.Separator />
		<DropdownMenu.Item on:click={confirmDelete} class="cursor-pointer">Delete</DropdownMenu.Item>
	</DropdownMenu.Content>
	
	{#if showModal}
		<div
			class="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-black bg-opacity-50"
		>
			<div class="bg-white p-8 rounded shadow-md">
				<p>Are you sure you want to delete this item?</p>
				<div class="mt-4 flex justify-end">
					<Button on:click={handleDelete} variant="outline" class="mr-2 bg-red-600 text-white"
						>Delete</Button
					>
					<Button on:click={closeModal} variant="outline">Cancel</Button>
				</div>
			</div>
		</div>
	{/if}
</DropdownMenu.Root>
