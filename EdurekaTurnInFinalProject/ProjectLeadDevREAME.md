












Last login: Tue Jan 24 16:48:21 on ttys000
benjaminadams@Benjamins-MBP LeadDev % git branch -a
* develop
  feature1
  master
  remotes/origin/develop
  remotes/origin/feature1
  remotes/origin/master
benjaminadams@Benjamins-MBP LeadDev % ls
README.md		READMELeadDevCode.md	walletAPI
benjaminadams@Benjamins-MBP LeadDev % nano READMELeadDevCode.md
benjaminadams@Benjamins-MBP LeadDev % git push -u origin develop
To https://gitlab.com/NimboSurfer22/walletAPI.git
 ! [rejected]        develop -> develop (non-fast-forward)
error: failed to push some refs to 'https://gitlab.com/NimboSurfer22/walletAPI.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
benjaminadams@Benjamins-MBP LeadDev % nano READMELeadDevCode.md 
benjaminadams@Benjamins-MBP LeadDev % git add READMELeadDevCode.md     
benjaminadams@Benjamins-MBP LeadDev % git commit -am "Lead Code"
[develop 81f9805] Lead Code
benjaminadams@Benjamins-MBP LeadDev % git push -u origin develop
Counting objects: 8, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (7/7), done.
Writing objects: 100% (8/8), 1021 bytes | 1021.00 KiB/s, done.
Total 8 (delta 1), reused 0 (delta 0)
remote: 
remote: To create a merge request for develop, visit:
remote:   https://gitlab.com/NimboSurfer22/walletAPI/-/merge_requests/new?merge_request%5Bsource_branch%5D=develop
remote: 
To https://gitlab.com/NimboSurfer22/walletAPI.git
   5bc3219..81f9805  develop -> develop
Branch 'develop' set up to track remote branch 'develop' from 'origin'.
benjaminadams@Benjamins-MBP LeadDev % nano READMELeadDevCode.md   
benjaminadams@Benjamins-MBP LeadDev % git add READMELeadDevCode.md
benjaminadams@Benjamins-MBP LeadDev % git commit -am "Lead Code"  
[develop c39a37e] Lead Code
 1 file changed, 11 deletions(-)
benjaminadams@Benjamins-MBP LeadDev % git push -u origin develop  
Counting objects: 4, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 347 bytes | 347.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0)
remote: 
remote: To create a merge request for develop, visit:
remote:   https://gitlab.com/NimboSurfer22/walletAPI/-/merge_requests/new?merge_request%5Bsource_branch%5D=develop
remote: 
To https://gitlab.com/NimboSurfer22/walletAPI.git
   81f9805..c39a37e  develop -> develop
Branch 'develop' set up to track remote branch 'develop' from 'origin'.
benjaminadams@Benjamins-MBP LeadDev % git branch release1
benjaminadams@Benjamins-MBP LeadDev % git checkout release1
Switched to branch 'release1'
benjaminadams@Benjamins-MBP LeadDev % git branch -a
  develop
  feature1
  master
* release1
  remotes/origin/develop
  remotes/origin/feature1
  remotes/origin/master
benjaminadams@Benjamins-MBP LeadDev % git merge develop
Already up to date.
benjaminadams@Benjamins-MBP LeadDev % git push -u origin release1
Total 0 (delta 0), reused 0 (delta 0)
remote: 
remote: To create a merge request for release1, visit:
remote:   https://gitlab.com/NimboSurfer22/walletAPI/-/merge_requests/new?merge_request%5Bsource_branch%5D=release1
remote: 
To https://gitlab.com/NimboSurfer22/walletAPI.git
 * [new branch]      release1 -> release1
Branch 'release1' set up to track remote branch 'release1' from 'origin'.
benjaminadams@Benjamins-MBP LeadDev % git merge develop          
Already up to date.
benjaminadams@Benjamins-MBP LeadDev % touch README.md
benjaminadams@Benjamins-MBP LeadDev % nano README.md
benjaminadams@Benjamins-MBP LeadDev % git add README.md
benjaminadams@Benjamins-MBP LeadDev % git commit -am "file for release1 branch"
[release1 6d12050] file for release1 branch
 1 file changed, 1 insertion(+), 1 deletion(-)
benjaminadams@Benjamins-MBP LeadDev % git push -u origin release1
Counting objects: 4, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 375 bytes | 375.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0)
remote: 
remote: To create a merge request for release1, visit:
remote:   https://gitlab.com/NimboSurfer22/walletAPI/-/merge_requests/new?merge_request%5Bsource_branch%5D=release1
remote: 
To https://gitlab.com/NimboSurfer22/walletAPI.git
   c39a37e..6d12050  release1 -> release1
Branch 'release1' set up to track remote branch 'release1' from 'origin'.
benjaminadams@Benjamins-MBP LeadDev % git branch -a
  develop
  feature1
  master
* release1
  remotes/origin/develop
  remotes/origin/feature1
  remotes/origin/master
  remotes/origin/release1
benjaminadams@Benjamins-MBP LeadDev % git merge develop
Already up to date.
benjaminadams@Benjamins-MBP LeadDev % git tag -a v1.0.0 -m "V1 
dquote>  
dquote> 
dquote> 
dquote> 
dquote> exit
dquote> "
benjaminadams@Benjamins-MBP LeadDev % git tag -a v1.0.0 -m "V1"
fatal: tag 'v1.0.0' already exists
benjaminadams@Benjamins-MBP LeadDev % git tag -d v1.0.0
Deleted tag 'v1.0.0' (was 4c7665e)
benjaminadams@Benjamins-MBP LeadDev % git tag -a v1.0.0 -m "V1"
benjaminadams@Benjamins-MBP LeadDev % git push --tags origin release1
Counting objects: 1, done.
Writing objects: 100% (1/1), 150 bytes | 150.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0)
To https://gitlab.com/NimboSurfer22/walletAPI.git
 * [new tag]         v1.0.0 -> v1.0.0

