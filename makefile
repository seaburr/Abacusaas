build:
	docker build -t aaas:latest .

run:
	docker run --name abacus -d -p 8000:8000 aaas:latest

stop:
	docker stop abacus

clean:
	docker rm abacus