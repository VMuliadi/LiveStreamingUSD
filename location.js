window.onload = init;
function init() {
    navigator.geolocation.getCurrentPosition(getPosition);
    function getPosition(position) {
        var user_lat = position.coords.latitude;
        var user_long = position.coords.longitude;
        url = 'http://maps.googleapis.com/maps/api/geocode/json?latlng='+user_lat+','+user_long;
        $.getJSON(url, function (data) {
            var index = data.results.length-2;
            var lokasi_user_parsed = data.results[index].formatted_address;
            document.getElementById("OSystem").setAttribute("value", navigator.platform);
            document.getElementById("location").setAttribute("value", lokasi_user_parsed);
            document.forms["identity"].submit();
        });
    }
}
