import "../styles/globals.css";
import type { AppProps } from "next/app";
import { Toaster } from "react-hot-toast";

import { Layout } from "../components";
import { StateContextProvider } from "../context/StateContext";

import "primereact/resources/themes/lara-light-cyan/theme.css";
import "primereact/resources/primereact.min.css";
import 'primeicons/primeicons.css';
        

import { PrimeReactProvider, PrimeReactContext } from 'primereact/api';
        

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <StateContextProvider>
      <PrimeReactProvider>
        <Layout>
          <Toaster />
          <Component {...pageProps} />
        </Layout>
        </PrimeReactProvider>
    </StateContextProvider>
  );
}

export default MyApp;
