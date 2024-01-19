all: init drop

init:
	@echo "Initializing..."
	./init.sh

drop:
	@echo "Dropping..."
	./drop.sh