<script>
    import { onMount } from "svelte";
    import { getHome } from "../services/api/blog";

    const pageName = "home page";
    let items = {};

    onMount(async () => {
        const res = await getHome();
        items = res;
    });
</script>

<h1>{pageName}!</h1>
<p>Welcome to <b>{items.text}</b></p>
