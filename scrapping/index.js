const { chromium } = require('playwright');
const fs = require('fs');

async function scrapeData(category, url) {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();

    console.log(`Navegando a la URL: ${url}`);
    await page.goto(url);

    // Esperar a que los productos carguen
    await page.waitForSelector('.s-product-image-container');

    // Extraer datos de los productos
    const data = await page.$$eval('.a-section.a-spacing-base', (products, category) => {
        return products.map(product => {
            try {
                // Título
                const title = product.querySelector('h2 span')?.innerText || "No disponible";

                // Precio
                const priceWhole = product.querySelector('.a-price-whole')?.innerText || "";
                const priceFraction = product.querySelector('.a-price-fraction')?.innerText || "00";
                const price = priceWhole ? `${priceWhole}.${priceFraction}` : "No disponible";

                // Rating
                const rating = product.querySelector('.a-icon-alt')?.innerText || "Sin calificación";

                // Link del producto
                const link = product.querySelector('a.a-link-normal')?.getAttribute('href') || "No disponible";
                const fullLink = link !== "No disponible" ? `https://www.amazon.com.mx${link}` : "No disponible";

                // Imagen
                const image = product.querySelector('img.s-image')?.getAttribute('src') || "No disponible";

                return {
                    title,
                    price,
                    rating,
                    link: fullLink,
                    category,
                    image
                };
            } catch (error) {
                console.error("Error al procesar un producto:", error);
                return null;
            }
        }).filter(item => item !== null); // Eliminar productos con error
    }, category);

    // Cerrar el navegador
    await browser.close();

    // Guardar datos en un archivo JSON
    const fileName = `buscados/${category}.json`;
    fs.writeFileSync(fileName, JSON.stringify(data, null, 4), 'utf-8');
    console.log(`Datos de ${data.length} productos guardados en ${fileName}`);
}

// Validar argumentos desde la consola
if (process.argv.length < 4) {
    console.error("Uso: node scrape_amazon.js <categoria> <url>");
    process.exit(1);
}

const category = process.argv[2];
const url = process.argv[3];

// Ejecutar el scraping
scrapeData(category, url).catch(err => {
    console.error("Error durante el scraping:", err);
});
