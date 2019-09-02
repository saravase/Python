$(function(){
	var reg = /\d/;
	$('.table-container table tbody tr td[contenteditable="true"]').keydown(function(event){
		var iKeyCode = (event.which) ? event.which : event.keyCode
		if (iKeyCode != 46 && iKeyCode > 31 && iKeyCode!=37 && iKeyCode!=38 && iKeyCode!=39 && iKeyCode!=40 && (iKeyCode < 48 || iKeyCode > 57))
			return false;
		return true;
	});

	$('#current-table').change(function(){
		var current_all = ['function','ptf','d2b']
		var visible_list = $('#current-table').selectpicker('val');
		var hide_list = current_all.filter( ( el ) => !visible_list.includes( el ) );
		visible_list.forEach(function(item, index, arr){
			$('#attendance-'+item+'-current-container').show();
		});
		hide_list.forEach(function(item, index, arr){
			$('#attendance-'+hide_list[index]+'-current-container').hide();
		});
	});

	$('#future-table').change(function(){
		var current_all = ['function','ptf','d2b']
		var visible_list = $('#future-table').selectpicker('val');
		var hide_list = current_all.filter( ( el ) => !visible_list.includes( el ) );
		visible_list.forEach(function(item, index, arr){
			$('#attendance-'+item+'-future-container').show();
		});		
		hide_list.forEach(function(item, index, arr){
			$('#attendance-'+item+'-future-container').hide();
		});
	});
	
	$('#add-btn').click(function(){
		var cmd_data = $('#add-cmd').val();
		if(cmd_data.length != 0)
			$('#area-cmd').text($('#area-cmd').text().concat('1'+cmd_data+'\n'))
	})

});