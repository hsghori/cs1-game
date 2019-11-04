## Git Strategy for Professor CS

1. Code will be developed in feature branches (not the master branch).
2. Merge requests will be opened once a feature is complete. Developers will tag each team member.
3. Rebase and/or squash commits before merging.
4. At least two team members need to approve the merge request for code to be merged.
5. Delete branch after merge.

## Practices
#### create branch before PR(Pull Request)
1. $ git checkout -b `<your-branch>`
2. $ git commit -m "added new module to project"
3. $ git push origin HEAD

#### update your branch with master: assumed that you are at `your-branch`
1. $ git checkout master
2. $ git pull
3. $ git checkout `<your-branch>`
4. $ git pull origin master

#### stash/rebase: assumed that you are at `your-branch`
1. $ git status
2. $ git stash
3. $ git checkout master
4. $ git pull
5. $ git checkout `<your-branch>`
6. $ git rebase master
7. $ git stash pop