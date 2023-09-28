<script lang="ts">
	import { onMount } from 'svelte';
	import { subtitleStore } from '$stores/subtitles';
	import { cardStore } from '$stores/card';
	import { localCache, clearLocalCache } from '$stores/cache';
	import Token from '$lib/Token.svelte';
	import { getIgnoreTokens } from '$utils/frequency';
	import { debounce } from 'lodash';
	import { getWordTranslation } from '$utils/api';

	// export let subtitles = [];
	export let subtitleLanguage = 'en';
	export let currentSubtitleIndex = 0;
	let debouncedAPICall;
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
	let ignoreTokens = getIgnoreTokens() || new Set();
	const myIgnoreTokens = new Set([
		'だ',
		'です',
		'ます',
		'て',
		'に',
		'を',
		'は',
		'が',
		'と',
		'の',
		'で',
		'た',
		'し',
		'ない',
		'も',
		'な',
		'い',
		'か',
		'よ',
		'ね',
		'ぞ',
		'ぜ',
		'ら',
		'ん',
		'あ',
		'え',
		'(',
		')',
		'（',
		'）',
		'１',
		'２',
		'３',
		'４',
		'５',
		'６',
		'７',
		'８',
		'９',
		'０',
		'“',
		'”',
		'))'
	]);
	let hideParticles = true;

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

		if (localStorage.getItem('hideParticles') === 'false') {
			hideParticles = false;
		}
		if (hideParticles) {
			for (const token of myIgnoreTokens) {
				ignoreTokens.add(token);
			}
		}
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

	let subtitle = { content: [{ token: '', pronounciation: '' }], start: 0, end: 0 };

	$: subtitle = $subtitleStore[currentSubtitleIndex] || { content: '', start: 0, end: 0 };
	$: currentSubtitleIndex = $cardStore.currentSubtitleIndex;
</script>

<div
	class="m-4 p-4 text-center bg-white border border-gray-200 rounded-lg shadow sm:p-8 dark:bg-gray-800 dark:border-gray-700 min-w-100"
>
	<div class="m-5 p-5 grid lg:grid-cols-2 gap-4">
		{#each subtitle.content as token}
			{#if !ignoreTokens.has(token.token)}
				<div
					class="grid grid-cols-2 place-items-center items-center rounded-lg border border-gray-200"
				>
					{#if token.token in $localCache}
						<Token {token} {subtitleLanguage} />
						<span class="place-self-start align-text-bottom">
							{$localCache[token.token]}
						</span>
					{:else}
						<Token {token} {subtitleLanguage} />
						<span class="place-self-start align-text-bottom">
							{#await getWordTranslation(token.token)}
								Loading...
							{:then response}
								{#if response.length > 0}
									<!-- {response[0].meaning.replaceAll(':', ', ')} -->

									{(response.reduce((acc, curr) => {
										if (curr?.meaning) {
											return acc + '\n' + curr.meaning.replaceAll(':', ', ').trim();
										} else {
											return acc;
										}
									}),
									'')}
								{:else}
									Not found
								{/if}
							{:catch error}
								{error}
							{/await}
						</span>
					{/if}
				</div>
			{/if}
		{/each}
	</div>
	<button
		class="btn border-gray-200 bg-gray-200 rounded-lg p-2 m-2"
		on:click={() => {
			hideParticles = !hideParticles;
			localStorage.setItem('hideParticles', JSON.stringify(hideParticles));
		}}
	>
		{hideParticles ? 'Show' : 'Hide'} particles and common characters
	</button>
</div>
