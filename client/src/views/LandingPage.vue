<script setup lang="ts">

import FooterComponent from "@/components/FooterComponent.vue";
import NavbarComponent from "@/components/NavbarComponent.vue";
import CarouselComponent from "@/components/CarouselComponent.vue";
import ContactComponent from "@/components/ContactComponent.vue";
</script>

<template>
  <section class="relative bg-white dark:bg-gray-900">
    <div id="about" class="py-8 px-4 mx-auto max-w-screen-xl text-center lg:py-16 lg:px-12">
      <h1 class="mb-4 text-4xl font-extrabold tracking-tight leading-none text-gray-900 md:text-5xl lg:text-6xl dark:text-white">
        Vítejte na stránkách Řemeslo v kostce
      </h1>
      <p class="mb-8 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 xl:px-48 dark:text-gray-400">
        <span class="font-bold">ŘEMESLO V KOSTCE</span> je ryze výrobní firma zaměřená především na zpracování papíru.
        Kancelářské potřeby a reklamní
        předměty spotřebního charakteru vyrábíme od roku 1997.
      </p>
      <p class="mb-8 text-lg font-normal text-gray-500 lg:text-xl sm:px-16 xl:px-48 dark:text-gray-400">
        Naše zboží lze zakoupit v celé řadě obchodů po celé ČR. Pokud máte zájem o velkoobchodní podmínky prodeje,
        prosím kontaktujte nás na
        <a href="mailto:obchod@remeslovkostce.cz" class="font-bold">obchod@remeslovkostce.cz</a>.
      </p>
      <div class="flex flex-col mb-8 lg:mb-16 space-y-4 sm:flex-row sm:justify-center sm:space-y-0 sm:space-x-4">
        <RouterLink to="/katalog"
                    class="inline-flex items-center justify-center px-5 py-3 text-base font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 dark:focus:ring-blue-900">
          Katalog
          <svg class="w-3.5 h-3.5 ml-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
               viewBox="0 0 14 10">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M1 5h12m0 0L9 1m4 4L9 9"/>
          </svg>
        </RouterLink>
      </div>
    </div>

    <CarouselComponent/>

    <ContactComponent/>
  </section>
</template>

<style scoped>

</style>
