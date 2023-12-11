<script lang="ts">
	import { Input } from '@/lib/components/ui/input';
	import { Button } from '@/lib/components/ui/button';
	export let data;
</script>

<div class="flex items-center justify-center mt-16 flex-col">
	<h2 class="text-2xl mb-8">Upade {data.category.name} category</h2>
	<form method="POST" action="?/update_category" class="space-y-4 flex flex-col w-[50%]">
		<Input type="text" name="name" placeholder="Name" value={data.category.name} />
		<input type="integer" name="id" hidden readonly value={data.category.id} />
		<Button class="w-full bg-black text-white" type="submit">Create</Button>
	</form>
</div>
