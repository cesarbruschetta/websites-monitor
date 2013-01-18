function geraGrafico(){
	var url = "/ajax-grafic"
	
	var site = $('select#site').val();
	var start_date = $('input#start-date').val();
	var end_date = $('input#end-date').val();
	
	$('div#content-grafico').html("");	
	$('div#ajax-load').show();
	
	if (site != ''){ 
		$.get(url,{site:site,
				   start_date:start_date,
				   end_date:end_date}, function(data){
	
			$('div#content-grafico').html(data);
			$('div#ajax-load').hide();
		});
	};
};

$(document).ready(function(){
	$('select#site').change(function(){
		geraGrafico();
	});
	$('input#gera').click(function(){
		geraGrafico();
	});
});