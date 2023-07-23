<script setup lang="ts">

</script>

<template>
  <div id="animation-carousel" class="relative mb-14 w-full lg:mb-24" data-carousel="static">
    <!-- Carousel wrapper -->
    <div class="relative h-56 overflow-hidden rounded-lg md:h-96">
      <!-- Item 1 -->
      <div class="hidden duration-200 ease-linear" data-carousel-item>
        <img src="../assets/images/carousel-4.svg"
             class="absolute top-1/2 left-1/2 block w-full -translate-x-1/2 -translate-y-1/2" alt="...">
      </div>
      <!-- Item 2 -->
      <div class="hidden duration-200 ease-linear" data-carousel-item>
        <img src="../assets/images/carousel-4.svg"
             class="absolute top-1/2 left-1/2 block w-full -translate-x-1/2 -translate-y-1/2" alt="...">
      </div>
      <!-- Item 3 -->
      <div class="hidden duration-200 ease-linear" data-carousel-item="active">
        <img src="../assets/images/carousel-4.svg"
             class="absolute top-1/2 left-1/2 block w-full -translate-x-1/2 -translate-y-1/2" alt="...">
      </div>
      <!-- Item 4 -->
      <div class="hidden duration-200 ease-linear" data-carousel-item>
        <img src="../assets/images/carousel-4.svg"
             class="absolute top-1/2 left-1/2 block w-full -translate-x-1/2 -translate-y-1/2" alt="...">
      </div>
      <!-- Item 5 -->
      <div class="hidden duration-200 ease-linear" data-carousel-item>
        <img src="../assets/images/carousel-4.svg"
             class="absolute top-1/2 left-1/2 block w-full -translate-x-1/2 -translate-y-1/2" alt="...">
      </div>
    </div>
    <!-- Slider controls -->
    <button type="button"
            class="absolute top-0 left-0 z-30 flex h-full cursor-pointer items-center justify-center px-4 group focus:outline-none"
            data-carousel-prev>
        <span
            class="inline-flex h-10 w-10 items-center justify-center rounded-full bg-white/30 group-hover:bg-white/50 group-focus:outline-none group-focus:ring-4 group-focus:ring-white dark:bg-gray-800/30 dark:group-hover:bg-gray-800/60 dark:group-focus:ring-gray-800/70">
            <svg class="h-4 w-4 text-white dark:text-gray-800" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                 fill="none" viewBox="0 0 6 10">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="M5 1 1 5l4 4"/>
            </svg>
            <span class="sr-only">Previous</span>
        </span>
    </button>
    <button type="button"
            class="absolute top-0 right-0 z-30 flex h-full cursor-pointer items-center justify-center px-4 group focus:outline-none"
            data-carousel-next>
        <span
            class="inline-flex h-10 w-10 items-center justify-center rounded-full bg-white/30 group-hover:bg-white/50 group-focus:outline-none group-focus:ring-4 group-focus:ring-white dark:bg-gray-800/30 dark:group-hover:bg-gray-800/60 dark:group-focus:ring-gray-800/70">
            <svg class="h-4 w-4 text-white dark:text-gray-800" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                 fill="none" viewBox="0 0 6 10">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                      d="m1 9 4-4-4-4"/>
            </svg>
            <span class="sr-only">Next</span>
        </span>
    </button>
  </div>
</template>

<style scoped>

</style>
