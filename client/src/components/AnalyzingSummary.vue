<script setup>
import { formatRelativeTime } from '../utils/time.js';
defineProps({
  result: { type: Object, required: true }
});
</script>
<template>
  <div class="rounded-xl border border-gray-100 p-4 shadow-xl lg:p-8">
    <div class="text-gray-500">
      <h3 class="text-lg font-medium text-yellow-500 uppercase">WORK SUMMARY</h3>

      <p class="mt-2 text-sm p-2 bg-yellow-50 border border-yellow-200 rounded-lg">
        <span class="font-bold">URL: </span>
        <span>{{ result.url }}</span>
      </p>

      <div class="grid md:grid-cols-2 gap-4 mt-4">
        <div class="border border-stale-100 rounded-xl p-4 md:p-6">
          <h2 class="font-medium uppercase text-yellow-500 text-sm">Execution details</h2>
          <div class="mt-3">
            <div class="flex gap-4 text-sm" v-if="!result.cached">
              <div>Execution time:</div>
              <div>
                <span class="border bg-yellow-50 px-2 py-0.5 rounded-lg font-bold text-indigo-500"
                  >{{ result.execution_time }}ms
                </span>
              </div>
            </div>
            <template v-if="result.cached">
              <div>
                <span
                  class="p-1 px-2 text-xs text-indigo-500 font-bold border border-indigo-500 rounded"
                  >This result is cached
                  {{ formatRelativeTime(new Date(result.completed_at)) }}</span
                >
              </div>
            </template>

            <button
              class="p-2 py-1 bg-indigo-500 hover:bg-indigo-700 text-xs text-white rounded uppercase mt-3"
              @click="$emit('reAnalyze')"
            >
              Analyze again
            </button>
          </div>
        </div>

        <div class="border border-stale-100 rounded-xl p-4 md:p-6">
          <h2 class="font-medium uppercase text-yellow-500 text-sm">Page statistics</h2>
          <table class="mt-3 text-sm">
            <tr>
              <td>Word count:</td>
              <td>
                <span
                  class="border bg-yellow-50 px-2 py-0.5 rounded-lg font-bold text-xs text-indigo-500"
                  >{{ result.word_count }}</span
                >
              </td>
            </tr>
            <tr>
              <td>Unique word:</td>
              <td>
                <span
                  class="border bg-yellow-50 px-2 py-0.5 rounded-lg font-bold text-xs text-indigo-500"
                  >{{ result.unique_word_count }}</span
                >
              </td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
