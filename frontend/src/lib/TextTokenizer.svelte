<script>
    import { onMount } from "svelte";
    import { APIURL } from "../config.js";
    let processedText = [];
    let text = "私は日本語を勉強しています。";
    onMount(() => {
        axios
            .post(`${APIURL}/subtitle/process/text`, {
                text: text
            })
            .then((response) => {
                // console.log(response);
                processedText = response.data.processed_content;
                // debugText = JSON.stringify(response.data.processed_content);
            })
            .catch((error) => {
                console.log(error);
            });
    });
</script>

<form method="post" class="flex place-content-center">
    <textarea
        type="textarea"
        name="text"
        class="m-2 rounded border-2"
        value={text}
        rows="3"
        cols="50"
    />
    <button class="rounded-full">Parse</button>
</form>

<div class="flex place-content-center">
    {#each processedText as item}
        <span class="m-2 grid grid-cols-1 place-content-center">
            {#if item.token !== item.pronounciation}
                <small class="grid place-content-center">{item.pronounciation}</small>
            {:else}
                <small class="grid place-content-center">&nbsp;</small>
            {/if}
            <span class="grid place-content-center">{item.token}</span>
        </span>
    {/each}
</div>
