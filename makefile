# Variables
SRC_DIR ?= .
DEST_DIR ?= ../data-guild/grpc

# Rule to copy files and directories
copy_all:
	@echo "Checking if destination directory exists..."
	@if [ ! -d "$(DEST_DIR)" ]; then \
		echo "$(DEST_DIR) does not exist, creating directory..."; \
		mkdir -p $(DEST_DIR); \
	fi
	@echo "Copying contents from $(SRC_DIR) to $(DEST_DIR), excluding dot files and folders..."
	@rsync -a --exclude '.*' $(SRC_DIR)/ $(DEST_DIR)
	@echo "Copy complete."

.PHONY: copy_all