<script>
    import { get_jwt_from_localstorage } from "../utils/api.js";
    import { onMount } from "svelte";

    let files = [];
    let subtitles = [];

    onMount(() => {
        const last_subtitles = localStorage.getItem("last_subtitles");
        if (last_subtitles) {
            subtitles = JSON.parse(last_subtitles);
            console.log(subtitles);
        }
    });

    async function handleDrop(event) {
        event.preventDefault();
        files = event.dataTransfer.files;
        await uploadFiles();
    }

    function uploadFiles() {
        if (files.length === 0) return;

        for (let i = 0; i < files.length; i++) {
            const formData = new FormData();
            formData.append("file", files[i]);

            axios
                .post("http://localhost:8001/api/v1/subtitle/process/file", formData, {
                    headers: {
                        "Content-Type": "multipart/form-data",
                        Authorization: get_jwt_from_localstorage()
                    }
                })
                .then((response) => {
                    console.log(response);
                    subtitles = response.data.processed_content;
                    localStorage.setItem("last_subtitles", JSON.stringify(subtitles));
                })
                .catch((error) => {
                    console.log(error);
                });
        }
    }

    function handleFileInput(event) {
        files = event.target.files;
        console.log(files);
        uploadFiles();
    }
</script>

<div
    class="drop-area m-4 grid place-content-center p-1"
    on:dragover={(event) => event.preventDefault()}
    on:drop={handleDrop}
>
    <div class="drop-message">Drag and drop files here</div>
    <div class="file-list">
        {#if files.length > 0}
            {#each files as file}
                <div class="file-item">{file.name}</div>
            {/each}
        {/if}
    </div>
    <input id="file-upload-button" type="file" on:change={handleFileInput} />
</div>

<div class="container">
    <div class="grid-columns-2 m-4 grid p-2">
        {#each subtitles as subtitle}
            <div class="m-1 border px-4 py-2">
                <span class="text-xs text-gray-500">
                    {subtitle.start} - {subtitle.end}
                </span>
                <div class="my-2 flex align-middle">
                    {#each subtitle.content as token}
                        <span class="grid-columns-1 grid place-content-center">
                            <span>
                                {#if token.pronounciation !== token.token}
                                    <span class="text-xs text-gray-500">{token.pronounciation}</span
                                    >
                                {:else}
                                    <span class="text-xs text-gray-500">&nbsp;</span>
                                {/if}
                            </span>
                            <span> {token.token.replaceAll("（", "(").replaceAll("）", ")")} </span>
                        </span>
                    {/each}
                </div>
            </div>
        {/each}
    </div>
</div>

<style>
    .drop-area {
        border: 2px dashed #ccc;
        padding: 20px;
        /* padding-up: 80px; */
        /* padding-bottom: 80px; */
        text-align: center;
        cursor: pointer;
    }

    .file-list {
        margin-top: 10px;
    }

    .drop-message {
        color: #999;
    }

    .file-item {
        margin-bottom: 5px;
    }
</style>
