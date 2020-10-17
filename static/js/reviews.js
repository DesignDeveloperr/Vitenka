
$('#send_review').click(() => {

    let review_success = (data) => { $('#review_form').hide(); $('#review_success').html(data.message) }

    $.ajax({
        url: location.href,
        data: $('#review_form').serialize(),
        type: 'POST'
    })
    .done((data) => data.type === 'error' ? $('#review_error').html(data.message) : review_success(data))
    .fail((data) => console.log(data))
})