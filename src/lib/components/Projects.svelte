<script lang="ts">
	import type { Project } from '$lib/types/projects';
	import { Github } from 'lucide-svelte';
	export let projects: Project[] = [];
	const text = 'Projects';
	const lines = text.split('\n');
	let returnedText: string[][] = [];

	console.log(projects)

	console.log(projects);
	returnedText = lines.map((line) =>
		Array.from(line).map((letter) => `<span class="inline-block zoom-animation">${letter}</span>`)
	);
</script>

<div class="flex items-center lg:top-36 w-full mt-2">
	<h2 class="text-xl lg:text-3xl font-bold leading-tight">
		<span>#</span>
		{@html returnedText.map((line) => line.join(''))}
	</h2>
	<!-- <hr class="w-[600px] border h-[3px] bg-[#1F2D5C] ml-9 hidden lg:flex" /> -->
	<!-- <a href="/#proj" class="absolute right-0 hidden lg:flex">View all ~~></a> -->
</div>

<div class="flex flex-col lg:flex-row space-y-4 lg:space-y-0 lg:space-x-4 mt-16">
    {#each projects as project}
        <div class="flex flex-col justify-between p-4 border w-full lg:w-[350px] h-[250px]">
            <div class="h-[150px] lg:h-[200px] w-full lg:w-[350px] bg-cover bg-center mb-4 lg:mb-0" style={`background-image: url(${project.images[0].image});`}></div>
            <div class="flex justify-between">
                <h3 class="text-sm md:text-base lg:text-lg">{project.name}</h3>
				{#if project.link}
                	<a href="{project.link}"><Github /></a>
				{/if}
            </div>
            <p class="mt-3 text-sm md:text-base lg:text-lg">{project.description.slice(0, 100)} ...</p>
            <div class="flex mt-3">
                {#each project.skills as skill (skill.id)}
                    <img src="{skill.icones}" alt="{skill.name}" width="40" height="40" class="mr-2">
                {/each}
            </div>
        </div>
    {/each}
</div>