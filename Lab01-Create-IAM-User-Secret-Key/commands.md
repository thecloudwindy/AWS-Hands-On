# 1. Adding new AWS User Profile by using AWS CLI
```c
$ aws configure --profile <new-user-name>
```

# 2. Enable Console access for an exist user by using AWS CLI
```c
aws iam create-login-profile --user-name <username> --password <set your password here> --password-reset-required
```
[Link Document](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-login-profile.html)

# 3. Update Login Profile for an exist user with no password reset required
```c
aws iam update-login-profile --user-name <username> --password <set your password here> --no-password-reset-required
```
[Link Document](https://docs.aws.amazon.com/cli/latest/reference/iam/update-login-profile.html)

# Command to generate SSH key
> ssh-keygen -t rsa -b 4096 -C "tamng.tng@gmail.com"