$(function () {
    $("#submit").click(function (event) {
        // 阻止默认操作
        event.preventDefault();
        var email = $("input[name='email']").val();
        var password = $("input[name='password']").val();
        // var csrf_token = $("input[name='csrf_token']").val();

        yioajax.ajax({
            'url': '/login/',
            'type': 'post',
            'data': {
                "email": email,
                "password": password,
            },
            'success': function (data, status) {
                console.log(data);
            }
        });
    });
});



