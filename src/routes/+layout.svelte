<script>
	import '../app.css';
	import LinkHeader from '@/lib/components/LinkHeader.svelte';
	import Header from './Header.svelte';
</script>

<div class="app min-h-full">
	<div class=" top-0 left-2">
		<span class="border h-[150px] ml-4 w-1 bg-[#1F2D5C] absolute"></span>
		<ul class="flex flex-col gap-2 max-w-[330px] mt-8 p-1 absolute top-32">
			<li><LinkHeader link="https://github.com/AkuseruW" target="_blank" icon="Github" /></li>
			<li><LinkHeader link="mailto:wolfs.axelw@gmail.com" icon="Mail" /></li>
			<li><LinkHeader link="/#exp" icon="Linkedin" /></li>
		</ul>
	</div>

	<div class="container mx-auto h-full relative">
		<div class="absolute w-full">
			<Header />
		</div>
		<main>
			<slot />
		</main>
	</div>

	<footer></footer>
</div>
