<script lang="ts">
	import type { Category, Skill } from '$lib/types/skills';

	export let skills: Category[] = [];
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
	<!-- <hr class="w-[600px] border h-[3px] bg-[#1F2D5C] ml-9 hidden lg:flex" /> -->
</div>

<div class="flex flex-col mt-16 md:flex-row md:justify-between">
	{#each skills as skill (skill.name)}
		<ul class="flex flex-col md:w-1/2 lg:w-1/3 mb-8">
			<h4 class="text-lg md:text-xl lg:text-2xl">{skill.name}</h4>
			{#each skill.skills as skillinfo (skillinfo.id)}
				<li class="text-lg mt-4 flex items-center gap-3">
					<img
						src={skillinfo.icones}
						alt={skillinfo.name}
						width={20}
						height={20}
						class="md:w-6 md:h-6 lg:w-8 lg:h-8"
					/>
					<span class="text-sm md:text-base lg:text-lg">{skillinfo.name}</span>
				</li>
			{/each}
		</ul>
	{/each}
</div>
