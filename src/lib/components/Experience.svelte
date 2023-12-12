<script lang="ts">
	const text = 'Experiences';
	const lines = text.split('\n');
	let returnedText: string[][] = [];

	returnedText = lines.map((line) =>
		Array.from(line).map((letter) => `<span class="inline-block zoom-animation">${letter}</span>`)
	);
</script>

<div class="flex items-center lg:top-36 w-full mt-2 ">
	<h2 class="text-xl lg:text-3xl font-bold leading-tight">
		<span>#</span>
		{@html returnedText.map((line) => line.join(''))}
	</h2>
	<!-- <hr class="w-[600px] border h-[3px] bg-[#1F2D5C] ml-9 hidden lg:flex" /> -->
	<!-- <a href="/#exp" class="absolute right-0 hidden lg:flex">View all ~~></a> -->
</div>
