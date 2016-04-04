window.onload = function() {
    // managing the incoming money
    var y = $("span#income");
    y.text(x*100);

    // define the font that render by browser
    $("body").css("font-family", "Open Sans");

    // calculate the exact dimension of some elements
    var x = $(window).innerWidth();
    var y = $(window).innerHeight();
    var video = $("iframe#youtube-video");
    var menubar = $("div#menubar-bottom");

    // some styling for webpage
    $("div.col-xs-12").css("padding", "0");
    menubar.css("text-align", "center");
    menubar.css("padding-top", "10px");
    menubar.css("padding-bottom", "10px");
    menubar.css("background", "rgb(128,0,0)");
    menubar.css("color", "#fff");

    // applying dimension of each elements
    video.css("margin", "0");
    video.width($("body").width());
    video.height(y - menubar.height() - 25);

    //automatically reload views every 5 minutes
    
};
