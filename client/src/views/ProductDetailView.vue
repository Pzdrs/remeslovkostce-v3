<script setup lang="ts">
import {Alert} from "flowbite-vue";
import {computed, ref} from "vue";
import {useRoute} from "vue-router";
import {deserializeProductDetail, fetchProduct} from "@/store";
import ProductCategoryTag from "@/components/ProductCategoryTag.vue";

const route = useRoute();
let loading = ref(true);
let fetchFailed = ref(false);
let product: Product = null!;

const contentReady = computed(() => !loading.value && !fetchFailed.value);
fetchProduct(parseInt(route.params.id.toString()))
    .then(res => {
      product = deserializeProductDetail(res.data);
      loading.value = false;
    })
    .catch(() => {
      fetchFailed.value = true;
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

    <div v-if="contentReady" class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div class="grid gap-4">
        <div>
          <img class="h-auto max-w-full rounded-lg"
               src="https://flowbite.s3.amazonaws.com/docs/gallery/featured/image.jpg"
               alt="">
        </div>
        <div class="grid grid-cols-5 gap-4">
          <div>
            <img class="h-auto max-w-full rounded-lg"
                 src="https://flowbite.s3.amazonaws.com/docs/gallery/square/image-1.jpg" alt="">
          </div>
          <div>
            <img class="h-auto max-w-full rounded-lg"
                 src="https://flowbite.s3.amazonaws.com/docs/gallery/square/image-2.jpg" alt="">
          </div>
          <div>
            <img class="h-auto max-w-full rounded-lg"
                 src="https://flowbite.s3.amazonaws.com/docs/gallery/square/image-3.jpg" alt="">
          </div>
          <div>
            <img class="h-auto max-w-full rounded-lg"
                 src="https://flowbite.s3.amazonaws.com/docs/gallery/square/image-4.jpg" alt="">
          </div>
          <div>
            <img class="h-auto max-w-full rounded-lg"
                 src="https://flowbite.s3.amazonaws.com/docs/gallery/square/image-5.jpg" alt="">
          </div>
        </div>
      </div>
      <section class="order-first md:order-last">
        <h4 class="text-2xl mb-1 md:mb-0 font-extrabold dark:text-white">
          {{ product.displayName }}
          <ProductCategoryTag :category="product.category" class="hidden md:inline"/>
        </h4>
        <ProductCategoryTag :category="product.category" class="inline md:hidden"/>
        <p v-if="product.description">{{ product.description }}</p>
        <p v-else class="mb-3 mt-2 font-normal text-gray-400 dark:text-gray-400"> bez popisku </p>
      </section>
    </div>
  </div>
</template>

<style scoped>

</style>
