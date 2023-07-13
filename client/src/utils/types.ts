interface ProductCategory {
    id: Number,
    name: string,
    description: string,
    products: number;
}

interface ProductSize {
    sheetCount: number | null,
    width: number,
    height: number | null,
    depth: number,
    unit: 'mm' | 'cm' | 'm',
}

interface ProductColor {
    label: string,
    hex: string,
}

interface Product {
    id: number,
    category: ProductCategory,
    name: string,
    displayName: string,
    description: string,
    tags: string[],
    size: ProductSize,
    color: ProductColor,
    thumbnail: string | null,
}
