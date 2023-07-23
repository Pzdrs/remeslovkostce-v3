<script setup lang="ts">

</script>

<template>
  <footer
      class="w-full border-t border-gray-200 bg-white p-4 shadow dark:border-gray-600 dark:bg-gray-800 md:flex md:items-center md:justify-between md:p-6">
    <span class="text-sm text-gray-500 dark:text-gray-400 sm:text-center">© 2023 Řemeslo v kostce. Všechna práva vyhrazena.
    </span>
    <ul class="mt-3 flex flex-wrap items-center text-sm font-medium text-gray-500 dark:text-gray-400 sm:mt-0">
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
