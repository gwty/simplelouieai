#!/bin/bash

# echo "Current shell: $SHELL"
# conda info

echo "Encoding 'Hello, world!'"
python -c "import tiktoken; enc = tiktoken.get_encoding('gpt2'); print(enc.encode('Hello, world!'))"
echo ""
echo "This is an example to show python environment is working"
