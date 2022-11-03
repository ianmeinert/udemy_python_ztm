<script>
    import { onMount } from "svelte";
    import { getResume } from "../services/api/blog.js";

    const pageName = "resume page";
    let items = {};

    onMount(async () => {
        const res = await getResume();
        items = res;
    });
</script>

<h1>{pageName}!</h1>
<p>Welcome to <b>{items.text}</b></p>
