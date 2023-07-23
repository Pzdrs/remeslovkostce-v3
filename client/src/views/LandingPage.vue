<script setup lang="ts">
import CarouselComponent from "@/components/CarouselComponent.vue";
import ContactComponent from "@/components/ContactComponent.vue";
</script>

<template>
  <section class="relative bg-white dark:bg-gray-900">
    <div id="about" class="mx-auto max-w-screen-xl px-4 py-8 text-center lg:px-12 lg:py-16">
      <h1 class="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 dark:text-white md:text-5xl lg:text-6xl">
        Vítejte na stránkách Řemeslo v kostce
      </h1>
      <p class="mb-8 text-lg font-normal text-gray-500 dark:text-gray-400 sm:px-16 lg:text-xl xl:px-48">
        <span class="font-bold">ŘEMESLO V KOSTCE</span> je ryze výrobní firma zaměřená především na zpracování papíru.
        Kancelářské potřeby a reklamní
        předměty spotřebního charakteru vyrábíme od roku 1997.
      </p>
      <p class="mb-8 text-lg font-normal text-gray-500 dark:text-gray-400 sm:px-16 lg:text-xl xl:px-48">
        Naše zboží lze zakoupit v celé řadě obchodů po celé ČR. Pokud máte zájem o velkoobchodní podmínky prodeje,
        prosím kontaktujte nás na
        <a href="mailto:obchod@remeslovkostce.cz" class="font-bold">obchod@remeslovkostce.cz</a>.
      </p>
      <div class="mb-8 flex flex-col space-y-4 sm:space-y-0 sm:space-x-4 sm:flex-row sm:justify-center lg:mb-16">
        <RouterLink :to="{name: 'catalogue'}"
                    class="inline-flex items-center justify-center rounded-lg bg-blue-700 px-5 py-3 text-center text-base font-medium text-white hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 dark:focus:ring-blue-900">
          Katalog
          <svg class="ml-2 w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
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
