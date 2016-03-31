$(document).ready(function() {
    // track where the user come from
    navigator.geolocation.getCurrentPosition(getPosition);
    function getPosition(position) {
        var user_lat = position.coords.latitude;
        var user_long = position.coords.longitude;
        url = 'http://maps.googleapis.com/maps/api/geocode/json?latlng='+user_lat+','+user_long;
        $.getJSON(url, function (data) {
            var index = data.results.length-2;
            var user_location = data.results[index].formatted_address;
            setGlobal(user_location);
            function setGlobal(location) {
                // managing the layout of sum of views
                var x = $("div.watch-view-count").text();
                $("div.watch-view-count").replaceWith("<span>" + x + "</span>");
                $("span#location").text(location);
            }
        });
    }
});
