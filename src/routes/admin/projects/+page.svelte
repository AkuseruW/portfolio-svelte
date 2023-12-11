<script lang="ts">
	import Button from '@/lib/components/ui/button/button.svelte';
	export let data;
	import DataTable from './data-table.svelte';
</script>

<div class="container mx-auto py-10">
	<div class="flex justify-between">
		<h2 class="text-2xl mb-8">Projects</h2>
		<Button class="border" href="/admin/projects/create">Create new project</Button>
	</div>
	<DataTable data={data.projects} />
</div>
