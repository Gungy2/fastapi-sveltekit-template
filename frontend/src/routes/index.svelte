<script context="module" lang="ts">
  import type { LoadInput } from "@sveltejs/kit";

  export async function load({ fetch }: LoadInput) {
    const url = `http://backend:8000/`;
    const res = await fetch(url);
    const data = await res.text();
    return { props: { data } };
  }
</script>

<script lang="ts">
  import Counter from "$lib/Counter.svelte";

  export let data: string;
</script>

<svelte:head>
  <title>Home</title>
</svelte:head>

<section>
  <h1>
    <div class="welcome">
      <picture>
        <source srcset="svelte-welcome.webp" type="image/webp" />
        <img src="svelte-welcome.png" alt="Welcome" />
      </picture>
    </div>

    to your mold<br />SvelteKit app
  </h1>

  <h2>
    try editing <strong> {data} </strong>
  </h2>

  <Counter />
</section>

<style>
  section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex: 1;
  }

  h1 {
    width: 100%;
  }

  .welcome {
    position: relative;
    width: 100%;
    height: 0;
    padding: 0 0 calc(100% * 495 / 2048) 0;
  }

  .welcome img {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    display: block;
  }
</style>
