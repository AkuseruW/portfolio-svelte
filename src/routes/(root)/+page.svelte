<script>
	export let data;
	import Home from '$lib/components/Home.svelte';
	import Experience from '$lib/components/Experience.svelte';
	import TimeLine from '$lib/components/TimeLine.svelte';
	import Skills from '$lib/components/Skills.svelte';
	import Projects from '$lib/components/Projects.svelte';
	import dots from '$lib/images/Dots.svg';
	import Contact from '@/lib/components/Contact.svelte';
</script>

<svelte:head>
	<title>Wolfs Axel</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section id="top" class="flex flex-col-reverse lg:flex-row items-center h-[90vh] lg:h-screen md:h-screen">
	<div class="w-full h-2/5 lg:w-3/5 lg:h-full md:w-3/5 pt-10 lg:p-0 lg:flex lg:items-center">
		<div class="lg:space-y-4 md:space-y-4 items-center flex flex-col">
			<Home />
		</div>
	</div>
	<div class="w-full lg:w-2/5 md:w-2/5 lg:h-full  flex items-center justify-center lg:justify-end md:justify-end">
		<img
			src="/images/40758068.png"
			alt="profile"
			class="rounded-full relative w-[200px] h-[200px] lg:w-[300px] lg:h-[300px] md:w-[300px] md:h-[300px]"
		/>
		<img src={dots} alt="dots" class="absolute lg:top-[450px]" />
	</div>
</section>

<section id="exp" class="min-h-screen flex flex-col items-start relative">
	<Experience />
	<TimeLine experiences={data.experiences} />
</section>

<section id="skills" class="mt-20 min-h-[60vh]">
	<Skills skills={data.skills} />
</section>

<section id="projects" class="min-h-screen relative">
	<Projects projects={data.projects} />
</section>

<section id="contact" class="h-[40vh]">
	<Contact />
</section>
