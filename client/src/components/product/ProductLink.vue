<script setup lang="ts">
import type {PropType} from "vue";

defineProps({
  product: {
    type: Object as PropType<Product>,
    required: true
  }
});
</script>

<template>
  <RouterLink :to="{name:'product-detail', params: {id: product.id}}" :key="product.id">
    {{ product.displayName }}
  </RouterLink>
</template>

<style scoped>

</style>
