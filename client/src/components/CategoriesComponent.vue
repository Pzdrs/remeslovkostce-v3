<script setup lang="ts">
import {Alert, Spinner} from "flowbite-vue";
import {computed, onMounted, ref} from "vue";
import {deserializeProductCategory, fetchCategories, getProductCategory, store} from "@/store";

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
    label: getProductCategory(category)?.name,
    callback: (product: Product) => product.category.id === category
  }
}

onMounted(() => {
  fetchCategories()
      .then(response => {
        loading.value = false;
      })
      .catch(() => fetchFailed.value = true);
});
</script>

<template>
  <div class="mb-5">
    <h5 class="mb-4 text-sm font-medium uppercase text-gray-500 dark:text-gray-400">
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
            class="flex w-full items-center justify-between group disabled:hover:text-red-500"
        >
          <span class="flex items-center">
            <span
                :aria-disabled="currentlyFiltering"
                class="text-base font-medium aria-disabled:text-gray-400 text-gray-900 aria-disabled:group-hover:text-gray-400 group-hover:text-blue-700 dark:text-white dark:group-hover:text-blue-600"
            >
              {{ category.name }}
            </span>
          </span>
          <span
              :aria-disabled="currentlyFiltering"
              class="text-base font-medium aria-disabled:text-gray-400 text-gray-500 aria-disabled:group-hover:text-gray-400 group-hover:text-blue-700 dark:text-gray-400 dark:group-hover:text-blue-600"
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
