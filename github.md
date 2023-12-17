# git and github

[**git**](https://xkcd.com/1597/) is arguably the most common Version Control System
on the market
and very popular with Open Source Software. https://github.com is one of the
[major contenders](https://en.wikipedia.org/wiki/Comparison_of_source-code-hosting_facilities),
although gitlab and bitbucket offer competative interfaces to
maintain your git repository.

In this class you will learn git, and how to use github to maintain a git repository, but if you
already use another host, feel free to use it. We will use git to submit homework.

If these terms makes sense to you, we will not use git branches, or learn how to submit
a pull request, or force main branch protection.
These will be available for extra credit though.


## Authentication

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

that you will then use as a password. When it was generated, you also had to give oit a lifetime. Pick one year,
or anything you prefer.

### 2. SSH keys

Settings -> SSH and GPG keys -> new SSH key

https://github.com/settings/keys

*There is more to come here how keys are generated with **ssh-keygen** and **ssh-copy-id**

## Class Repository

You actually don't need a github account to get a public repository, e.g. this will *always* work:

      git clone https://github.com/astroumd/PHYS265-spring24

or if you have setup your git using ssh keys, this one will work as well:

      git clone git@github.com:astroumd/PHYS265-spring24.git


but to share your class work with the instructors, *your* repository needs to be private!

Typically you will start at https://github.com/new to create a new repository, but make
sure the **Private** button has been checked, and let it create a default **README.md** file!
After this github will throw you into your new repository.

Then add the instructors as *collaborators*:

      Settings (top right) -> Collaborators (top of left column) -> Add People

where you add the instructors:

      gcarterhall
      teuben
      our_TA_TBD
