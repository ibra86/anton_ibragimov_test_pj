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

$(document).ready(function() {
    initNewNote();
});