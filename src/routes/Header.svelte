<script>
	import { page } from '$app/stores';
</script>

<header class="relative">
	<nav class="absolute top-0 right-0">
		<ul class="flex gap-8">
			<li aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
				<a href="#home"><span> # </span> Home</a>
			</li>
			<li aria-current={$page.url.pathname === '/about' ? 'page' : undefined}>
				<a href="/about"><span> # </span> Experience</a>
			</li>
			<li aria-current={$page.url.pathname.startsWith('/sverdle') ? 'page' : undefined}>
				<a href="/sverdle"><span> # </span> Skills</a>
			</li>
			<li aria-current={$page.url.pathname.startsWith('/sverdle') ? 'page' : undefined}>
				<a href="/sverdle"><span> # </span> Projects</a>
			</li>
		</ul>
	</nav>
</header>