# k8s-secret-example

Secretの生成:

```
$ cat << EOF | base64
{
  "user": "example-user",
  "password": "example-password"
}
EOF
ewogICJ1c2VyIjogImV4YW1wbGUtdXNlciIsCiAgInBhc3N3b3JkIjogImV4YW1wbGUtcGFzc3dvcmQiCn0K
```

Secret適用:

```
$ kubectl apply -f secret.yml
secret/my-config-secret created

$ kubectl get secrets
NAME               TYPE     DATA   AGE
my-config-secret   Opaque   1      106s

$ kubectl get secret my-config-secret -o yaml
apiVersion: v1
data:
  credentials.json: ewogICJ1c2VyIjogImV4YW1wbGUtdXNlciIsCiAgInBhc3N3b3JkIjogImV4YW1wbGUtcGFzc3dvcmQiCn0K
kind: Secret
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","data":{"credentials.json":"ewogICJ1c2VyIjogImV4YW1wbGUtdXNlciIsCiAgInBhc3N3b3JkIjogImV4YW1wbGUtcGFzc3dvcmQiCn0K"},"kind":"Secret","metadata":{"annotations":{},"name":"my-config-secret","namespace":"default"}}
  creationTimestamp: "2024-01-14T12:11:48Z"
  name: my-config-secret
  namespace: default
  resourceVersion: "1345"
  uid: 7245a991-70b2-4712-82fe-9ffa752817b1
type: Opaque

$ echo 'ewogICJ1c2VyIjogImV4YW1wbGUtdXNlciIsCiAgInBhc3N3b3JkIjogImV4YW1wbGUtcGFzc3dvcmQiCn0K' | base64 --decode
{
  "user": "example-user",
  "password": "example-password"
}
```

Dockerビルド:

```
docker build . -t simple-app
minikube image load simple-app:latest
```

マニフェスト適用:

```
$ kubectl apply -f deployment.yml
deployment.apps/simple-app-deployment created

$ kubectl get pods
NAME                                     READY   STATUS      RESTARTS   AGE
simple-app-deployment-85995766c4-82rk5   0/1     Completed   0          1s

$ kubectl logs simple-app-deployment-85995766c4-82rk5
example-user:example-password
```
