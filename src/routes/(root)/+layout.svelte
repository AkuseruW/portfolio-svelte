<script lang="ts">
	import Header from '@/lib/components/Header.svelte';
	import LinkHeader from '@/lib/components/LinkHeader.svelte';
	import type { Config } from '@sveltejs/adapter-vercel';

	export const config: Config = {
		runtime: 'nodejs18.x'
	};
</script>

<div class="app min-h-full">
	<div class="hidden lg:block md:block top-0 left-6 items-center">
		<span class="border h-[150px] ml-4 w-1 bg-[#1F2D5C] absolute"></span>
		<ul class="flex flex-col gap-6 mt-8 p-1 absolute ml-1 top-32">
			<li><LinkHeader link="https://github.com/AkuseruW" target="_blank" icon="Github" /></li>
			<li><LinkHeader link="mailto:wolfs.axelw@gmail.com" icon="Mail" /></li>
			<li><LinkHeader link="/#exp" icon="Linkedin" /></li>
		</ul>
	</div>

	<div class="container mx-auto h-full">
		<div class="w-full hidden lg:block md:block">
			<Header />
		</div>
		<main>
			<slot />
		</main>
	</div>

	<footer class="h-16 mt-16 flex flex-col justify-center items-center container mx-auto ">
		<hr class="w-full border h-[3px] bg-[#1F2D5C]" />
		<p class="mt-2">© 2023 - {new Date().getFullYear()} Axel Wolfs</p>
	</footer>
</div>

<style>
	.container {
		max-width: 1200px;
		margin: 0 auto;
	}
</style>
