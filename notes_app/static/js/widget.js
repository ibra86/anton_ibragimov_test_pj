(function() {

    // portal_url of current js file
    var portal_url = (function() {
        var scripts = document.getElementsByTagName("script");
        var current_scr = scripts[scripts.length - 1].src;
        var pathArray = current_scr.split('/');
        return pathArray[0] + '//' + pathArray[2];
    })();

    var script_tag = document.createElement('script');
    script_tag.setAttribute("src", "//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.js");

    script_tag.onload = scriptLoadHandler;
    (document.getElementsByTagName("head")[0] || document.documentElement).appendChild(script_tag);


    function scriptLoadHandler() {

        $.ajax({
            url: portal_url,
            success: function(data) {
                var hrefs = new Array();

                // array of all notes href
                $(data).find('#page-content a[href*="/note/"]').each(function() {
                    hrefs.push($(this).attr('href'));
                });

                // random href url
                var http_url_random = hrefs[Math.floor(Math.random() * hrefs.length)];
                $.ajax({
                    url: http_url_random,
                    success: function(data) {
                        $('#widget-container').html($(data).find('.row').html()).after("<br/>");
                    }
                });
            },
            error: function(xhr, errmsg, err) {
                alert(xhr.status + ": " + xhr.responseText);
            }
        });
    }

})();