<script setup lang="ts">

</script>

<template>
  <footer
      class="w-full p-4 bg-white border-t border-gray-200 shadow md:flex md:items-center md:justify-between md:p-6 dark:bg-gray-800 dark:border-gray-600">
    <span class="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2023 Řemeslo v kostce. Všechna práva vyhrazena.
    </span>
    <ul class="flex flex-wrap items-center mt-3 text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0">
      <li>
        <RouterLink to="/#about" active-class="" class="mr-4 hover:underline md:mr-6">
          O nás
        </RouterLink>
      </li>
      <li>
        <RouterLink to="/katalog" active-class="" class="mr-4 hover:underline md:mr-6">
          Katalog
        </RouterLink>
      </li>
      <li>
        <RouterLink to="/#contact" active-class="" class="mr-4 hover:underline md:mr-6">
          Kontakt
        </RouterLink>
      </li>
    </ul>
  </footer>
</template>

<style scoped>

</style>
