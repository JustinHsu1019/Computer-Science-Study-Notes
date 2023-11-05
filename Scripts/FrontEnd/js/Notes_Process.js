$(document).ready(function () {
    $('#notes-upload-form').on('submit', function (e) {
        e.preventDefault();
        var formData = new FormData(this);

        $.ajax({
            url: 'http://127.0.0.1:5000/notes-process',
            type: 'POST',
            data: formData,
            contentType: false,
            processData: false,
            xhrFields: {
                responseType: 'blob'
            },
            success: function (blob) {
                var url = window.URL.createObjectURL(blob);
                var a = document.createElement('a');
                a.href = url;
                a.download = 'notes_result.zip';
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
            },
            error: function (xhr, status, error) {
                $('#alert-placeholder-notes').html(
                    '<div class="alert alert-danger" role="alert">' +
                    'An error occurred: ' + error +
                    '</div>'
                );
            }
        });
    });
});
