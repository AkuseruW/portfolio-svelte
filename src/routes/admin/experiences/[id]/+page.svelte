<script lang="ts">
	import { Input } from '@/lib/components/ui/input';
	import { Button } from '@/lib/components/ui/button';
	import Textarea from '@/lib/components/ui/textarea/textarea.svelte';
	export let data;

</script>

<div class="flex items-center justify-center h-screen flex-col">
	<h2 class="text-2xl mb-8">Update {data.experience.title} experience</h2>
	<form
		method="POST"
		action="?/update_experience"
		enctype="multipart/form-data"
		class="space-y-4 flex flex-col w-[50%]"
	>
		<Input type="text" name="title" value={data.experience.title} />
		<Textarea name="description" value={data.experience.description} />
		<div class="flex">
			<Input type="number" name="startTime" autocomplete="off" value={data.experience.startTime} />
			<Input type="number" name="endTime" autocomplete="off" value={data.experience.endTime} />
		</div>
		<Input type="link" name="link" placeholder="link" value={data.experience.link} />
		<input type="number" name="id" value={data.experience.id} hidden />
		<Button class="w-full bg-black text-white" type="submit">Create</Button>
	</form>
</div>
