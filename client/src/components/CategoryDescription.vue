<script setup lang="ts">
import type {PropType} from "vue";

defineProps({
  category: {
    type: Object as PropType<ProductCategory | null>,
  }
});
</script>

<template>
  <section v-if="category !== null"
           class="mb-4 rounded-lg border border-gray-200 bg-gray-50 p-4 dark:border-gray-700 dark:bg-gray-800"
  >
    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
      {{ category?.name }}
    </h5>
    {{ category?.description }}
  </section>
</template>

<style scoped>

</style>
