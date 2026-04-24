document.addEventListener('DOMContentLoaded', () => {
	const getCookie = (name) => {
		let cookieValue = null
		if (document.cookie && document.cookie !== "") {
			const cookies = document.cookie.split(";")
			for (let cookie of cookies) {
				cookie = cookie.trim()
				if (cookie.startsWith(name + "=")) {
					cookieValue = decodeURIComponent(cookie.split("=")[1])
					break
				}
			}
		}
		return cookieValue;
	}

	const selectedArray = []
	let currentCurrency = ''
	const items = document.querySelectorAll('.item-wrapper')

	items.forEach((item) => {
		const itemId = item.getAttribute('data-item-id')
		const input = item.querySelector('input')
		const currency = item.getAttribute('data-currency')
		item.addEventListener('click', () => {
			if (input.checked) {
				selectedArray.splice(selectedArray.indexOf(itemId), 1)
				if (!selectedArray.length) {
					currentCurrency = ''
					createOrder.classList.remove('active')
					items.forEach((item) => {
						const markerWrapper = item.querySelector('.marker-wrapper')
						markerWrapper.classList.remove('disabled')
					})
				}
				input.checked = false
				return
			}
			selectedArray.push(itemId)
			if (selectedArray.length === 1) {
				currentCurrency = currency
				items.forEach((item) => {
					const currency = item.getAttribute('data-currency')
					const markerWrapper = item.querySelector('.marker-wrapper')
					if (currentCurrency !== currency) markerWrapper.classList.add('disabled')
				})
			}
			createOrder.classList.add('active')
			input.checked = true
		})
	})

	createOrder.addEventListener('click', async () => {
		if (createOrder.textContent === 'Создаём...' || !selectedArray.length) return
		createOrder.textContent = 'Создаём...'
		const response = await fetch(createOrder.getAttribute('data-create-order-url'), {
			headers: {
				'Content-Type': 'application/json',
				"X-CSRFToken": getCookie("csrftoken"),
			},
			method: 'POST',
			body: JSON.stringify({
				items: selectedArray,
			}),
		})
		const data = await response.json()
		createOrder.textContent = 'Успешно, редиректим...'
		const link = document.createElement('a')
		link.href = data.orderUrl
		link.click()
	})
})