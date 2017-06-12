// var a = 5;
//     var ws = new WebSocket('ws://' + window.location.host + '/users/');
	var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
	var ws = new WebSocket(ws_scheme + '://' + window.location.host);

    ws.onopen = function open() {
    	var d2 = new Date();
    	d2.setHours(d2.getHours()+2); 
	    var time2 = d2.toISOString().split('T')[1];
      console.log('WebSockets connection '+
      ws.url+' created.' + ' - ' + time2);
      var loc = location.pathname;
      console.log(loc);
      ws.send(loc);
      
    }; 
    
	ws.onclose = function(){
		console.log('Closed connection');
		};
		
//    if (ws.readyState == WebSocket.OPEN) {
//    	console.log('if created');
//       ws.onopen();
//     }
    
    
    
    
    