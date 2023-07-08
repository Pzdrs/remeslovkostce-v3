<script setup lang="ts">
import {Dropdown, ListGroup, ListGroupItem} from "flowbite-vue";
import FooterComponent from "@/components/FooterComponent.vue";
import NavbarComponent from "@/components/NavbarComponent.vue";
</script>

<template>
  <NavbarComponent/>
  <RouterView v-slot="{Component}">
    <Component :is="Component"/>
  </RouterView>
  <FooterComponent/>
</template>

<style scoped>

</style>
