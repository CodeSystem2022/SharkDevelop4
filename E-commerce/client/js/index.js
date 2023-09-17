// shopContent es el id, capturamos el contenedor hijo
const shopContent = document.getElementById("shopContent");
const cart = [];//Este es nuestro carrito

productos.forEach((product) => {
    const content = document.createElement("div");
    
    content.innerHTML = `
    <img src = "${product.img}">
    <h3>${product.productName}</h3>
    <p>${product.price} $</p>
    `;// Las comillas al lado de la letra P en windows

    shopContent.append(content);

    // Carrito de compras
    const buyButton = document.createElement("button");
    buyButton.innerText = "Comprar";

    //Agrego boton
    content.append(buyButton);

    //Donde se agregan los productos
    buyButton.addEventListener("click", ()=>{
        const repeat = cart.some((repeatProduct) => repeatProduct.id === product.id);
        if(repeat){
            cart.map((prod) => {
                if(prod.id === product.id){
                    prod.quanty++
                }        
            });
        } else {
            cart.push({
                id: product.id,
                productName: product.productName, 
                price: product.price,
                quanty: product.quanty,
                img: product.img,
            });
        }
        })  
});