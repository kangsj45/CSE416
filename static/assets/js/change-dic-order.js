$(document).ready(function(){


    $.ajax({
        url:'./getAllDic',
        type:'get',
        success:function(dicList){
            $.each(JSON.parse(dicList),function(index,obj){
                var number = obj.number;
                var source = obj.source;
                var element = $('.my-select[data-index="'+number+'"]');
                element.find('select').val(source);
            });
        },
        error:function(err){

        }
   });


    $('#change-btn').on('click',function(){
        var isDefaultValue=false;

        var all_select = $('.my-select');
        var arr=[];
        all_select.each(function(i,item){
            var obj = {};
            obj.index=parseInt($(item).data('index'));
            obj.source = $(item).find('select').val();
            arr.push(obj);
        });
      
        
    $.each(arr,function(index,obj){
       if(obj.source=='Open this select menu'){
            isDefaultValue=true;
       } 
    });
    
    if(!isDefaultValue){
        $.each(arr,function(index,obj){
            var number = obj.index;
            var source = obj.source;
     
            $.ajax({
                 url:'./addDicOrder',
                 type:'post',
                 data:{
                     number:parseInt(number),
                     source:source
                 },
                 success:function(res){
                     console.log(res);
                 },
                 error:function(err){
     
                 }
            });
         })
    }else{
        alert('모든 항목을 입력하세요');
    }


    })
})