document.addEventListener('DOMContentLoaded', () => {
	const stripe = Stripe(buyOrderButton.getAttribute('data-stripe-public-key'))

	buyOrderButton.addEventListener('click', async (event) => {
		const response = await fetch(buyOrderButton.getAttribute('data-buy-url'))
		const data = await response.json()
		if (data?.sessionId) {
			stripe.redirectToCheckout({
				sessionId: data.sessionId,
			})
		}
	})
})