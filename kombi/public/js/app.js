/* Javascript Usage: */

var ws = new WebSocket('ws://flyingdutchman.local:8000/ws');
var app = (function($) {
    var config = $('#config');
    var app = JSON.parse(config.text());
    $(document).ready(function() {
        var router = new app.router();
        var navbar = new app.views.NavbarView();
        ws.onopen = function(event){ console.log('socket open'); };
        ws.onclose = function(event){ console.log('socket closed'); };
        ws.onerror = function(error){ console.log('error:', err); };
        ws.onmessage = function(event){ console.log('message:', event.data); };
    });
    return app;
})(jQuery);
