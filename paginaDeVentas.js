// paginaDeVentas.js

document.addEventListener("DOMContentLoaded", () => {
    const navLinks = document.querySelectorAll(".nav-link");
    const sections = document.querySelectorAll("main > section");
    const cartItemsDiv = document.getElementById("cart-items");
    const totalPriceSpan = document.getElementById("total-price");
    let totalPrice = 0;

    navLinks.forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const target = e.target.dataset.target;

            sections.forEach(section => {
                section.style.display = "none";
            });

            document.getElementById(target).style.display = "block";
        });
    });

    document.querySelectorAll(".add-to-cart").forEach(button => {
        button.addEventListener("click", (e) => {
            const product = e.target.closest(".producto, .oferta");
            const name = product.dataset.name;
            const price = parseFloat(product.dataset.price);
            const image = product.dataset.image;

            totalPrice += price;
            totalPriceSpan.textContent = totalPrice.toFixed(2);

            const cartItem = document.createElement("div");
            cartItem.innerHTML = `
                <img src="${image}" alt="${name}" style="max-width: 50px;">
                <p>${name} - $${price.toFixed(2)}</p>
            `;
            cartItemsDiv.appendChild(cartItem);
        });
    });
});
