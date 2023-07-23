<script setup lang="ts">
import type {PropType} from "vue";
import ProductLink from "@/components/product/ProductLink.vue";

defineProps({
  product: {
    type: Object as PropType<Product>,
    required: true
  }
});
</script>

<template>
  <div class="max-w-sm rounded-lg border border-gray-200 bg-white shadow dark:border-gray-700 dark:bg-gray-800">
    <img class="rounded-t-lg"
         :src="`http://127.0.0.1:8000/media/${product.thumbnail}`"
         alt="Product thumbnail"
    />
    <div class="p-5">
      <ProductLink :product="product" class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"/>
      <p v-if=" product.description.length> 0"
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
