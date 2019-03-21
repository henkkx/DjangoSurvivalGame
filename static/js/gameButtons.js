function post_fun(inp) {
    // all buttons except the New Game button call this
    // It will POST data to a view which will get it to the game. The data is just a string of commands.
    // It deletes all created buttons, then runs get_fun and proceeds to scroll down.
    $.ajax({
        type: "POST",
        url: "/post_data",
        data: inp,
        success: function(){
            $(".actionBtn").remove();
            get_fun();
            scroll();
        }
    })
}
function buffer_fun(inp){
    // this function runs when we click the New Game button ( everything else calls post_fun)
    // it will delete all text on screen, and then call post_fun to handle creating a new game, the scroll down
    $("#gameText").text("");
    post_fun(inp)
    scroll()
}
function get_fun(){
    // The code below will get all the actions the player can perform at this point and create a button for all of them.
    // It also gets and displays text from the game (descriptions, data etc. Anything displayed ) see else statement
    $.ajax({
            type: 'GET',
            url: "/get_actions",
            dataType: "json",
            success: function (data) {
                for (var i in data) {
                    if (i != "text") {
                        if (i == "Inventory") {
                            for (var j in data[i]) {
                                $('#buttons').append('<button class="actionBtn btn btn-success" onClick=post_fun(this.firstChild.nodeValue)>' + i + " " + data[i][j] + '</button>');
                            }
                        } else if (i == "Enter") {
                            for (var j in data[i]) {
                                $('#buttons').append('<button class="actionBtn btn btn-light" onClick=post_fun(this.firstChild.nodeValue)>' + i + " " + data[i][j] + '</button>');
                            }
                        }else if (i== "Fight" || i=="Game over"){
                            for (var j in data[i]) {
                                $('#buttons').append('<button class="actionBtn btn btn-danger" onClick=post_fun(this.firstChild.nodeValue)>' + i + " " + data[i][j] + '</button>');
                            }
                        }else if( i== "Exit"){
                            for (var j in data[i]) {
                                $('#buttons').append('<button class="actionBtn btn btn-secondary" onClick=post_fun(this.firstChild.nodeValue)>' + i + " " + data[i][j] + '</button>');
                            }
                        }else if(i=="Talk to"){
                            for (var j in data[i]) {
                                $('#buttons').append('<button class="actionBtn btn btn-danger" onClick=post_fun(this.firstChild.nodeValue)>' + i + " " + data[i][j] + '</button>');
                            }
                        }else if(i== "Read" || i=="Consume"){
                            for (var j in data[i]) {
                                $('#buttons').append('<button class="actionBtn btn btn-warning" onClick=post_fun(this.firstChild.nodeValue)>' + i + " " + data[i][j] + '</button>');
                            }
                        }else if(i == "Pick" || i == "Drop"){
                            for (var j in data[i]) {
                                $('#buttons').append('<button class="actionBtn btn btn-light" onClick=post_fun(this.firstChild.nodeValue)>' + i + " " + data[i][j] + '</button>');
                            }
                        }
                        else{
                            for (var j in data[i]) {
                                $('#buttons').append('<button class="actionBtn btn btn-dark" onClick=post_fun(this.firstChild.nodeValue)>' + i + " " + data[i][j] + '</button>');
                            }
                        }
                        // for (var j in data[i]) {
                        //     $('#buttons').append('<button class="actionBtn btn btn-danger" onClick=post_fun(this.firstChild.nodeValue)>' + i + " " + data[i][j] + '</button>');
                        // }
                    } else {
                        $("#gameText").append('<p>' + " " + data[i] + '</p>');
                    }
                }
            }
        });
    scroll()
}
$(document).ready(function() {
    // the moment the page is ready, get the available actions ( view will initialise game)
    get_fun();
});

function scroll(){
    // scrolls the text to the bottom
    var scroll_view = document.getElementById("gameText");
    scroll_view.scrollTop=scroll_view.scrollHeight;
}

