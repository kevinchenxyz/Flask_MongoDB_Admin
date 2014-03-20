$(document).ready(function(){

    /* Reading */
    if($('#p_type').val() == 'reading'){
        $('#1-1-1').css('display', 'block');
        $('#q-1').css('display', 'block');
        $('.q_index').bind('click', function(){

            q_control = $(this).attr('serial-num').split('-');
            $('.question').css('display', 'none');
            $('#q-' + q_control[1]).css('display', 'block');
            $('.sub_q').css('display', 'none');
            $('#' + $(this).attr('serial-num')).css('display', 'block');
        });
    }
    else{

        $('#1-1').css('display', 'block');
        $('.q_index').bind('click', function(){

            $('.question').css('display', 'none');
            $('#'+$(this).attr('serial-num')).css('display', 'block');
        });

    }

    //讓checkbox擁有像raio button的行為(group單選)
    $("input:checkbox").click(function() {
        if ($(this).is(":checked")) {
            var name = $(this).attr('name'),
                group = "input:checkbox[name='" + name + "']";
            $(group).prop("checked", false);
            $(this).prop("checked", true);
            $(this).parent().parent().children('label').css('border', '');
            $(this).parent().css('border', '1px solid red')

        } else {
            $(this).prop("checked", false);
        }
    });
});
