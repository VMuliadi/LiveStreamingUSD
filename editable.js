$(document).ready(function() {
    // managing the layout of sum of views
    var x = $("div.watch-view-count").text();
    $("div.watch-view-count").replaceWith("<span>" + x + "</span>");

    // managing the incoming money
    var y = $("span#income");
    y.text(x*100);
});
