# Change a commit message

## Changing the most recent commit message

```bash
# 가장 마지막 commit 내용 수정

$ git commit --amend

# 수정완료 후 Esc 누르고

:wq
```

```bash
:wq 저장종료
:q 종료
:w 저장
:wq! 강제종료저장
:q! 강제종료
:w! 강제저장
```

## Changing the message of older or multiple commit messages

```bash
# 특정 commit 내용 수정

$ git rebase -i HEAD~2
# 2는 거슬러 올라가는 commit의 수

pick 1bdca1... <commiiiiiiiiiiiiiiiit>
pick asdf12... <commit>

# i 입력하여 편집모드로 변경한 후 수정을 진행한다

reword 1bdca1... <commit>
pick asdf12... <commit>

# ESC 누른 후 :wq!

$ git push -f origin main

```
