$(document).ready(function() {
    $('.signin-form').submit(function(e) {
        e.preventDefault();
        var _this = this;
        $(_this).find('.btn-login').addClass('loading');
        $(_this).find('input').addClass('loading');
        $(_this).find('.btn-login').attr('disabled', 'disabled');
        $(_this).find('input').attr('disabled', 'disabled');

        var data = {};
        data['username'] = $(this).find('input[name=email]').val();
        data['password'] = $(this).find('input[name=password]').val();

        $.post('/api/login', data, function(data) {
            if (data['success']) {
                window.location="/";
            } else {
                $(_this).find('.btn-login').removeClass('loading');
                $(_this).find('input').removeClass('loading');
                $(_this).find('.btn-login').removeAttr('disabled');
                $(_this).find('input').removeAttr('disabled');
                $(_this).find('input').addClass('btn-danger')
            }
        }).fail(function(data) {
            $(_this).find('.btn-login').removeClass('loading');
            $(_this).find('input').removeClass('loading');
            $(_this).find('.btn-login').removeAttr('disabled');
            $(_this).find('input').removeAttr('disabled');
            $(_this).find('input').addClass('btn-danger')
        })
    });

    $('.signup-form').submit(function(e) {
        e.preventDefault();
        var _this = this;
        var data = {};
        data['username'] = $(_this).find('input[name=username]').val();
        data['password'] = $(_this).find('input[name=password]').val();


        $(_this).find('.btn-login').addClass('loading');
        $(_this).find('.uneditable-input').addClass('loading');
        $(_this).find('input').addClass('loading');

        $(_this).find('.btn-login').attr('disabled', 'disabled');
        $(_this).find('.uneditable-input').attr('disabled', 'disabled');
        $(_this).find('input').attr('disabled', 'disabled');

        $.post('/api/register', data, function(data) {
            window.location="/";
        }).fail(function(data) {
            $(_this).find('.btn-login').removeClass('loading');
            $(_this).find('.uneditable-input').removeClass('loading');
            $(_this).find('input').removeClass('loading');
            $(_this).find('input').addClass('btn-danger');

            $(_this).find('.btn-login').removeAttr('disabled');
            $(_this).find('.uneditable-input').removeAttr('disabled');
            $(_this).find('input').removeAttr('disabled');
        })
    });
});
