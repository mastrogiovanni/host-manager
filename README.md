# host-manager

Management of /etc/hosts file to add and remove mappings

Usage:
```
host-manager [add|del] hostname [ip]
```

## Examples

The following maps host kubeflow.development.com to ip 192.168.0.1:
```
> host-manager add kubeflow.development.com 192.168.0.1
```

The following removes the mapping of host kubeflow.development.com
```
> host-manager del kubeflow.development.com
```
