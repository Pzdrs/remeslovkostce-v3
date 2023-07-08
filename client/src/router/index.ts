import {createRouter, createWebHistory} from "vue-router";
import LandingPage from "@/views/LandingPage.vue";
import CatalogueView from "@/views/CatalogueView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    linkActiveClass: "block py-2 pl-3 pr-4 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0 md:dark:text-blue-500",
    routes: [
        {
            path: "/",
            name: "Domů",
            component: LandingPage
        },
        {
            path: "/katalog",
            name: "Katalog",
            component: CatalogueView
        }
    ]
});

export default router;
