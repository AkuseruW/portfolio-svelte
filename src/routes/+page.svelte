<script>
	export let data;
	import Home from '$lib/components/Home.svelte';
	import Experience from '$lib/components/Experience.svelte';
	import TimeLine from '$lib/components/TimeLine.svelte';
	import Skills from '$lib/components/Skills.svelte';
	import Projects from '$lib/components/Projects.svelte';
	import dots from '$lib/images/Dots.svg';
</script>

<svelte:head>
	<title>Wolfs Axel</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section id="top" class="flex items-center h-screen">
	<div class="w-4/5">
		<div class="space-y-4">
			<Home />
		</div>
	</div>
	<div class="w-1/5 h-full flex items-center">
		<img
			src="/images/40758068.png"
			alt="profile"
			height="400"
			width="400"
			class="rounded-full relative"
		/>
		<img src={dots} alt="dots" class="absolute top-[450px]" />
	</div>
</section>

<section id="exp" class="min-h-screen flex flex-col items-start relative">
	<Experience />
	<TimeLine experiences={data.experiences} />
</section>

<section id="skills" class="mt-20 min-h-[60vh]">
	<Skills skills={data.skills} />
</section>

<section id="projects" class="h-screen relative">
	<!-- <Projects projects={data.projects} /> -->
</section>
