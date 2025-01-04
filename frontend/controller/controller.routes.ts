import axios from "axios";
import {IProduct} from '../dto/index'
const API_BASE_URL = process.env.API_BASE_URL || ""; // Asegúrate de definir esta variable en un archivo .env


export const getProducts = async (): Promise<IProduct[]> => {
  try {
    const response = await axios.get(`${API_BASE_URL}/productos`);
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error("Error fetching products:", error);
    throw error;
  }
};

export const getSimilarProducts = async (productID: string): Promise<IProduct[]> => {
  try {
    const response = await axios.post(`${API_BASE_URL}/productos/similares/${productID}`);
    return response.data;
  } catch (error) {
    console.error("Error calling API:", error);
    throw error;
  }
};

export const getDetails = async (product: string): Promise<IProduct> => {
  try {
    const response = await axios.post(`${API_BASE_URL}/product/${product}`);
    return response.data;
  } catch (error) {
    console.error("Error calling API:", error);
    throw error;
  }
};
