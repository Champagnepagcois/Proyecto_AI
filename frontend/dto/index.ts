export interface IProduct {
  id: string;
  image: any;
  name: string;
  category:string;
 /*  slug: {
    current: string;
  }; */
  price: number;
  rating: number;
  /* quantity: number;
  details: string; */
}

export interface IBanner {
  id: string;
  image: any;
  buttonText: string;
  product: string;
  description: string;
  smallText: string;
  midText: string;
  largeText1: string;
  largeText2: string;
  discount: string;
  saleTime: string;
  category: string;
}