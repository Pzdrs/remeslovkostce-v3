<script setup lang="ts">

</script>

<template>
  <section id="contact">
    <h1 class="text-3xl font-bold text-center">Kontaktujte nás</h1>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-4 lg:mx-32 my-4  ">
      <div class="flex flex-col items-center my-4">
        <span class="bg-gray-100 p-4 rounded-md">
           <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960"
                class="w-8 h-8 text-gray-800 dark:text-white" fill="#374151"><path
               d="M80-120v-560l400-160 400 160v560H640v-320H320v320H80Zm290 0v-60h60v60h-60Zm80-120v-60h60v60h-60Zm80 120v-60h60v60h-60Z"/></svg>
        </span>
        <h2 class="font-bold text-xl my-2">Informace o společnosti:</h2>
        <ul class="flex flex-col items-center justify-center">
          <li class="text-neutral-500 text-lg">IČ: 10161171</li>
          <li class="text-neutral-500 text-lg">DIČ: CZ6703151488</li>
        </ul>
      </div>

      <div class="flex flex-col items-center my-4">
        <span class="bg-gray-100 p-4 rounded-md">
           <svg class="w-8 h-8 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                fill="#374151" viewBox="0 0 16 20">
          <path
              d="M8 0a7.992 7.992 0 0 0-6.583 12.535 1 1 0 0 0 .12.183l.12.146c.112.145.227.285.326.4l5.245 6.374a1 1 0 0 0 1.545-.003l5.092-6.205c.206-.222.4-.455.578-.7l.127-.155a.934.934 0 0 0 .122-.192A8.001 8.001 0 0 0 8 0Zm0 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z"/>
          </svg>
        </span>
        <h2 class="font-bold text-xl my-2">Adresa:</h2>
        <ul class="flex flex-col items-center justify-center">
          <li class="text-neutral-500 text-lg">Jatecká 399</li>
          <li class="text-neutral-500 text-lg">277 35, Mšeno</li>
          <li class="text-neutral-500 text-lg">Česká Republika</li>
        </ul>
      </div>

      <div class="flex flex-col items-center my-4">
        <span class="bg-gray-100 p-4 rounded-md">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -960 960 960"
               class="w-8 h-8 text-gray-800 dark:text-white" fill="#374151"><path
              d="M798-120q-129 0-251.5-57.5t-217-152q-94.5-94.5-152-217T120-798q0-18 12-30t30-12h162q14 0 25 9t13 23l26 140q2 14-.5 25.5T376-622l-96 98q42 72 105 135t139 109l94-94q9-9 23.5-13.5T670-390l138 28q14 3 23 13.5t9 24.5v162q0 18-12 30t-30 12Z"/>
          </svg>
        </span>
        <h2 class="font-bold text-xl my-2">Kontakt:</h2>
        <ul class="flex flex-col items-center justify-center">
          <li class="text-neutral-500 text-lg">+420 315 693 889</li>
          <li class="text-neutral-500 text-lg">
            <a href="mailto:obchod@remeslovkostce.cz" class="font-bold text-black hover:underline">petr.bohac@remeslovkostce.cz</a>
          </li>
        </ul>
      </div>


    </div>
  </section>
</template>

<style scoped>

</style>
