<script setup lang="ts">
import type {PropType} from "vue";

defineProps({
  category: {
    type: Object as PropType<ProductCategory>,
    required: true
  }
});
</script>

<template>
<span
    class="rounded bg-blue-100 text-sm font-medium text-blue-800 px-2.5 py-0.5 dark:bg-blue-900 dark:text-blue-300"
>
  {{ category.name }}
</span>
</template>

<style scoped>

</style>
