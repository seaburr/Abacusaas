IMAGE ?= ghcr.io/seaburr/abacusaas:latest

publish: build push

build:
	docker buildx build --platform linux/amd64,linux/arm64 -t $(IMAGE) .

push:
	docker push $(IMAGE)

run:
	docker run --name abacus -d -p 8080:8080 $(IMAGE)

stop:
	docker stop abacus

clean:
	docker rm abacus

test:
	python -m pytest tests/ -v
