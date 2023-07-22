import {createRouter, createWebHistory} from "vue-router";
import LandingPage from "@/views/LandingPage.vue";
import CatalogueView from "@/views/CatalogueView.vue";
import ProductDetailView from "@/views/ProductDetailView.vue";

const TITLE_SUFFIX = 'Řemeslo v kostce';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    linkActiveClass: "block py-2 pl-3 pr-4 text-white bg-blue-700 rounded md:bg-transparent md:text-blue-700 md:p-0 md:dark:text-blue-500",
    routes: [
        {
            path: "/",
            name: 'home',
            component: LandingPage,
            meta: {
                navbar: true,
                title: 'Domů'
            }
        },
        {
            path: "/katalog",
            name: "catalogue",
            component: CatalogueView,
            meta: {
                navbar: true,
                title: 'Katalog'
            }
        },
        {
            path: '/produkt/:id',
            name: 'product-detail',
            component: ProductDetailView
        }
    ]
});

router.beforeEach((toRoute, fromRoute, next) => {
    window.document.title = toRoute.meta && toRoute.meta.title ? `${toRoute.meta.title} | ${TITLE_SUFFIX}` : TITLE_SUFFIX;
    next();
})

export default router;
