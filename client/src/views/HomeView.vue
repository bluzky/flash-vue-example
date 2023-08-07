<script setup>
import { ref, inject } from 'vue';
import AnalyzingSummary from '../components/AnalyzingSummary.vue';
import TopWords from '../components/TopWords.vue';
import LoadingMessage from '../components/LoadingMessage.vue';

const axios = inject('axios');
const loading = ref(false);
const url = ref('https://flask-migrate.readthedocs.io/en/latest/');

const analyzedResult = ref(null);

/**
 * Request server to analyze given url
 *
 * @param {String} url: url to analyze
 * @param {Boolean} ignoreCache: skip cache and re-run analyzing procedure. Default to `false`.
 */
async function analyzeUrl(ignoreCache = false) {
  loading.value = true;
  analyzedResult.value = null;
  const api = `/analyze?url=${url.value}${ignoreCache ? '&ignore_cache=true' : ''}`;
  const response = await axios.get(api).catch((err) => console.log(err));
  analyzedResult.value = response.data.data;
  loading.value = false;
}

function submit() {
  analyzeUrl();
}
</script>

<template>
  <main class="max-w-4xl mx-auto p-4 md:p-8">
    <section class="flex py-10">
      <div class="grow">
        <label for="url" class="sr-only">URL</label>

        <input
          type="text"
          id="url"
          name="url"
          v-model="url"
          @keyup.enter="submit"
          :disabled="loading"
          placeholder="paste URL here"
          class="w-full rounded-s border-gray-200 p-3 border border-stale-50 shadow-sm sm:text-sm focus:ring-0 focus:ring-offset-0"
        />
      </div>
      <button
        class="inline-block p-3 rounded-e bg-indigo-600 text-white uppercase text-xs"
        :disabled="loading"
        @click="submit"
      >
        Analyze
      </button>
    </section>

    <section class="md:p-5" v-if="!analyzedResult && !loading">
      <p class="rounded-2xl bg-yellow-50 sm:text-sm text-center text-gray-700 p-4 md:p-10">
        Paste a link to a webpage and press
        <code class="border border-yellow-700 rounded p-1 shadow text-yellow-500">ENTER</code> or
        click
        <code class="border border-yellow-700 rounded p-1 shadow text-yellow-500">ANALYZE</code> to
        start analyzing word usage in the page's content
      </p>
    </section>

    <section class="md:p-5" v-if="loading">
      <LoadingMessage />
    </section>

    <section class="md:p-5" v-if="analyzedResult">
      <AnalyzingSummary
        :result="analyzedResult"
        @re-analyze="() => analyzeUrl(true)"
      ></AnalyzingSummary>
    </section>

    <!-- Chart section -->

    <section class="md:p-5 mt-5" v-if="analyzedResult">
      <TopWords :topwords="analyzedResult.top_words"></TopWords>
    </section>
  </main>
</template>
