<script lang="ts">
	import { Input } from '@/lib/components/ui/input';
	import type { PageData } from './$types';
	import { Button } from '@/lib/components/ui/button';

	export let data: PageData;
	export const form = {};
</script>

<div class="flex items-center justify-center h-screen flex-col">
	<h2 class="text-2xl mb-8">Create new skills</h2>
	<form
		method="POST"
		action="?/create_skill"
		enctype="multipart/form-data"
		class="space-y-4 flex flex-col w-[50%]"
	>
		<Input type="text" name="name" placeholder="name" />
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
	
		<Button class="w-full bg-black text-white" type="submit">Create</Button>
	</form>

</div>
