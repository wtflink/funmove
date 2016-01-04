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
							header: {
								left: 'prev,next today',
								center: 'title',
								right: 'basicWeek,basicDay'
							},
							defaultView: 'basicDay',
							defaultDate: new Date(),
							editable: false,
							eventLimit: true, // allow "more" link when too many events
							buttonText: {
						        today: '今日訂單',
						        week: '周訂單',
						        day: '日訂單',
								prev: '◄', // left triangle
                				next: '►', // right triangle
						    },
						    timeFormat: 'H:mm',
						    columnFormat: {
						    	week: 'dddd MMMM/D ',
						        day: 'dddd'
						    },
						    titleFormat: {
						    	week: 'YYYY年MMMM月D日',
						        day: 'YYYY年MMMM月D日'
						    },
						    monthNames: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
						    dayNames: ["星期天", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"],
						    eventAfterRender: function (event, element) {
                				$('.fc-content, .fc-time, .fc-title').css('font-size', '2em');
                			},
							events: //'/order/events.json'
							[
		                        {
		                   			title: 'Reserved',
		                            start  : '2016-01-03 06:00:00',
		                            end  : '2016-01-03 08:00:00',                          
		                            allDay : false
		                    }]
						});	
						

					$('#id_reservation_date').change(function(){
		            	var chooseDay = $(this).val();
		            	$('#calendar').fullCalendar( 'gotoDate', chooseDay );
					});		

					$('.fc-content, .fc-time, .fc-title').css('font-size', '2em');

					$('#id_time_needed_hr,#id_time_needed_min').change(function(){
		            	var hr = $('#id_time_needed_hr').val();
		            	var min = $('#id_time_needed_min').val();
		            	calPrice(hr,min);
					});

					$('#priceHelp').bubbletip($('#priceTip'), { 
						deltaDirection: 'right' ,
						positionAtElement: $('#hint')
					});

					$('.checkPos').bubbletip($('#mapTip'), { 
						deltaDirection: 'right' ,
						positionAtElement: $('.yesPos')
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

function checkForm(){
	var alertMessage = "";
	if(funmove.time_needed_hr.value==0&&funmove.time_needed_min.value==0){
		alertMessage += "您的使用服務時間忘了填喔！\n\n"
	}
	if(funmove.name.value==""){
		alertMessage += "您的姓名忘了填喔！\n\n"
	}
	if(funmove.email.value==""){
		alertMessage += "您的Email忘了填喔！\n\n"
	}
	if(funmove.cell_phone.value==""){
		alertMessage += "您的手機忘了填喔！\n\n"
	}
	if(alertMessage==""){
		funmove.submit();
	}else{
		alert(alertMessage);
	}
	
}

function cacheData(){
	document.getElementById("departure").innerHTML = "起始地: " + document.getElementById("id_departure").value.substring(5);
	document.getElementById("destination").innerHTML = "目的地: " + document.getElementById("id_destination").value.substring(5);
	document.getElementById("reservation_date").innerHTML = "預約時間: " + document.getElementById("id_reservation_date").value + " " + document.getElementById("id_reservation_time").value;
	document.getElementById("time_needed").innerHTML = "預計多久: " + document.getElementById("id_time_needed_hr").value + "小時" + document.getElementById("id_time_needed_min").value + "分鐘";
	document.getElementById("user_name").innerHTML = "姓名: " + document.getElementById("id_name").value;
	document.getElementById("user_email").innerHTML = "Email: " + document.getElementById("id_email").value;
	document.getElementById("user_cellphone").innerHTML = "手機: " + document.getElementById("id_cell_phone").value;
	document.getElementById("user_birth").innerHTML = "生日: " + document.getElementById("id_birth_year").value + "/" + document.getElementById("id_birth_month").value + "/" + document.getElementById("id_birth_day").value;
	document.getElementById("remarks").innerHTML = "備註: " + document.getElementById("id_remarks").value;
	document.getElementById("price").innerHTML = document.getElementById("dollar").innerHTML ;
}


