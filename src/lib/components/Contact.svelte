<script lang="ts">
	import { Github, Mail, Linkedin } from 'lucide-svelte';
	const text = 'Contact';
	const lines = text.split('\n');
	let returnedText: string[][] = [];

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
</div>
<div class="flex mt-16 space-x-5 justify-center">
	<ul class="flex flex-col gap-8">
		<li>
			<a href="https://github.com/AkuseruW" target="_blank" class="flex space-x-5 hover:underline"
				><Github /> <span>Akuseru_W</span></a
			>
		</li>
		<li>
			<a href="mailto:wolfs.axelw@gmail.com" class="flex space-x-5 hover:underline"
				><Mail /> <span>wolfs.axelw@gmail.com</span></a
			>
		</li>
		<li><a href="https://www.linkedin.com/in/wolfs-axel" class="flex space-x-5 hover:underline" target="_blank"><Linkedin /> <span>Wolfs Axel</span> </a></li>
	</ul>
</div>
