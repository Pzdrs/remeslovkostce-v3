<script setup lang="ts">
import {computed} from "vue";

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

function previousPage() {
  console.log('previousPage')
}

function nextPage() {
  console.log('nextPage')
}
</script>

<template>
  <div class="flex items-center justify-center mt-6" v-if="objectCount > perPage">
    <nav aria-label="Page navigation example">
      <ul class="flex items-center -space-x-px h-10 text-base">
        <li>
          <button :disabled="isAtFirstPage" @click="$emit('pageChange', currentPage - 1)"
                  class="disabled:bg-gray-200 flex items-center justify-center px-4 h-10 ml-0 leading-tight text-gray-500 bg-white border border-gray-300 rounded-l-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
            <span class="sr-only">Previous</span>
            <svg class="w-3 h-3 mr-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                 viewBox="0 0 6 10">
              <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M5 1 1 5l4 4"/>
            </svg>
            {{ previousLabel }}
          </button>
        </li>
        <li v-for="i in pageCount" :key="i">
          <a href="#" v-if="i === currentPage" @click.prevent="$emit('pageChange', i)"
             class="z-10 flex items-center justify-center px-4 h-10 leading-tight text-blue-600 border border-blue-300 bg-blue-50 hover:bg-blue-100 hover:text-blue-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white">
            {{ i }}
          </a>
          <a href="#" v-else @click.prevent="$emit('pageChange', i)"
             aria-current="page"
             class="flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
            {{ i }}
          </a>
        </li>
        <li>
          <button :disabled="isAtLastPage" @click="$emit('pageChange', currentPage + 1)"
                  class="disabled:bg-gray-200 flex items-center justify-center px-4 h-10 leading-tight text-gray-500 bg-white border border-gray-300 rounded-r-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
            <span class="sr-only">Next</span>
            {{ nextLabel }}
            <svg class="w-3 h-3 ml-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
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
