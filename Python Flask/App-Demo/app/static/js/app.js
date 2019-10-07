$(function(){

$('#json').click(function(){
	var data = {
		'username': $('input[name=username]').val(),
		'email': $('input[name=email]').val(),
		'password': $('input[name=password]').val()
	};
	data = JSON.stringify(data);
	$.ajax({
		type: 'POST',
		url: '/json',
		data: data,
		contentType: 'application/json;charset=UTF-8',
		dataType: 'json',
		success: function (data,status,xhr) {   
				console.log(data)
				},
		error: function (jqXhr, textStatus, errorMessage) { // error callback 		
			console.log(errorMessage)
			   }
		});
});

$('#button-sent').click(function(){
	var data = {
		'name': $('#name').val(),
		'message': $('#message').val()
	};

	fetch('/guest_msg',{
		method: 'POST',
		credentials : 'include',
		body: JSON.stringify(data),
		cache: 'no-cache',
		headers: new Headers({
			'content-type': 'application/json'
		})
	}).then(function(response){
		if(!response.status === 200){
			console.log('Negative Response')
		}else{
			console.log('Positive Response')
		}
	});

});

$('#image').on('change', function(){
	var fileSizeMap = {};
	$.each(this.files, function(index, image){
		fileSizeMap[image['name']] = image['size'];
	});
	document.cookie = `imagesSize= ${JSON.stringify(fileSizeMap)}`;
	console.log(document.cookie);
});

$('#set-cookie').click(function(){
	document.cookie = 'name=optimus'
	document.cookie = 'age=20'
});

$('#add').click(function(){
	var title = $('#link-title').val();
	var content = $('#link-content').val();
	var container = "<div id='link-container'><a href='"+content+"'>"+title+"</a><input type='button' id='remove' value='X'></div>";
	$('.card-footer').append(container);
});

$('.card-footer').on('click', '#remove',function(){
	$(this).parent().remove();
});

});
