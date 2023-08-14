<script setup lang="ts">
import type {PropType} from "vue";
import ProductLink from "@/components/product/ProductLink.vue";
import {getMediaURL} from "@/axios";

defineProps({
  product: {
    type: Object as PropType<Product>,
    required: true
  }
});

</script>

<template>
  <div class="max-w-sm rounded-lg border border-gray-200 bg-white shadow dark:border-gray-700 dark:bg-gray-800 h-[390px] relative flex flex-col justify-between">
    <img class="min-h-[250px] w-full object-contain"
         :src="getMediaURL(product.thumbnail)"
         alt="Product thumbnail"
    />
    <div class="p-5">
      <ProductLink :product="product" class="mb-2 text-l lg:text-2xl font-bold tracking-tight text-gray-900 dark:text-white"/>
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
