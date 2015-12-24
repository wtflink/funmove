$(document).ready(function(){ 

			    	$("input").addClass("form-control");

				      var opt1={
				      	dateFormat: "yy-mm-dd"
				      }	
				      var opt2={
				      	showSecond: true,
		                stepHour:1, 
		                stepMinute:30,
		                secondText:"will use"
		              };
				      $("#id_reservation_date").datepicker(opt1);
				      $("#id_reservation_time").timepicker();


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
							events: [
								
							]
						});	

					$('#id_reservation_date').change(function(){
		            	var chooseDay = $(this).val();
		            	$('#calendar').fullCalendar( 'gotoDate', chooseDay );
					});		

});
//onDRAGSTART="window.event.returnValue=false" onCONTEXTMENU="window.event.returnValue=false" onSelectStart="event.returnValue=false"

				
function calPrice(){
	var usedTime = document.getElementById("id_time_needed_min").value;
	if(usedTime==6){
		document.getElementById("dollar").innerHTML = "費用另計，請與服務人員聯絡" ;
	}else{
		document.getElementById("dollar").innerHTML = "費用: " + usedTime * 300 + "元" ;
	}
}

function cacheData(){
	document.getElementById("departure").innerHTML = "出發地: " + document.getElementById("id_departure").value;
	document.getElementById("destination").innerHTML = "目的地: " + document.getElementById("id_destination").value;
	document.getElementById("reservation_date").innerHTML = "日期: " + document.getElementById("id_reservation_date").value;
	document.getElementById("reservation_time").innerHTML = "時間: " + document.getElementById("id_reservation_time").value;
	document.getElementById("time_needed_min").innerHTML = "使用服務: " + document.getElementById("id_time_needed_min").value + "個半小時";
	document.getElementById("user_name").innerHTML = "姓名: " + document.getElementById("id_name").value;
	document.getElementById("user_email").innerHTML = "Email: " + document.getElementById("id_email").value;
	document.getElementById("user_cellphone").innerHTML = "手機: " + document.getElementById("id_cell_phone").value;
	document.getElementById("user_birth").innerHTML = "生日: " + document.getElementById("id_birth_year").value + "/" + document.getElementById("id_birth_month").value + "/" + document.getElementById("id_birth_day").value;
	document.getElementById("price").innerHTML = document.getElementById("dollar").innerHTML ;
}

