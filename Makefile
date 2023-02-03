.PHONY: init deploy run build publish


build:
	docker buildx build --push --platform linux/arm/v7,linux/arm/v8,linux/amd64 -t ghcr.io/anydef/viessmann-exporter:latest .

publish:
	docker push ghcr.io/anydef/viessmann-exporter:latest