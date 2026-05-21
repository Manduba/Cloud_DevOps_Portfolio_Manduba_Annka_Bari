terraform {
  required_providers {
    openstack = {
      source = "terraform-provider-openstack/openstack"
    }
  }
}

provider "openstack" {
  cloud = "openstack"
}

resource "openstack_compute_instance_v2" "worker" {
  count       = 3
  name        = "worker-${count.index + 1}"
  flavor_name = "Ubuntu 24.04-LTS (Noble Numbat)"
  key_pair    = "pre_2c2r_50g"
  security_groups = ["default"]

  network {
    name = "oslomet"
  }
}

output "worker_ips" {
  value = [for instance in openstack_compute_instance_v2.worker : instance.access_ip_v4]
}