<script>
	import { createEventDispatcher } from 'svelte';
	import { onMount } from 'svelte';

	const dispatch = createEventDispatcher();

	export let subtitleLanguage = 'en';

	onMount(() => {
		const last_subtitle_language = localStorage.getItem('last_subtitle_language');
		if (last_subtitle_language) {
			subtitleLanguage = last_subtitle_language;
			dispatch('subtitleLanguageChange', subtitleLanguage);
		}
	});

	function onSubtitleLanguageChange(event) {
		subtitleLanguage = event.target.value;
		localStorage.setItem('last_subtitle_language', subtitleLanguage);
		dispatch('subtitleLanguageChange', subtitleLanguage);
	}
</script>

<select
	class="m-4 rounded border p-2"
	on:change={onSubtitleLanguageChange}
	bind:value={subtitleLanguage}
>
	<option value="en">English</option>
	<option value="ja">Japanese</option>
</select>
