<script setup lang="ts">
import ProductLink from "@/components/product/ProductLink.vue";
import ProductCategoryTag from "@/components/ProductCategoryTag.vue";

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
        class="flex items-center whitespace-nowrap px-4 py-2 font-medium text-gray-900 dark:text-white">
      <img src="https://flowbite.s3.amazonaws.com/blocks/application-ui/products/imac-front-image.png"
           alt="iMac Front Image" class="mr-3 h-8 w-auto">
      <ProductLink :product="product"/>
    </th>
    <td class="px-4 py-2">
      <ProductCategoryTag :category="product.category"/>
    </td>
    <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 dark:text-white">
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
    <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 dark:text-white">
      {{ product.size.dimensions_display_name }}
    </td>
  </tr>
</template>

<style scoped>

</style>
