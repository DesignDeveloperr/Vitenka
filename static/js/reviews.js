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
const show_review_from_json = () => {

    let review_template = item => `<div class="container mx-auto bg-white p-8 rounded mb-4 review_item animate__animated animate__fadeIn">${ item.name }<div class="text-2xl">${ item.text }</div><div class="text-gray-700 my-2">${ item.date }</div><div class="text-gray-500"></div></div>`
    let no_reviews_template = () => `<div class="container mx-auto bg-white p-8 rounded mb-4 review_item animate__animated animate__fadeIn"><div class="text-2xl text-center">Отзывов пока нет</div></div>`

    //Удаляем отзывы со страницы
    $('.review_item').remove()

    //Получаем JSON массив с отзывавми и показываем их
    $.get(json_reviews_url, data => data.length > 0 ? data.map(item => setTimeout(() => $('#reviews').append(review_template(item)), 100 * data.indexOf(item))) : $('#reviews').append(no_reviews_template()))
}

show_review_from_json()