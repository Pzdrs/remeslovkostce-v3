<script setup lang="ts">
defineProps<{
  to: string,
  label: string
}>()
</script>

<template>
  <RouterLink
      :to="to"
      class="block rounded py-2 pr-4 pl-3 text-gray-900 hover:bg-gray-100 dark:border-gray-700 dark:text-white md:p-0 dark:hover:bg-gray-700 dark:hover:text-white md:hover:bg-transparent md:hover:text-blue-700 md:dark:hover:bg-transparent md:dark:hover:text-blue-500"
  >{{ label }}
  </RouterLink>
</template>

<style scoped>

</style>
