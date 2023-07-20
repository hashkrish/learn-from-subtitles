<script>
	export let token = {};
	export let subtitleLanguage = 'en';
	let japanese = subtitleLanguage === 'ja' ? 'text-3xl' : '';
</script>

<span class="grid-columns-1 grid place-content-center">
	{#if subtitleLanguage === 'ja'}
		<span>
			{#if token.pronounciation !== token.token}
				<span class="text-xs text-gray-500">
					{token.pronounciation}
				</span>
			{:else}
				<span class="text-xs text-gray-500">&nbsp;</span>
			{/if}
		</span>
	{/if}
	<span class={japanese}>
		{token?.token?.replaceAll('（', '(').replaceAll('）', ')')}
	</span>
</span>
