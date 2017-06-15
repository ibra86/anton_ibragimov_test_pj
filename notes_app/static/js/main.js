function initNewNote() {
    $("#id-note-form").ajaxForm({
        success: function(data, status, xhr) {
            // $(data).find(".form-saved").html('<div class="alert alert-success" role="alert">New note have been added!</div>')
            data = data.replace('<p></p>', '<div class="alert alert-success" role="alert">New note has been added!</div>');
            $("body").html(data);
        },
        error: function(xhr, errmsg, err) {
            alert(xhr.status + ": " + xhr.responseText);
        }
    });
}

function initNewRequestStat() {

    var requests_url = (function() {
        var scripts = document.getElementsByTagName("script");
        for (index = 0; index <= scripts.length - 1; ++index) {
            var scr_f = scripts[index].src;
            if (RegExp("static/js/main.js").test(scr_f)) {
                var scr_ind = index;
            };
        };
        var current_scr = scripts[scr_ind].src;
        var pathArray = current_scr.split('/');
        return pathArray[0] + '//' + pathArray[2] + '/' + 'requests';
    })();

    $.ajax({
        url: requests_url,
        dataType: "json",
        success: function(data, status, xhr) {
            localStorage.newRequestsCount = data.new_req_num;
            localStorage.setItem('Requests', JSON.stringify(data.req_stat));

            if (location.pathname == "/requests/") {
                localStorage.setItem("clicked", false);
                localStorage.setItem("focused", true);
            } else {
                localStorage.setItem("clicked", true);
                localStorage.setItem("focused", false);
            };
        },
        error: function(xhr, status, error) {
//             alert(xhr.status + ": " + xhr.responseText);
        }
    });
};

$(document).ready(function() {
    initNewNote();
//     initNewRequestStat();
});