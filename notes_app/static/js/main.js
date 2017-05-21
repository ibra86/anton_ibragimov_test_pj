
function initNewNote(){
  $("#id-note-form").ajaxForm({
    success: function(data, status, xhr){
        // console.log(data);
        // $("html").html(data);
        $("body").html(data);
    //   alert('New note is published!');
    //   $('.form-control').val('')
    //   cnt = $("#noteNumber").text();
    //    $("#noteNumber").text(parseInt(cnt)+1);
},
error : function(xhr,errmsg,err) {
                            alert(xhr.status + ": " + xhr.responseText);
  });
}

// function initNewRequestStat(){
//   var requests_url = "http://localhost:8000/requests"
//   var counter = 0;
//   counter ++;
//   $.ajax({
//     url: requests_url,
//     // data:{'counter':counter},
//     dataType: "json",
//     success: function(data, status, xhr){
//       localStorage.clear();// sanity step
//       localStorage.newRequestsCount = data.new_req_num;
//       localStorage.setItem('Requests',JSON.stringify(data.req_stat));
//             console.log(status);
//             console.log(xhr.getResponseHeader("content-type"));
//     },
//     error: function(xhr, status, error){
//       console.log(status);
//       console.log(error);
//     }
//   })
// }

$(document).ready(function(){
  initNewNote();
  // initNewRequestStat();
});
