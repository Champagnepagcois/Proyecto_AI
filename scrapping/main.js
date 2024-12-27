const { chromium } = require("playwright");
const fs = require("fs");

(async () => {
  // Obtener el parámetro desde la consola
  const args = process.argv.slice(2);
  const nombre_categoria = args[0] || "No disponible"; // Usa un valor predeterminado si no se pasa un argumento
  const url_page = args[1] || "";

  // Iniciar el navegador y abrir una nueva página
  const browser = await chromium.launch({ headless: true }); // Cambiar a `false` para depuración
  const page = await browser.newPage();

  // Navegar a la página deseada
  await page.goto(url_page);

  // Seleccionar todos los productos dentro de la sección principal
  const productos = await page.$$(".p13n-gridRow .a-cardui");

  // Lista para almacenar la información de los productos
  const productosData = [];

  // Iterar sobre los productos y extraer información
  for (const producto of productos) {
    const titulo = await producto
      .$eval(".a-link-normal ._cDEzb_p13n-sc-css-line-clamp-3_g3dy1", (el) =>
        el.innerText.trim()
      )
      .then((text) => (text.length > 100 ? text.slice(0, 100) + "..." : text)) // Limita a 100 caracteres y agrega "..."
      .catch(() => "No disponible");

    const precio = await producto
      .$eval("._cDEzb_p13n-sc-price_3mJ9Z", (el) => el.innerText)
      .catch(() => "No disponible");

    const rating = await producto
      .$eval(".a-icon-alt", (el) => el.innerText)
      .catch(() => "No disponible");

    const link = await producto
      .$eval("a.a-link-normal", (el) => el.href)
      .catch(() => "No disponible");

    const categoria = await producto
      .$eval("._cDEzb_p13n-sc-category_3O-OU", (el) => el.innerText)
      .catch(() => nombre_categoria);

    const imagen = await producto
      .$eval(
        "div.a-section.a-spacing-mini._cDEzb_noop_3Xbw5 img",
        (el) => el.src
      )
      .catch(() => "No disponible");

    // Agregar los datos del producto a la lista
    productosData.push({
      titulo,
      precio,
      rating,
      link,
      categoria,
      imagen,
    });
  }

  // Guardar los datos en un archivo JSON
  const jsonPath = `./productos/${nombre_categoria}.json`;
  fs.writeFileSync(jsonPath, JSON.stringify(productosData, null, 2));
  console.log(`Información guardada en: ${jsonPath}`);

  // Cerrar el navegador
  await browser.close();
})();
