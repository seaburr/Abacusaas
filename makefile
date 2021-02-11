build:
	docker build -t aaas:latest .

run:
	docker run --name abacus -d -p 5000:5000 aaas:latest

stop:
	docker stop abacus

clean:
	docker rm abacus