$(function(){
    $('.logout').bind('click', function(){
        if(confirm("請問您是否確定登出？")){
            location.href = '/logout'
        }
    });
});
