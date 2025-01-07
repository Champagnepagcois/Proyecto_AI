import { IProduct } from "../../dto";
import Link from "next/link";
import { urlFor } from "../../lib/client";

interface Props {
  product: IProduct;
}

const Product = ({ product: { id,image, name, price } }: Props) => {
  return (
    <div>
      {/* <Link href={`/productos/${slug.current}`}> */}
      <Link href={`/productos/${id}`}>
        <div className="product-card">
          <img
            src={image}
            width={250}
            height={250}
            className="product-image"
          />
          <div className="product-name-card">
            <p className="product-name">{name}</p>
            <span className="tooltip-text-product-name">{name}</span>
          </div>
          <p className="product-price">${price}</p>
        </div>
      </Link>
    </div>
  );
};

export default Product;
