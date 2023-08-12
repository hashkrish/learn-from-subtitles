<script lang="ts">
	import { onMount } from 'svelte';
	import { subtitleStore } from '../store/subtitles';
	import Token from '$lib/Token.svelte';
	import { secondsToTimestamp } from '../utils/time';

	// export let subtitles = [];
	export let subtitleLanguage = 'en';
	export let currentSubtitleIndex = 0;

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
			console.log($subtitleStore);
		}
		currentSubtitleIndex = last_subtitle_index > 0 ? last_subtitle_index : 0;
	});

	let subtitle = { content: '', start: 0, end: 0 };
	$: subtitle = $subtitleStore[currentSubtitleIndex] || { content: '', start: 0, end: 0 };
</script>

<div
	class="min-w-md-100 w-full p-4 text-center bg-white border border-gray-200 rounded-lg shadow sm:p-8 dark:bg-gray-800 dark:border-gray-700 min-w-100"
>
	<span class="text-xs text-gray-500">
		{secondsToTimestamp(subtitle.start || 0)} - {secondsToTimestamp(subtitle.end || 0)}
	</span>
	<div
		class="items-center justify-center mb-2 text-3xl text-gray-900 dark:text-white my-2 flex flex-wrap align-middle"
	>
		{#each subtitle.content as token}
			<Token {token} {subtitleLanguage} />
		{:else}
			<span> Upload a subtitle file to get started. </span>
		{/each}
	</div>
	<!-- <p class="mb-5 text-base text-gray-500 sm:text-lg dark:text-gray-400"> -->
	<!-- 	{JSON.stringify($subtitleStore[currentSubtitleIndex])} -->
	<!-- </p> -->
	<div class="items-center justify-center space-y-4 sm:flex sm:space-y-0 sm:space-x-4">
		<button
			class="my-2 w-full sm:w-auto bg-gray-800 hover:bg-gray-700 focus:ring-4 focus:outline-none focus:ring-gray-300 text-white rounded-lg inline-flex items-center justify-center px-4 py-2.5 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700"
			on:click={() => {
				if (currentSubtitleIndex <= 0) {
					return;
				}
				currentSubtitleIndex = parseInt(currentSubtitleIndex) - 1;
				localStorage.setItem('last_subtitle_index', currentSubtitleIndex || 0);
			}}
		>
			Previous
		</button>
		<button
			class="my-2 w-full sm:w-auto bg-gray-800 hover:bg-gray-700 focus:ring-4 focus:outline-none focus:ring-gray-300 text-white rounded-lg inline-flex items-center justify-center px-4 py-2.5 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700"
			on:click={() => {
				if (currentSubtitleIndex >= $subtitleStore.length - 1) {
					return;
				}
				currentSubtitleIndex = parseInt(currentSubtitleIndex) + 1;
				localStorage.setItem('last_subtitle_index', currentSubtitleIndex || 0);
			}}
		>
			Next
		</button>
	</div>
</div>
