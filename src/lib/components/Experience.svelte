<script lang="ts">
	const text = 'Experiences';
	const lines = text.split('\n');
	let returnedText: string[][] = [];

	returnedText = lines.map((line) =>
		Array.from(line).map((letter) => `<span class="inline-block zoom-animation">${letter}</span>`)
	);
</script>

<div class="flex items-center lg:top-36 mt-2 justify-between">
	<h2 class="text-xl lg:text-3xl font-bold leading-tight">
		<span>#</span> {@html returnedText.map((line) => line.join(''))}
	</h2>
	<hr class="w-[700px] border h-1 bg-[#1F2D5C]">
	<span class="">View all ~~></span>
</div>
