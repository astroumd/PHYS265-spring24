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

With Linux, Mac or Window+WSL git is already included. Try the command **git --version** in
a terminal and you should see something like 2.34.1 - the exact version does not matter for
us very much. There is also an official "Github CLI", usually installed as the command
**gh**.


## Steps

0. Create an account on github.com and share your username with the instructors

1. Clone an existing repo.   Try https://github.com/astroumd/PHYS265-spring24  - Note the file you are
   reading is

2. Update this repo with a **pull**, though on Desktop it's called **fetch**. Most often there is nothing.
   Look at the *History* tab
   on the top left when the latest file was modified/added.

3. Create your own new repo for Lab1, and create a README file. Suggested name is PHYS265-spring24-lab1,
   but feel free to pick any name.
   Set permissions (to be discussed if we are using private or public)

4. Modify the README file, and put your name in it.  Upload this file back to github.


## Authentication (advanced)

This applies to the web interface

As of January 2024 github will enforce 2FA (two-factor authentication). Although you will find
everything you need to know to work with github on their website, there are numerous
web pages summarizing this. One example is on https://swcarpentry.github.io/git-novice/ which
covers the all important
[*Installing Git*](https://swcarpentry.github.io/git-novice/#installing-git)
and
[*Creating a GitHub Account*](https://swcarpentry.github.io/git-novice/#creating-a-github-account)
to get your started on Linux, Mac, or Windows.

To summarize, there are two methods how to automate your authentication with github:

### 1. Personal Access Tokens

Settings -> Developer Setting  -> Personal access tokens -> Tokens (classic) -> generate new token

https://github.com/settings/tokens

Typically you will get a token, something like

      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

that you will then use as a password. When it was generated, you also had to give it a lifetime. Pick one year,
or anything you prefer.

### 2. SSH keys

Settings -> SSH and GPG keys -> new SSH key

https://github.com/settings/keys

*There is more to come here how keys are generated with **ssh-keygen** and **ssh-copy-id**

## Class Repositories

You actually don't need a github account to get a public repository, e.g. this will *always* work:

      git clone https://github.com/astroumd/PHYS265-spring24

or if you have setup your git using ssh keys, this one will work as well:

      git clone git@github.com:astroumd/PHYS265-spring24.git

### Homework - method 1

To share your class work with the instructors, *your* repository needs to be private!

Typically you will start at https://github.com/new to create a new repository, but make
sure the **Private** button has been checked, and let it create a default **README.md** file!
After this github will throw you into your new repository.

Then add the instructors as *collaborators*:

      Settings (top right) -> Collaborators (top of left column) -> Add People

where you add the instructors:

      gcarterhall
      teuben
      sjean022

### Homework - method 2

You can also fork our own template. For this, sign in to **github** and navigate to

      https://github.com/astroumd/PHYS265-spring24-hw

and find the **fork** button in the top right corner of the page. In the README file you
will find some instructions to make your forked repo a *private* one, and give the
instructors *read* permission to pull your homework.
