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

<h2 class="text-5xl lg:text-5xl font-bold leading-tight">
	{@html returnedText.map((line) => line.join(''))}
</h2>
{#each skills as skill}
	<div class="mb-8 ml-8 flex justify-between items-center w-full">
		<div class="py-2 flex items-center justify-center">
			<img src={skill.icones} alt={skill.name} width={50} height={50} />
			<span class="text-sm md:text-base lg:text-lg">{skill.name}</span>
		</div>
	</div>
{/each}
