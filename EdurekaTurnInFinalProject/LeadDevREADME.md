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
benjaminadams@Benjamins-MBP LeadDev % clear

benjaminadams@Benjamins-MBP LeadDev % cd
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
benjaminadams@Benjamins-MBP JuniorDeveloper % git checkout master
Branch 'master' set up to track remote branch 'master' from 'origin'.
Switched to a new branch 'master'
benjaminadams@Benjamins-MBP JuniorDeveloper % git branch -a
  develop
  feature2
* master
  remotes/origin/develop
  remotes/origin/feature2
  remotes/origin/master
benjaminadams@Benjamins-MBP JuniorDeveloper % ls
LeadDev		pom.xml		src		walletAPI
benjaminadams@Benjamins-MBP JuniorDeveloper % touch ProjectJunDevREADME.md
benjaminadams@Benjamins-MBP JuniorDeveloper % nano ProjectJunDevREADME.md
benjaminadams@Benjamins-MBP JuniorDeveloper % git add ProjectJunDevREADME.md
benjaminadams@Benjamins-MBP JuniorDeveloper % git commit -am "Junior Dev Case Study" 
[master 0d65eca] Junior Dev Case Study
 1 file changed, 69 insertions(+)
 create mode 100644 ProjectJunDevREADME.md
benjaminadams@Benjamins-MBP JuniorDeveloper % git push -u origin master
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 1.29 KiB | 1.29 MiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://gitlab.com/NimboSurfer22/walletAPI.git
   a4130fb..0d65eca  master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
benjaminadams@Benjamins-MBP JuniorDeveloper % cd
benjaminadams@Benjamins-MBP ~ % cd LeadDev
benjaminadams@Benjamins-MBP LeadDev % ls
README.md		READMELeadDevCode.md	walletAPI
benjaminadams@Benjamins-MBP LeadDev % nano README.md
benjaminadams@Benjamins-MBP LeadDev % git branch -a
  develop
  feature1
  master
* release1
  remotes/origin/develop
  remotes/origin/feature1
  remotes/origin/master
  remotes/origin/release1
benjaminadams@Benjamins-MBP LeadDev % git checkout master
Switched to branch 'master'
benjaminadams@Benjamins-MBP LeadDev % git branch -a      
  develop
  feature1
* master
  release1
  remotes/origin/develop
  remotes/origin/feature1
  remotes/origin/master
  remotes/origin/release1
benjaminadams@Benjamins-MBP LeadDev % ls
walletAPI
benjaminadams@Benjamins-MBP LeadDev % touch ProjectLeadDevREADME.md
benjaminadams@Benjamins-MBP LeadDev % nano ProjectLeadDevREAME.md
benjaminadams@Benjamins-MBP LeadDev % git add ProjectLeadDevREADME.md
benjaminadams@Benjamins-MBP LeadDev % git commit -am "Lead Dev Case Study"
[master 66562ea] Lead Dev Case Study
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 LeadDev/ProjectLeadDevREADME.md
benjaminadams@Benjamins-MBP LeadDev % git push -u origin master
To https://gitlab.com/NimboSurfer22/walletAPI.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'https://gitlab.com/NimboSurfer22/walletAPI.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
benjaminadams@Benjamins-MBP LeadDev % git pull master
fatal: 'master' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
benjaminadams@Benjamins-MBP LeadDev % git branch -a
  develop
  feature1
* master
  release1
  remotes/origin/develop
  remotes/origin/feature1
  remotes/origin/master
  remotes/origin/release1
benjaminadams@Benjamins-MBP LeadDev % git push master
fatal: 'master' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
benjaminadams@Benjamins-MBP LeadDev % git add remote origin https://gitlab.com/NimboSurfer22/walletAPI.git
fatal: pathspec 'remote' did not match any files
benjaminadams@Benjamins-MBP LeadDev % ls
ProjectLeadDevREADME.md	ProjectLeadDevREAME.md	walletAPI
benjaminadams@Benjamins-MBP LeadDev % git push -u origin walletAPI                                        
error: src refspec walletAPI does not match any.
error: failed to push some refs to 'https://gitlab.com/NimboSurfer22/walletAPI.git'
benjaminadams@Benjamins-MBP LeadDev % nano ProjectLeadDevREAME.md                                     
benjaminadams@Benjamins-MBP LeadDev % git init                   
Initialized empty Git repository in /Users/benjaminadams/LeadDev/.git/
benjaminadams@Benjamins-MBP LeadDev % nano ProjectLeadDevREAME.md 
benjaminadams@Benjamins-MBP LeadDev % git add ProjectLeadDevREADME.md
benjaminadams@Benjamins-MBP LeadDev % git commit -am "Lead Dev Case Study"
[master (root-commit) 0380d9e] Lead Dev Case Study
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 ProjectLeadDevREADME.md
benjaminadams@Benjamins-MBP LeadDev % git push -u origin master
fatal: 'origin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
benjaminadams@Benjamins-MBP LeadDev % git remote add origin origin https://gitlab.com/NimboSurfer22/walletAPI.git
usage: git remote add [<options>] <name> <url>

    -f, --fetch           fetch the remote branches
    --tags                import all tags and associated objects when fetching
                          or do not fetch any tag at all (--no-tags)
    -t, --track <branch>  branch(es) to track
    -m, --master <branch>
                          master branch
    --mirror[=<push|fetch>]
                          set up remote as a mirror to push to or fetch from

benjaminadams@Benjamins-MBP LeadDev % git fetch master                                                           
fatal: 'master' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
benjaminadams@Benjamins-MBP LeadDev % cd      
benjaminadams@Benjamins-MBP ~ % mkdir GitFinalProject
benjaminadams@Benjamins-MBP ~ % cd GitFinalProject
benjaminadams@Benjamins-MBP GitFinalProject % touch DevOpsEngineerREADME.md
benjaminadams@Benjamins-MBP GitFinalProject % touch JuniorDeveloperREADME.md
benjaminadams@Benjamins-MBP GitFinalProject % touch LeadDevREADME.md
benjaminadams@Benjamins-MBP GitFinalProject % nano JuniorDeveloperREADE.md
benjaminadams@Benjamins-MBP GitFinalProject % cd       
benjaminadams@Benjamins-MBP ~ % cd LeadDev
benjaminadams@Benjamins-MBP LeadDev % ls
ProjectLeadDevREADME.md	ProjectLeadDevREAME.md	walletAPI
benjaminadams@Benjamins-MBP LeadDev % nano ProjectLeadDevREADME.md
benjaminadams@Benjamins-MBP LeadDev % nano ProjectLeadDevREAME.md 

  GNU nano 2.0.6                                                  File: ProjectLeadDevREAME.md                                                                                                            

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
