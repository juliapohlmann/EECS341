$(function(){
	$('#showAllDonors').unbind("click").click(function(){
		console.log("Showing all donors working so far");
		$.ajax({
			url: '/showAllDonors',
			type: 'GET',
			success: function(res){
				$('#allDonors').empty();
				console.log(res);
	            var listItem = $('<li>');
            
	            var donorObj = JSON.parse(res);
	            var donor = '';
	            
	            $.each(donorObj,function(index, value){
	              donor = $(listItem).clone();
	              $(donor).addClass('list-group-item');
	              $(donor).val(value.Name);
	              $(donor).text(value.Name);
	              // $(exhibit).text(value.Location);
	              $('#allDonors').append(donor);
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	}),
	$('#showAllDonatedPieces').unbind("click").click(function(){
		console.log("Showing all donated pieces working so far");
		$.ajax({
			url: '/showAllDonatedPieces',
			type: 'GET',
			success: function(res){
				$('#allDonatedPieces').empty();
				console.log(res);
	            var listItem = $('<li>');
            
	            var donorObj = JSON.parse(res);
	            var donor = '';
	            
	            $.each(donorObj,function(index, value){
	              donor = $(listItem).clone();
	              $(donor).addClass('list-group-item');
	              $(donor).val(value.Name + ' (' + value.Artist + ')');
	              $(donor).text(value.Name + ' (' + value.Artist + ')');
	              // $(exhibit).text(value.Location);
	              $('#allDonatedPieces').append(donor);
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	}),
	$('#submitGetDonationsByDate').unbind("click").click(function(){
		console.log("Finding donations by date working so far");
		$.ajax({
			url: '/getDonationsByDate',
			type: 'POST',
			data: $('form').serialize(),
			success: function(res){
				$('#donationByDate').empty();

				console.log(res);
	            var listItem = $('<li>');
            
	            var pieceObj = JSON.parse(res);
	            var piece = '';
	            
	            $.each(pieceObj,function(index, value){
	              piece = $(listItem).clone();
	              $(piece).addClass('list-group-item');
	              $(piece).val(value.DonorName + ' (' + value.PieceName + ')');
	              $(piece).text(value.DonorName + ' (' + value.PieceName + ')');
	              // $(exhibit).text(value.Location);
	              $('#donationByDate').append(piece);
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	});
});
