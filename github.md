# git and github

[**git**](https://xkcd.com/1597/) is arguably the most common Version
Control System on the market and very popular with Open Source
Software. https://github.com is one of the [major
contenders](https://en.wikipedia.org/wiki/Comparison_of_source-code-hosting_facilities),
although gitlab and bitbucket offer competative interfaces to maintain
your git repository. For private use you can also use git on
personal laptop or a home network. Obviously for collaboration something
like *github* is the way to go.

In this class you will learn to git, and how to use github to maintain a
git repository, but if you already use another host, feel free to use
it. We will use git as an option to submit the lab work.

If these terms makes sense to you, we will **not** use git *branches*, or
learn how to submit a *pull request*, or force *main branch protection*.
In git terminology, all we need is:  clone, add, commit, pull and push.

## Installation

### GUI: GitHub Desktop for Mac/Win

For both MacOS and Windows has a nice GUI frontend to git called *GitHub Desktop*, which you can install
from https://desktop.github.com.  This application greatly simplifies working with Git.

### GUI: GitKraken for Linux

More on this as Peter hasn't really used git desktop GUI's.  There are other useful
GUI applications to browse a local repo, e.g. **gitg** and **gitk**.

### CLI: Linux / Mac / Win

With Linux, Mac or Window+WSL (Windows subsystem for Linux)
git is already included. Try the command **git --version** in
a terminal and you should see something like 2.34.1 - the exact version does not matter for
us very much. There is also an official "Github CLI", usually installed as the command
**gh**.  Nobody in class should need to use  the CLI version, though it can be useful
for power users with fast fingers.


## Steps

0. Create an account on github.com and share your username with the instructors.

1. Clone an existing repo.   Try https://github.com/astroumd/PHYS265-spring24 

2. Update this repo with a **pull**, on Desktop it's called **fetch**. Most often there is nothing.
   Look at the *History* tab
   on the top left when the latest file was modified/added. You can also view differences between
   successive versions of the files.

3. Create your own new repo for Lab1, and add a README file from the menu. Or create one later.
   Strongly suggested to name this **PHYS265-spring24-labs**,   and
   When asked, pick a private repo.

4. Modify the README file, and put your name in it.  Upload this file back to github but first committing
   it to the **main** branch (blue button bottom left), after which on the right side you will see your
   pending actions, in this case **Push Origin**.

4. Your work (labs, coding) will be done within sub-folders.  Do not create a new github repo for each
   problem. Do not use branches either, unless you known how to deal with them. You instructors will only
   look at the main branch.

5. Since your repo is private, you'll need to give permission to the graders to read your code. Do this
   from the web interface of your repo:

        Settings (top right) -> Collaborators (top of left column) -> Add People

   where you add your instructors:

        gcarterhall
        sjean022
        teuben

6. (optional) Create a public README.md file in your own github.com/yourname/yourname repository.
   For example look at my barebones one   https://github.com/teuben/teuben/   but there are many
   better examples online.

This document printed from: https://github.com/astroumd/PHYS265-spring24/blob/main/github.md

