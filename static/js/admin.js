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
				console.log(error)
				// console.log(JSON.stringify(error));
			}
		});
	});
}),
$(function(){
	$('#submitButtonAddNewCurator').click(function(){
		console.log("Creating curating is working so far");
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
}),
$(function(){
	$('#submitButtonAddPieceToExhibit').click(function(){
		console.log("Adding piece to exhibit is working so far");
		$.ajax({
			url: '/addPieceToExhibit',
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