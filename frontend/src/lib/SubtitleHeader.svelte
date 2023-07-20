<script>
	import { onMount } from 'svelte';
	export let title = 'Sample subtitle heading';

	onMount(() => {
		const last_subtitle_title = localStorage.getItem('last_subtitle_title');
		if (last_subtitle_title) {
			title = last_subtitle_title;
		}
	});
</script>

<div class="flex place-content-center p-1"><h1 class="text-xl">{title}</h1></div>
