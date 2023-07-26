<script setup lang="ts">
import {computed, onMounted, ref} from "vue";
import CategoriesComponent from "@/components/CategoriesComponent.vue";

import {fetchProducts, store} from "@/store";
import {Alert, Spinner} from "flowbite-vue";
import CategoryDescription from "@/components/CategoryDescription.vue";
import PaginationComponent from "@/components/PaginationComponent.vue";
import ProductListingTable from "@/components/ProductListingTable.vue";
import ProductCard from "@/components/product/ProductCard.vue";

const PAGINATE_BY = {
  'list': 10,
  'grid': 4
}

let loading = ref(true);
let fetchFailed = ref(false);
let viewType = ref<string>('grid');

const currentPage = ref(1);
const perPage = computed(() => PAGINATE_BY[viewType.value as 'list' | 'grid']);
const activeFilters = ref<Filter[]>([]);
const currentCategory = ref<ProductCategory | null>(null);

const filteredProducts = computed(() => {
  let products = store.products;
  activeFilters.value.forEach(filter => {
    products = products.filter(filter.callback);
  })
  return products;
});
const paginatedProducts = computed(
    () => filteredProducts.value.slice((currentPage.value - 1) * perPage.value, currentPage.value * perPage.value)
);

const contentReady = computed(() => !loading.value && !fetchFailed.value);

function removeFilter(filterId?: number) {
  if (filterId === undefined) {
    activeFilters.value = [];
    currentCategory.value = null;
  } else {
    // if the filter is of type category, reset the current category
    if (activeFilters.value[filterId].type === 'category') {
      currentCategory.value = null;
    }
    activeFilters.value = activeFilters.value.filter(filter => filter.id !== filterId);
  }
  currentPage.value = 1;
}

function handleCategoryChange(filter: Filter, category: ProductCategory) {
  activeFilters.value.push(filter);
  currentCategory.value = category;
  currentPage.value = 1;
}

onMounted(() => {
  fetchProducts()
      .then(() => loading.value = false)
      .catch(() => fetchFailed.value = true)
});
</script>

<template>
  <section class="mt-6 bg-white pb-8 dark:bg-gray-900 lg:pb-24 w-full">
    <div class="mx-auto px-4 max-w-8xl">
      <div class="mb-6 w-full">

        <div
            class="flex flex-col items-center justify-between rounded-lg border border-gray-200 bg-gray-50 p-4 dark:border-gray-700 dark:bg-gray-800 lg:flex-row">
          <div class="w-full flex-shrink-0 lg:flex lg:w-auto">
            <div class="relative mb-4 w-full flex-shrink-0 lg:mr-5 lg:mb-0 lg:w-64 xl:w-96">
              <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                     stroke="currentColor" aria-hidden="true" class="h-5 w-5 text-gray-500 dark:text-gray-400">
                  <path stroke-linecap="round" stroke-linejoin="round"
                        d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                </svg>
              </div>
              <label for="search" class="hidden">Hledat z {{ store.products.length }} produktů...:</label>
              <input
                  :disabled="store.products.length === 0"
                  id="search"
                  type="text"
                  class="block w-full rounded-lg border border-gray-300 bg-white pl-10 text-sm text-gray-900 p-2.5 py-2.5 focus:border-blue-500 focus:ring-blue-500 dark:placeholder-gray-400 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:focus:border-blue-500 dark:focus:ring-blue-500"
                  :placeholder="'Hledat z ' + store.products.length + ' produktů...'"
              >
            </div>
          </div>
          <div class="flex items-center justify-center text-sm text-gray-600 dark:text-gray-400">
            <div class="w-fit" data-testid="flowbite-tooltip-target">
              <button type="button" @click="viewType = 'list';currentPage = 1"
                      class="mr-1 inline-flex items-center rounded-lg p-2 text-center text-sm font-medium text-white hover:bg-gray-200 focus:outline-none focus:ring-4 focus:ring-gray-300 dark:hover:bg-gray-700 dark:focus:ring-gray-800">
                <svg aria-hidden="true" class="h-5 w-5 text-gray-500 dark:text-gray-400" viewBox="0 0 18 10" fill="none"
                     xmlns="http://www.w3.org/2000/svg">
                  <path
                      d="M2.22913 0H1.18746C0.899811 0 0.666626 0.223858 0.666626 0.5V1.5C0.666626 1.77614 0.899811 2 1.18746 2H2.22913C2.51677 2 2.74996 1.77614 2.74996 1.5V0.5C2.74996 0.223858 2.51677 0 2.22913 0Z"
                      fill="currentColor"></path>
                  <path
                      d="M2.22913 4H1.18746C0.899811 4 0.666626 4.22386 0.666626 4.5V5.5C0.666626 5.77614 0.899811 6 1.18746 6H2.22913C2.51677 6 2.74996 5.77614 2.74996 5.5V4.5C2.74996 4.22386 2.51677 4 2.22913 4Z"
                      fill="currentColor"></path>
                  <path
                      d="M2.22913 8H1.18746C0.899811 8 0.666626 8.22386 0.666626 8.5V9.5C0.666626 9.77614 0.899811 10 1.18746 10H2.22913C2.51677 10 2.74996 9.77614 2.74996 9.5V8.5C2.74996 8.22386 2.51677 8 2.22913 8Z"
                      fill="currentColor"></path>
                  <path
                      d="M16.2916 2H5.87496C5.59869 2 5.33374 1.89464 5.13839 1.70711C4.94304 1.51957 4.83329 1.26522 4.83329 1C4.83329 0.734784 4.94304 0.48043 5.13839 0.292893C5.33374 0.105357 5.59869 0 5.87496 0H16.2916C16.5679 0 16.8328 0.105357 17.0282 0.292893C17.2235 0.48043 17.3333 0.734784 17.3333 1C17.3333 1.26522 17.2235 1.51957 17.0282 1.70711C16.8328 1.89464 16.5679 2 16.2916 2Z"
                      fill="currentColor"></path>
                  <path
                      d="M16.2916 6H5.87496C5.59869 6 5.33374 5.89464 5.13839 5.70711C4.94304 5.51957 4.83329 5.26522 4.83329 5C4.83329 4.73478 4.94304 4.48043 5.13839 4.29289C5.33374 4.10536 5.59869 4 5.87496 4H16.2916C16.5679 4 16.8328 4.10536 17.0282 4.29289C17.2235 4.48043 17.3333 4.73478 17.3333 5C17.3333 5.26522 17.2235 5.51957 17.0282 5.70711C16.8328 5.89464 16.5679 6 16.2916 6Z"
                      fill="currentColor"></path>
                  <path
                      d="M16.2916 10H5.87496C5.59869 10 5.33374 9.89464 5.13839 9.70711C4.94304 9.51957 4.83329 9.26522 4.83329 9C4.83329 8.73478 4.94304 8.48043 5.13839 8.29289C5.33374 8.10536 5.59869 8 5.87496 8H16.2916C16.5679 8 16.8328 8.10536 17.0282 8.29289C17.2235 8.48043 17.3333 8.73478 17.3333 9C17.3333 9.26522 17.2235 9.51957 17.0282 9.70711C16.8328 9.89464 16.5679 10 16.2916 10Z"
                      fill="currentColor"></path>
                </svg>
                <span class="sr-only">Toggle list view</span></button>
            </div>
            <div class="w-fit" data-testid="flowbite-tooltip-target">
              <button type="button" @click="viewType = 'grid'; currentPage = 1"
                      class="inline-flex items-center rounded-lg text-center text-sm font-medium text-white p-2.5 hover:bg-gray-200 focus:outline-none focus:ring-4 focus:ring-gray-300 dark:hover:bg-gray-700 dark:focus:ring-gray-800">
                <svg aria-hidden="true" class="h-4 w-4 text-gray-500 dark:text-gray-400" viewBox="0 0 16 16" fill="none"
                     xmlns="http://www.w3.org/2000/svg">
                  <path
                      d="M5.61917 0.5H2.0475C1.19284 0.5 0.5 1.19284 0.5 2.0475V5.61917C0.5 6.47383 1.19284 7.16667 2.0475 7.16667H5.61917C6.47383 7.16667 7.16667 6.47383 7.16667 5.61917V2.0475C7.16667 1.19284 6.47383 0.5 5.61917 0.5Z"
                      fill="currentColor"></path>
                  <path
                      d="M13.9525 0.5H10.3808C9.52617 0.5 8.83333 1.19284 8.83333 2.0475V5.61917C8.83333 6.47383 9.52617 7.16667 10.3808 7.16667H13.9525C14.8072 7.16667 15.5 6.47383 15.5 5.61917V2.0475C15.5 1.19284 14.8072 0.5 13.9525 0.5Z"
                      fill="currentColor"></path>
                  <path
                      d="M5.61917 8.83333H2.0475C1.19284 8.83333 0.5 9.52617 0.5 10.3808V13.9525C0.5 14.8072 1.19284 15.5 2.0475 15.5H5.61917C6.47383 15.5 7.16667 14.8072 7.16667 13.9525V10.3808C7.16667 9.52617 6.47383 8.83333 5.61917 8.83333Z"
                      fill="currentColor"></path>
                  <path
                      d="M13.9525 8.83333H10.3808C9.52617 8.83333 8.83333 9.52617 8.83333 10.3808V13.9525C8.83333 14.8072 9.52617 15.5 10.3808 15.5H13.9525C14.8072 15.5 15.5 14.8072 15.5 13.9525V10.3808C15.5 9.52617 14.8072 8.83333 13.9525 8.83333Z"
                      fill="currentColor"></path>
                </svg>
                <span class="sr-only">Toggle grid view</span></button>
            </div>

          </div>
        </div>

      </div>
      <div class="mt-4 grid grid-cols-5 gap-6">
        <div>
          <aside
              class="col-span-1 hidden flex-1 rounded-lg border border-gray-200 bg-gray-50 p-5 dark:border-gray-700 dark:bg-gray-800 lg:block">
            <CategoriesComponent
                :active-filters="activeFilters"
                @category-change="(f, c) => handleCategoryChange(f, c)"
            />
          </aside>
        </div>
        <div class="col-span-5 lg:col-span-4">
          <div class="mb-4 flex items-center min-h-[28px]">
            <span class="mr-3 flex-shrink-0 text-sm font-medium text-gray-900 dark:text-white">
              <span v-if="store.products.length === 0">
                Nejsou zobrazeny žádné produkty.
              </span>
              <span v-else>
                Zobrazeno
                {{ currentPage * perPage - perPage + 1 }}
                až
                {{ currentPage * perPage > filteredProducts.length ? filteredProducts.length : currentPage * perPage }}
                produktů z
                {{ filteredProducts.length }}
                celkem.
              </span>
            </span>
            <div class="flex flex-wrap items-center space-x-3">
              <span
                  v-for="filter in activeFilters"
                  :key="filter.id"
                  class="inline-flex items-center rounded-md bg-gray-100 px-2 py-1 text-sm font-medium text-gray-900 dark:bg-gray-800 dark:text-white"
              >
                {{ filter.label }}
                <button
                    @click="removeFilter(filter.id)"
                    type="button"
                    class="ml-2 inline-flex items-center rounded-sm bg-transparent p-1 text-sm text-gray-400 hover:bg-gray-200 hover:text-gray-900 dark:hover:bg-gray-700 dark:hover:text-gray-300"
                    aria-label="Remove filter">
                  <svg aria-hidden="true" class="text-gray-500 w-2.5 h-2.5"
                       viewBox="0 0 10 10"
                       fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M5.83196 5.00717L8.91955 1.91958C8.97526 1.86577 9.0197 1.8014 9.05027 1.73023C9.08084 1.65907 9.09693 1.58252 9.09761 1.50507C9.09828 1.42761 9.08352 1.3508 9.05419 1.27911C9.02486 1.20742 8.98155 1.14229 8.92677 1.08752C8.872 1.03275 8.80687 0.989433 8.73518 0.960103C8.66349 0.930772 8.58668 0.916013 8.50923 0.916686C8.43177 0.917359 8.35523 0.933451 8.28406 0.964023C8.21289 0.994595 8.14852 1.03903 8.09471 1.09475L5.00713 4.18233L1.91954 1.09475C1.80953 0.98849 1.66217 0.929693 1.50923 0.931022C1.35628 0.932351 1.20997 0.9937 1.10182 1.10185C0.993662 1.21001 0.932313 1.35632 0.930984 1.50926C0.929655 1.66221 0.988452 1.80956 1.09471 1.91958L4.18229 5.00717L1.09471 8.09475C1.039 8.14856 0.994557 8.21293 0.963985 8.2841C0.933413 8.35527 0.917321 8.43181 0.916648 8.50927C0.915975 8.58672 0.930734 8.66353 0.960065 8.73522C0.989395 8.80691 1.03271 8.87204 1.08748 8.92681C1.14225 8.98158 1.20738 9.0249 1.27907 9.05423C1.35076 9.08356 1.42757 9.09832 1.50503 9.09765C1.58248 9.09697 1.65903 9.08088 1.7302 9.05031C1.80137 9.01974 1.86573 8.9753 1.91954 8.91958L5.00713 5.832L8.09471 8.91958C8.20473 9.02584 8.35208 9.08464 8.50503 9.08331C8.65798 9.08198 8.80428 9.02063 8.91244 8.91248C9.02059 8.80432 9.08194 8.65801 9.08327 8.50507C9.0846 8.35212 9.0258 8.20477 8.91955 8.09475L5.83196 5.00717Z"
                        fill="currentColor">
                    </path>
                  </svg>
                  <span class="sr-only">Zrušit filtr</span>
                </button>
              </span>
            </div>
            <button
                @click="removeFilter()"
                v-if="activeFilters.length > 0"
                type="button"
                class="ml-3 flex-shrink-0 rounded-md border border-gray-400 bg-white px-2 py-1 text-sm font-medium text-gray-500 hover:bg-gray-50 dark:border-gray-700 dark:bg-gray-900 dark:text-gray-400 dark:hover:bg-gray-800">
              Zrušit filtry
            </button>
          </div>
          <CategoryDescription :category="currentCategory"/>
          <Alert v-if="fetchFailed" type="danger" :icon="false">Nepodařilo se načíst produkty</Alert>
          <Spinner v-if="loading && !fetchFailed" class="m-auto"/>
          <div v-if="contentReady">
            <div v-if="viewType === 'grid'" class="grid grid-cols-1 gap-3 sm:grid-cols-3 lg:grid-cols-3 xl:grid-cols-4 justify-items-center sm:justify-items-stretch">
              <div v-for="product in paginatedProducts" :key="product.id">
                <ProductCard :product="product"/>
              </div>
            </div>
            <div v-else-if="viewType === 'list'" class="mx-auto">
              <div class="relative overflow-hidden bg-white shadow-md dark:bg-gray-800 sm:rounded-lg">
                <div class="overflow-x-auto">
                  <ProductListingTable :products="paginatedProducts"/>
                </div>
              </div>
            </div>
            <PaginationComponent
                :current-page="currentPage"
                :object-count="filteredProducts.length"
                :per-page="perPage"
                @page-change="page => currentPage = page"
            />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>

</style>
