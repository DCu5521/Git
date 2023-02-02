benjaminadams@Benjamins-MBP ~ % mkdir JuniorDeveloper
benjaminadams@Benjamins-MBP ~ % cd JuniorDeveloper
benjaminadams@Benjamins-MBP JuniorDeveloper % git init
Initialized empty Git repository in /Users/benjaminadams/JuniorDeveloper/.git/
benjaminadams@Benjamins-MBP JuniorDeveloper % git remote add origin https://gitlab.com/NimboSurfer22/walletAPI.git
benjaminadams@Benjamins-MBP JuniorDeveloper % git clone https://gitlab.com/NimboSurfer22/walletAPI.git
Cloning into 'walletAPI'...
remote: Enumerating objects: 58, done.
remote: Total 58 (delta 0), reused 0 (delta 0), pack-reused 58
Unpacking objects: 100% (58/58), done.
benjaminadams@Benjamins-MBP JuniorDeveloper % git branch -a
benjaminadams@Benjamins-MBP JuniorDeveloper % git checkout develop
error: pathspec 'develop' did not match any file(s) known to git.
benjaminadams@Benjamins-MBP JuniorDeveloper % git branch develop
fatal: Not a valid object name: 'master'.
benjaminadams@Benjamins-MBP JuniorDeveloper % git ls-remote --heads https://gitlab.com/NimboSurfer22/walletAPI.git
c39a37e9b4238fab7d088bcdc685e5b41cd0459e	refs/heads/develop
a4130fb30c56e0dad72e16bbd9d009a54a1c30c0	refs/heads/master
benjaminadams@Benjamins-MBP JuniorDeveloper % git checkout develop
error: pathspec 'develop' did not match any file(s) known to git.
benjaminadams@Benjamins-MBP JuniorDeveloper % git fetch 
remote: Enumerating objects: 58, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 58 (delta 0), reused 1 (delta 0), pack-reused 57
Unpacking objects: 100% (58/58), done.
From https://gitlab.com/NimboSurfer22/walletAPI
 * [new branch]      develop    -> origin/develop
 * [new branch]      master     -> origin/master
 * [new tag]         v1.0.0     -> v1.0.0
benjaminadams@Benjamins-MBP JuniorDeveloper % git checkout develop
Branch 'develop' set up to track remote branch 'develop' from 'origin'.
Switched to a new branch 'develop'
benjaminadams@Benjamins-MBP JuniorDeveloper % git pull origin develop
From https://gitlab.com/NimboSurfer22/walletAPI
 * branch            develop    -> FETCH_HEAD
Already up to date.
benjaminadams@Benjamins-MBP JuniorDeveloper % git branch -a
* develop
  remotes/origin/develop
  remotes/origin/master
benjaminadams@Benjamins-MBP JuniorDeveloper % git branch feature2
benjaminadams@Benjamins-MBP JuniorDeveloper % git checkout feature2
Switched to branch 'feature2'
benjaminadams@Benjamins-MBP JuniorDeveloper % git branch -a
  develop
* feature2
  remotes/origin/develop
  remotes/origin/master
benjaminadams@Benjamins-MBP JuniorDeveloper % touch JuniorDevCodeREADME.md
benjaminadams@Benjamins-MBP JuniorDeveloper % nano JuniorDevCodeREADME.md
benjaminadams@Benjamins-MBP JuniorDeveloper % nano JuniorDevCodeREADME.md
benjaminadams@Benjamins-MBP JuniorDeveloper % git add JuniorDevCodeREADME.md
benjaminadams@Benjamins-MBP JuniorDeveloper % git commit -am "Junior Dev Logging code"
[feature2 d69bee6] Junior Dev Logging code
 1 file changed, 27 insertions(+)
 create mode 100644 JuniorDevCodeREADME.md
benjaminadams@Benjamins-MBP JuniorDeveloper % git push -u origin feature2
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 564 bytes | 564.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote: 
remote: To create a merge request for feature2, visit:
remote:   https://gitlab.com/NimboSurfer22/walletAPI/-/merge_requests/new?merge_request%5Bsource_branch%5D=feature2
remote: 
To https://gitlab.com/NimboSurfer22/walletAPI.git
 * [new branch]      feature2 -> feature2
Branch 'feature2' set up to track remote branch 'feature2' from 'origin'.
