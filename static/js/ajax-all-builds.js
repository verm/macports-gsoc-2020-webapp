$(function () {
    $('.filter').change(function () {
        $.ajax({
            type: 'POST',
            url: '/all_builds/filter/',
            data: {
                'builder': $('#builder-filter').val(),
                'status': $('#status-filter').val(),
                'page': 1,
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: filterSuccess,
            beforeSend: function () {
                $('#all_builds_table').html("Applying filter...")
            },
            dataType: 'html'
        });
    });
});

$(function () {
    $('.filter').ready(function () {
        $.ajax({
            type: 'POST',
            url: '/all_builds/filter/',
            data: {
                'builder': $('#builder-filter').val(),
                'status': $('#status-filter').val(),
                'page': 1,
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
            },
            success: filterSuccess,
            beforeSend: function () {
                $('#all_builds_table').html("Loading Builds...")
            },
            dataType: 'html'
        });
    });
});

function changePage(page) {
    console.log("Got you");
    $.ajax({
        type: 'POST',
        url: '/all_builds/filter/',
        data: {
            'builder': $('#builder-filter').val(),
            'status': $('#status-filter').val(),
            'page': page,
            'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()
        },
        success: filterSuccess,
        beforeSend: function () {
            $('#all_builds_table').html("Changing page...")
        },
        dataType: 'html'
    });
};

function filterSuccess(data, textStatus, jqXHR) {
    $('#all_builds_table').html(data);
}