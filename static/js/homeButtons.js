
$(document).ready(function(){

    $("ol li").click(function(){
      location.href = $(this).find("a").attr("href");
    });

    // Add smooth scrolling to all links
    $(".btn").on('click', function(event) {
        
      // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
        // Prevent default anchor click behavior
        event.preventDefault();
  
        // Store hash
        var hash = this.hash;
  
        $('html, body').animate({
          scrollTop: $(hash).offset().top
        }, 1000, function(){
     
          // Add hash (#) to URL when done scrolling (default click behavior)
          window.location.hash = hash;
        });
      }
    });
});