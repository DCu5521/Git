benjaminadams@Benjamins-MBP ~ % mkdir calculator
benjaminadams@Benjamins-MBP ~ % cd calculator
benjaminadams@Benjamins-MBP calculator % git init
Initialized empty Git repository in /Users/benjaminadams/calculator/.git/
benjaminadams@Benjamins-MBP calculator % touch Calculator.py
benjaminadams@Benjamins-MBP calculator % nano Calculator.py
benjaminadams@Benjamins-MBP calculator % nano Calculator.py
benjaminadams@Benjamins-MBP calculator % git add Calculator.py
benjaminadams@Benjamins-MBP calculator % git commit -m "First commit of calculator phase."
[master (root-commit) 6e6a7b8] First commit of calculator phase.
 1 file changed, 20 insertions(+)
 create mode 100644 Calculator.py
benjaminadams@Benjamins-MBP calculator % git remote add origin https://gitlab.com/NimboSurfer22/calculator.git
benjaminadams@Benjamins-MBP calculator % git push -u origin master
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 415 bytes | 415.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote: 
remote: To create a merge request for master, visit:
remote:   https://gitlab.com/NimboSurfer22/calculator/-/merge_requests/new?merge_request%5Bsource_branch%5D=master
remote: 
To https://gitlab.com/NimboSurfer22/calculator.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
benjaminadams@Benjamins-MBP calculator % git clone https://gitlab.com/NimboSurfer22/calculator.git
Cloning into 'calculator'...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (6/6), done.
benjaminadams@Benjamins-MBP calculator % git ls-remote --heads origin

4ad003f8de7a263645f0c2410466de7b666eae4b	refs/heads/main
6e6a7b8c812bf86d11d52b7fd0a45a9967097451	refs/heads/master
benjaminadams@Benjamins-MBP calculator % git branch -a

* master
  remotes/origin/master
benjaminadams@Benjamins-MBP calculator % git branch feature-addition

benjaminadams@Benjamins-MBP calculator % git branch
  feature-addition
* master
benjaminadams@Benjamins-MBP calculator % git branch checkout addition
fatal: Not a valid object name: 'addition'.
benjaminadams@Benjamins-MBP calculator % git branch checkout feature-addition
benjaminadams@Benjamins-MBP calculator % git branch
  checkout
  feature-addition
* master
benjaminadams@Benjamins-MBP calculator % git branch feature-subtraction
benjaminadams@Benjamins-MBP calculator % git branch feature-division
benjaminadams@Benjamins-MBP calculator % git branch feature-multiplication
benjaminadams@Benjamins-MBP calculator % git checkout feature subtraction
error: pathspec 'feature' did not match any file(s) known to git.
error: pathspec 'subtraction' did not match any file(s) known to git.
benjaminadams@Benjamins-MBP calculator % git branch
  checkout
  feature-addition
  feature-division
  feature-multiplication
  feature-subtraction
* master
benjaminadams@Benjamins-MBP calculator % git checkout feature-addition
Switched to branch 'feature-addition'
benjaminadams@Benjamins-MBP calculator % touch calculator.py
benjaminadams@Benjamins-MBP calculator % nano calculator.py
benjaminadams@Benjamins-MBP calculator % nano calculator.py
benjaminadams@Benjamins-MBP calculator % git add calculator.py
benjaminadams@Benjamins-MBP calculator % git commit -m "addition"
On branch feature-addition
Changes not staged for commit:
	modified:   Calculator.py

Untracked files:
	calculator/

no changes added to commit
benjaminadams@Benjamins-MBP calculator % git commit -m "addition changes"
On branch feature-addition
Changes not staged for commit:
	modified:   Calculator.py

Untracked files:
	calculator/

no changes added to commit
benjaminadams@Benjamins-MBP calculator % touch Calculator.py             
benjaminadams@Benjamins-MBP calculator % nano Calculator.py
benjaminadams@Benjamins-MBP calculator % nano Calculator.py
benjaminadams@Benjamins-MBP calculator % git add Calculator.py          
benjaminadams@Benjamins-MBP calculator % git commit -m "addition changes"
[feature-addition 3c91fea] addition changes
 1 file changed, 6 insertions(+), 20 deletions(-)
 rewrite Calculator.py (93%)
benjaminadams@Benjamins-MBP calculator % git push -u origin master
Branch 'master' set up to track remote branch 'master' from 'origin'.
Everything up-to-date
benjaminadams@Benjamins-MBP calculator % git checkout feature-subtraction
Switched to branch 'feature-subtraction'
benjaminadams@Benjamins-MBP calculator % git branch
  checkout
  feature-addition
  feature-division
  feature-multiplication
* feature-subtraction
  master
benjaminadams@Benjamins-MBP calculator % touch Calculator.py
benjaminadams@Benjamins-MBP calculator % nano Calculator.py
benjaminadams@Benjamins-MBP calculator % nano Calculator.py
benjaminadams@Benjamins-MBP calculator % git add Calculator.py
benjaminadams@Benjamins-MBP calculator % git commit -m "subtraction changes"
[feature-subtraction fd93061] subtraction changes
 1 file changed, 5 insertions(+), 20 deletions(-)
 rewrite Calculator.py (86%)
benjaminadams@Benjamins-MBP calculator % git push -u origin master       
Branch 'master' set up to track remote branch 'master' from 'origin'.
Everything up-to-date
benjaminadams@Benjamins-MBP calculator % git branch
  checkout
  feature-addition
  feature-division
  feature-multiplication
* feature-subtraction
  master
benjaminadams@Benjamins-MBP calculator % git checkout feature-division
Switched to branch 'feature-division'
benjaminadams@Benjamins-MBP calculator % git branch
  checkout
  feature-addition
* feature-division
  feature-multiplication
  feature-subtraction
  master
benjaminadams@Benjamins-MBP calculator % touch Calculator.py
benjaminadams@Benjamins-MBP calculator % nano Calculator.py
benjaminadams@Benjamins-MBP calculator % nano Calculator.py
benjaminadams@Benjamins-MBP calculator % git add Calculator.py
benjaminadams@Benjamins-MBP calculator % git commit -m "division changes"
[feature-division c0297ad] division changes
 1 file changed, 6 insertions(+), 20 deletions(-)
 rewrite Calculator.py (87%)
benjaminadams@Benjamins-MBP calculator % git push -u origin master
Branch 'master' set up to track remote branch 'master' from 'origin'.
Everything up-to-date
benjaminadams@Benjamins-MBP calculator % git push origin feature-division
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 302 bytes | 302.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: 
remote: To create a merge request for feature-division, visit:
remote:   https://gitlab.com/NimboSurfer22/calculator/-/merge_requests/new?merge_request%5Bsource_branch%5D=feature-division
remote: 
To https://gitlab.com/NimboSurfer22/calculator.git
 * [new branch]      feature-division -> feature-division
benjaminadams@Benjamins-MBP calculator % git checkout feature-addtion
error: pathspec 'feature-addtion' did not match any file(s) known to git.
benjaminadams@Benjamins-MBP calculator % git checkout feature-addition
Switched to branch 'feature-addition'
benjaminadams@Benjamins-MBP calculator % nano Calculator.py
benjaminadams@Benjamins-MBP calculator % git push origin feature-addition
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 344 bytes | 344.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote: 
remote: To create a merge request for feature-addition, visit:
remote:   https://gitlab.com/NimboSurfer22/calculator/-/merge_requests/new?merge_request%5Bsource_branch%5D=feature-addition
remote: 
To https://gitlab.com/NimboSurfer22/calculator.git
 * [new branch]      feature-addition -> feature-addition
benjaminadams@Benjamins-MBP calculator % git checkout feature-subtraction
Switched to branch 'feature-subtraction'
benjaminadams@Benjamins-MBP calculator % git branch
  checkout
  feature-addition
  feature-division
  feature-multiplication
* feature-subtraction
  master
benjaminadams@Benjamins-MBP calculator % nano Calculator.py
benjaminadams@Benjamins-MBP calculator % git add Calculator.py
benjaminadams@Benjamins-MBP calculator % git commit -m "subtraction changes"
On branch feature-subtraction
Untracked files:
	calculator/

nothing added to commit but untracked files present
benjaminadams@Benjamins-MBP calculator % git push origin feature-subtraction
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 308 bytes | 308.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: 
remote: To create a merge request for feature-subtraction, visit:
remote:   https://gitlab.com/NimboSurfer22/calculator/-/merge_requests/new?merge_request%5Bsource_branch%5D=feature-subtraction
remote: 
To https://gitlab.com/NimboSurfer22/calculator.git
 * [new branch]      feature-subtraction -> feature-subtraction
benjaminadams@Benjamins-MBP calculator % git checkout feature-multiplication
Switched to branch 'feature-multiplication'
benjaminadams@Benjamins-MBP calculator % git branch
  checkout
  feature-addition
  feature-division
* feature-multiplication
  feature-subtraction
  master
benjaminadams@Benjamins-MBP calculator % touch Calculator.py
benjaminadams@Benjamins-MBP calculator % nano Calculator.py
benjaminadams@Benjamins-MBP calculator % nano Calculator.py
benjaminadams@Benjamins-MBP calculator % git add Calculator.py
benjaminadams@Benjamins-MBP calculator % git commit -m "Multiplication changes"
[feature-multiplication 212ba4e] Multiplication changes
 1 file changed, 6 insertions(+), 20 deletions(-)
 rewrite Calculator.py (85%)
benjaminadams@Benjamins-MBP calculator % git push origin feature-multiplication
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 311 bytes | 311.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: 
remote: To create a merge request for feature-multiplication, visit:
remote:   https://gitlab.com/NimboSurfer22/calculator/-/merge_requests/new?merge_request%5Bsource_branch%5D=feature-multiplication
remote: 
To https://gitlab.com/NimboSurfer22/calculator.git
 * [new branch]      feature-multiplication -> feature-multiplication
benjaminadams@Benjamins-MBP calculator % git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
benjaminadams@Benjamins-MBP calculator % git branch
  checkout
  feature-addition
  feature-division
  feature-multiplication
  feature-subtraction
* master
benjaminadams@Benjamins-MBP calculator % nano Calculator.py
benjaminadams@Benjamins-MBP calculator % nano Calculator.py
benjaminadams@Benjamins-MBP calculator % git add
Nothing specified, nothing added.
Maybe you wanted to say 'git add .'?
benjaminadams@Benjamins-MBP calculator % git add Calculator.py
benjaminadams@Benjamins-MBP calculator % git git commit -m "changes"
git: 'git' is not a git command. See 'git --help'.

The most similar command is
	init
benjaminadams@Benjamins-MBP calculator % git commit -m "changes" 
[master 21f4211] changes
 1 file changed, 4 insertions(+), 4 deletions(-)
benjaminadams@Benjamins-MBP calculator % git push -u origin master
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 325 bytes | 325.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: 
remote: To create a merge request for master, visit:
remote:   https://gitlab.com/NimboSurfer22/calculator/-/merge_requests/new?merge_request%5Bsource_branch%5D=master
remote: 
To https://gitlab.com/NimboSurfer22/calculator.git
   6e6a7b8..21f4211  master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
benjaminadams@Benjamins-MBP calculator % git merge MultiMerge
merge: MultiMerge - not something we can merge
benjaminadams@Benjamins-MBP calculator % git branch --merged
  checkout
* master
benjaminadams@Benjamins-MBP calculator % git log --merges
benjaminadams@Benjamins-MBP calculator % git branch -vv
  checkout               6e6a7b8 First commit of calculator phase.
  feature-addition       3c91fea addition changes
  feature-division       c0297ad division changes
  feature-multiplication 212ba4e Multiplication changes
  feature-subtraction    fd93061 subtraction changes
* master                 21f4211 [origin/master] changes
benjaminadams@Benjamins-MBP calculator % git branch -v --merged
  checkout 6e6a7b8 First commit of calculator phase.
* master   21f4211 changes
benjaminadams@Benjamins-MBP calculator % git branch -d checkout
Deleted branch checkout (was 6e6a7b8).
benjaminadams@Benjamins-MBP calculator % git branch
  feature-addition
  feature-division
  feature-multiplication
  feature-subtraction
* master
benjaminadams@Benjamins-MBP calculator % git branch -vv        
  feature-addition       3c91fea addition changes
  feature-division       c0297ad division changes
  feature-multiplication 212ba4e Multiplication changes
  feature-subtraction    fd93061 subtraction changes
* master                 21f4211 [origin/master] changes
benjaminadams@Benjamins-MBP calculator % git branch -v --merged
* master 21f4211 changes

