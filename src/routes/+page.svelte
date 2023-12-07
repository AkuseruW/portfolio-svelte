<script>
	import { Github, Linkedin, Mail } from 'lucide-svelte';
	import LinkHeader from '$lib/components/LinkHeader.svelte';
	import Home from '$lib/components/Home.svelte';
	import Experience from '$lib/components/Experience.svelte';
	import TimeLine from '$lib/components/TimeLine.svelte';
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
		<div class="flex gap-16 max-w-[330px] mt-8 p-1">
			<LinkHeader link="https://github.com/AkuseruW" target="_blank" icon="Github" />
			<LinkHeader link="mailto:wolfs.axelw@gmail.com" icon="Mail" />
			<LinkHeader link="/#exp" icon="Linkedin" />
		</div>
	</div>
	<div class="w-2/5 h-full">
		<!-- <CanvasSection /> -->		
	</div>
</section>
<section id='exp' class="min-h-screen flex flex-col items-start max-w-[40%]">
	<Experience />
	<TimeLine />
</section>
