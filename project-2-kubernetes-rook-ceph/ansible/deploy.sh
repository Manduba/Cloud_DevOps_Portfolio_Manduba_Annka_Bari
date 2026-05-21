#!/bin/bash

echo "Running terraform init..."
terraform init

echo "Running terraform plan..."
terraform plan

echo "Applying Terraform to create VMs..."
terraform apply --auto-approve

echo "Generating dynamic inventory for Ansible..."
./generate_inventory.sh

echo "Running Ansible setup..."
ansible-playbook -i inventory.ini setup.yml

echo "DONE: All steps completed successfully!"