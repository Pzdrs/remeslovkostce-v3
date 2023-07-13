<script setup lang="ts">
import axios from "@/axios";
import {Alert, Spinner} from "flowbite-vue";
import {ref} from "vue";

let categories = ref<ProductCategory[]>([]);
let loading = ref(true);
let fetchFailed = ref(false);

axios.get('/categories')
    .then(response => {
      categories.value = response.data.map((category: any) => {
        return {
          id: category.id,
          name: category.name,
          products: category.products
        }
      })
      loading.value = false;
    })
    .catch(() => {
      fetchFailed.value = true;
    })
</script>

<template>
  <Alert v-if="fetchFailed" type="danger" :icon="false">Nepodařilo se načíst kategorie</Alert>
  <Spinner v-if="loading && !fetchFailed" class="m-auto"/>
  <ul v-else>
    <li class="mb-3" v-for="category in categories" :key="category.id">
      <button
          type="button"
          class="flex items-center justify-between group w-full"
      >
        <span class="flex items-center">
          <span
              class="text-gray-900 dark:text-white text-base font-medium group-hover:text-blue-700 dark:group-hover:text-blue-600"
          >
            {{ category.name }}
          </span>
        </span>
        <span
            class="text-base font-medium text-gray-500 dark:text-gray-400 group-hover:text-blue-700 dark:group-hover:text-blue-600"
        >
          ({{ category.products }})
        </span>
      </button>
    </li>
  </ul>
</template>

<style scoped>

</style>
