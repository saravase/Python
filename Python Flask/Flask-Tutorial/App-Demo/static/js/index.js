$(function(){
	var getTableHeader = function(tableId){
		var head = [];
		$('#'+tableId+' tr:eq(0)').find('td').each(function(){
			head.push($(this).html())
		});
		return head;
	};

	var getTableData = function(tableId){
		var data = [];
		var head = getTableHeader(tableId)
		$('#'+tableId+' tbody tr').each(function(){
			var temp = {};
			var i=0;
			$(this).find('td').each(function(){
				temp[head[i]] = $(this).text()
				i++;
			});
			data.push(temp);
		});
		return data;
	};


	$("table").hover(function(){
		$('table thead').toggleClass("table-danger");
		$('tr:odd').toggleClass('table-info');
		$('tr:even:not(tr:nth-child(1))').toggleClass('table-warning');
	});

	$('table tbody').on('click', 'td[contentEditable="true"]',function(){
		var bval = $(this).text();
		$(this).focusout(function(){
			var cval = $(this).text();
			if(bval !== cval){
				$(this).css({
					'color': 'green'
				});
			}
		});
	});

	$('table tbody').find('td').attr('contentEditable','true');
	$('#detail').click(function(){
		$.get('/detail', function(data){
			$('#detail-index').html(data);
		});
		$.post('/custom', {'id':34}, function(data){
			alert(data)
		}, 'json');

		var emp = {
			'name': 'Optimus Prime',
			'age': 23,
			'salary': 233000
		};
		$.ajax({
			url: '/emp-detail',
			data: {'employee':JSON.stringify(emp)},
			dataType: 'json',
			success: function(data, status, xhr){
				alert(status)
			},
			error: function(xhr, status, error){
				alert(status)
			}
		});
	});
})
