$(function () {
    $('[data-toggle="tooltip"]').tooltip();

    jQuery.i18n.properties({
        name: 'Messages',
        path: '/static/i18n/',
        mode: 'both',
        async: true,
        debug: false,
        callback: function () {
            $('#loginForm').validate({
                rules: {
                    email: {
                        required: true,
                        email: true
                    },
                    password: {
                        required: true,
                        minLength: 6,
                        maxLength: 20
                    }
                },
                messages: {
                    email: {
                        required: jQuery.i18n.prop('msg_email_required'),
                        email: jQuery.i18n.prop('msg_email_format_error')
                    },
                    password: {
                        required: jQuery.i18n.prop('msg_password_required'),
                        minLength: jQuery.i18n.prop('msg_password_min_length'),
                        maxLength: jQuery.i18n.prop('msg_password_max_length')
                    }
                }
            });
        }
    });
})