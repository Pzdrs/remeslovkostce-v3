<script setup lang="ts">
import axios from "@/axios";
import {Alert, Spinner} from "flowbite-vue";
import {computed, onMounted, ref} from "vue";
import {deserializeProductCategory, getProductCategory, store} from "@/store";

const props = defineProps({
  activeFilters: {
    type: Array as () => Array<Filter>,
    required: true
  }
})
let currentlyFiltering = computed(
    () => props.activeFilters?.some(filter => filter.type === 'category')
);
let loading = ref(true);
let fetchFailed = ref(false);

function getFilter(category: number) {
  return {
    id: props.activeFilters?.length,
    type: 'category',
    label: getProductCategory(category).name,
    callback: (product: Product) => product.category.id === category
  }
}

onMounted(() => {
  axios.get('/categories')
      .then(response => {
        store.categories = response.data.map((category: any) => deserializeProductCategory(category));
        loading.value = false;
      })
      .catch(() => fetchFailed.value = true);
});
</script>

<template>
  <div class="mb-5">
    <h5 class="uppercase text-sm font-medium text-gray-500 dark:text-gray-400 mb-4">
      Kategorie
    </h5>
    <Alert v-if="fetchFailed" type="danger" :icon="false">Nepodařilo se načíst kategorie</Alert>
    <Spinner v-if="loading && !fetchFailed" class="m-auto"/>
    <ul v-else>
      <li class="mb-3"
          v-for="category in store.categories" :key="category.id"
      >
        <button
            :disabled="currentlyFiltering"
            @click="$emit('categoryChange', getFilter(category.id), category)"
            type="button"
            class="flex items-center justify-between group w-full disabled:hover:text-red-500"
        >
          <span class="flex items-center">
            <span
                :aria-disabled="currentlyFiltering"
                class="text-gray-900 dark:text-white text-base font-medium group-hover:text-blue-700 dark:group-hover:text-blue-600 aria-disabled:text-gray-400 aria-disabled:group-hover:text-gray-400"
            >
              {{ category.name }}
            </span>
          </span>
          <span
              :aria-disabled="currentlyFiltering"
              class="text-base font-medium text-gray-500 dark:text-gray-400 group-hover:text-blue-700 dark:group-hover:text-blue-600  aria-disabled:text-gray-400 aria-disabled:group-hover:text-gray-400"
          >
            ({{ category.products }})
          </span>
        </button>
      </li>
    </ul>
  </div>
</template>

<style scoped>

</style>
