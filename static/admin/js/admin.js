

function sign_in() {
    var j_name = $('#j_name').val();
    var j_age = $('#j_age').val();
    var j_city = $('#j_city').val();
    var j_phone = $('#j_phone').val();
    var l_password = $('#l_password').val;
    var valid = 0;

    if (j_name === '') {
        $('#error_name').text('Please enter the Name').show();
        $('#j_name').css('border-color', 'red');
        $('#j_name').focus();
        return false;
    } else {
        $("#error_name").text('').hide();
        $('#j_name').css('border-color', 'inherit');
        valid++;
    }

    if (j_age === '') {
        $('#error_age').text('Please enter the age').show();
        $('#j_age').css('border-color', 'red');
        $('#j_age').focus();
        return false;
    } else {
        $("#error_age").text('').hide();
        $('#j_age').css('border-color', 'inherit');
        valid++;
    }

    if (j_city === '') {
        $('#error_city').text('Please enter the city').show();
        $('#j_city').css('border-color', 'red');
        $('#j_city').focus();
        return false;
    } else {
        $("#error_city").text('').hide();
        $('#j_city').css('border-color', 'inherit');
        valid++;
    }

    if (j_phone === '') {
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

    if (l_password === '') {
        $('#error_password').text('Please enter the password').show();
        $('#l_password').css('border-color', 'red');
        $('#l_password').focus();
        return false;
    } else {
        $("#error_password").text('').hide();
        $('#l_password').css('border-color', 'inherit');
        valid++;
    }
    return true;

}

function readURL(input,img) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#' + img).attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
    }
}

$("#id_team_logo").change(function () {
    var e = false;
    t = this;
    var n = window.URL || window.webkitURL;
    var i = $(this).siblings('img').attr('id');
    var s = Checkfiles(this.files[0]);
    if (s) {
        var o, u;
        if (o = this.files[0]) {
            u = new Image;
            u.onload = function () {
                if (this.width < "30" && this.height < "30") {
                    readURL(t,i);
                } else {
                    alert('Please upload image with width 28px and heigth 28px');
                    $("#id_team_logo").val('');
                    return false;
                }
            };
            u.src = n.createObjectURL(o);
        }
    } else {
        return false;
    }
});

$("#id_image_player").change(function () {
    var e = false;
    t = this;
    var n = window.URL || window.webkitURL;
    var i = $(this).siblings('img').attr('id');
    var s = Checkfiles(this.files[0]);
    if (s) {
        var o, u;
        if (o = this.files[0]) {
            u = new Image;
            u.onload = function () {
                if (this.width >= "320" && this.height >= "385") {
                    readURL(t,i);
                } else {
                    alert('Please upload image with width 320px and heigth 385px');
                    $("#id_image_player").val('');
                    return false;
                }
            };
            u.src = n.createObjectURL(o);
        }
    } else {
        return false;
    }
});

$("#id_image_news").change(function () {
    var e = false;
    t = this;
    var n = window.URL || window.webkitURL;
    var i = $(this).siblings('img').attr('id');
    var s = Checkfiles(this.files[0]);
    if (s) {
        var o, u;
        if (o = this.files[0]) {
            u = new Image;
            u.onload = function () {
                if (this.width >= "1160" && this.height >= "550") {
                    readURL(t,i);
                } else {
                    alert('Please upload image with width 1160px and heigth 550px');
                    $("#id_image_news").val('');
                    return false;
                }
            };
            u.src = n.createObjectURL(o);
        }
    } else {
        return false;
    }
});

$("#id_image_event").change(function () {
    var e = false;
    t = this;
    var n = window.URL || window.webkitURL;
    var i = $(this).siblings('img').attr('id');
    var s = Checkfiles(this.files[0]);
    if (s) {
        var o, u;
        if (o = this.files[0]) {
            u = new Image;
            u.onload = function () {
                if (this.width >= "750" && this.height >= "440") {
                    readURL(t,i);
                } else {
                    alert('Please upload image with width 750px and heigth 440px');
                    $("#id_image_event").val('');
                    return false;
                }
            };
            u.src = n.createObjectURL(o);
        }
    } else {
        return false;
    }
});

$("#id_image").change(function () {
    var e = false;
    t = this;
    var n = window.URL || window.webkitURL;
    var i = $(this).siblings('img').attr('id');
    var s = Checkfiles(this.files[0]);
    if (s) {
        var o, u;
        if (o = this.files[0]) {
            u = new Image;
            u.onload = function () {
                if (this.width >= "750" && this.height >= "440") {
                    readURL(t,i);
                } else {
                    alert('Please upload image with width 750px and heigth 440px');
                    $("#id_image").val('');
                    return false;
                }
            };
            u.src = n.createObjectURL(o);
        }
    } else {
        return false;
    }
});


function Checkfiles(e) {
    var t = e.size;
    var n = Math.round(parseInt(t) / 1024);
    var r = e.name;
    var i = r.substring(r.lastIndexOf(".") + 1);
    if (i === "jpg" || i === "JPG" || i === "JPEG" || i === "jpeg" || i === "png" || i === "PNG") {
        return true;
    } else {
        alert("Please Upload jpg or png");
        return false;
    }
}



$(document).on('click','.confirm-delete', function(){
    return confirm('Are you sure want to delete this?');
    })


