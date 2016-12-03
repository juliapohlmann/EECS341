$(function(){
	$('#showAllExhibits').unbind("click").click(function(){
		console.log("Showing all exhibits working so far");
		$.ajax({
			url: '/showAllExhibits',
			type: 'GET',
			success: function(res){
				$('#allExhibits').empty();
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
	$('#submitButtonSeePiecesOfGivenTypeFromExhibit').unbind("click").click(function(){
		console.log("Showing all pieces of given typein exhibit so far");
		$.ajax({
			url: '/getPiecesFromExhibitByType',
			type: 'POST',
			data: $('form').serialize(),
			success: function(res){
				$('#piecesInExhibitByType').empty();

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
	              $('#piecesInExhibitByType').append(piece);
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	}),
	$('#submitButtonSeeExhibitsInLocation').unbind("click").click(function(){
		console.log("Finding exhibits by location");
		$.ajax({
			url: '/getExhibitsByLocation',
			type: 'POST',
			data: $('form').serialize(),
			success: function(res){
				$('#exhibitsInLocation').empty();

				console.log(res);
	            var listItem = $('<li>');
            
	            var exhibitObj = JSON.parse(res);
	            var exhibit = '';
	            
	            $.each(exhibitObj,function(index, value){
	              exhibit = $(listItem).clone();
	              $(exhibit).addClass('list-group-item');
	              $(exhibit).val(value.Name);
	              $(exhibit).text(value.Name);
	              // $(exhibit).text(value.Location);
	              $('#exhibitsInLocation').append(exhibit);
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
