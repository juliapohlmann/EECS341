$(function () {
    $('#submitButtonSignUp').click(function () {
        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {
                console.log("SUCCESS")
                console.log(response);
            },
            error: function (error) {
                console.log("BROKEN")
                console.log(JSON.stringify(error));
            }
        });
    });
});
