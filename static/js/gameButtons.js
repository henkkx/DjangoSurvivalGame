function post_fun(inp) {
    // NOTE IMPORTANT: this function will go to the error branch because it get's no response
    // for now at least, it DOES post the data though
    $.ajax({
        type: "POST",
        url: "/post_data",
        data: inp,
        success: function(){
            $(".actionBtn").remove();
            get_fun();
            scroll();
            scroll();
        }
    })
}
function buffer_fun(inp){
    $("#gameText").text("");
    post_fun(inp)
}
function get_fun(){
    $.ajax({
            type: 'GET',
            url: "/get_actions",
            dataType: "json",
            success: function (data) {
                for (var i in data) {
                    if (i != "text") {
                        for (var j in data[i]) {
                            $('#buttons').append('<button class="actionBtn" onClick=post_fun(this.firstChild.nodeValue)>' + i + " " + data[i][j] + '</button>');
                        }
                    }else{
                        $("#gameText").append('<p>' + " " + data[i] + '</p>');
                        }
                    }
                }
        });
}
$(document).ready(function() {
    get_fun();
});

function scroll(){
    var scroll_view = document.getElementById("gameText");
    scroll_view.scrollTop=scroll_view.scrollHeight;
}

