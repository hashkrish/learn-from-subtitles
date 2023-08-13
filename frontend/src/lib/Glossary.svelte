<script lang="ts">
	import { onMount } from 'svelte';
	import { subtitleStore } from '$stores/subtitles';
	import { cardStore } from '$stores/card';
	import Token from '$lib/Token.svelte';
	import { secondsToTimestamp } from '../utils/time';
	import { writable } from 'svelte/store';
	import { APIURL } from '$config';
	import axios from 'axios';

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

	async function getWordTranslation(word, from, to) {
		from = from || 'ja';
		to = to || 'en';
		const url = `${APIURL}/translate/${from}/${to}?word=${word}`;
		const response = await axios.get(url);
		if (response.status === 200) {
			return response.data;
		} else {
			return null;
		}
	}

	let subtitle = { content: { token: '', pronounciation: '' }, start: 0, end: 0 };
	let meaning = {};

	$: subtitle = $subtitleStore[currentSubtitleIndex] || { content: '', start: 0, end: 0 };
	$: currentSubtitleIndex = $cardStore.currentSubtitleIndex;
</script>

<div
	class="m-4 p-4 text-center bg-white border border-gray-200 rounded-lg shadow sm:p-8 dark:bg-gray-800 dark:border-gray-700 min-w-100"
>
	<div class="m-5 p-5 grid lg:grid-cols-2 gap-4">
		{#each subtitle.content as token}
			<div
				class="grid grid-cols-2 place-items-center items-center rounded-lg border border-gray-200"
			>
				<Token {token} {subtitleLanguage} />
				<span class="place-self-start align-text-bottom">
					{#await getWordTranslation(token.token)}
						Loading...
					{:then response}
						{#if response.length > 0}
							{response[0].meaning.replaceAll(':', ', ')}
						{:else}
							Not found
						{/if}
					{:catch error}
						{error}
					{/await}
					<!-- {getWordTranslation(token.token)} -->
				</span>
			</div>
		{/each}
	</div>
</div>
