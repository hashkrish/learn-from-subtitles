<script>
	import axios from 'axios';
	import { get_jwt_from_localstorage } from '../utils/api';
	import { APIURL } from '../config';
	import { createEventDispatcher } from 'svelte';
	import { subtitleStore } from '$stores/subtitles';

	const dispatch = createEventDispatcher();

	let files = [];
	let subtitles = [];
	export let subtitleLanguage = 'en';

	async function handleDrop(event) {
		event.preventDefault();
		files = event.dataTransfer.files;
		uploadFiles();
	}

	function handleFileInput(event) {
		files = event.target.files;
		console.log(files);
		uploadFiles();
	}

	function uploadFiles() {
		if (files.length === 0) return;

		for (let i = 0; i < files.length; i++) {
			const formData = new FormData();
			formData.append('file', files[i]);
			dispatch('subtitlesUploadFilename', 'Uploading...' + files[i].name);

			axios
				.post(`${APIURL}/subtitle/process/file`, formData, {
					headers: {
						'Content-Type': 'multipart/form-data',
						Authorization: get_jwt_from_localstorage()
					}
				})
				.then((response) => {
					// console.log(response);
					subtitles = response.data.processed_content;
					localStorage.setItem('last_subtitles', JSON.stringify(subtitles));
					localStorage.setItem('last_subtitle_language', subtitleLanguage);
					localStorage.setItem('last_subtitle_title', files[i].name);
					$subtitleStore = subtitles;
					dispatch('subtitlesUpload', subtitles);
					dispatch('subtitlesUploadFilename', files[i].name);
				})
				.catch((error) => {
					console.log(error);
					dispatch('subtitlesUploadFilename', 'Error: ' + error);
				});
		}
	}
</script>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<div
	class="drop-area m-4 grid place-content-center p-1"
	on:dragover={(event) => event.preventDefault()}
	on:drop={handleDrop}
	aria-label="Drop SRT file here"
>
	<div class="file-list">
		<div class="drop-message">Drag and drop files here</div>
		<label id="file-upload-button-label" for="file-upload-button" class="text-blue-500">
			<span class="text-sm">or click to select files</span>
		</label>
		<input id="file-upload-button" type="file" accept=".srt" value="" on:change={handleFileInput} />
	</div>
</div>

<style>
	.drop-area {
		border: 2px dashed #ccc;
		padding: 20px;
		/* padding-up: 80px; */
		/* padding-bottom: 80px; */
		text-align: center;
		/* cursor: pointer; */
	}

	.file-list {
		margin-top: 10px;
	}

	.drop-message {
		color: #999;
	}

	/* .file-item { */
	/* 	margin-bottom: 5px; */
	/* } */

	#file-upload-button {
		color: transparent;
		background-color: transparent;
		border: none;
		outline: none;
		width: 0;
	}

	#file-upload-button-label {
		cursor: pointer;
	}
</style>
