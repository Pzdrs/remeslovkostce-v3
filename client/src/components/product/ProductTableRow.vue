<script setup lang="ts">
import ProductLink from "@/components/product/ProductLink.vue";
import ProductCategoryTag from "@/components/ProductCategoryTag.vue";
import {getMediaURL} from "@/axios";

defineProps({
  products: {
    type: Array as () => Array<Product>,
    required: true
  }
});
</script>

<template>
  <tr v-for="product in products" :key="product.id"
      class="border-b hover:bg-gray-100 dark:border-gray-600 dark:hover:bg-gray-700">
    <th scope="row"
        class="flex items-center whitespace-nowrap px-4 py-2 font-medium text-gray-900 dark:text-white h-14">
      <img :src="getMediaURL(product.thumbnail)"
           alt="iMac Front Image" class="mr-3 w-8 rounded">
      <ProductLink :product="product"/>
    </th>
    <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 dark:text-white hidden sm:table-cell">
      <ProductCategoryTag :category="product.category"/>
    </td>
    <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 dark:text-white hidden md:table-cell">
      <div class="flex items-center">
        <div v-if="product.color.hex"
             class="mr-2 inline-block h-4 w-4 rounded-full border border-gray-300"
             :style="{'background-color': '#'+product.color.hex}"
        >
          <span class="mb-2 ml-5">
            {{ product.color.label }}
          </span>
        </div>
        <span v-else>{{ product.color.label }}</span>
      </div>
    </td>
    <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 dark:text-white hidden md:table-cell">
      {{ product.size.dimensions_display_name }}
    </td>
  </tr>
</template>

<style scoped>

</style>
