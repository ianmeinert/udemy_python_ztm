<script>
  import Home from "./components/home.svelte";
  import About from "./components/about.svelte";
  import Resume from "./components/resume.svelte";

  export let menu = 0;
</script>

<main>
  <ul id="menu">
    <li>
      <a href="/">Home</a>
    </li>
    |
    <li>
      <a href="/" on:click|preventDefault={() => (menu = 1)}>About Me</a>
    </li>
    |
    <li>
      <a href="/" on:click|preventDefault={() => (menu = 2)}>Resume</a>
    </li>
    |
    <li>
      <a
        href="https://github.com/ianmeinert"
        target="_blank"
        rel="noopener noreferrer">Find me on Github</a
      >
    </li>
  </ul>
  <h1>Works of Ian</h1>

  {#if menu === 1}
    <About />
  {:else if menu === 2}
    <Resume />
  {:else}
    <Home />
  {/if}
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  ul#menu li {
    display: inline;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>
