$(document).ready(function(){
	$('select#site').change(function(){
		var url = "/ajax-grafic"
		
		var site = $(this).val();
		var start_date = $('input#start-date').val();
		var end_date = $('input#end-date').val();
		
		if (site != ''){ 
			$.get(url,{site:site,
					   start_date:start_date,
					   end_date:end_date}, function(data){
	
						$('div#content-grafico').html(data);
				});
		}else{
			$('div#content-grafico').html("");			
		}
				
	});
	

});