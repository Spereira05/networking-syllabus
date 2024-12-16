.PHONY: build run stop clean

certificate:
	openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
        -keyout server.key \
        -out server.crt \
        -subj "/C=US/ST=State/L=City/O=Organization/CN=localhost"

up:
	docker compose up --build

down:
	docker compose down

clean:
	docker compose down
	docker system prune -f

test-get:
	curl -k https://localhost

test-post:
	curl -k -X POST https://localhost/items -H 'Content-Type: application/json' -d '{"name": "NovoItem"}'

test-put:
	curl -k -X PUT https://localhost/items/0 -H 'Content-Type: application/json' -d '{"name": "ItemAlterado"}'

test-delete:
	curl -k -X DELETE https://localhost/items/0