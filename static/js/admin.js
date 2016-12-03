$(function(){
	$('#submitButtonCreateNewExhibit').click(function(){
		console.log("Creating exhibit is working so far");
		$.ajax({
			url: '/addExhibit',
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
}),
$(function(){
	$('#submitButtonCreateNewPiece').click(function(){
		console.log("Creating piece is working so far");
		$.ajax({
			url: '/addPiece',
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
}),
$(function(){
	$('#submitButtonAddNewCurator').click(function(){
		console.log("Adding curator is working so far");
		$.ajax({
			url: '/addCurator',
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
