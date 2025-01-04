import { Product, FooterBanner, HeroBanner } from "../components";
import { IBanner, IProduct } from "../dto";
import { client } from "../lib/client";
import {getProducts,
  getSimilarProducts,
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
        <h2>Best Selling Products</h2>
        <p>Speakers of many variations</p>
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
  //const query = '*[_type == "product"]';
  const products = await getProducts();

  //const bannerQuery = '*[_type == "banner"]';
  //const bannerData = await client.fetch(bannerQuery);
  const bannerData = await getProducts();
  console.log("Data bannerData--------------------")
  console.log(bannerData);

  return {
    props: { products, bannerData },
  };
};

export default Home;
