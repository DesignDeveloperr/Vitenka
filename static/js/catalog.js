
let get_json_catalog = (page) => {
    $('.product_item').remove()

    let search_query = $('input[name="search"]').val() === '' ? 'all' : $('input[name="search"]').val()
    let order_by = $('input[name="filter"]:checked').val() === undefined ? 'none' : $('input[name="filter"]:checked').val()

    $.get('/catalog/json/' + page + '/' + search_query + '/' + order_by + '/', (data) => {
        for (i in data) {
            let item = data[i]
            setTimeout(function () {
                $('#products').append(
                    '<div class="xl:col-span-4 lg:col-span-6 col-span-12 rounded bg-white p-4 product_item animate__animated animate__fadeIn">\n' +
                    '    <img src="' + item.image + '" class="object-cover h-64 w-full rounded" alt="">\n' +
                    '    <div class="font-medium my-2 text-2xl">' + item.name + '</div>\n' +
                    '    <div class="mb-2">' + item.price + '</div>\n' +
                    '    <div>' + item.date + '</div>\n' +
                    '</div>'
                )
            }, 200 * i)
        }
    })
}

get_json_catalog(1)

$('input[name="search"]').change(() => get_json_catalog(1))
$('input[name="filter"]').click(() => get_json_catalog(1))