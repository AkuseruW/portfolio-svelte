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
	<h2 class="text-xl lg:text-3xl font-bold leading-tight">
		<span>#</span>
		{@html returnedText.map((line) => line.join(''))}
	</h2>
	<hr class="w-[700px] border h-[3px] bg-[#1F2D5C] ml-9" />
</div>

<div class="flex mt-16 justify-between">
	{#each skills as skill (skill.name)}
	<ul class="flex flex-col">
			<h4 class="text-lg md:text-xl lg:text-2xl">{skill.name}</h4>
			{#each skill.skills as skillinfo (skillinfo.id)}
				<li class="text-lg mt-4 flex gap-3">
					<img src={skillinfo.icones} alt={skillinfo.name} width={20} height={20} />
					<span class="text-sm md:text-base lg:text-lg">{skillinfo.name}</span>
				</li>
			{/each}
		</ul>
	{/each}
</div>
