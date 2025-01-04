import { IProduct } from "../../dto";
import Link from "next/link";
import { urlFor } from "../../lib/client";

interface Props {
  product: IProduct;
}

const Product = ({ product: { id,image, titulo, precio } }: Props) => {
  return (
    <div>
      {/* <Link href={`/productos/${slug.current}`}> */}
      <Link href={`/productos/${id}`}>
        <div className="product-card">
          <img
            src={(image ||image[0]).toString()}
            width={250}
            height={250}
            className="product-image"
          />
          <p className="product-name">{titulo}</p>
          <p className="product-price">${precio}</p>
        </div>
      </Link>
    </div>
  );
};

export default Product;
