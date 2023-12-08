<script lang="ts">
	import type { Experience } from '$lib/types/experiences';
	export let experiences: Experience[] = [];
</script>

<div class="relative flex flex-col lg:pt-6 h-full">
	<span class="absolute h-full border" style="border: 1px solid, borderRadius: 1% "></span>
	{#each experiences as experience (experience.id)}
		<div class="mb-8 ml-8 flex flex-col items-start w-full">
			<span class="mb-3 text-sm md:text-base lg:text-lg"
				>{experience.startTime} - {experience.endTime}</span
			>
			<h4 class="mb-3 text-base md:text-xl lg:text-2xl text-gradient font-bold">
				{experience.title}
			</h4>
			<p class="text-xs md:text-sm lg:text-base leading-snug">{experience.description}</p>
		</div>
	{/each}
</div>
