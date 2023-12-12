<script>
	import { Button } from "@/lib/components/ui/button";
	import { Input } from "@/lib/components/ui/input";


</script>

<svelte:head>
	<title>Wolfs Axel</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<form action="?/login" method="POST" class="flex flex-col space-y-4">
	<label for="email">Email</label>
	<Input type="email" name="email" placeholder="Email" />

	<label for="password">Password</label>
	<Input type="password" name="password" placeholder="Password" />

	<Button variant="outline" type="submit">Connexion</Button>
</form>