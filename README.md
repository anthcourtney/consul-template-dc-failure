# consul-template-dc-failure

A simple ansible playbook which demonstrates how to handle the failure of a consul datacenter (in a distributed WAN setup) by using a plugin.

## Execution

```
$ ansible-playbook -i localhost site.yml
```

## Basics

This playbook:

1. Sets up a 3 datacenter consul setup:

* alpha
* beta
* gamma

2. Runs consul-template and validates that all 3 datacenters are mentioned in the outputted template.

3. Stops 2 of the 3 servers in the beta datacenter (thereby causing the cluster to lose consensus).

4. Runs consul-template and validates that the `alpha` and `gamma` dataceters are mentioned in the outputted template, and that the `beta` datacenter is not present in the outputted template.

