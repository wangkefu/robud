/**
 * Created by 123 on 2018/2/26.
 */
var works_wrap = document.getElementsByClassName('works_wrap');
works_wrap[0].addEventListener('click',function (e) {
    var e = e||window.event;
    var target = e.target || e.srcElement;
    if($(target).hasClass('glyphicon-heart')){
        var like_id = $(target).parents('.works_item').attr('data-id');
        $.ajax({
            type:"POST",
            url:"/like/",
            data: {"id":parseInt(like_id)},
            dataType: 'json',
            async:true,
            success:function(data){
                console.log(data);
                $('.works_item[data-id='+ data.id +']').find('i').html(data.likes);
                if(data.visitor_like){
                    $('.works_item[data-id='+ data.id +']').find('.like span').css('color','red');
                }else {
                    $('.works_item[data-id='+ data.id +']').find('.like span').css('color','#939598');
                }
            },
            error:function(){
                console.log('error')
            }
        })
    }
});

$('.buttons_wrap b').click(function () {
    var data = {};
    $(this).parents('.buttons_wrap').find('b').removeClass('active_customer');
    $(this).addClass('active_customer');
    if($('.cate_wrap .active_customer').length>0){
        data['type'] = parseInt($('.cate_wrap .active_customer').attr('data-id'));
    }
    if($('.month_wrap .active_customer').length>0){
        data['month'] = $('.month_wrap .active_customer').attr('data-id')
    }
    console.log(data);
    $.ajax({
        type:"GET",
        url:"/get_artists_work/",
        data: data,
        dataType: 'json',
        async:true,
        success:function(data){
			console.log(data);
            $('.works_wrap').html('');
            $.each(data.images,function (index) {
                console.log($(this)[0].id);
                if( $(this)[0].visitor_like){
                    var item = "<div class='works_item col-md-3 col-sm-6' data-id="+ $(this)[0].id +">" +
                        "<img src="+ $(this)[0].image +">" +
                        "<span>"+ $(this)[0].author +"</span>" +
                        "<span>"+ $(this)[0].age +"</span>" +
                        "<span class='like'><i>"+ $(this)[0].likes +"</i><span class='glyphicon glyphicon-heart' style='color:red'></span></span>";
                }else {
                    var item = "<div class='works_item col-md-3 col-sm-6' data-id="+ $(this)[0].id +">" +
                        "<img src="+ $(this)[0].image +">" +
                        "<span>"+ $(this)[0].author +"</span>" +
                        "<span>"+ $(this)[0].age +"</span>" +
                        "<span class='like'><i>"+ $(this)[0].likes +"</i><span class='glyphicon glyphicon-heart'></span></span>";
                }
                $('.works_wrap').append($(item))
            })
        },
        error:function(){
            console.log('error')
        }
    })
});