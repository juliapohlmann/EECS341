$(function(){
	$('#showAllPieces').unbind("click").click(function(){
		console.log("Showing all pieces working so far");
		$.ajax({
			url: '/showAllPieces',
			type: 'GET',
			success: function(res){
				$('#allPieces').empty();
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
	              $('#allPieces').append(piece);
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	}),
	$('#getExhibitOfPiece').unbind("click").click(function(){
		console.log("Showing exhibit of piece working so far");
		$.ajax({
			url: '/getpiecelocation',
			type: 'POST',
			data: $('form').serialize(),
			success: function(res){
				$('#exhibitOfPiece').empty();
				console.log(res);
	            var listItem = $('<li>');
            
	            var pieceObj = JSON.parse(res);
	            var piece = '';
	            $.each(pieceObj,function(index, value){
	              piece = $(listItem).clone();
	              $(piece).addClass('list-group-item');
	              $(piece).val(value.ExhibitName +  ' (' + value.ExhibitLocation + ')');
	              $(piece).val(value.ExhibitName +  ' (' + value.ExhibitLocation + ')');
	              $('#exhibitOfPiece').append(piece);
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	}),
	$('#showAllAvailablePieces').unbind("click").click(function(){
		console.log("Showing all available pieces working so far");
		$.ajax({
			url: '/getAvailablePieces',
			type: 'GET',
			success: function(res){
				$('#allAvailablePieces').empty();
				console.log(res);
	            var listItem = $('<li>');
            
	            var pieceObj = JSON.parse(res);
	            var piece = '';
	            
	            $.each(pieceObj,function(index, value){
	              piece = $(listItem).clone();
	              $(piece).addClass('list-group-item');
	              $(piece).val(value.Name + ' (' + value.Artist + ')');
	              $(piece).text(value.Name + ' (' + value.Artist + ')');
	              $('#allAvailablePieces').append(piece);
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	}),
	$('#getInfoOnGivenPiece').unbind("click").click(function(){
		console.log("Getting info on piece working so far");
		$.ajax({
			url: '/getPieceById',
			type: 'POST',
			data: $('form').serialize(),
			success: function(res){
				$('#detailsAboutPiece').empty();

				console.log(res);
	            var listItem = $('<li>');
            
	            var pieceObj = JSON.parse(res);
	            console.log(pieceObj);
	            var piece = '';
	            $.each(pieceObj,function(index, value){
		            //Name
		       		piece = $(listItem).clone();
		       		$(piece).addClass('list-group-item');
		       		$(piece).val(value.Name);
		            $(piece).text('Name: ' + value.Name);
					$('#detailsAboutPiece').append(piece);
					//Artist
		       		piece = $(listItem).clone();
		       		$(piece).addClass('list-group-item');
		       		$(piece).val(value.Artist);
		            $(piece).text('Artist: ' + value.Artist);
					$('#detailsAboutPiece').append(piece);
					//Type
		       		piece = $(listItem).clone();
		       		$(piece).addClass('list-group-item');
		       		$(piece).val(value.Type);
		            $(piece).text('Type: ' + value.Type);
					$('#detailsAboutPiece').append(piece);
					//Date_Created
		       		piece = $(listItem).clone();
		       		$(piece).addClass('list-group-item');
		       		$(piece).val(value.Date_Created);
		            $(piece).text('Date Created: ' + value.Date_Created);
					$('#detailsAboutPiece').append(piece);
					//Piece_Desc
		       		piece = $(listItem).clone();
		       		$(piece).addClass('list-group-item');
		       		$(piece).val(value.Piece_Desc);
		            $(piece).text('Description: ' + value.Piece_Desc);
					$('#detailsAboutPiece').append(piece);
				});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	}),
	$('#submitButtonSeePiecesFromArtist').unbind("click").click(function(){
		console.log("Showing all pieces by artist so far");
		$.ajax({
			url: '/getPiecesByArtist',
			type: 'POST',
			data: $('form').serialize(),
			success: function(res){
				$('#piecesByArtist').empty();

				console.log(res);
	            var listItem = $('<li>');
            
	            var pieceObj = JSON.parse(res);
	            console.log(pieceObj);

	            var piece = '';
	            
	            $.each(pieceObj,function(index, value){
	              piece = $(listItem).clone();
	              $(piece).addClass('list-group-item');
	              $(piece).val(value.Id);
	              $(piece).text(value.Name);
	              // $(exhibit).text(value.Location);
	              $('#piecesByArtist').append(piece);
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
				$('#currentExhibits').empty();

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
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	}),
	$('#submitGetExhibitsByTimeFrame').unbind("click").click(function(){
		console.log("Finding exhibits by date working so far");
		$.ajax({
			url: '/getExhibitsByTimeFrame',
			type: 'POST',
			data: $('form').serialize(),
			success: function(res){
				$('#exhibitsByTimeFrame').empty();

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
	              $('#exhibitsByTimeFrame').append(exhibit);
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	}),
	

	$('#submitButtonSeePiecesOfGivenType').unbind("click").click(function(){
		console.log("Showing all pieces of given type so far");
		$.ajax({
			url: '/getPiecesByType',
			type: 'POST',
			data: $('form').serialize(),
			success: function(res){
				$('#piecesByType').empty();

				console.log(res);
	            var listItem = $('<li>');
            
	            var pieceObj = JSON.parse(res);
	            console.log(pieceObj);

	            var piece = '';
	            
	            $.each(pieceObj,function(index, value){
	              piece = $(listItem).clone();
	              $(piece).addClass('list-group-item');
	              $(piece).val(value.Name + ' (' + value.Artist + ')');
	              $(piece).text(value.Name + ' (' + value.Artist + ')');
	              // $(exhibit).text(value.Location);
	              $('#piecesByType').append(piece);
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	}),
	$('#submitButtonSeePiecesInGivenTimeFrame').unbind("click").click(function(){
		console.log("Finding piece by time period");
		$.ajax({
			url: '/getPiecesByTimePeriod',
			type: 'POST',
			data: $('form').serialize(),
			success: function(res){
				$('#piecesInTimePeriod').empty();

				console.log(res);
	            var listItem = $('<li>');
            
	            var pieceObj = JSON.parse(res);
	            console.log(pieceObj);

	            var piece = '';
	            
	            $.each(pieceObj,function(index, value){
	              piece = $(listItem).clone();
	              $(piece).addClass('list-group-item');
	              $(piece).val(value.Name + ' (' + value.Artist + ')');
	              $(piece).text(value.Name + ' (' + value.Artist + ')');
	              // $(exhibit).text(value.Location);
	              $('#piecesInTimePeriod').append(piece);
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	}),
	$('#submitButtonSeePiecesFromExhibit').unbind("click").click(function(){
		console.log("Showing all pieces in exhibit so far");
		$.ajax({
			url: '/getPiecesFromExhibit',
			type: 'POST',
			data: $('form').serialize(),
			success: function(res){
				$('#piecesInExhibit').empty();

				console.log(res);
	            var listItem = $('<li>');
            
	            var pieceObj = JSON.parse(res);
	            console.log(pieceObj);

	            var piece = '';
	            
	            $.each(pieceObj,function(index, value){
	              piece = $(listItem).clone();
	              $(piece).addClass('list-group-item');
	              $(piece).val(value.Name + ' (' + value.Artist + ')');
	              $(piece).text(value.Name + ' (' + value.Artist + ')');
	              // $(exhibit).text(value.Location);
	              console.log('index: ' + index + ' piece: ' + value.Name)
	              $('#piecesInExhibit').append(piece);
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	});
});
