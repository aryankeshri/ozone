if ($(window).width() > 768) {
    $('header .header-menu ul li').mouseenter(function () {
        if ($(this).find('.menu-dropdown').length !== 0) {
            $(this).addClass('in');
        }
    });
}
$('header .header-menu ul li').mouseleave(function () {
    $(this).removeClass('in');
});

$(window).scroll(function (e) {
    if ($(this).scrollTop() > 1)
    {
        $('header').addClass('scrolled');
    } else
    {
        $('header').removeClass('scrolled');
    }
});

function join_us() {
    var j_name = $('#j_name').val();
    var j_age = $('#j_age').val();
    var j_city = $('#j_city').val();
    var j_phone = $('#j_phone').val();
    var valid = 0;

    if (j_name == '') {
        $('#error_name').text('Please enter the Name').show();
        $('#j_name').css('border-color', 'red');
        $('#j_name').focus();
        return false;
    } else {
        $("#error_name").text('').hide();
        $('#j_name').css('border-color', 'inherit');
        valid++;
    }

    if (j_age == '') {
        $('#error_age').text('Please enter the age').show();
        $('#j_age').css('border-color', 'red');
        $('#j_age').focus();
        return false;
    } else {
        $("#error_age").text('').hide();
        $('#j_age').css('border-color', 'inherit');
        valid++;
    }

    if (j_city == '') {
        $('#error_city').text('Please enter the city').show();
        $('#j_city').css('border-color', 'red');
        $('#j_city').focus();
        return false;
    } else {
        $("#error_city").text('').hide();
        $('#j_city').css('border-color', 'inherit');
        valid++;
    }

    if (j_phone == '') {
        $('#error_phone').text('Please enter the phone number');
        $('#j_phone').css('border-color', 'red');
        $('#j_phone').focus();
        return false;
    } else if ((j_phone.length) < 10 || (j_phone.length) > 15) {
        $('#error_phone').text('Please enter 10 digit phone number');
        $('#j_phone').css('border-color', 'red');
        $('#j_phone').focus();
        return false;
    } else {
        $("#error_phone").text('');
        $('#j_phone').css('border-color', 'inherit');
        valid++;
    }

    return true;

}
function join_us_popup() {
    var p_name = $('#p_name').val();
    var p_age = $('#p_age').val();
    var p_city = $('#p_city').val();
    var p_phone = $('#p_phone').val();
    var valid = 0;

    if (p_name == '') {
        $('#p_error_name').text('Please enter the Name').show();
        $('#p_name').css('border-color', 'red');
        $('#p_name').focus();
        return false;
    } else {
        $("#p_error_name").text('').hide();
        $('#p_name').css('border-color', 'inherit');
        valid++;
    }

    if (p_age == '') {
        $('#p_error_age').text('Please enter the age').show();
        $('#p_age').css('border-color', 'red');
        $('#p_age').focus();
        return false;
    } else {
        $("#p_error_age").text('').hide();
        $('#p_age').css('border-color', 'inherit');
        valid++;
    }

    if (p_city == '') {
        $('#p_error_city').text('Please enter the city').show();
        $('#p_city').css('border-color', 'red');
        $('#p_city').focus();
        return false;
    } else {
        $("#p_error_city").text('').hide();
        $('#p_city').css('border-color', 'inherit');
        valid++;
    }

    if (p_phone == '') {
        $('#p_error_phone').text('Please enter the phone number');
        $('#p_phone').css('border-color', 'red');
        $('#p_phone').focus();
        return false;
    } else if ((p_phone.length) < 10 || (p_phone.length) > 15) {
        $('#p_error_phone').text('Please enter 10 digit phone number');
        $('#p_phone').css('border-color', 'red');
        $('#p_phone').focus();
        return false;
    } else {
        $("#p_error_phone").text('');
        $('#p_phone').css('border-color', 'inherit');
        valid++;
    }

    return true;

}

$(window).load(function () {
    $('#preloader').fadeOut('slow', function () {
        $(this).remove();
    });
});
