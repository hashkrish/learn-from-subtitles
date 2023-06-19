<script>
    import Token from "./Token.svelte";

    export let subtitle = {};
    export let subtitleLanguage = "en";

    function secondsToTimestamp(seconds) {
        const hours = Math.floor(seconds / 3600);
        const minutes = Math.floor((seconds - hours * 3600) / 60);
        const seconds_ = Math.floor(seconds - hours * 3600 - minutes * 60);
        const hours_str = hours < 10 ? "0" + hours : hours;
        const minutes_str = minutes < 10 ? "0" + minutes : minutes;
        const seconds_str = seconds_ < 10 ? "0" + seconds_ : seconds_;
        return `${hours_str}:${minutes_str}:${seconds_str}`;
    }
</script>

<div class="m-1 border px-4 py-2">
    <span class="text-xs text-gray-500">
        {secondsToTimestamp(subtitle.start)} - {secondsToTimestamp(subtitle.end)}
    </span>
    <div class="my-2 flex flex-wrap align-middle">
        {#each subtitle.content as token}
            <Token {token} {subtitleLanguage} />
        {:else}
            <span> Upload a subtitle file to get started. </span>
        {/each}
    </div>
</div>
