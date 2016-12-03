$(function(){
	$('#showAllExhibits').unbind("click").click(function(){
		console.log("Showing all exhibits working so far");
		$.ajax({
			url: '/showAllExhibits',
			type: 'GET',
			success: function(res){
				console.log(res);
	            var listItem = $('<li>');
            
	            var exhibitObj = JSON.parse(res);
	            var exhibit = '';
	            
	            $.each(exhibitObj,function(index, value){
	              exhibit = $(listItem).clone();
	              $(exhibit).addClass('list-group-item');
	              $(exhibit).val(value.Name + ' (' + value.Location + ')');
	              $(exhibit).text(value.Name + ' (' + value.Location + ')');
	              // $(exhibit).text(value.Location);
	              $('#allExhibits').append(exhibit);
	              exhibit = '';
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	}),
	$('#showCurrentExhibits').unbind("click").click(function(){
		console.log("Showing all current exhibits working so far");
		$.ajax({
			url: '/getActiveExhibits',
			type: 'GET',
			success: function(res){
				console.log(res);
	            var listItem = $('<li>');
            
	            var exhibitObj = JSON.parse(res);
	            var exhibit = '';
	            
	            $.each(exhibitObj,function(index, value){
	              exhibit = $(listItem).clone();
	              $(exhibit).addClass('list-group-item');
	              $(exhibit).val(value.Name + ' (' + value.Location + ')');
	              $(exhibit).text(value.Name + ' (' + value.Location + ')');
	              // $(exhibit).text(value.Location);
	              $('#currentExhibits').append(exhibit);
	              exhibit = '';
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	}),
	$('#submitButtonSeePiecesFromExhibit').click(function(){
		console.log("Showing all pieces in exhibit so far");
		$.ajax({
			url: '/getPiecesFromExhibit',
			type: 'GET',
			data: $('form-seePiecesFromExhibit').serialize(),
			success: function(res){
				console.log(res);
	            var listItem = $('<li>');
            
	            var pieceObj = JSON.parse(res);
	            var piece = '';
	            
	            $.each(pieceObj,function(index, value){
	              piece = $(listItem).clone();
	              $(piece).addClass('list-group-item');
	              $(piece).val(value.Name + ' (' + value.Artist + ')');
	              $(piece).text(value.Name + ' (' + value.Artist + ')');
	              // $(exhibit).text(value.Location);
	              $('#piecesInExhibit').append(piece);
	              piece = '';
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	});
});
