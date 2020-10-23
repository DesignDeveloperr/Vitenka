//Тут нет ничего такого, что отличаается от reviews.js
const get_catalog_pages = page => {
    $('.catalog_pages_item').remove()

    let active_nav_template = item => `<li class="p-2 bg-pink-600 m-1 text-white cursor-pointer catalog_pages_item">${ item }</li>`
    let nav_template = item => `<li class="p-2 m-1 bg-pink-400 text-white cursor-pointer catalog_pages_item" onclick="get_json_catalog(${ item })">${ item }</li>`

    $.get(json_catalog_pages_url, data => data.map(item => page === item ? $('#catalog_pages').append(active_nav_template(item)) : $('#catalog_pages').append(nav_template(item))))
}

const get_json_catalog = page => {
    $('.product_item').remove()

    let search_query = $('input[name="search"]').val() === '' ? 'all' : $('input[name="search"]').val()
    let order_by = $('input[name="filter"]:checked').val() === undefined ? 'none' : $('input[name="filter"]:checked').val()
    let product_template = item => `<div class="xl:col-span-4 lg:col-span-6 col-span-12 rounded bg-white p-4 product_item animate__animated animate__fadeIn"><img src="${ item.image }" class="object-cover h-64 w-full rounded" alt=""><div class="font-medium my-2 text-2xl">${ item.name }</div><div class="mb-2">${ item.price }</div><div>${ item.date }</div></div>`

    $.get('/catalog/json/' + page + '/' + search_query + '/' + order_by + '/', data => data.map(item => setTimeout(() => $('#products').append(product_template(item)), 100 * data.indexOf(item))))

    get_catalog_pages(page)
}

get_json_catalog(1)

$('input[name="search"]').change(() => get_json_catalog(1))
$('input[name="filter"]').click(() => get_json_catalog(1))