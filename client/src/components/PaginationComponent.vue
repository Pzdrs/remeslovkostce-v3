<script setup lang="ts">
import {computed} from "vue";
import {useMediaQuery} from "@vueuse/core";

const isMobile = useMediaQuery('(max-width: 640px)')
const isDesktop = useMediaQuery('(min-width: 1024px)')

const props = defineProps({
  currentPage: {
    type: Number,
    required: true
  },
  objectCount: {
    type: Number,
    required: true
  },
  perPage: {
    type: Number,
    default: 8
  },
  previousLabel: {
    type: String,
    default: 'Předchozí'
  },
  nextLabel: {
    type: String,
    default: 'Další'
  },
})

const pageCount = computed(() => Math.ceil(props.objectCount / props.perPage))
const isAtFirstPage = computed(() => props.currentPage === 1)
const isAtLastPage = computed(() => props.currentPage === pageCount.value)

const visiblePageRange = computed(() => {
  const maxPages = isMobile.value ? 3 : isDesktop.value ? 7 : 3;
  const range = Math.floor(maxPages / 2);
  let start = props.currentPage - range;
  let end = props.currentPage + range;

  start = Math.max(1, start);
  end = Math.min(pageCount.value, end);

  const diffStart = maxPages - (end - start + 1);
  if (diffStart > 0) {
    start = Math.max(start - diffStart, 1);
  }

  const diffEnd = maxPages - (end - start + 1);
  if (diffEnd > 0) {
    end = Math.min(end + diffEnd, pageCount.value);
  }

  return Array.from({ length: end - start + 1 }, (_, i) => start + i);
});



</script>

<template>
  <div class="mt-6 flex items-center justify-center" v-if="objectCount > perPage">
    <nav aria-label="Page navigation example">
      <ul class="flex h-10 items-center text-base -space-x-px">
        <li>
          <button :disabled="isAtFirstPage" @click="$emit('pageChange', currentPage - 1)"
                  class="ml-0 flex h-10 items-center justify-center rounded-l-lg border border-gray-300 bg-white px-4 leading-tight text-gray-500 hover:bg-gray-100 hover:text-gray-700 disabled:bg-gray-200 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
            <span class="sr-only">Previous</span>
            <svg class="mr-2 h-3 w-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                 viewBox="0 0 6 10">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M5 1 1 5l4 4"/>
            </svg>
            {{ previousLabel }}
          </button>
        </li>

        <li v-for="i in visiblePageRange" :key="i">
          <a href="#" v-if="i === currentPage" @click.prevent="$emit('pageChange', i)"
             class="z-10 flex h-10 items-center justify-center border border-blue-300 bg-blue-50 px-4 leading-tight text-blue-600 hover:bg-blue-100 hover:text-blue-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white">
            {{ i }}
          </a>
          <a href="#" v-else @click.prevent="$emit('pageChange', i)"
             aria-current="page"
             class="flex h-10 items-center justify-center border border-gray-300 bg-white px-4 leading-tight text-gray-500 hover:bg-gray-100 hover:text-gray-700 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
            {{ i }}
          </a>
        </li>

        <li>
          <button :disabled="isAtLastPage" @click="$emit('pageChange', currentPage + 1)"
                  class="flex h-10 items-center justify-center rounded-r-lg border border-gray-300 bg-white px-4 leading-tight text-gray-500 hover:bg-gray-100 hover:text-gray-700 disabled:bg-gray-200 dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
            <span class="sr-only">Next</span>
            {{ nextLabel }}
            <svg class="ml-2 h-3 w-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                 viewBox="0 0 6 10">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="m1 9 4-4-4-4"/>
            </svg>
          </button>
        </li>
      </ul>
    </nav>
  </div>
</template>

<style scoped>

</style>
