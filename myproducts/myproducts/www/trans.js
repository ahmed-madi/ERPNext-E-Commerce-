$(function() {
    $(".addCart").click(function(e) {
        //e.preventDefault;

        var inp = $(this).parent().parent().find("input").val();
        var qty = $(this).parent().parent().find(".avail").text();
        qty = parseInt(qty);
        inp = parseInt(inp);
        //alert(qty);
        if(inp == "" || inp ==0 || isNaN(inp) ){
            alert("Please insert a quantity");
        }
        else if (qty == "" ||inp == 0 || isNaN(inp)){
           alert("No more items available of this product")
        }
        else if (inp > qty){
            alert("Please insert an available quantity");
        }
        else {
            // if (inp )
            var clickedid = this.id;
            var price = $(this).parent().parent().find(".price").text();
            var forAction = $(this).parent().parent().find(".avail");
            price = parseInt(price);
            // var first_name = $("#first_name").val();
            // var username = $("#username").val();
            // var password = $("#password").val();
            // var phone = $("#phone").val();
            // var last_name = $("#last_name").val();

            // alert(inp);
            // var str = JSON.stringify({"email": email, "first_name": first_name, "username": username, "new_password": password});
            // //console.log(str);
            // var post = { "data": str };
            //
            if (confirm(" The price of this transaction is" + price*inp +" $ Are you sure")) {

                $.post('/api/method/myproducts.www.shopcart.addToShopcart',
                    {id: clickedid, qty: inp, price: price},
                    function (data) {
                    forAction.text(qty - inp+" ");

                    });
            }
            // $.ajax({
            //     url:"http://localhost:8000/api/method/myproducts.www.shopcart.list",
            //     type : "POST",
            //     data : {id:clickedid},
            //     dataType : "jsonp"
            //
            //
            // });

        }
        return false;
    });
    // $("#view").click(function(e){
    // 	e.preventDefault();
    // 	$.getJSON('http://0.0.0.0:8004/api/resource/Person',function(data){
    // 		$("body").append("<ul></ul>");
    // 		for(var i in data.data){
    // 			var obj = data.data[i];
    // 			$("ul").append("<li>"+obj.fullname+" "+obj.age+"</li>");

    // 		}
    // 	});
    // "phone":phone,"last_name":last_name
    // });
});
