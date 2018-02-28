/**
 * Created by 123 on 2017/10/10.
 */

$(".nav_item_wrap").each(function (index) {
	$(this).mouseenter(function () {
		$(this).find('.nav_icon').attr('src',"/static/images/base/nav_icon"+ parseInt(index+1) +"_active.png");
		$(this).find('.nav_dropdown').show();
		if($(this).find('.nav_dropdown').length==1){
			$('.dropdown_bg').height($(this).find('.nav_dropdown').height()+20);
			if($(document).width()>=981){
				$('.dropdown_bg').show();
			}
		}
	}).mouseleave(function () {
		$(this).find('.nav_icon').attr('src',"/static/images/base/nav_icon"+ parseInt(index+1) +".png");
		$(this).find('.nav_dropdown').hide();
		$('.dropdown_bg').hide();
	})
});
$('.sssss').click(function () {
	$('.nav_link_wrap').toggleClass("nav_item_toggle");
});

//首页的
$('.grow_item').each(function (index) {
	$(this).mouseenter(function () {
		$(this).find('.grow_hover').show();
	}).mouseleave(function () {
		$(this).find('.grow_hover').hide();
	})
});

var mySwiper = new Swiper('.swiper-container',{
		autoplay:3000,
		autoplayDisableOnInteraction : false,
		loop:true,
		pagination: '.swiper-pagination',
		paginationClickable :true,
		nextButton: '.swiper-button-next',
	    prevButton: '.swiper-button-prev',
	});


$('.xs_to').each(function (index) {
	$(this).mouseenter(function () {
		$(this).find('.nav_item_dropdown').show()
	});
	$(this).mouseleave(function () {
		// $(this).find('.nav_item_dropdown').hide()
	});
});


//导航获取数据
$.ajax({
        type:"get",
        url:"/get_labels",
        async:true,
        success:function(data){
			console.log(data)
			for(var i=0;i<data.label_age.length;i++){
				$node = '<li><a href="/products/'+ data.label_age[i].type +'/'+ data.label_age[i].id +'">'+ data.label_age[i].name +'</a></li>'
				$('.divi_by_age').append($node)
			}
			for(var i=0;i<data.label_category.length;i++){
				$node = '<li><a href="/products/'+ data.label_category[i].type +'/'+ data.label_category[i].id +'">'+ data.label_category[i].name +'</a></li>'
				$('.divi_by_cate').append($node)
			}
			for(var i=0;i<data.video_type.length;i++){
				$node = '<li><a href="/video_index/'+ data.video_type[i].id +'/">'+ data.label_category[i].name +'</a></li>'
				$('.divi_by_videotype').append($node)
			}
        },
        error:function(){
            console.log('error')
        }
    });

