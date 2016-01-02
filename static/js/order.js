$(document).ready(function(){ 

			    	$("input").addClass("form-control");

				      var opt1={
				      	dateFormat: "yy-mm-dd"
				      }	
				      var opt2={
				      	
		                stepHour:1, 
		                stepMinute:30,
		                
		              };
				      $("#id_reservation_date").datepicker(opt1);
				      $("#id_reservation_time").timepicker(opt2);


					$(".btn1").click(function(){
						$("html,body").animate({scrollTop:$('#main').offset().top},800);
					});
					
					$(".btn2").click(function(){
						$("html,body").animate({scrollTop:$('#user').offset().top},800);
					});

					$(".btn3").click(function(){
						$("html,body").animate({scrollTop:$('header').offset().top},800);
					});

					$(".btn4").click(function(){
						$("html,body").animate({scrollTop:$('#verify').offset().top},800);
					});


			    	var rule_phone = /^09\d{8}/;
			    	$('#id_cell_phone').blur(function(){
			    		if(rule_phone.test($(this).val())){
			    			$(this).css("border-color","");
			    			$('#vali_phone').empty().append("<p>OK</p>");
			    		}else{
			    			$(this).css("border-color","red");
			    			$('#vali_phone').empty().append("<p>Not available!</p>")
			    		}
		            });

		            
						$('#calendar').fullCalendar({
							defaultView: 'basicDay',
							defaultDate: new Date(),
							editable: false,
							eventLimit: true, // allow "more" link when too many events
							buttonText: {
						        today: '今日訂單',
								prev: '上一日', // left triangle
                				next: '下一日', // right triangle
						    },
						    timeFormat: 'H:mm',
						    columnFormat: {
						        day: 'dddd'
						    },
						    titleFormat: {
						        day: 'YYYY/MMMM/D'
						    },
						    monthNames: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
						    dayNames: ["星期天", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"],
							events: [
								{
									"title": 'Meeting',
									"start": '2016-01-02T10:30:00',
									"end": '2016-01-02T12:30:00'
								},
								{
									"start": "2015-12-31T12:00:00", 
									"allDay": false, 
									"end": "2015-12-31T12:00:00", 
									"id": 1, 
									"title": "reserved"
								}, 
								{
									"start": "2015-12-31T12:00:00", 
									"allDay": false, 
									"end": "2015-12-31T14:00:00", 
									"id": 2, 
									"title": "reserved"
								}
							]
						});	

					$('#id_reservation_date').change(function(){
		            	var chooseDay = $(this).val();
		            	$('#calendar').fullCalendar( 'gotoDate', chooseDay );
					});		

					$('#id_time_needed_hr,#id_time_needed_min').change(function(){
		            	var hr = $('#id_time_needed_hr').val();
		            	var min = $('#id_time_needed_min').val();
		            	calPrice(hr,min);
					});

					$('#priceHelp').bubbletip($('#priceTip'), { 
						deltaDirection: 'right' ,
						positionAtElement: $('#hint')
					});

					$('#cont').bubbletip($('#contTip'), { 
						deltaDirection: 'down'
					});		

});
//onDRAGSTART="window.event.returnValue=false" onCONTEXTMENU="window.event.returnValue=false" onSelectStart="event.returnValue=false"

				
function calPrice(hr,min){
	var total = 0;
	total = hr * 600 + (min/30)*300 ; 
	if(total==0){
		document.getElementById("dollar").innerHTML = "費用另計，請與服務人員聯絡" ;
	}else{
		document.getElementById("dollar").innerHTML = "估計費用約為： " + total + " 元整" ;
	}
}

function cacheData(){
	document.getElementById("departure").innerHTML = "出發地: " + document.getElementById("id_departure").value;
	document.getElementById("destination").innerHTML = "目的地: " + document.getElementById("id_destination").value;
	document.getElementById("reservation_date").innerHTML = "預約時間: " + document.getElementById("id_reservation_date").value + " " + document.getElementById("id_reservation_time").value;
	document.getElementById("time_needed").innerHTML = "使用服務時間: " + document.getElementById("id_time_needed_hr").value + "小時" + document.getElementById("id_time_needed_min").value + "分鐘";
	document.getElementById("user_name").innerHTML = "姓名: " + document.getElementById("id_name").value;
	document.getElementById("user_email").innerHTML = "Email: " + document.getElementById("id_email").value;
	document.getElementById("user_cellphone").innerHTML = "手機: " + document.getElementById("id_cell_phone").value;
	document.getElementById("user_birth").innerHTML = "生日: " + document.getElementById("id_birth_year").value + "/" + document.getElementById("id_birth_month").value + "/" + document.getElementById("id_birth_day").value;
	document.getElementById("price").innerHTML = document.getElementById("dollar").innerHTML ;
}


