var non_viewed_req_num = 0;

ws.onmessage = function(event) {

    // list of variables of data received from ws
    var request_data = JSON.parse(event.data);
    var req = request_data.req_stat;
    var new_req_num = request_data.new_req_num + non_viewed_req_num;
    var req_page_path = request_data.req_page_path;

    // other variables
    var requestsList = $('#req-list-id');
    var content = '';

    // general counter for unviewed request
    non_viewed_req_num = new_req_num;

    // processing array 'req' to be rendered on web page
    $.each(req, function(index, value) {
        var req_array = value.split(" -- ", 4);
        // x = req_array[3];
        // k = x.split(": ")[1] == "True" ? "New!" : "";

        content += ' \
        <div class="col-xs-8"> \
            <span class="label label-info label-as-badge" id="req_id">' + req_array[0] + '</span>\
            <span class="label label-info label-as-badge" id="req_time">' + req_array[2] + '</span>\
            <span class="label label-info label-as-badge" id="req_line">' + req_array[1] + '</span>\
        </div> \
        <div class="col-xs-4"> \
            <span class="label label-info label-as-badge" id="req_new">New!</span>\
        </div> \
        <br/>\
        <br/>'
    });

    // rendering html
    requestsList.html(content);

    // put over aditional style for new inputs
    $(".container  span#req_id:lt(" + new_req_num + ")").css("background-color", "lime");
    $(".container  span#req_time:lt(" + new_req_num + ")").css("background-color", "lime");
    $(".container  span#req_line:lt(" + new_req_num + ")").css("background-color", "lime");
    $(".container  span#req_new:lt(" + new_req_num + ")").css({
        "background-color": "lightgrey",
        "color": "DimGray"
        });
    $(".container  span#req_new:gt(" + (new_req_num - 1) + ")").text('');

    // title new request counter logic - if visited
    $("title").html("(" + new_req_num + ") Requests");
    setTimeout(function() {
        if (req_page_path == '/requests/') {
            $("title").html("Requests");
            non_viewed_req_num = 0;
        };
    }, 500);

    window.addEventListener("focus", function(event) {
        $("title").html("Requests");
        non_viewed_req_num = 0;
    }, false);

};