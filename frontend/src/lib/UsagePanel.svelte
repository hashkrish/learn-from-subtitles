<script lang="ts">
	import { onMount } from 'svelte';
	import { subtitleStore } from '$stores/subtitles';
	import Token from './Token.svelte';
	import { getFrequency, getOrderedTokensByFrequency } from '$utils/frequency';

	$: orderedWordsByFrequency = getOrderedTokensByFrequency(getFrequency($subtitleStore));

	let orderedWordsByFrequency = [];
	let showFrequency = false;
	onMount(() => {
		// console.clear();
		// console.log('s:', subtitleToTokens($subtitleStore[4]));
		// console.log('ss:', subtitlesToTokens($subtitleStore));
		orderedWordsByFrequency = getOrderedTokensByFrequency(getFrequency($subtitleStore));
		// console.log('ow:', orderedWordsByFrequency);
		console.log('Loaded UsagePanel');
	});
</script>

<div class="flex justify-center">
	<button
		on:click={() => {
			showFrequency = !showFrequency;
			// console.log(showFrequency);
		}}
		class="btn-primary m-4 p-2 rounded"
	>
		{showFrequency ? 'Hide' : 'Show'} Frequency
	</button>
</div>

{#if showFrequency}
	<div class="m-4 p-2">
		<div class="flex flex-wrap">
			{#each orderedWordsByFrequency as item}
				<!-- {JSON.stringify(item)} -->
				<div class="flex m-4 p-2">
					<Token token={item} subtitleLanguage="ja" />
					<!-- <span>{item?.text} </span> -->
					<span><small class="bg-sky-100 p-2 rounded-lg">{item?.frequency}</small></span>
				</div>
			{/each}
		</div>
	</div>
{/if}
