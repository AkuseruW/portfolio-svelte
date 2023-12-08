<!-- skillsTable.svelte -->
<script lang="ts">
	import type { Skills } from '$lib/types/skills';

	export let skills: Skills[] = [];
	const text = 'Skills';
	const lines = text.split('\n');
	let returnedText: string[][] = [];

	returnedText = lines.map((line) =>
		Array.from(line).map((letter) => `<span class="inline-block zoom-animation">${letter}</span>`)
	);
</script>

<div class="flex items-center lg:top-36 mt-2">
	<h2 class="text-5xl lg:text-5xl font-bold leading-tight">
		{@html returnedText.map((line) => line.join(''))}
	</h2>
	<hr class="w-[500px] border h-1 bg-[#1F2D5C]">
</div>

<div class="flex lg:top-36 mt-2 space-x-3">
	{#each skills as skill (skill.name)}
		<table class="border-2 border-solid border-[#1F2D5C]">
			<tr class="text-2xl font-bold border-solid border-2 border-[#1F2D5C]">
				<th>{skill.name}</th>
			</tr>
			<tr class="py-2 flex flex-col items-center justify-center">
				{#each skill.skills as skillinfo (skillinfo.id)}
					<td class="flex items-center gap-2 text-lg w-full">
						<img src={skillinfo.icones} alt={skillinfo.name} width={20} height={20} />
						<span class="text-sm md:text-base lg:text-lg">{skillinfo.name}</span>
					</td>
				{/each}
			</tr>
		</table>
	{/each}
</div>
