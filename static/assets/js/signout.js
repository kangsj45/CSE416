$(document).ready(function(){


    $('#signout-btn').on('click',function(){


        var con = confirm('정말 로그아웃 하시겠습니까?');

        if(con){
            $.ajax({
                url:'./signout',
                type:'post',
                data:{
                },
                success:function(msg){
                   if(msg=='ok'){
                      location.replace('./');
                   }else{
                      alert('로그아웃 실패'); 
                   }
                },
                error:function(err){
      
                }
            });
        }

      
    })
 })