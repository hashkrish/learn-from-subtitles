<script>
	import MainContent from '$lib/MainContent.svelte';
	import UsagePanel from '$lib/UsagePanel.svelte';
	import Container from '../lib/Container.svelte';
	import DragAndDrop from '../lib/DragAndDrop.svelte';
	import Dropdown from '../lib/Dropdown.svelte';
	import Sidebar from '../lib/Sidebar.svelte';
	import SubtitleHeader from '../lib/SubtitleHeader.svelte';
	import SubtitleList from '../lib/SubtitleList.svelte';
	import TextTokenizer from '../lib/TextTokenizer.svelte';

	let debugText = '';
	let title = 'Sample Header';
	let subtitles = [];
	let subtitleLanguage = 'en';

	function onSubtitlesUpload(event) {
		subtitles = event.detail;
		// console.log("loaded processed subtitles");
	}

	function onSubtitlesUploadFileName(event) {
		title = event.detail;
		localStorage.setItem('last_subtitle_title', title);
		// console.log("loaded processed subtitles");
	}

	function onSubtitleLanguageChange(event) {
		subtitleLanguage = event.detail;
		localStorage.setItem('last_subtitle_language', subtitleLanguage);
		// console.log("subtitle language changed");
	}
</script>

<div class="m-2 flex place-content-center p-2"><h1 class="text-3xl">Learn from Subtitles</h1></div>

<!-- <p>{debugText}</p> -->
<span class="flex place-content-center">
	<Dropdown on:subtitleLanguageChange={onSubtitleLanguageChange} />
	<!-- <div class="flex place-content-center py-5"><h1 class="text-3xl">→</h1></div> -->
	<!-- <Dropdown on:subtitleLanguageChange={onSubtitleLanguageChange} /> -->
</span>
<DragAndDrop
	on:subtitlesUpload={onSubtitlesUpload}
	on:subtitlesUploadFilename={onSubtitlesUploadFileName}
/>
<SubtitleHeader {title} />
<Container>
	<MainContent>
		<SubtitleList {subtitles} {subtitleLanguage} />
	</MainContent>
	<Sidebar>
		<TextTokenizer />
		<UsagePanel />
	</Sidebar>
</Container>
