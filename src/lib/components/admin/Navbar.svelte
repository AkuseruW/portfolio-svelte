<script lang="ts">
	import { cn } from '$lib/utils';

	let className: string | undefined | null = undefined;
	export { className as class };
</script>

<nav class={cn('flex items-center space-x-4 lg:space-x-6', className)}>
	<a href="/admin" class="text-sm font-medium transition-colors hover:text-primary"> Overview </a>

	<a
		href="/admin/skills"
		class="text-sm font-medium text-muted-foreground transition-colors hover:text-primary"
	>
		Skills
	</a>
	<a
		href="/admin/projects"
		class="text-sm font-medium text-muted-foreground transition-colors hover:text-primary"
	>
		Projects
	</a>
	<a
		href="/admin/categories"
		class="text-sm font-medium text-muted-foreground transition-colors hover:text-primary"
	>
		categories
	</a>
	<a
		href="/admin/settings"
		class="text-sm font-medium text-muted-foreground transition-colors hover:text-primary"
	>
		Settings
	</a>
</nav>
