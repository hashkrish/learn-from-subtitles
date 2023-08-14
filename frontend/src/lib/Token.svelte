<script>
	import { localCache } from '$src/stores/cache';
	import { convertToFullWidth } from '$utils/lang_jp';
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	export let token = {};
	export let subtitleLanguage = 'en';
	let japanese = '';
	$: japanese = subtitleLanguage === 'ja' ? 'text-3xl' : '';
</script>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<span
	class="grid-columns-1 grid place-content-center"
	on:mouseenter={() => {
		if (token) {
			$localCache.currentToken = token;
		}
	}}
>
	{#if subtitleLanguage === 'ja'}
		<span>
			{#if token.pronounciation !== token.token}
				<span class="text-xs text-gray-500 select-none">
					{token.pronounciation}
				</span>
			{:else}
				<span class="text-xs text-gray-500 select-none">&nbsp;</span>
			{/if}
		</span>
	{/if}
	<span class={japanese}>
		{convertToFullWidth(token?.token)?.replaceAll('（', '(').replaceAll('）', ')')}
	</span>
</span>
