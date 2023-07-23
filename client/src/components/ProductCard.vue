<script setup lang="ts">
import type {PropType} from "vue";

const props = defineProps({
  product: {
    type: Object as PropType<Product>,
    required: true
  }
});
</script>

<template>
  <div class="max-w-sm rounded-lg border border-gray-200 bg-white shadow dark:border-gray-700 dark:bg-gray-800">
    <a href="#">
      <img class="rounded-t-lg" src="http://127.0.0.1:8000/media/products/blok_1.jpg" alt=""/>
    </a>
    <div class="p-5">
      <a href="#">
        <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
          {{ product.displayName }}
        </h5>
      </a>
      <p v-if="product.description.length > 0"
         class="mb-3 font-normal text-gray-700 dark:text-gray-400">
        {{ product.description }}
      </p>
      <p v-else
         class="mb-3 font-normal text-gray-400 dark:text-gray-400">
        bez popisku
      </p>
    </div>
  </div>
</template>

<style scoped>

</style>
