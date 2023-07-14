<script setup lang="ts">
import type {PropType} from "vue";

const props = defineProps({
  category: {
    type: Object as PropType<ProductCategory | null>,
  }
});
</script>

<template>
  <section v-if="category !== null"
           class="p-4 mb-4 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-800 dark:border-gray-700"
  >
    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
      {{ category.name }}
    </h5>
    {{ category.description }}
  </section>
</template>

<style scoped>

</style>
