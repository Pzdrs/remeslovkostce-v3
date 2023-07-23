import {reactive} from 'vue'
import axios from "@/axios";

export const store = reactive({
    categories: [] as ProductCategory[],
    products: [] as Product[],
});

export function fetchCategories() {
    return axios.get('/categories');
}

export function fetchProducts() {
    return axios.get('/products')
}

export function fetchProduct(id: number) {
    return axios.get(`/products/${id}`)
}

export function getProductCategory(id: number): ProductCategory | undefined {
    return store.categories.find(category => category.id === id);
}

export function deserializeProduct(product: any) {
    return {
        id: product.id,
        category: getProductCategory(product.category),
        displayName: product.display_name,
        description: product.description,
        tags: product.tags,
        size: {
            sheetCount: product.size.sheetCount,
            width: product.size.width,
            height: product.size.height,
            depth: product.size.depth,
            unit: product.size.unit,
            dimensions_display_name: product.size.dimensions_display_name
        },
        color: {
            label: product.color.label,
            hex: product.color.hex,
        },
        thumbnail: product.thumbnail
    }
}

export function deserializeProductDetail(product: any): Product {
    return <Product>{
        id: product.id,
        category: getProductCategory(product.category),
        displayName: product.display_name,
        description: product.description,
        tags: product.tags,
        size: {
            sheetCount: product.size.sheetCount,
            width: product.size.width,
            height: product.size.height,
            depth: product.size.depth,
            unit: product.size.unit,
            dimensions_display_name: product.size.dimensions_display_name
        },
        color: {
            label: product.color.label,
            hex: product.color.hex,
        },
        thumbnail: product.thumbnail,
        images: product.images,
        variants: product.variants,
    }
}

export function deserializeProductCategory(category: any) {
    return {
        id: category.id,
        name: category.name,
        description: category.description,
        products: category.products
    }
}

