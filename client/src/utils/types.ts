interface ProductCategory {
    id: number,
    name: string,
    description: string,
    products: number;
}

interface ProductImage {
    id: number,
    thumbnail: boolean,
    image: string;
}

interface ProductSize {
    sheetCount: number | null,
    width: number,
    height: number | null,
    depth: number,
    unit: 'mm' | 'cm' | 'm',
    dimensions_display_name: string;
}

interface ProductColor {
    label: string,
    hex: string | null,
}

interface VariantGroup {
    name: string,
    products: number[],
}

interface Product {
    id: number,
    category: ProductCategory,
    displayName: string,
    description: string,
    tags: string[],
    size: ProductSize,
    color: ProductColor,
    thumbnail: string | null,
    images: ProductImage[],
    variants: VariantGroup | null
}

interface Filter {
    id: number,
    type: string,
    label: string,
    callback: (product: any) => boolean;
}
