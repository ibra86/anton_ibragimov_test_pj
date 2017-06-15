// defining websocket
var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
var ws = new WebSocket(ws_scheme + '://' + window.location.host);

ws.onopen = function open() {
	// sending location to server on open websocket
	var loc = location.pathname;
    ws.send(loc);
};

ws.onclose = function() {
    console.log('Closed connection');
};