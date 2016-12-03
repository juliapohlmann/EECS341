$(function(){
	$('#submitButtonSignIn').click(function(){
		console.log("Sign in is working so far");
		$.ajax({
			url: '/signIn',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	});
});