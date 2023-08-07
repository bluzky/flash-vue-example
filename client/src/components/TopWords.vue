<script setup>
import { ref, onMounted } from 'vue';
import { Bar } from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';
ChartJS.register(Title, Tooltip, BarElement, CategoryScale, LinearScale, ChartDataLabels);

const props = defineProps({
  topwords: {
    type: Array,
    required: true
  }
});

const chartData = ref(null);
const chartOptions = {
  responsive: true,
  indexAxis: 'y',
  scales: {
    x: {
      display: false,
      title: {
        display: false
      }
    },
    y: {
      ticks: {
        autoSkip: false
      }
    }
  },
  backgroundColor: 'indigo',
  plugins: {
    // Change options for ALL labels of THIS CHART
    datalabels: {
      font: {
        weight: 'bold'
      },
      color: 'black',
      anchor: 'end',
      align: 'right'
    }
  }
};

onMounted(() => {
  const labels = props.topwords.map(([word, _count]) => word);
  const data = props.topwords.map(([, count]) => count);
  chartData.value = { labels: labels, datasets: [{ data: data }] };
});
</script>

<template>
  <div class="rounded-xl border border-gray-100 p-4 shadow-xl">
    <h3 class="text-xl font-medium text-yellow-500 uppercase">Top 100 words</h3>
    <div>
      <Bar
        id="my-chart-id"
        :options="chartOptions"
        :data="chartData"
        :height="topwords.length * 10"
        v-if="chartData"
      />
    </div>
  </div>
</template>
