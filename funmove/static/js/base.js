// 簡化寫法
$(document).ready(function(){

	$('.carousel').carousel({
		 // 時間差
		 interval: 3000
	});

	 $('#responsive-menu-button').sidr({
      name: 'sidr-main',
      source: '#navigation'
    });
});