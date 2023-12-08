<script lang="ts">
	import { Github, Mail, Linkedin } from 'lucide-svelte';
	const iconComponents = { Github, Mail, Linkedin };

	export let icon: keyof typeof iconComponents;
	export let link: string;
	export let target: string = '';

	let IconComponent: any;
	IconComponent = iconComponents[icon] || null;
</script>

<div>
	<a href={link} {target}>
		<svelte:component this={IconComponent} />
	</a>
</div>
