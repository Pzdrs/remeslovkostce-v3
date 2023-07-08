<script setup lang="ts">
import {Dropdown, ListGroup, ListGroupItem} from "flowbite-vue";
import FooterComponent from "@/components/FooterComponent.vue";
import NavbarComponent from "@/components/NavbarComponent.vue";
</script>

<template>
  <NavbarComponent/>
  <div class="flex flex-col min-h-screen">
    <main class="flex-grow">
      <RouterView v-slot="{Component}">
        <Component :is="Component"/>
      </RouterView>
    </main>

    <FooterComponent/>
  </div>
</template>

<style scoped>

</style>
