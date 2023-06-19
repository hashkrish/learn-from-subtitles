<script>
    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();
</script>

<select
    class="m-4 rounded border p-2"
    on:change={(event) => dispatch("subtitleLanguageChange", event.target.value)}
>
    <option value="en">English</option>
    <option value="ja">Japanese</option>
</select>
