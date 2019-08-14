<head>
<script src="jquery-3.4.1.min.js"></script>
</head>

<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>
<script type="text/javascript">

var geocoder = new google.maps.Geocoder();
var address = jQuery('#address').val();

geocoder.geocode( { 'address': address}, function(results, status) {

if (status == google.maps.GeocoderStatus.OK) {
    var latitude = results[0].geometry.location.lat();
    var longitude = results[0].geometry.location.lng();
    jQuery('#coordinates').val(latitude+', '+longitude);
    }
});
</script>
