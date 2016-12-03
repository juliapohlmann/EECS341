$(function(){
	$('#showAllCurators').unbind("click").click(function(){
		console.log("Showing all curators working so far");
		$.ajax({
			url: '/showAllCurators',
			type: 'GET',
			success: function(res){
				$('#allCurators').empty();
				console.log(res);
	            var listItem = $('<li>');
            
	            var curatorObj = JSON.parse(res);
	            var curator = '';
	            
	            $.each(curatorObj,function(index, value){
	              curator = $(listItem).clone();
	              $(curator).addClass('list-group-item');
	              $(curator).val(value.Name + ' (' + value.Expertise + ')');
	              $(curator).text(value.Name + ' (' + value.Expertise + ')');
	              $('#allCurators').append(curator);
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	}),
	$('#showCurrentCurators').unbind("click").click(function(){
		console.log("Showing all current curators working so far");
		$.ajax({
			url: '/showCurrentCurators',
			type: 'GET',
			success: function(res){
				$('#allCurrentCurators').empty();
				console.log(res);
	            var listItem = $('<li>');
            
	            var curatorObj = JSON.parse(res);
	            var curator = '';
	            
	            $.each(curatorObj,function(index, value){
	              curator = $(listItem).clone();
	              $(curator).addClass('list-group-item');
	              $(curator).val(value.Name + ' (' + value.Expertise + ')');
	              $(curator).text(value.Name + ' (' + value.Expertise + ')');
	              $('#allCurrentCurators').append(curator);
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	}),
	$('#submitGetCuratorsByDate').unbind("click").click(function(){
		console.log("Finding curators by date working so far");
		$.ajax({
			url: '/getCuratorsByDate',
			type: 'POST',
			data: $('form').serialize(),
			success: function(res){
				$('#curatorsByDate').empty();

				console.log(res);
	            var listItem = $('<li>');
            
	            var curatorObj = JSON.parse(res);
	            var curator = '';
	            
	            $.each(curatorObj,function(index, value){
	              curator = $(listItem).clone();
	              $(curator).addClass('list-group-item');
	              $(curator).val(value.Name + ' (' + value.Expertise + ')');
	              $(curator).text(value.Name + ' (' + value.Expertise + ')');
	              $('#curatorsByDate').append(curator);
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	}),
	$('#getCuratorsOfExpertise').unbind("click").click(function(){
		console.log("Finding curators by expertise working so far");
		$.ajax({
			url: '/getCuratorsByExpertise',
			type: 'POST',
			data: $('form').serialize(),
			success: function(res){
				$('#curatorsByExpertise').empty();

				console.log(res);
	            var listItem = $('<li>');
            
	            var curatorObj = JSON.parse(res);
	            var curator = '';
	            
	            $.each(curatorObj,function(index, value){
	              curator = $(listItem).clone();
	              $(curator).addClass('list-group-item');
	              $(curator).val(value.Name);
	              $(curator).text(value.Name);
	              $('#curatorsByExpertise').append(curator);
	          	});
			},
			error: function(error){
				console.log(JSON.stringify(error));
			}
		});
	});
});
