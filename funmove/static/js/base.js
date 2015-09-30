$(window).on('beforeunload', function() {
    $(window).scrollTop(0); 
});
// 簡化寫法
$(document).ready(function(){
	// RWD Sider Menu
	$('#responsive-menu-button').sidr({
      name: 'sidr-main',
      source: '#navigation'
    });

	// Navbar的滾動影響
	$(window).scroll(function(){
		var current_height = $(window).scrollTop();
		var navbar_bottom_height = 100;
		// console.log('current height = ' + current_height)
		// 往下滾動時
		if(current_height > navbar_bottom_height) {
			//顯示css
			$('.navbar-fixed-top').removeClass('navbar-no-background')
			.addClass('navbar-background',{duration:500});
		}
		// 滾動回去
		else if(current_height == 0){
			$('.navbar-fixed-top').removeClass('navbar-background')
			.addClass('navbar-no-background',{duration:500});
		}
		
	});
});