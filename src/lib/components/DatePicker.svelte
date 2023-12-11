<script lang="ts">
    import { Calendar } from '$lib/components/ui/calendar';
    import * as Popover from '$lib/components/ui/popover';
    import { type DateValue, DateFormatter, getLocalTimeZone } from '@internationalized/date';
    import { createEventDispatcher } from 'svelte';
	import Button from './ui/button/button.svelte';
	import { cn } from '../utils';
  
    const df = new DateFormatter('en-US', {
      dateStyle: 'long'
    });
  
    let value: DateValue | undefined = undefined;
    const dispatch = createEventDispatcher();
  
    const handleDateSelect = () => {
      dispatch('dateSelected', value);
    };
  </script>
  
  <Popover.Root>
    <Popover.Trigger asChild let:builder>
      <Button
        variant="outline"
        on:click={handleDateSelect}
        class={cn('w-[280px] justify-start text-left font-normal', !value && 'text-muted-foreground')}
        builders={[builder]}
      >
        {#if value}
          {df.format(value.toDate(getLocalTimeZone()))}
        {:else}
          Pick a date
        {/if}
      </Button>
    </Popover.Trigger>
    <Popover.Content class="w-auto p-0 bg-white">
      <Calendar bind:value initialFocus />
    </Popover.Content>
  </Popover.Root>
  