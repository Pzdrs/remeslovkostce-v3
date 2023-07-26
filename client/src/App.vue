<script setup lang="ts">
import FooterComponent from "@/components/FooterComponent.vue";
import NavbarComponent from "@/components/NavbarComponent.vue";
</script>

<template>
  <NavbarComponent/>
  <div class="flex min-h-screen flex-col">
    <main class="flex-grow">
      <RouterView v-slot="{Component}" :key="$route.fullPath">
        <Component :is="Component"/>
      </RouterView>
    </main>
    <FooterComponent/>
  </div>
</template>

<style scoped>

</style>
