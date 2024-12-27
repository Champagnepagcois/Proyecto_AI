import { useState } from "react";
import { client, urlFor } from "../../lib/client";
import { useRef } from 'react';

import { Toast } from 'primereact/toast';
        
import {
  AiOutlineMinus,
  AiOutlinePlus,
  AiFillStar,
  AiOutlineStar,
} from "react-icons/ai";
import { Product } from "../../components";
import { useStateContext } from "../../context/StateContext";

const ProductDetails = ({ product, products }: any) => {
  const toast = useRef<Toast>(null);
  const { image, name, details, price } = product;
  const [index, setIndex] = useState(0);
  const { decreaseQty, increaseQty, qty, onAdd } = useStateContext();

  const handleClickTest = () => {
    toast.current?.show({severity:'success', summary: 'Success', detail:'Message Content', life: 3000});
  };

  return (
    <div>
      <Toast ref={toast} />
      <div className="product-detail-container">
        <div>
          <div className="image-container">
            <img
              src={urlFor(image && image[index]).toString()}
              className="product-detail-image"
            />
          </div>
          <div className="small-images-container">
            {image?.map((item: any, i: number) => (
              <img
                key={i}
                src={urlFor(item).toString()}
                className={
                  i === index ? "small-image selected-image" : "small-image"
                }
                onMouseEnter={() => {
                  setIndex(i);
                }}
              />
            ))}
          </div>
        </div>

        <div className="product-detail-desc">
          <h1>{name}</h1>
          <div className="reviews">
            <div>
              <AiFillStar />
              <AiFillStar />
              <AiFillStar />
              <AiFillStar />
              <AiOutlineStar />
            </div>
            <p>(20)</p>
          </div>
          <h4>Detalles: </h4>
          <p>{details}</p>
          <p className="price">${price}</p>

          <div className="quantity">
            <h3>Cantidad</h3>
            <p className="quantity-desc">
              <span className="minus" onClick={decreaseQty}>
                <AiOutlineMinus />
              </span>
              <span className="num" onClick={() => {}}>
                {qty}
              </span>
              <span className="plus" onClick={increaseQty}>
                <AiOutlinePlus />
              </span>
            </p>
          </div>

          <div className="buttons">
            <button
              type="button"
              className="add-to-cart"
              onClick={() => onAdd(product, qty)}
            >
              Agregar al carrito
            </button>
            <button type="button" className="buy-now" onClick={handleClickTest}>
              Comprar Ahora
            </button>
          </div>
        </div>
      </div>

      <div className="maylike-products-wrapper">
        <h2>Productos relacionados</h2>
        <div className="list_products_like">
          <div className="maylike-products-container track">
            {products.concat(products).map((item: any) => (
              <Product key={item._id} product={item} />
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export const getStaticPaths = async () => {
  const query = `*[_type == "product"] {
    slug {
      current
    }
  }
  `;

  const products = await client.fetch(query);
  const paths = products.map((product: any) => ({
    params: {
      slug: product.slug.current,
    },
  }));

  return {
    paths,
    fallback: "blocking",
  };
};

export const getStaticProps = async ({ params }: any) => {
  const query = `*[_type == "product" && slug.current == '${params.slug}'][0]`;
  const productsQuery = '*[_type == "product"]';

  const product = await client.fetch(query);
  const products = await client.fetch(productsQuery);

  return {
    props: { product, products },
  };
};

export default ProductDetails;
