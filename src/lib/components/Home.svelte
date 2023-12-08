<script lang="ts">
	const text = "Hi, there \nI'm Wolfs Axel";
	const lines = text.split('\n');
	let returnedText: string[][] = [];

	returnedText = lines.map((line) =>
		Array.from(line).map((letter) =>
            `<span class="inline-block zoom-animation">${letter}</span>`
		)
	);

</script>

<h1 class="text-5xl lg:text-5xl font-bold leading-tight">
	{@html returnedText.map((line) => line.join('')).join('<br />')}
</h1>
<p class="text-sm lg:text-lg">Front End Developer / Back End Developer</p>
