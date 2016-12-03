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
	});
});