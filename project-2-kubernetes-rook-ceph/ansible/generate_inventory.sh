#!/bin/bash

echo "[workers]" > inventory.ini

terraform output -json worker_ips | jq -r '.[]' | while read ip; do
  echo "$ip ansible_host=$ip" >> inventory.ini
done

echo "" >> inventory.ini
echo "[all:vars]" >> inventory.ini
echo "ansible_user=ubuntu" >> inventory.ini

echo "inventory.ini generated:"
cat inventory.ini