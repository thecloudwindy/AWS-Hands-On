## Clone codecommit repository 
```c
> git clone ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/myrepo
```

## Các lệnh tương tác:
> cd myrepo

>
## Tương tác với Git và push lên CodeCommit Repository
```c
> git checkout -b dev
> touch README.txt
> git add .
> git commit -m "Add Readme text file"
> git push origin dev
```

**Tạo Pull Request và thực hiện Merge từ nhánh dev sang nhánh master trên CodeCommit Console**
