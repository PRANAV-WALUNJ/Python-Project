$(document).ready(function() {
 
    $("#owl-demo").owlCarousel({
        
        loop:true,
        margin:10,
        autoplay:true,
        autoPlay: 1000, //Set AutoPlay to 3 seconds
   
        items : 4,
        itemsDesktop : [1199,3],
        itemsDesktopSmall : [979,3]
   
    });
   
  });

$('.navbar-nav>li>a').on('click', function(){
  $('.navbar-collapse').collapse('hide');
});


$('.plus-cart').click(function(){
  console.log("Plus Clicked");
  var id=$(this).attr("pid").toString();
  console.log("id = ",id);
  var eml=this.parentNode.children[2]
  $.ajax({
    type:"GET",
    url:"/pluscart",
    data:{
      prod_id:id
    },
    success:function(data){
      console.log("data = ",data);
      eml.innerText=data.quantity
      document.getElementById("amount").innerText="Rs. "+data.amount;
      document.getElementById("totalamount").innerText="Rs. "+data.totalamount;
    }
  })
 })
 
$('.minus-cart').click(function(){
  console.log("minus click");
  var id=$(this).attr("pid").toString();
  console.log("id = ",id);
  var eml=this.parentNode.children[2]
  $.ajax({
    type:"GET",
    url:"/minuscart",
    data:{
      prod_id:id
    },
    success:function(data){
      eml.innerText=data.quantity
      document.getElementById("amount").innerText="Rs. "+data.amount;
      document.getElementById("totalamount").innerText="Rs. "+data.totalamount;
    }
  })
})

$('.remove-cart').click(function(){
  var id=$(this).attr("pid").toString();
  var eml=this
  $.ajax({
    type:"GET",
    url:"/removecart",
    data:{
      prod_id:id
    },
    success:function(data){
      document.getElementById("amount").innerText="Rs. "+data.amount;
      document.getElementById("totalamount").innerText="Rs. "+data.totalamount;
      eml.parentNode.parentNode.parentNode.remove()
    }
  })
})
 
