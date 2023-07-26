<script setup lang="ts">
import ProductTableRow from "@/components/product/ProductTableRow.vue";

defineProps({
  products: {
    type: Array as () => Array<Product>,
    required: true
  }
});
</script>

<template>
  <table class="w-full text-left text-sm text-gray-500 dark:text-gray-400">
    <thead class="bg-gray-50 text-xs uppercase text-gray-700 dark:bg-gray-700 dark:text-gray-400">
    <tr>
      <th scope="col" class="px-4 py-3">Produkt</th>
      <th scope="col" class="px-4 py-3 hidden sm:table-cell">Kategorie</th>
      <th scope="col" class="px-4 py-3 hidden md:table-cell">Barva</th>
      <th scope="col" class="px-4 py-3 hidden md:table-cell">Rozměry</th>
    </tr>
    </thead>
    <tbody>
    <ProductTableRow :products="products"/>
    </tbody>
  </table>
</template>

<style scoped>

</style>
