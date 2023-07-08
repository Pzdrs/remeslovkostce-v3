<script setup lang="ts">

</script>

<template>
  <section>
    <h1 class="text-3xl font-bold text-center">Kontakt</h1>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-4 lg:mx-32 my-4  ">
      <div class="flex flex-col items-center my-4">
        <span class="bg-gray-100 p-4 rounded-md">
         <svg class="w-8 h-8 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
              fill="#374151" viewBox="0 0 16 20">
          <path
              d="M8 0a7.992 7.992 0 0 0-6.583 12.535 1 1 0 0 0 .12.183l.12.146c.112.145.227.285.326.4l5.245 6.374a1 1 0 0 0 1.545-.003l5.092-6.205c.206-.222.4-.455.578-.7l.127-.155a.934.934 0 0 0 .122-.192A8.001 8.001 0 0 0 8 0Zm0 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6Z"/>
          </svg>
        </span>
        <h2 class="font-bold text-xl my-2">Informace o společnosti:</h2>
        <ul class="flex flex-col items-center justify-center">
          <li class="text-neutral-500 text-lg">Jatecká 399</li>
          <li class="text-neutral-500 text-lg">Mšeno</li>
          <li class="text-neutral-500 text-lg">277 35</li>
          <li class="text-neutral-500 text-lg">Česká Republika</li>
        </ul>
      </div>

      <div class="flex flex-col items-center my-4">
        <span class="bg-gray-100 p-4 rounded-md">
          <svg class="w-8 h-8 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
               fill="#374151" viewBox="0 0 20 16">
            <path d="m10.036 8.278 9.258-7.79A1.979 1.979 0 0 0 18 0H2A1.987 1.987 0 0 0 .641.541l9.395 7.737Z"/>
            <path
                d="M11.241 9.817c-.36.275-.801.425-1.255.427-.428 0-.845-.138-1.187-.395L0 2.6V14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2.5l-8.759 7.317Z"/>
          </svg>
        </span>
        <h2 class="font-bold text-xl my-2">Kontakt:</h2>
        <ul class="flex flex-col items-center justify-center">
          <li class="text-neutral-500 text-lg">+420 315 693 889</li>
          <li class="text-neutral-500 text-lg">
            <a href="mailto:obchod@remeslovkostce.cz" class="underline text-blue-600">obchod@remeslovkostce.cz</a>
          </li>
        </ul>
      </div>

      <div class="flex flex-col items-center my-4">
        <span class="bg-gray-100 p-4 rounded-md">
        <svg class="w-8 h-8 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
             fill="#374151" viewBox="0 0 20 20">
         <path
             d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
        </svg>
        </span>
        <h2 class="font-bold text-xl my-2">Ostatní informace:</h2>
        <ul class="flex flex-col items-center justify-center">
          <li class="text-neutral-500 text-lg">IČ: 10161171</li>
          <li class="text-neutral-500 text-lg">DIČ: CZ6703151488</li>
        </ul>
      </div>
    </div>
  </section>
</template>

<style scoped>

</style>
