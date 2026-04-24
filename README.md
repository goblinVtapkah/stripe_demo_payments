# Django app with Stripe payment

## Start

To launch the application, install docker-compose-v2
```sudo apt install docker-compose-v2```

Create an .env file and transfer the data from .env.example there, change the variables with stripe tokens (STRIPE_SECRET_KEY, STRIPE_PUBLIC_KEY)

Run: ```docker compose up --build```

## 🌐 Network

- `GET /item/:id` *get item's page*
- `GET /buy/:id` *get stripe session id*