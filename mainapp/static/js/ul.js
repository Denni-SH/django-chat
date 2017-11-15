socket = new WebSocket("ws://" + window.location.host + "/chat/");
socket.onmessage = function(e) {
    $("#textfield").append(e.data+'<br/>');
}
socket.onopen = function() {

}
$(document).ready(function(){
    $("#send_text").click(function(e) {
        var val = $("#text_to_send").val();
        socket.send(val);
    })
    // Call onopen directly if socket is already open
    if (socket.readyState == WebSocket.OPEN) socket.onopen();
});
