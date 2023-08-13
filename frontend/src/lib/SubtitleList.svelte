<script>
	import { onMount } from 'svelte';
	import Subtitle from './Subtitle.svelte';
	import { subtitleStore } from '$stores/subtitles';

	export let subtitles = [];
	export let subtitleLanguage = 'en';

	onMount(() => {
		const last_subtitles = localStorage.getItem('last_subtitles');
		const last_subtitle_language = localStorage.getItem('last_subtitle_language');
		const last_subtitle_title = localStorage.getItem('last_subtitle_title');
		if (last_subtitles) {
			$subtitleStore = JSON.parse(last_subtitles);
		}
	});
</script>

<div class="flex place-content-center">
	<div class="m-4 grid p-2">
		{#each $subtitleStore as subtitle}
			<Subtitle {subtitle} {subtitleLanguage} />
		{/each}
	</div>
</div>
