<script lang="ts">
    import * as icons from 'lucide-svelte';
    export let icon: string;
    export let link: string;
    export let target: string = '';
</script>

<div>
    <a href={link} target={target}>
        
        <!-- <svelte:component this="{icons[icon]}" /> -->
    </a>
</div>