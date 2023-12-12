<script lang="ts">
	import { Input } from '@/lib/components/ui/input';
	import { Button } from '@/lib/components/ui/button';
	import Textarea from '@/lib/components/ui/textarea/textarea.svelte';

	export const form = {};
</script>

<div class="flex items-center justify-center h-screen flex-col">
	<h2 class="text-2xl mb-8">Create new experience</h2>
	<form
		method="POST"
		action="?/create_experience"
		enctype="multipart/form-data"
		class="space-y-4 flex flex-col w-[50%]"
	>
		<Input type="text" name="title" placeholder="title" />
		<Textarea name="description" placeholder="description" />
		<div class="flex">
			<Input type="number" name="startTime" placeholder="startTime" autocomplete="off" />
			<Input type="number" name="endTime" placeholder="endTime" autocomplete="off" />
		</div>
		<Input type="link" name="link" placeholder="link" />

		<Button class="w-full bg-black text-white" type="submit">Create</Button>
	</form>
</div>
