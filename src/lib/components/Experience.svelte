<script lang="ts">
	const text = 'Experiences';
	const lines = text.split('\n');
	let returnedText: string[][] = [];

	returnedText = lines.map((line) =>
		Array.from(line).map((letter) => `<span class="inline-block zoom-animation">${letter}</span>`)
	);
</script>

<div class="flex flex-col lg:top-36 mt-2">
	<h1 class="text-5xl lg:text-5xl font-bold leading-tight">
		{@html returnedText.map((line) => line.join('')).join('<br />')}
	</h1>
</div>
