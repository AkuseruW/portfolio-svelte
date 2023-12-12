<script lang="ts">
	import { Input } from '@/lib/components/ui/input';
	import type { PageData } from './$types';
	import { Button } from '@/lib/components/ui/button';
	import { Textarea } from '@/lib/components/ui/textarea';
	import type { Skill } from '@/lib/types/skills';

	export let data: PageData;
	export const form = {};

	let selected_skills: Skill[] = [];
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
	<h2 class="text-2xl mb-8">Create new projects</h2>
	<form
		method="POST"
		action="?/create_project"
		enctype="multipart/form-data"
		class="space-y-4 flex flex-col w-[50%]"
	>
		<Input type="text" name="name" placeholder="Name" />
		<Textarea name="description" placeholder="Description" />
		<Input type="link" name="link" placeholder="Link" />
		<Input type="date" name="dateOfCreation" placeholder="dateOfCreation" />

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

		<Button class="w-full bg-black text-white" type="submit">Create</Button>
	</form>
</div>
