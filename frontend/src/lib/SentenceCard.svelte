<script lang="ts">
	import { onMount } from 'svelte';
	import { subtitleStore } from '$stores/subtitles';
	import { cardStore } from '$stores/card';
	import Token from '$lib/Token.svelte';
	import { secondsToTimestamp } from '../utils/time';
	import { localCache } from '$src/stores/cache';
	import { getWordTranslation } from '$utils/api';
	import { textToSpeech } from '$utils/tts';

	// export let subtitles = [];
	export let subtitleLanguage = 'en';
	export let currentSubtitleIndex = 0;
	const incrementCurrentSubtitleIndex = () => {
		currentSubtitleIndex = parseInt(currentSubtitleIndex);
		if (currentSubtitleIndex >= $subtitleStore.length - 1) {
			return;
		}
		currentSubtitleIndex += 1;
		localStorage.setItem('last_subtitle_index', currentSubtitleIndex);
	};
	const decrementCurrentSubtitleIndex = () => {
		currentSubtitleIndex = parseInt(currentSubtitleIndex);
		if (currentSubtitleIndex <= 0) {
			return;
		}
		currentSubtitleIndex -= 1;
		localStorage.setItem('last_subtitle_index', currentSubtitleIndex);
	};
	onMount(() => {
		const last_subtitles = localStorage.getItem('last_subtitles');
		const last_subtitle_language = localStorage.getItem('last_subtitle_language');
		const last_subtitle_title = localStorage.getItem('last_subtitle_title');
		const last_subtitle_index_ = parseInt(localStorage.getItem('last_subtitle_index'));
		const last_subtitle_index =
			last_subtitle_index_ && last_subtitle_index_ > 0
				? localStorage.getItem('last_subtitle_index')
				: 0;
		if (last_subtitles) {
			$subtitleStore = JSON.parse(last_subtitles);
		}
		currentSubtitleIndex = last_subtitle_index > 0 ? last_subtitle_index : 0;

		// add event listener for right arrow
		window.addEventListener('keydown', (event) => {
			if (event.key === 'ArrowRight') {
				incrementCurrentSubtitleIndex();
			}
		});

		// add event listener for left arrow
		window.addEventListener('keydown', (event) => {
			if (event.key === 'ArrowLeft') {
				decrementCurrentSubtitleIndex();
			}
		});
	});

	let subtitle = { content: '', start: 0, end: 0 };
	let translationText = JSON.stringify($subtitleStore[currentSubtitleIndex]?.content[0].token);
	$: subtitle = $subtitleStore[currentSubtitleIndex] || { content: '', start: 0, end: 0 };
	$: $cardStore.currentSubtitleIndex = currentSubtitleIndex;
</script>

<div
	class="m-4 p-4 text-center bg-white border border-gray-200 rounded-lg shadow sm:p-8 dark:bg-gray-800 dark:border-gray-700 min-w-100"
>
	<div
		class="items-center justify-center mb-2 text-3xl text-gray-900 dark:text-white my-2 flex flex-wrap align-middle place-content-around"
	>
		<button
			class="flex-grow place-self-stretch justify-items-stretch text-left"
			on:click={decrementCurrentSubtitleIndex}
		>
			&nbsp;〈 &nbsp;
		</button>
		{#each subtitle.content as token}
			<Token {token} {subtitleLanguage} />
		{:else}
			<span> Upload a subtitle file to get started. </span>
		{/each}
		<button
			class="flex-grow place-self-stretch justify-items-stretch text-right"
			on:click={incrementCurrentSubtitleIndex}
		>
			&nbsp; 〉&nbsp;
		</button>
	</div>
	<!-- <p class="mb-5 text-base text-gray-500 sm:text-lg dark:text-gray-400"> -->
	<!-- 	{JSON.stringify($subtitleStore[currentSubtitleIndex])} -->
	<!-- </p> -->
	<div class="items-center justify-center space-y-4 sm:flex sm:space-y-0 sm:space-x-4 my-4">
		<span class="text-gray-500 whitespace-nowrap">
			{secondsToTimestamp(subtitle.start || 0)} - {secondsToTimestamp(subtitle.end || 0)}
		</span>
		<input
			type="range"
			min="0"
			max={$subtitleStore.length - 1}
			bind:value={currentSubtitleIndex}
			class="w-full"
		/>
		<input
			type="number"
			min="0"
			max={$subtitleStore.length - 1}
			bind:value={currentSubtitleIndex}
			class="text-gray-500 bg-gray-100 border border-gray-200 rounded-lg shadow-sm dark:bg-gray-700 dark:border-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:ring-gray-700 dark:focus:border-gray-700 focus:ring-4 focus:outline-none text-center"
		/>
		<span>
			<button
				class="bg-gray-100 border border-gray-200 rounded-lg shadow-sm dark:bg-gray-700 dark:border-gray-700 dark:text-white dark:placeholder-gray-400 dark:focus:ring-gray-700 dark:focus:border-gray-700 focus:ring-4 focus:outline-none text-center"
				on:click={() => textToSpeech(subtitle.content.reduce((acc, curr) => acc + curr.token, ''))}
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					class="h-6 w-6 text-gray-500"
					viewBox="0 0 20 20"
					fill="currentColor"
				>
					<path d="M5 4v12h3v-5h4V9H8V4H5z" />
				</svg>
			</button>
		</span>
	</div>
	<span class="text-gray-700">
		{$localCache.currentToken?.token || ''}:
		{#await getWordTranslation($localCache?.currentToken?.token)}
			Loading...
		{:then translation}
			{#if translation[0]?.pronounciation}
				{'(' + translation[0].pronounciation + ')'}
			{/if}
			<!-- {translation.reduce((acc, curr) => acc + ', ' + curr.meaning.replaceAll(':', ', '), '')} -->
			{translation[0]?.meaning?.replaceAll(':', ', ')}
		{:catch error}
			Something went wrong
			{console.log(error)}
		{/await}
	</span>
</div>
