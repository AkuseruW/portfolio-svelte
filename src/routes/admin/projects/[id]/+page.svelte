<script lang="ts">
	import { Input } from '@/lib/components/ui/input';
	import { Button } from '@/lib/components/ui/button';
	import { Textarea } from '@/lib/components/ui/textarea/index.js';
	import type { Skill } from '@/lib/types/skills.js';

	export let data;
	let selected_skills: Skill[] = data.project.skills;
	let skills: Skill[] = data.skills;

	let added_skills: Skill[] = [];

	const selectSkill = (event: any) => {
		const selectedSkillId = parseInt(event.target.value);
		added_skills = skills.filter((skill) => skill.id === selectedSkillId);

		if (selected_skills.some((skill) => skill.id === selectedSkillId)) {
			selected_skills = selected_skills.filter((skill) => skill.id !== selectedSkillId);
		}

		selected_skills = [...selected_skills, ...added_skills];
	};

	const deleteSkill = (event: any) => {
		const deletedSkillId = parseInt(event.target.value);
		selected_skills = selected_skills.filter((skill) => skill.id !== deletedSkillId);
	};
</script>

<div class="flex items-center justify-center mt-16 flex-col">
	<h2 class="text-2xl mb-8">Create {data.project.name} projects</h2>
	<form
		method="POST"
		action="?/update_project"
		enctype="multipart/form-data"
		class="space-y-4 flex flex-col w-[50%]"
	>
		<Input type="text" name="name" placeholder="Name" value={data.project.name} />
		<Textarea name="description" placeholder="Description" value={data.project.description} />
		<Input type="link" name="link" placeholder="Link" value={data.project.link} />
		<Input
			type="date"
			name="dateOfCreation"
			placeholder="dateOfCreation"
			value={data.project.dateOfCreation.split('T')[0]}
		/>

		<div class="flex">
			<select
				class="flex w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				multiple
			>
				{#each data.skills as skill}
					<option on:dblclick={selectSkill} value={skill.id}>{skill.name}</option>
				{/each}
			</select>

			<select
				class="flex w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
				multiple
			>
				{#each selected_skills as skill}
					<option on:dblclick={deleteSkill} value={skill.id}>{skill.name}</option>
				{/each}
			</select>

			{#each selected_skills as skill}
				<input type="hidden" name="skills" value={skill.id} />
			{/each}
		</div>

		<input type="file" name="images" id="images" multiple />
		<input type="number" name="id" value={data.project.id} hidden />
		<Button class="w-full bg-black text-white" type="submit">Update</Button>
	</form>

	<div class="flex mt-32">
		{#if data.project.images}
			{#each data.project.images as image}
				<div class="flex flex-col items-center">
					<img src={image.image} alt={image.name} class="w-[300px] h-[300px]" />
					<Button variant="outline" class="bg-red-600 text-white">delete</Button>
				</div>
			{/each}
		{/if}
	</div>
</div>
