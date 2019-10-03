### Basic

   github 사이트에서 새로운 repo를 만든다. 
    
   `git clone 'https://github.com/github계정/github레포'`  : 로컬에서 원하는 디렉토리에 github repo를 clone한다.
    
    
   `git add -A`
 
   
   `git commit -m "Type about commit message"`
   
   `git push origin `

- 푸시할 때 내가 git push를 처음 하는 경우에는 git push origin master라고 해준다.


### Faced Error

- case 1 : 깃헙 사이트에서 변경사항이 있을 경우 발생하는 에러

    사이트에서 내가 직접 변경했을 때는 로컬에서 변경된 상황이 적용되지 않았으므로 푸시과정에서 에러가 발생한다. 
    ```python 
    error: failed to push some refs to 'https://github.com/github계정/github레포'
    hint: Updates were rejected because the remote contains work that you do
    hint: not have locally. This is usually caused by another repository pushing
    hint: to the same ref. You may want to first integrate the remote changes
    hint: (e.g., 'git pull ...') before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.
    ```
    이럴 경우에 힌트에서도 나와있듯이 push 전에 pull을 하면 변경된 상황이 로컬에도 적용되고, 그 뒤에는 정상적으로 푸시된다!
    
   
 ### Rules about commit message
