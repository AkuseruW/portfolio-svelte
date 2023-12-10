<script lang="ts">
	import type { Project } from '$lib/types/projects';
	export let projects: Project[] = [];
	const text = 'Projects';
	const lines = text.split('\n');
	let returnedText: string[][] = [];

	returnedText = lines.map((line) =>
		Array.from(line).map((letter) => `<span class="inline-block zoom-animation">${letter}</span>`)
	);
</script>

<div class="flex items-center lg:top-36 w-full mt-2">
	<h2 class="text-xl lg:text-3xl font-bold leading-tight">
		<span>#</span>
		{@html returnedText.map((line) => line.join(''))}
	</h2>
	<hr class="w-[700px] border h-[2px] bg-[#1F2D5C] ml-9" />
	<a href="/#proj" class="absolute right-0">View all ~~></a>
</div>

{#each projects as project}
	<div class="mb-8 ml-8 flex justify-between items-center w-full">
		<div class="py-2 flex items-center justify-center">
			<!-- <img src={project.icones} alt={project.name} width={50} height={50} /> -->
			<!-- <span class="text-sm md:text-base lg:text-lg">{project.name}</span> -->
		</div>
	</div>
{/each}
