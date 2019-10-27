# Git Guide

[Return to main page](../index.md)

Written by Annie Williams

## What is Git?
Git is a version control system for writing code. It allows us to all edit the same piece of code, kind of like Google Documents. Git also allows us to revert our code back to previous versions when we break things, test out different versions, and easily decide whose changes we want to keep or discard. 

## What is the difference between Git and Github?
Git is the actual version control system that *lives on your computer*, while [Github](https://github.com) is an *online service* that stores projects. Github is also a good place to find open source projects to contribute to, and network with other people. If you want to contribute code to the JC project, you will need to create an account and install Git - instructions for getting Git based on your machine are [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Getting Started
1. [Create a Github account](https://github.com/)
2. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
3. [Get comfortable with Git by making your own repo & adding to it](https://guides.github.com/activities/hello-world/)
4. Fork the jjcap repository (aka repo - a fancy name for where our project lives online) when you are ready to start working by going [here](https://github.com/Juanjo-Capital/jjcap) and clicking the "fork" button in the upper right hand corner

## What is forking?
Forking is copying somebody else’s repo so that you can completely mess up your own version without any consequences. It also allows the owner of the parent repository to decide which changes get added to the final copy. 

Once you fork the Juanjo-Capital repository, it will create a new copy under yourusername/repositoryname. This is the new repository you will add your code to instead of the parent one.  

In order to download this new repository onto your computer, you will need to **clone** by going to the repo page on [github.com](https://github.com/), clicking the green "clone or download" button, and copying the link. On your command line, use the command `git clone` followed by the URL you just copied. If you ever mess things up beyond belief and just want to start over, you can always delete your version and clone the most up to date version from Github.

## What are branches? 
If you look at the Juanjo-Capital repository, you will see that there is a "master branch." This is the version of the code that should (in theory) always be a functioning copy of the code that we can fall back on. Code shouldn’t go onto the master branch until we are certain that the code does exactly what we want it to do.

For each new feature you want to code, you should create a new branch and work on it there. This is a helpful way to have multiple versions of the code on your machine at the same time. You can have a fully functioning master branch, as well as other branches with potential versions to play with and screw up. 

To create a new branch: 
1. `git branch` - this will show you all of your available branches. Make sure you are on the master branch & that your master branch is up to date by fetching (see below)
2. `git checkout -b newbranchname` - this will create a new branch (`-b`) and put you on that branch (`git checkout`).  

## How do I add code to a remote repository (how do I put my code online for everyone else to use)? 

In your terminal/shell, change directories (`cd`) into the folder that your new code is in that you want to add to the repository so that everybody else can access it. 

1. `git status` - this will show you which files you have changed, and which are ready to go
2. `git add filename` - select the new updated files you want to go up into the repo
3. `git commit -m "description of changes"` - after adding the files you want, this command saves a version of your changes on your computer. You can revert back to a commit if you break stuff and want to go back. Don’t forget the quotes around your commit message, or git will get upset.
4. `git push origin branchname` - when we push it sends our commit history of the branch we are on to the repository online for everybody else to see. We use `origin` to specify that we are sending code to the place we cloned from earlier. Check online to see if your code is there or if you aren’t sure your push worked. 

## I've done some work, how do I add it to the main Juanjo Capital repo?
Once you've committed your changes to your fork, you will need to create a pull request if you want your changes merged into the main repo:

1. Go to the main page of your fork (the URL should be github.com/yourname/jjcap).
2. Click on the **Pull requests** tab (it's located next to the Code tab).
3. Click on the green button **New pull request** in the upper right corner.
4. GitHub will compare your fork against the main repo so that you can see any changes you've made. Make sure that the base repository is *Juanjo-Capital/jjcap* and the head repository is *yourname/jjcap* (which should be the default setting).
5. Click on the green button **Create pull request**.
6. Enter a title and some comments describing your changes, and click on the green button **Create pull request**.
7. Once you have submitted your pull request, the officers will take a look at it and hopefully merge it into the main repo. If your pull request gets merged, its status will change from "Open" to "Merged".

## Everybody has been pushing code… how do I get their code onto my computer? 
1. Commit your code (see above) and make sure you are on the branch that you want to update. 
2. If you say `git status`, it might specify that you are already up to date. This is because it is comparing the status of your local version with the version of *yourname/reponame*, not Juanjo-Capital/reponame. 
3. We will need to set Juanjo-Capital/reponame as the **upstream** (the parent) of our repository, by typing `git remote add upstream https://github.com/Juanjo-Capital/jjcap.git`
4. Once the upstream is set, we run `git pull upstream master` to grab the code from the parent repository and merge it into our own work.

## Other help
- Help, I broke something: https://github.com/k88hudson/git-flight-rules
- Oh shit, git: https://ohshitgit.com/
- Learn how to use branches: https://learngitbranching.js.org/?locale=en_US
- Github’s guide to forking: https://help.github.com/en/articles/fork-a-repo
- Slack Annie