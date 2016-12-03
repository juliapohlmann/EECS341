$(function(){
    $('#submitButtonSignUp').click(function(){
        console.log("This is working so far");
        $.ajax({
            url: '/signUp',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response){
                console.log("SUCCESS")
                console.log(response);
            },
            error: function(error){
                console.log("BROKEN")
                console.log(JSON.stringify(error));
            }
        });
    });
});