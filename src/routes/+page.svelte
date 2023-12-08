<script>
	export let data;
	import LinkHeader from '$lib/components/LinkHeader.svelte';
	import Home from '$lib/components/Home.svelte';
	import Experience from '$lib/components/Experience.svelte';
	import TimeLine from '$lib/components/TimeLine.svelte';
	import Skills from '$lib/components/Skills.svelte';
	import Projects from '$lib/components/Projects.svelte';
</script>

<svelte:head>
	<title>Wolfs Axel</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section id="top" class="flex items-center h-screen">
	<div class="w-3/5">
		<div class="space-y-4">
			<Home />
		</div>
	</div>
	<div class="w-2/5 h-full flex items-center">
		<img src="/images/40758068.png" alt="" height="400" width="400" class="rounded-full">
	</div>
</section>

<section id="exp" class="min-h-screen flex flex-col items-start">
	<Experience />
	<TimeLine experiences={data.experiences} />
</section>

<section id="skills" class="h-screen">
	<Skills skills={data.skills} />
</section>

<section id="projects" class="h-screen">
	<Projects projects={data.projects} />
</section>