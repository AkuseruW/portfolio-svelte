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

<h2 class="text-4xl leading-normal md:leading-relaxed mb-2 text-gradient font-bold">
    {@html returnedText.map((line) => line.join(''))}
</h2>

{#each projects as project}
    <div class="mb-8 ml-8 flex justify-between items-center w-full">
        <div class="py-2 flex items-center justify-center">
            <!-- <img src={project.icones} alt={project.name} width={50} height={50} /> -->
            <!-- <span class="text-sm md:text-base lg:text-lg">{project.name}</span> -->
        </div>
    </div>
{/each}