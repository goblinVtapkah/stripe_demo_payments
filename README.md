# Django app with Stripe payment

## Start

To launch the application, install docker-compose-v2
```
sudo apt install docker-compose-v2
```

Create an .env file and transfer the data from .env.example there, change the variables with stripe tokens (STRIPE_SECRET_KEY, STRIPE_PUBLIC_KEY)

Run:
```
docker compose up --build
```

For create superuser run command:
```
sh ./scripts/django_createsuperuser.sh
```

## 🌐 Network

- `GET /admin` *Админка*
- `GET /item/` *get all items page*
- `GET /item/:id` *get item's page*
- `GET /buy/:id` *get stripe session id for *
- `GET /order/` *get all orders page*
- `POST /order/create/` *create order*
- `GET /order/:id` *get order's page*
- `GET /order/buy/:id` *get stripe session id*