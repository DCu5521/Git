benjaminadams@Benjamins-MBP ~ % mkdir DesignMethod
benjaminadams@Benjamins-MBP ~ % cd DesignMethod
benjaminadams@Benjamins-MBP DesignMethod % git init
Initialized empty Git repository in /Users/benjaminadams/DesignMethod/.git/
benjaminadams@Benjamins-MBP DesignMethod % git remote add origin https://gitlab.com/NimboSurfer22/gitmethodologydesign.git                                                         
benjaminadams@Benjamins-MBP DesignMethod % git flow init
No branches exist yet. Base branches must be created now.
Branch name for production releases: [master] 
Branch name for "next release" development: [develop] 

How to name your supporting branch prefixes?
Feature branches? [feature/] 
Bugfix branches? [bugfix/] 
Release branches? [release/] 
Hotfix branches? [hotfix/] 
Support branches? [support/] 
Version tag prefix? [] 
Hooks and filters directory? [/Users/benjaminadams/DesignMethod/.git/hooks] 
benjaminadams@Benjamins-MBP DesignMethod % git branch -a
* develop
  master
benjaminadams@Benjamins-MBP DesignMethod % git flow feature start feature/112
Switched to a new branch 'feature/feature/112'

Summary of actions:
- A new branch 'feature/feature/112' was created, based on 'develop'
- You are now on branch 'feature/feature/112'

Now, start committing on your feature. When done, use:

     git flow feature finish feature/112

benjaminadams@Benjamins-MBP DesignMethod % git branch -a
  develop
* feature/feature/112
  master
benjaminadams@Benjamins-MBP DesignMethod % git flow feature start 112
Switched to a new branch 'feature/112'

Summary of actions:
- A new branch 'feature/112' was created, based on 'develop'
- You are now on branch 'feature/112'

Now, start committing on your feature. When done, use:

     git flow feature finish 112

benjaminadams@Benjamins-MBP DesignMethod % git branch -a
  develop
* feature/112
  feature/feature/112
  master
benjaminadams@Benjamins-MBP DesignMethod % git status
On branch feature/112
nothing to commit, working tree clean
benjaminadams@Benjamins-MBP DesignMethod % touch README.md
benjaminadams@Benjamins-MBP DesignMethod % nano README.md
benjaminadams@Benjamins-MBP DesignMethod % nano README.md
benjaminadams@Benjamins-MBP DesignMethod % git add .
benjaminadams@Benjamins-MBP DesignMethod % git commit -m "Commits 112"
[feature/112 584ebc1] Commits 112
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
benjaminadams@Benjamins-MBP DesignMethod % git push origin feature/112
Counting objects: 5, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (5/5), 386 bytes | 386.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0)
remote: 
remote: To create a merge request for feature/112, visit:
remote:   https://gitlab.com/NimboSurfer22/gitmethodologydesign/-/merge_requests/new?merge_request%5Bsource_branch%5D=feature%2F112
remote: 
To https://gitlab.com/NimboSurfer22/gitmethodologydesign.git
 * [new branch]      feature/112 -> feature/112
benjaminadams@Benjamins-MBP DesignMethod % git flow feature publish /112       
Fatal: Branch 'feature//112' does not exist and is required.
benjaminadams@Benjamins-MBP DesignMethod % git flow feature publish 112 
Branch 'feature/112' set up to track remote branch 'feature/112' from 'origin'.
Everything up-to-date
Already on 'feature/112'
Your branch is up to date with 'origin/feature/112'.

Summary of actions:
- The remote branch 'feature/112' was created or updated
- The local branch 'feature/112' was configured to track the remote branch
- You are now on branch 'feature/112'

benjaminadams@Benjamins-MBP DesignMethod % git branch -a
  develop
* feature/112
  feature/feature/112
  master
  remotes/origin/feature/112
  remotes/origin/main
benjaminadams@Benjamins-MBP DesignMethod % git flow develop
usage: git flow <subcommand>

Available subcommands are:
   init      Initialize a new git repo with support for the branching model.
   feature   Manage your feature branches.
   bugfix    Manage your bugfix branches.
   release   Manage your release branches.
   hotfix    Manage your hotfix branches.
   support   Manage your support branches.
   version   Shows version information.
   config    Manage your git-flow configuration.
   log       Show log deviating from base branch.

Try 'git flow <subcommand> help' for details.
benjaminadams@Benjamins-MBP DesignMethod % git checkout develop
Switched to branch 'develop'
benjaminadams@Benjamins-MBP DesignMethod % git flow feature finish 112 
Already on 'develop'
Updating 5072cb1..584ebc1
Fast-forward
 README.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
To https://gitlab.com/NimboSurfer22/gitmethodologydesign.git
 - [deleted]         feature/112
Deleted branch feature/112 (was 584ebc1).

Summary of actions:
- The feature branch 'feature/112' was merged into 'develop'
- Feature branch 'feature/112' has been locally deleted; it has been remotely deleted from 'origin'
- You are now on branch 'develop'

benjaminadams@Benjamins-MBP DesignMethod % git add .
benjaminadams@Benjamins-MBP DesignMethod % git commit -m "Finished feature 112"
On branch develop
nothing to commit, working tree clean
benjaminadams@Benjamins-MBP DesignMethod % nano README.md
benjaminadams@Benjamins-MBP DesignMethod % git commit -m "Finished feature 112"
On branch develop
Changes not staged for commit:
	modified:   README.md

no changes added to commit
benjaminadams@Benjamins-MBP DesignMethod % touch README.md
benjaminadams@Benjamins-MBP DesignMethod % nano README.md
benjaminadams@Benjamins-MBP DesignMethod % git add .                           
benjaminadams@Benjamins-MBP DesignMethod % git commit -m "Finished feature 112"
[develop caa1d33] Finished feature 112
 1 file changed, 3 insertions(+)
benjaminadams@Benjamins-MBP DesignMethod % git push
fatal: The current branch develop has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin develop

benjaminadams@Benjamins-MBP DesignMethod % git push --set-upstream origin develo
error: src refspec develo does not match any.
error: failed to push some refs to 'https://gitlab.com/NimboSurfer22/gitmethodologydesign.git'
benjaminadams@Benjamins-MBP DesignMethod % git push --set-upstream origin develop
Counting objects: 8, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (8/8), 639 bytes | 639.00 KiB/s, done.
Total 8 (delta 0), reused 0 (delta 0)
remote: 
remote: To create a merge request for develop, visit:
remote:   https://gitlab.com/NimboSurfer22/gitmethodologydesign/-/merge_requests/new?merge_request%5Bsource_branch%5D=develop
remote: 
To https://gitlab.com/NimboSurfer22/gitmethodologydesign.git
 * [new branch]      develop -> develop
Branch 'develop' set up to track remote branch 'develop' from 'origin'.
benjaminadams@Benjamins-MBP DesignMethod % git branch -a
* develop
  feature/feature/112
  master
  remotes/origin/develop
  remotes/origin/main
benjaminadams@Benjamins-MBP DesignMethod % git flow feature start 113
Switched to a new branch 'feature/113'

Summary of actions:
- A new branch 'feature/113' was created, based on 'develop'
- You are now on branch 'feature/113'

Now, start committing on your feature. When done, use:

     git flow feature finish 113

benjaminadams@Benjamins-MBP DesignMethod % touch README.md
benjaminadams@Benjamins-MBP DesignMethod % nano README.md
benjaminadams@Benjamins-MBP DesignMethod % nano README.md
benjaminadams@Benjamins-MBP DesignMethod % git add .      
benjaminadams@Benjamins-MBP DesignMethod % git commit -m "Commits 113"
[feature/113 bf63dd2] Commits 113
 1 file changed, 1 insertion(+)
benjaminadams@Benjamins-MBP DesignMethod % git push origin feature/113
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 285 bytes | 285.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote: 
remote: To create a merge request for feature/113, visit:
remote:   https://gitlab.com/NimboSurfer22/gitmethodologydesign/-/merge_requests/new?merge_request%5Bsource_branch%5D=feature%2F113
remote: 
To https://gitlab.com/NimboSurfer22/gitmethodologydesign.git
 * [new branch]      feature/113 -> feature/113
benjaminadams@Benjamins-MBP DesignMethod % git flow feature publish 113 
Branch 'feature/113' set up to track remote branch 'feature/113' from 'origin'.
Everything up-to-date
Already on 'feature/113'
Your branch is up to date with 'origin/feature/113'.

Summary of actions:
- The remote branch 'feature/113' was created or updated
- The local branch 'feature/113' was configured to track the remote branch
- You are now on branch 'feature/113'

benjaminadams@Benjamins-MBP DesignMethod % git branch -a
  develop
* feature/113
  feature/feature/112
  master
  remotes/origin/develop
  remotes/origin/feature/113
  remotes/origin/main
benjaminadams@Benjamins-MBP DesignMethod % git checkout devleop       
error: pathspec 'devleop' did not match any file(s) known to git.
benjaminadams@Benjamins-MBP DesignMethod % git checkout develop  
Switched to branch 'develop'
Your branch is up to date with 'origin/develop'.
benjaminadams@Benjamins-MBP DesignMethod % git fetch
remote: Enumerating objects: 1, done.
remote: Counting objects: 100% (1/1), done.
remote: Total 1 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (1/1), done.
From https://gitlab.com/NimboSurfer22/gitmethodologydesign
   caa1d33..5e0aeb3  develop    -> origin/develop
benjaminadams@Benjamins-MBP DesignMethod % git merge origin/develop
Updating caa1d33..5e0aeb3
Fast-forward
 README.md | 1 +
 1 file changed, 1 insertion(+)
benjaminadams@Benjamins-MBP DesignMethod % git add .
benjaminadams@Benjamins-MBP DesignMethod % git commit -m "Complete merges"
On branch develop
Your branch is up to date with 'origin/develop'.

nothing to commit, working tree clean
benjaminadams@Benjamins-MBP DesignMethod % nano README.md
benjaminadams@Benjamins-MBP DesignMethod % nano README.md
benjaminadams@Benjamins-MBP DesignMethod % git push
Everything up-to-date
benjaminadams@Benjamins-MBP DesignMethod % git flow release start 1.0
Fatal: Working tree contains unstaged changes. Aborting.
benjaminadams@Benjamins-MBP DesignMethod % git branch -a
* develop
  feature/113
  feature/feature/112
  master
  remotes/origin/develop
  remotes/origin/feature/113
  remotes/origin/main
benjaminadams@Benjamins-MBP DesignMethod % git flow release start 1.0
Fatal: Working tree contains unstaged changes. Aborting.
benjaminadams@Benjamins-MBP DesignMethod % git checkout develop
M	README.md
Already on 'develop'
Your branch is up to date with 'origin/develop'.
benjaminadams@Benjamins-MBP DesignMethod % git flow release start 1.0
Fatal: Working tree contains unstaged changes. Aborting.
benjaminadams@Benjamins-MBP DesignMethod % git status
On branch develop
Your branch is up to date with 'origin/develop'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
benjaminadams@Benjamins-MBP DesignMethod % git add README.md
benjaminadams@Benjamins-MBP DesignMethod % git commit -m "all commits"
[develop c943851] all commits
 1 file changed, 2 insertions(+)
benjaminadams@Benjamins-MBP DesignMethod % git push
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 299 bytes | 299.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote: 
remote: To create a merge request for develop, visit:
remote:   https://gitlab.com/NimboSurfer22/gitmethodologydesign/-/merge_requests/new?merge_request%5Bsource_branch%5D=develop
remote: 
To https://gitlab.com/NimboSurfer22/gitmethodologydesign.git
   5e0aeb3..c943851  develop -> develop
benjaminadams@Benjamins-MBP DesignMethod % git flow release start 1.0 
Switched to a new branch 'release/1.0'

Summary of actions:
- A new branch 'release/1.0' was created, based on 'develop'
- You are now on branch 'release/1.0'

Follow-up actions:
- Bump the version number now!
- Start committing last-minute fixes in preparing your release
- When done, run:

     git flow release finish '1.0'

benjaminadams@Benjamins-MBP DesignMethod % git status
On branch release/1.0
nothing to commit, working tree clean
benjaminadams@Benjamins-MBP DesignMethod % git branch -a
  develop
  feature/113
  feature/feature/112
  master
* release/1.0
  remotes/origin/develop
  remotes/origin/feature/113
  remotes/origin/main
benjaminadams@Benjamins-MBP DesignMethod % git push --all
Total 0 (delta 0), reused 0 (delta 0)
remote: 
remote: To create a merge request for feature/feature/112, visit:
remote:   https://gitlab.com/NimboSurfer22/gitmethodologydesign/-/merge_requests/new?merge_request%5Bsource_branch%5D=feature%2Ffeature%2F112
remote: 
remote: 
remote: To create a merge request for master, visit:
remote:   https://gitlab.com/NimboSurfer22/gitmethodologydesign/-/merge_requests/new?merge_request%5Bsource_branch%5D=master
remote: 
remote: 
remote: To create a merge request for release/1.0, visit:
remote:   https://gitlab.com/NimboSurfer22/gitmethodologydesign/-/merge_requests/new?merge_request%5Bsource_branch%5D=release%2F1.0
remote: 
To https://gitlab.com/NimboSurfer22/gitmethodologydesign.git
 * [new branch]      feature/feature/112 -> feature/feature/112
 * [new branch]      master -> master
 * [new branch]      release/1.0 -> release/1.0
benjaminadams@Benjamins-MBP DesignMethod % git push --tags 
Everything up-to-date
benjaminadams@Benjamins-MBP DesignMethod % git log
commit c943851fda9681a00aa872f438b7bd94dd96250c (HEAD -> release/1.0, origin/release/1.0, origin/develop, develop)
Author: Ben <newemail@gmail.com>
Date:   Wed Jan 18 20:01:12 2023 -0600

    all commits

commit 5e0aeb3e12f3dc1407aa18ee7d702728dbceb1c2
Merge: caa1d33 bf63dd2
Author: Benjamin Adams <techmcunetworks33@gmail.com>
Date:   Thu Jan 19 01:50:42 2023 +0000

    Merge branch 'feature/113' into 'develop'
    
    Commits 113
    
    See merge request NimboSurfer22/gitmethodologydesign!3

commit bf63dd24a1f6361c2a9e363c1587e0ee5eadbb6e (origin/feature/113, feature/113)
Author: Ben <newemail@gmail.com>
Date:   Wed Jan 18 19:44:51 2023 -0600

    Commits 113

commit caa1d337012023ecea9220e6061f3829142f7ead
Author: Ben <newemail@gmail.com>
Date:   Wed Jan 18 19:41:09 2023 -0600

    Finished feature 112

commit 584ebc153c7d3eaadf7ab4d6a59210ea795acb98
Author: Ben <newemail@gmail.com>
Date:   Wed Jan 18 19:35:01 2023 -0600

    Commits 112

commit 5072cb1b97c3e90e3fd507a0306aa9056da234cd (origin/master, origin/feature/feature/112, master, feature/feature/112)
Author: Ben <newemail@gmail.com>
Date:   Wed Jan 18 19:32:28 2023 -0600

    Initial commit
benjaminadams@Benjamins-MBP DesignMethod % git status
On branch release/1.0
nothing to commit, working tree clean
benjaminadams@Benjamins-MBP DesignMethod % 

