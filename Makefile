serv:
	uvicorn main.asgi:app --reload --port 8002
lint:
	isort --check-only --diff --recursive .
	black --check --diff .
