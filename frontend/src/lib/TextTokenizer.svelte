<script>
	import { onMount } from 'svelte';
	import { APIURL } from '../config';
	let processedText = [];
	let text = '私は日本語を勉強しています。';

	const processText = () => {
		axios
			.post(`${APIURL}/subtitle/process/text`, {
				text: text
			})
			.then((response) => {
				// console.log(response);
				processedText = response.data.processed_content;
				// debugText = JSON.stringify(response.data.processed_content);
			})
			.catch((error) => {
				console.log(error);
			});
	};
	onMount(() => {
		processedText;
	});
</script>

<div class="m-4 p-2">
	<div class="place-content-center">
		<textarea name="text" class="m-2 rounded border-2" bind:value={text} rows="3" cols="50" />
		<button class="rounded-full" on:click={processText}>Parse</button>
	</div>

	<div class="flex place-content-center">
		{#each processedText as item}
			<span class="m-2 grid grid-cols-1 place-content-center">
				{#if item.token !== item.pronounciation}
					<small class="grid place-content-center">{item.pronounciation}</small>
				{:else}
					<small class="grid place-content-center">&nbsp;</small>
				{/if}
				<span class="grid place-content-center">{item.token}</span>
			</span>
		{/each}
	</div>
</div>
