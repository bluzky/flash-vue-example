<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<template>
  <div class="mx-auto max-w-screen-xl">
    <header class="flex gap-2 justify-center items-center p-3 border-b-2 border-yellow-500 sticky">
      <img alt="Lemon analyzer" class="h-8" src="@/assets/logo.png" />
      <span class="text-2xl text-yellow-500">Lemon Project</span>
    </header>

    <RouterView />
  </div>
</template>
