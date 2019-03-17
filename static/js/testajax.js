$(document).ready(function () {
    alert("test")
    $("#test").click(function(){
        // alert("test")
        var data = {
            q: 'search',
            text: 'my text'
        };

        $.ajax({
            type: 'GET',
            url: "test",
            data: "test",
            
            dataType: 'json',
            success: function (data) {
                data = JSON.stringify(data);
                alert(data)
            }
        });
    });
});    
