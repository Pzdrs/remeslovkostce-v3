<script setup lang="ts">
import type {PropType} from "vue";

const props = defineProps({
  product: {
    type: Object as PropType<Product>,
    required: true
  }
});

let parameters = [
  {name: 'Barva', value: props.product?.color?.label},
  {name: 'Rozměry', value: props.product?.size?.dimensions_display_name},
];

function getRowClassList(index: number) {
  const classes = ["bg-white", "dark:bg-gray-800"];

  // If it's the last parameter row, add additional classes
  if (index < Object.keys(parameters).length - 1) {
    classes.push("border-b", "dark:border-gray-700");
  }

  return classes.join(" ");
}
</script>

<template>
  <div class="relative overflow-x-auto lg:w-3/4">
    <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
      <tbody>
      <tr v-for="(parameter, index) in parameters"
          :key="index"
          :class="getRowClassList(index)"
      >
        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
          {{ parameter.name }}
        </th>
        <td class="px-6 py-4">
          {{ parameter.value }}
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>

</style>
