<script lang="ts">
	import type { PageData } from './$types';

	export let data: PageData;
	export const form = {};
	let formData = {
		name: '',
		categorie: '',
		image: ''
	};
</script>

<form
	method="POST"
	action="?/create_skill"
	enctype="multipart/form-data"
	class="space-y-4 flex flex-col w-[50%]"
>
	<label for="name">Name</label>
	<input type="text" name="name" />

	<select
		class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
		name="category"
	>
        <option value="">categories</option>
		{#each data.categories as category}
			<option value={category.id}>{category.name}</option>
		{/each}
	</select>

	<input type="file" name="icon" id="icon" />

	<button type="submit">Create</button>
</form>
