<script>
    import { getAbout } from "../services/api/blog.js";
    import { onMount } from "svelte";

    const pageName = "about page";
    let items = {};

    onMount(async () => {
        const res = await getAbout();
        items = res;
    });
</script>

<h1>{pageName}!</h1>
<p>Welcome to <b>{items.text}</b></p>
