//Ждем события нажатия кнопки в форме отзыва
$('#send_review').click(() => {

    //Выполняется при успешном ответе от сервера
    let review_success = (data) => { $('#review_form').hide(); $('#review_success').html(data.message); show_review_from_json() }

    //Посылаем AJAX (AJAJ - Asynchronous Javascript And JSON) запрос на сервер
    $.ajax({
        url: location.href,
        //Получаем данные с полей формы
        data: $('#review_form').serialize(),
        type: 'POST'
    })
    //Получаем ответ от сервера
    .done((data) => data.type === 'error' ? $('#review_error').html(data.message) : review_success(data))
    .fail(() => $('#review_error').html('Возникла ошибка при отправке данных'))
})


//Показываем отзывы на странице
let show_review_from_json = () => {

    //Удаляем отзывы со страницы
    $('.review_item').remove()

    //Получаем JSON массив с отзывавми и показываем их
    $.get(json_reviews_url, (data) => {
        if (data.length > 0) {
            for (let i in data) {
                setTimeout(function () {
                    let item = data[i]
                    $('#reviews').append(
                        '<div class="container mx-auto bg-white p-8 rounded mb-4 review_item animate__animated animate__fadeIn">\n' +
                        '    <div class="text-2xl">' + item.name + '</div>\n' +
                        '    <div class="text-gray-700 my-2">' + item.text + '</div>\n' +
                        '    <div class="text-gray-500">' + item.date + '</div>\n' +
                        '</div>'
                    )
                }, 200 * i)
            }
        } else {
            $('#reviews').append(
                '<div class="container mx-auto bg-white p-8 rounded mb-4 review_item animate__animated animate__fadeIn">\n' +
                '    <div class="text-2xl text-center">Отзывов пока нет</div>\n' +
                '</div>'
            )
        }
    })
}

show_review_from_json()