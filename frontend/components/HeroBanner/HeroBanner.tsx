import Link from "next/link";
import { IBanner } from "../../dto";
import { urlFor } from "../../lib/client";

type Props = {
  heroBanner: IBanner;
};

const HeroBanner = ({ heroBanner }: Props) => {
  return (
    <div className="hero-banner-container">
      <div>
        <p className="beats-solo">{heroBanner.discount? 'Descuento del ' +heroBanner.discount + ' en': ''}</p>
      </div>
      <h3>{heroBanner.description.split(' ').slice(0,3).join(' ')}</h3>
      <h1>{heroBanner.largeText1 || "Promociones"}</h1>
      <img
        src={(heroBanner.image).toString()}
        alt="headphones"
        className="hero-banner-image"
      />
      {/* <div>
        <Link href={`/product/${heroBanner.product}`}>
          <button type="button">{heroBanner.buttonText || "comprar ahora"}</button>
        </Link>
        <div className="desc">
          <h5>{'Categoría '+heroBanner.category}</h5>
        </div>
      </div> */}
    </div>
  );
};

export default HeroBanner;
