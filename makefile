publish: build push

build:
	docker buildx build --platform linux/amd64,linux/arm64 -t registry.digitalocean.com/seaburr/aaas:latest .

push:
	docker push registry.digitalocean.com/seaburr/aaas:latest

run:
	docker run --name abacus -d -p 8000:8000 registry.digitalocean.com/seaburr/aaas:latest

stop:
	docker stop abacus

clean:
	docker rm abacus