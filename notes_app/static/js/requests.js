// localStorage.clear();
setInterval(function() {
    if (JSON.parse(localStorage.getItem("clicked")) && (!JSON.parse(localStorage.getItem("focused")))) {
        $("title").html("(" + localStorage.newRequestsCount + ") Requests");
    } else {
        $("title").html("Requests");
    };


    //resetting style due to possible multiple requests
    $(".container > span").css("background-color", "");
    //defining style for final request
    $(".container > span#req_id:lt(" + localStorage.newRequestsCount + ")").css("background-color", "lime");
    $(".container > span#req_time:lt(" + localStorage.newRequestsCount + ")").css("background-color", "lime");
    $(".container > span#req_line:lt(" + localStorage.newRequestsCount + ")").css("background-color", "lime");

    var req = JSON.parse(localStorage.getItem('Requests'));
    $.each(req, function(index, value) {
        var req_array = value.split(" -- ", 3);
        $(".container > span#req_id:eq(" + index + ")").text(req_array[0]);
        $(".container > span#req_time:eq(" + index + ")").text(req_array[2]);
        $(".container > span#req_line:eq(" + index + ")").text(req_array[1]);
    });

    window.onfocus = function() {
        localStorage.setItem("clicked", false);
        localStorage.setItem("focused", true);
    };

    window.onblur = function() {
        localStorage.setItem("focused", false);
    };

}, 1000);