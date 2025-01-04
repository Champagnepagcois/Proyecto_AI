export interface IProduct {
  id: string;
  image: any;
  titulo: string;
  categoria:string;
 /*  slug: {
    current: string;
  }; */
  precio: number;
  /* quantity: number;
  details: string; */
}

export interface IBanner {
  id: string;
  image: any;
  buttonText: string;
  product: string;
  desc: string;
  smallText: string;
  midText: string;
  largeText1: string;
  largeText2: string;
  discount: string;
  saleTime: string;
}