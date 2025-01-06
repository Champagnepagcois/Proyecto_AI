import { Product, FooterBanner, HeroBanner } from "../components";
import { IBanner, IProduct } from "../dto";
import {getProducts,
  getSimilarProducts,
  getProductBanner,
  getDetails} from "../controller/controller.routes";

interface Props {
  products: IProduct[];
  bannerData: IBanner[];
}

const Home = ({ products, bannerData }: Props) => {
  return (
    <>
      <HeroBanner heroBanner={bannerData && bannerData[0]} />

      <div className="products-heading">
        <h2>Los productos mas famosos</h2>
        <br/>
      </div>
      <div className="products-container">
        {products.map((product) => (
          <Product key={product.id} product={product} />
        ))}
      </div>

      <FooterBanner footerBanner={bannerData && bannerData[0]} />
    </>
  );
};

export const getServerSideProps = async () => {
  const products = await getProducts();
  const bannerData = await getProductBanner();

  return {
    props: { products, bannerData },
  };
};

export default Home;
