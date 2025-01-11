console.log("working fine");
/*
$("#commentForm").submit(function(e){
    e.preventDefault();

    $.ajax({
        data: $(this).serialize(),     
        
        method: $(this).attr("method"),

        url: $(this).attr("action"),

        dataType: "json",
        
        success: function(response){
            console.log("Comment Save to DB...")

        },
        error: function(xhr, status, error) {
            console.error("AJAX error:", status, error);
        }
    })


})*/

//add to cart
/*
$(document).ready(function () {
    console.log("DOM is ready!");

    $("#add-to-cart-btn").on("click", function () {
        let quantity = $("#product-quantity").val();
        let product_title = $(".product-title").val();
        let product_id = $(".product-id").val();
        let product_price = $(".current-product-price").text();
        let this_val = $(this);

        console.log("Quantity:", quantity);
        console.log("Title:", product_title);
        console.log("Price:", product_price);
        console.log("Id:", product_id);
        console.log("Current element:", this_val);
    });
});

*/