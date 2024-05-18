# TRÌNH TỰ BÀI LAB
1. Tạo Policy có tên là `DevPolicy` với full Permissions ở các dịch vụ sau: Codecommit, CodeBuild, CodeDeploy, CodePipeline, S3, DynamoDB.

- **Thực thi file:** 01-create-dev-policy.py
 
2. Tạo Group có tên là `DevGroup`.
- **Thực thi file:** 03-create-dev-group.py
 
3. Gán Policy được tạo ở bước 1 cho Group tạo ở bước 2.
- **Thực thi file:** 04-attach-dev-policy-to-dev-group.py

4. Tạo User và đặt tên là `DevUser`
- **Thực thi file:** 05-create-dev-users.py

5. Thêm user `DevUser` vào group `DevGroup` đã tạo.
- **Thực thi file:** 06-add-dev-user-to-dev-group.py

6. Tạo Access Key và Secret Access Key cho `DevUser`.
- **Thực thi file:** 07-create-access-key-for-dev-user.py

## LƯU Ý

- Thêm profile của `DevUser` vào cấu hình trên máy tính local:
    ```c
    $ aws configure --profile DevUser
    ```

- Đối với User `DevUser` được tạo ở trên không có quyền truy cập thông qua AWS Console, để kích hoạt chức năng cho phép `DevUser` có thể Login thông qua AWS Console ta thực hiện câu lệnh sau:

    ```c
    aws iam create-login-profile --user-name DevUser --password simplepassword123 --no-password-reset-required
    ```

- Để tạo SSH Keypair, dùng lệnh:
`ssh-keygen -t rsa -b 4096 -C "example@example.com"`

