<script setup lang="ts">
import {Alert} from "flowbite-vue";
import {computed, onMounted, ref} from "vue";
import {onBeforeRouteUpdate, useRoute} from "vue-router";
import {deserializeProductDetail, fetchProduct} from "@/store";
import ProductCategoryTag from "@/components/ProductCategoryTag.vue";
import ProductParameterTable from "@/components/ProductParameterTable.vue";
import ProductLink from "@/components/product/ProductLink.vue";
import {getMediaURL} from "@/axios";

const route = useRoute();
let loading = ref(true);
let fetchFailed = ref(false);
let product: Product = null!;
const variants = ref<Product[]>([]);
const thumbnailURL = computed(() => getMediaURL(product.thumbnail));

const contentReady = computed(() => !loading.value && !fetchFailed.value);

onMounted(() => {
  fetchProduct(parseInt(route.params.id.toString()))
      .then(res => {
        product = deserializeProductDetail(res.data);
        product.variants?.products.forEach(product => {
          fetchProduct(product).then(res => {
            variants.value.push(deserializeProductDetail(res.data))
          });
        })
        loading.value = false;
      })
      .catch(() => {
        fetchFailed.value = true;
      });
});
</script>

<template v-if="product !== null">
  <div class="p-5">
    <Alert v-if="fetchFailed" type="danger" :icon="false" class="mx-auto sm:w-1/2">
      Nepodařilo se načíst informace o produktu
    </Alert>

    <div v-if="loading && !fetchFailed" role="status"
         class="animate-pulse space-y-8 md:space-y-0 md:space-x-8 md:flex md:items-center">
      <div class="flex h-48 w-full items-center justify-center rounded bg-gray-300 dark:bg-gray-700">
        <svg class="h-10 w-10 text-gray-200 dark:text-gray-600" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
             fill="currentColor" viewBox="0 0 20 18">
          <path
              d="M18 0H2a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3Zm4.376 10.481A1 1 0 0 1 16 15H4a1 1 0 0 1-.895-1.447l3.5-7A1 1 0 0 1 7.468 6a.965.965 0 0 1 .9.5l2.775 4.757 1.546-1.887a1 1 0 0 1 1.618.1l2.541 4a1 1 0 0 1 .028 1.011Z"/>
        </svg>
      </div>
      <div class="w-full">
        <div class="mb-4 w-48 rounded-full bg-gray-200 h-2.5 dark:bg-gray-700"></div>
        <div class="h-2 rounded-full bg-gray-200 max-w-[480px] mb-2.5 dark:bg-gray-700"></div>
        <div class="h-2 rounded-full bg-gray-200 mb-2.5 dark:bg-gray-700"></div>
        <div class="h-2 rounded-full bg-gray-200 max-w-[440px] mb-2.5 dark:bg-gray-700"></div>
        <div class="h-2 rounded-full bg-gray-200 max-w-[460px] mb-2.5 dark:bg-gray-700"></div>
        <div class="h-2 rounded-full bg-gray-200 max-w-[360px] dark:bg-gray-700"></div>
      </div>
      <span class="sr-only">Loading...</span>
    </div>

    <div v-if="contentReady" class="grid grid-cols-1 gap-4 md:grid-cols-2">
      <!--   Heading for mobile devices   -->
      <div class="md:hidden">
        <h4 class="mb-1 text-2xl font-extrabold dark:text-white md:mb-0">
          {{ product.displayName }}
        </h4>
        <ProductCategoryTag :category="product.category"/>
        <p v-if="product.description">{{ product.description }}</p>
        <p v-else class="mt-2 mb-3 font-normal text-gray-400 dark:text-gray-400">bez popisku</p>
      </div>
      <!--   Gallery   -->
      <div class="grid gap-4">
        <div>
          <img class="object-contain h-96 mx-auto rounded-lg"
               :src="thumbnailURL"
               alt="Product thumbnail">
        </div>
        <hr>
        <div class="grid grid-cols-5 gap-4">
          <a target="_blank" class="border-2 rounded p-2"
             :href="thumbnailURL"
             v-for="image in product.images" :key="image.id"
          >
            <img class="rounded-lg"
                 :src="thumbnailURL"
                 alt="Alternate product image">
          </a>
        </div>
      </div>
      <section>
        <h4 class="mb-1 hidden text-2xl font-extrabold dark:text-white md:mb-0 md:block">
          {{ product.displayName }}
          <ProductCategoryTag :category="product.category"/>
        </h4>
        <div class="hidden md:block">
          <p v-if="product.description">{{ product.description }}</p>
          <p v-else class="mt-2 mb-3 font-normal text-gray-400 dark:text-gray-400">bez popisku</p>
        </div>
        <h5 class="mt-5 text-xl font-medium">Parametry</h5>
        <ProductParameterTable :product="product"/>

        <section v-if="product.variants">
          <h5 class="mt-5 text-xl font-medium">
            <span v-if="variants.length <= 4">Další <span class="font-bold">{{ variants.length }}</span> varianty</span>
            <span v-else>Dalších <span class="font-bold">{{ variants.length }}</span> variant</span>
            z kategorie <span class="font-extrabold">{{ product.variants.name }}</span>
          </h5>

          <div class="mt-2 lg:w-3/4">
            <div v-for="variant in variants" :key="variant.id"
                 class="mb-4 rounded-lg border border-gray-200 p-2 dark:border-gray-700 dark:bg-gray-800 flex"
            >
              <img class="rounded-lg h-12 w-auto"
                   :src="getMediaURL(variant.thumbnail)"
                   alt="">
              <ProductLink :product="variant" class="ml-7 my-auto font-medium"/>
            </div>
          </div>

        </section>
      </section>
    </div>
  </div>
</template>

<style scoped>

</style>
