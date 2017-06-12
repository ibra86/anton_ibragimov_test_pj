// var a = 5;
//     var ws = new WebSocket('ws://' + window.location.host + '/users/');
	var ws = new WebSocket('ws://localhost:8000');




    ws.onopen = function open() {
    	var d2 = new Date();
    	d2.setHours(d2.getHours()+2); 
	    var time2 = d2.toISOString().split('T')[1];
      console.log('!!WebSockets connection '+
      ws.url+' created.' + ' - ' + time2);
      var loc = location.pathname;
      console.log(loc);
      ws.send(loc);
      
    }; 
//     
//     ws.send('test sent');

// 	var bd=document.getElementsByTagName("BODY")[0];
//     
//     ws.onmessage = function(event){
// 		var d = new Date();
// 		d.setHours(d.getHours()+2); 
// 		var time = d.toISOString().split('T')[1];
//     	console.log('Message0 - ' + event.data + ' - ' + time);
//     	var dh = $(bd).find('#page-header h1 a').html();
//     	var dt = $(bd).find('#page-header h1 a').text();
// //     	console.log(dh, dt);
//     	$(bd).find('#page-header h1').html('<a href="/">'+dh+'</a>' + ' - ' + time);
//     	console.log($(bd).find('#page-header h1 a').html());
//     	};
// 	
// // 	ws.close();
// 	
	ws.onclose = function(){
		console.log('Closed connection');
		};
// 		
// // 	ws.close();
// 
//    if (ws.readyState == WebSocket.OPEN) {
//    	console.log('if created');
//       ws.onopen();
//     }
    
    
    
    
    