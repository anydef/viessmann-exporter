build:
	docker build -t ghcr.io/anydef/viessmann-exporter:latest .

publish:
	docker push ghcr.io/anydef/viessmann-exporter:latest