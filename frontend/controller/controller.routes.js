import axios from 'axios';
import dotenv from 'dotenv';
//require('dotenv').config();

const getProducts = async () => {
    try {
        const response = await axios.get(`${process.env.API_BASE_URL}/productos`);
        return response.data;
    } catch (error) {
        console.error('Error fetching products:', error);
        throw error;
    }
};

const getSimilarProducts = async (productID) => {
    try {
        const response = await axios.post(`${process.env.API_BASE_URL}/productos/similares/${productID}`);
        return response.data;
    } catch (error) {
        console.error('Error calling API:', error);
        throw error;
    }
};
const getDetails = async (product) => {
    try {
        const response = await axios.post(`${process.env.API_BASE_URL}/product/${product}`);
        return response.data;
    } catch (error) {
        console.error('Error calling API:', error);
        throw error;
    }
};

module.exports = {
    getProducts,
    getSimilarProducts,
    getDetails
};