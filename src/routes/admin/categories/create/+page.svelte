<script lang="ts">
	import { Input } from '@/lib/components/ui/input';
	import { Button } from '@/lib/components/ui/button';

	export const form = {};
</script>

<div class="flex items-center justify-center mt-16 flex-col">
	<h2 class="text-2xl mb-8">Create new category</h2>
	<form method="POST" action="?/create_project" class="space-y-4 flex flex-col w-[50%]">
		<Input type="text" name="name" placeholder="Name" />
		<Button class="w-full bg-black text-white" type="submit">Create</Button>
	</form>
</div>
