document.addEventListener('DOMContentLoaded', () => {
	const stripe = Stripe(buyButton.getAttribute('data-stripe-public-key'))

	buyButton.addEventListener('click', async (event) => {
		const response = await fetch(buyButton.getAttribute('data-buy-url'))
		const data = await response.json()
		if (data?.sessionId) {
			stripe.redirectToCheckout({
				sessionId: data.sessionId,
			})
		}
	})
})