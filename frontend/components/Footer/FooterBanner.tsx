import { IBanner } from "../../dto";
import Link from "next/link";
import { urlFor } from "../../lib/client";

interface Props {
  footerBanner: IBanner;
}

const FooterBanner = ({ footerBanner }: Props) => {
  return (
    <div className="footer-banner-container">
      <div className="banner-desc">
        <div className="left">
          <p>{footerBanner.product.split(' ').slice(0,3).join(' ') || "discontr"}</p>
          <h3>{footerBanner.largeText1||"Promoción"}</h3>
          {/* <h3>{footerBanner.largeText2 ||"enero"}</h3> */}
          <p>{footerBanner.category||"saleTime"}</p>
        </div>
        <div className="right">
          <p>{footerBanner.smallText || "Descuento del"}</p>
          <h3>{footerBanner.discount ||"midText"}</h3>
          <p>{footerBanner.description.split(' ').slice(3,6).join(' ')}</p>
          <Link href={`/product/${footerBanner.product}`}>
            <button type="button">{footerBanner.buttonText || "comprar ahora"}</button>
          </Link>
        </div>
        <img
          src={(footerBanner.image).toString()}
          className="footer-banner-image"
        />
      </div>
    </div>
  );
};

export default FooterBanner;
