<script lang="ts">
	import { onMount } from 'svelte';
	import { subtitleStore } from '../store/subtitles';
	import Token from './Token.svelte';
	import Subtitle from './Subtitle.svelte';

	const ignoreTokens = new Set([
		'!?',
		'(',
		')',
		'?',
		'…',
		'→',
		'《',
		'》',
		'！',
		'？',
		'～',
		'～！',
		'｡',
		'の'
	]);

	const subtitleToTokens = (subtitle) => {
		const tokens = subtitle.content.reduce((acc, cur) => {
			if (ignoreTokens.has(cur.token)) {
				return acc;
			}
			acc.push(cur);
			return acc;
		}, []);
		return tokens;
	};

	const subtitlesToTokens = (subtitles) => {
		const tokens = subtitles.reduce((acc, cur) => {
			acc.push(...subtitleToTokens(cur));
			return acc;
		}, []);
		return tokens;
	};

	const getFrequency = () => {
		frequency = subtitlesToTokens($subtitleStore).reduce((acc, cur) => {
			acc[cur?.token] = acc[cur?.token] || cur;
			acc[cur?.token].frequency = (acc[cur?.token].frequency || 0) + 1;
			// console.log(acc[cur?.token]);
			return acc;
		}, {});
		// console.log(frequency);
		return frequency;
	};

	const getOrderedTokensByFrequency = (frequency) => {
		orderedWordsByFrequency = Object.keys(frequency)
			.sort((a, b) => frequency[b].frequency - frequency[a].frequency)
			.map((key) => frequency[key]);
		// console.log('gow:', orderedWordsByFrequency);
		return orderedWordsByFrequency;
	};

	$: orderedWordsByFrequency = getOrderedTokensByFrequency(getFrequency());

	let frequency = {};
	let orderedWordsByFrequency = [];
	onMount(() => {
		// console.clear();
		// console.log('s:', subtitleToTokens($subtitleStore[4]));
		// console.log('ss:', subtitlesToTokens($subtitleStore));
		orderedWordsByFrequency = getOrderedTokensByFrequency(getFrequency($subtitleStore));
		// console.log('ow:', orderedWordsByFrequency);
	});
</script>

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
